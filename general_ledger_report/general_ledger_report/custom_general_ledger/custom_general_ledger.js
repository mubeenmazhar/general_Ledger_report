frappe.query_reports["Custom General Ledger"] = {
    "filters": [
        {
            "fieldname": "company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("Company"),
            "reqd": 1
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        }
    ],
    
    // Add a formatter for currency fields
    "formatter": function(value, row, column, data, default_formatter) {
        if (column.fieldtype == "Currency") {
            value = format_currency(value, "INR");
        }
        return value;
    },
    
    // Add a function to show total at the end of the report
    "onload": function(report) {
        report.page.add_inner_button(__("Show Total"), function() {
            var total_debit = 0;
            var total_credit = 0;
            
            // Calculate totals
            report.data.forEach(function(row) {
                total_debit += row.debit;
                total_credit += row.credit;
            });
            
            // Show totals in a dialog
            frappe.msgprint(
                __("Total Debit: {0}<br>Total Credit: {1}", [
                    format_currency(total_debit, "INR"),
                    format_currency(total_credit, "INR")
                ])
            );
        });
    }
};