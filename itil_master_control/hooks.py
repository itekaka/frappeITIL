app_name = "itil_master_control"
app_title = "ITIL 4 Master Control Panel"
app_publisher = "ITIL Master Team"
app_description = "Enterprise ITIL 4 ITSM Control Plane with Service Value Stream Mapper"
app_email = "dev@itilmaster.local"
app_license = "mit"

# Includes in Desk
app_include_css = "/assets/itil_master_control/css/itil_master.css"
app_include_js = "/assets/itil_master_control/js/itil_master.js"


# Desktop / Workspace Notifications
doctype_js = {
	"ITIL Incident": "public/js/itil_incident.js",
	"ITIL Problem": "public/js/itil_problem.js",
	"ITIL Change Request": "public/js/itil_change_request.js"
}

# Scheduled Tasks for Practice Health Score Recalculation
scheduler_events = {
	"cron": {
		"*/15 * * * *": [
			"itil_master_control.itil_master_control.api.recalculate_all_practice_health"
		]
	},
	"daily": [
		"itil_master_control.itil_master_control.api.generate_daily_health_snapshots"
	]
}

# DocType Event Hooks for Cross-Practice Auto Correlation
doc_events = {
	"ITIL Incident": {
		"on_update": "itil_master_control.itil_master_control.api.on_incident_update"
	},
	"ITIL Problem": {
		"on_update": "itil_master_control.itil_master_control.api.on_problem_update"
	},
	"ITIL Change Request": {
		"on_update": "itil_master_control.itil_master_control.api.on_change_update"
	},
	"ITIL Deployment Log": {
		"on_submit": "itil_master_control.itil_master_control.api.on_deployment_submit"
	}
}

# Fixtures / Workspace exports
fixtures = [
	"Workspace",
	"ITIL Practice"
]
