from models.insights import Insights
from flask import Blueprint, request, jsonify

insights_routes = Blueprint('insights_routes', __name__)


@insights_routes.route('/employee_insights')
def employee_insights():
    employee_id = request.args.get('employee_id')
    total_sales_month = Insights().total_sales_month(employee_id)
    total_hours_week = Insights().total_hours_worked_week(employee_id)
    avg_hours_day = Insights().total_hours_worked_week(employee_id)
    return jsonify({
        'total_sales_month': total_sales_month[0],
        'total_hours_week': total_hours_week[0],
        'avg_hours_day': avg_hours_day[0]
    })


@insights_routes.route('/customer_insights')
def customer_insights():
    customer_id = request.args.get('customer_id')
    total_money_spent = Insights().total_money_spent(customer_id)
    avg_fuel_purchased = Insights().avg_fuel_purchase(customer_id)
    frequent_fuel_type = Insights().frequent_fuel_type(customer_id)
    return jsonify({
        'total_money_spent': total_money_spent,
        'avg_fuel_purchased': avg_fuel_purchased,
        'frequent_fuel_type': frequent_fuel_type
    })


@insights_routes.route('/general_insights')
def general_insights():
    top_performing_employee = Insights().top_performing_employee()
    popular_fuel_type = Insights().popular_fuel_type()
    avg_purchase_quantity = Insights().avg_purchase_quantity()
    total_monthly_sales = Insights().total_sales_month()
    return jsonify({
        'top_performing_employee': f'{top_performing_employee[0]} {top_performing_employee[1]}',
        'popular_fuel_type': popular_fuel_type[0],
        'avg_purchase_quantity': avg_purchase_quantity[0],
        'total_monthly_sales': total_monthly_sales[0]
    })
