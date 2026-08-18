frappe.pages['service-value-stream-mapper'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Service Value Stream Mapper (ITIL 4 & Lean)'),
		single_column: true
	});

	page.main.addClass('vsm-wrapper');
	$(wrapper).find('.page-content').css('padding', '15px');

	// Render Header Summary Metrics & Controls
	var html = `
		<div class="vsm-container">
			<div class="vsm-header-metrics">
				<div class="metric-card">
					<div class="metric-label">Flow Efficiency</div>
					<div class="metric-value text-primary" id="vsm-flow-eff">--%</div>
					<div class="metric-sub">Process Time / Lead Time</div>
				</div>
				<div class="metric-card">
					<div class="metric-label">Total Lead Time</div>
					<div class="metric-value" id="vsm-lead-time">-- hrs</div>
					<div class="metric-sub">End-to-End Duration</div>
				</div>
				<div class="metric-card">
					<div class="metric-label">Process Touch Time</div>
					<div class="metric-value text-success" id="vsm-process-time">-- hrs</div>
					<div class="metric-sub">Active Value Work</div>
				</div>
				<div class="metric-card">
					<div class="metric-label">Wait Time (Waste)</div>
					<div class="metric-value text-danger" id="vsm-wait-time">-- hrs</div>
					<div class="metric-sub">Queue & Hand-off Delay</div>
				</div>
			</div>

			<div class="vsm-toolbar">
				<button class="btn btn-primary btn-sm" id="btn-refresh-vsm">
					<i class="octicon octicon-sync"></i> Refresh Stream Data
				</button>
				<span class="vsm-stream-title" id="vsm-stream-name">Loading Value Stream...</span>
			</div>

			<div class="vsm-canvas-wrapper">
				<svg id="vsm-canvas" width="100%" height="520" style="background: #0f172a; border-radius: 10px; border: 1px solid #334155;">
					<defs>
						<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
							<path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8" />
						</marker>
					</defs>
					<g id="vsm-edges-group"></g>
					<g id="vsm-nodes-group"></g>
				</svg>
			</div>
		</div>
	`;

	page.main.html(html);

	// Fetch Stream Data
	function load_vsm_data() {
		frappe.call({
			method: 'itil_master_control.itil_master_control.api.get_value_stream_graph',
			callback: function(r) {
				if (r.message) {
					render_vsm(r.message);
				}
			}
		});
	}

	function render_vsm(data) {
		var vs = data.value_stream;
		$('#vsm-flow-eff').text(vs.flow_efficiency + '%');
		$('#vsm-lead-time').text(vs.total_lead_time_hrs + ' hrs');
		$('#vsm-process-time').text(vs.total_process_time_hrs + ' hrs');
		$('#vsm-wait-time').text(vs.total_wait_time_hrs + ' hrs');
		$('#vsm-stream-name').text(vs.stream_name + ' (' + vs.trigger_condition + ' → ' + vs.target_outcome + ')');

		var svgNodes = $('#vsm-nodes-group');
		var svgEdges = $('#vsm-edges-group');
		svgNodes.empty();
		svgEdges.empty();

		var nodeMap = {};
		data.nodes.forEach(function(node) {
			nodeMap[node.id] = node;
		});

		// Default node positions if missing
		var defaultX = 60;
		data.nodes.forEach(function(node, index) {
			var x = node.pos_x || (defaultX + index * 200);
			var y = node.pos_y || 200;

			// Draw Node Box
			var g = $(document.createElementNS('http://www.w3.org/2000/svg', 'g'))
				.attr('class', 'vsm-node-group')
				.attr('transform', 'translate(' + x + ',' + y + ')')
				.css('cursor', 'pointer')
				.on('click', function() {
					if (node.practice_doctype) {
						frappe.set_route('List', node.practice_doctype);
					}
				});

			var rect = $(document.createElementNS('http://www.w3.org/2000/svg', 'rect'))
				.attr('width', 160)
				.attr('height', 90)
				.attr('rx', 8)
				.attr('fill', '#1e293b')
				.attr('stroke', '#3b82f6')
				.attr('stroke-width', 2);

			var title = $(document.createElementNS('http://www.w3.org/2000/svg', 'text'))
				.attr('x', 12)
				.attr('y', 25)
				.attr('fill', '#f8fafc')
				.attr('font-size', '13px')
				.attr('font-weight', 'bold')
				.text(node.label);

			var practice = $(document.createElementNS('http://www.w3.org/2000/svg', 'text'))
				.attr('x', 12)
				.attr('y', 45)
				.attr('fill', '#94a3b8')
				.attr('font-size', '11px')
				.text(node.practice || 'ITIL Practice');

			var leadTime = $(document.createElementNS('http://www.w3.org/2000/svg', 'text'))
				.attr('x', 12)
				.attr('y', 65)
				.attr('fill', '#38bdf8')
				.attr('font-size', '11px')
				.text('Lead Time: ' + node.avg_actual_lead_time + 'h');

			var badgeRect = $(document.createElementNS('http://www.w3.org/2000/svg', 'rect'))
				.attr('x', 115)
				.attr('y', 10)
				.attr('width', 35)
				.attr('height', 20)
				.attr('rx', 4)
				.attr('fill', node.open_count > 0 ? '#ef4444' : '#10b981');

			var badgeText = $(document.createElementNS('http://www.w3.org/2000/svg', 'text'))
				.attr('x', 132)
				.attr('y', 24)
				.attr('fill', '#ffffff')
				.attr('font-size', '10px')
				.attr('text-anchor', 'middle')
				.text(node.open_count);

			g.append(rect).append(title).append(practice).append(leadTime).append(badgeRect).append(badgeText);
			svgNodes.append(g);
		});

		// Draw Edges
		data.edges.forEach(function(edge) {
			var source = nodeMap[edge.source];
			var target = nodeMap[edge.target];
			if (source && target) {
				var sx = (source.pos_x || 60) + 160;
				var sy = (source.pos_y || 200) + 45;
				var tx = target.pos_x || 260;
				var ty = (target.pos_y || 200) + 45;

				var line = $(document.createElementNS('http://www.w3.org/2000/svg', 'path'))
					.attr('d', 'M ' + sx + ' ' + sy + ' L ' + tx + ' ' + ty)
					.attr('stroke', '#38bdf8')
					.attr('stroke-width', 2)
					.attr('stroke-dasharray', '4')
					.attr('marker-end', 'url(#arrow)');

				svgEdges.append(line);
			}
		});
	}

	$('#btn-refresh-vsm').on('click', function() {
		load_vsm_data();
	});

	load_vsm_data();
};
