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
    $('#records-hours').DataTable({
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
            $('#totalFuelSales').text(data.total_sales_month ? '₹' + data.total_sales_month : '₹' + 0);
            $('#totalHoursWorked').text(data.total_hours_week ? data.total_hours_week : 0);
            $('#avgHoursWorkedPerDay').text(data.avg_hours_day ? data.avg_hours_day : 0);
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
            $('#frequentFuelType').text(data.frequent_fuel_type ? data.frequent_fuel_type[0] : 'None');
        });
    }).change();
});

$(document).ready(function ()
{

    $.getJSON('/general_insights', function (data)
    {
        $('#totalMonthlySales').text(data.total_monthly_sales ? '₹' + data.total_monthly_sales : '₹' + 0);
        $('#avgPurchaseQuantity').text(data.avg_purchase_quantity ? data.avg_purchase_quantity + ' litres' : '0 litres');
        $('#popularFuelType').text(data.popular_fuel_type ? data.popular_fuel_type : 'None');
        $('#topPerformingEmployee').text(data.top_performing_employee ? data.top_performing_employee : 'None');

    });
});

const toast = new bootstrap.Toast(document.getElementById('toast'))
toast.show();
