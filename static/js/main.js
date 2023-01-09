$(document).ready(function ()
{
    $('#records').DataTable({
        colReorder: true,
        responsive: true,
        paging: true,
        searching: true,
        ordering: true,
        border: "1"
    });
});

$(document).ready(function ()
{
    $('#employeeSelect').change(function ()
    {
        var employee = $(this).val();
        var data = $.param({ employee_id: employee });
        $.getJSON('/employee_insights', data, function (data)
        {
            $('#totalFuelSales').text(data.total_sales_month[0] ? '₹' + data.total_sales_month[0] : 0);
            $('#totalHoursWorked').text(data.total_hours_week[0] ? data.total_hours_week : 0);
            $('#avgHoursWorkedPerDay').text(data.avg_hours_day[0] ? data.avg_hours_day : 0);
        });
    }).change();
});

$(document).ready(function ()
{
    $('#customerSelect').change(function ()
    {
        var customer = $(this).val();
        var data = $.param({ customer_id: customer });
        $.getJSON('/customer_insights', data, function (data)
        {
            $('#totalMoneySpent').text(data.total_money_spent ? '₹' + data.total_money_spent : '₹' + 0);
            $('#avgFuelPurchased').text(data.avg_fuel_purchased ? data.avg_fuel_purchased + ' litres' : '0 litres');
            $('#frequentFuelType').text(data.frequent_fuel_type[0] ? data.frequent_fuel_type[0] : 'None');
        });
    }).change();
});