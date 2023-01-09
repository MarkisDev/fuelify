from models.insights import Insights
from flask import Blueprint, request, jsonify

insights_routes = Blueprint('insights_routes', __name__)


@insights_routes.route('/employee_insights', methods=['GET', 'POST'])
def employee_insights():
    employee_id = request.args.get('employee')
    total_sales_month = Insights().total_sales_month(employee_id)
    total_hours_week = Insights().total_hours_worked_week(employee_id)
    avg_hours_day = Insights().total_hours_worked_week(employee_id)
    return jsonify({
        'total_sales_month': total_sales_month,
        'total_hours_week': total_hours_week,
        'avg_hours_day': avg_hours_day
    })
