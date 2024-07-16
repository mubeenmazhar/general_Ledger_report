from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    """
    Main execution function for the Custom General Ledger report.
    
    :param filters: Dict containing filter parameters
    :return: Tuple of columns and data
    """
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    """
    Define the columns for the report.
    
    :return: List of column definitions
    """
    return [
        {
            "fieldname": "posting_date",
            "label": _("Date"),
            "fieldtype": "Date",
            "width": 90
        },
        {
            "fieldname": "voucher_type",
            "label": _("Voucher Type"),
            "fieldtype": "Data",
            "width": 120
        },
        {
            "fieldname": "debit",
            "label": _("Debit"),
            "fieldtype": "Currency",
            "width": 130
        },
        {
            "fieldname": "credit",
            "label": _("Credit"),
            "fieldtype": "Currency",
            "width": 130
        }
    ]

def get_data(filters):
    """
    Retrieve and process data for the report based on filters.
    
    :param filters: Dict containing filter parameters
    :return: List of data rows
    """
    # Construct the SQL query
    query = """
        SELECT 
            posting_date,
            voucher_type,
            debit,
            credit
        FROM 
            `tabGL Entry`
        WHERE 
            company = %(company)s
            AND posting_date BETWEEN %(from_date)s AND %(to_date)s
        ORDER BY 
            posting_date
    """
    
    # Execute the query with filters
    result = frappe.db.sql(query, filters, as_dict=1)
    
    return result