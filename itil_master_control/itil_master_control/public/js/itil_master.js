/* ITIL 4 Master Control Panel - Desk Initialization Script */

console.log("[ITIL Master Control] Initializing Desk Assets & Control Plane v1.0.0...");

frappe.provide("frappe.itil_master_control");

frappe.itil_master_control = {
	init: function() {
		console.log("[ITIL Master Control] Core Suite Loaded Successfully.");
	},

	open_value_stream_mapper: function() {
		frappe.set_route("service-value-stream-mapper");
	}
};

$(document).on("app_ready", function() {
	frappe.itil_master_control.init();
});
