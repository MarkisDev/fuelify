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
        $.getJSON('/employee_insights', { employee: employee }, function (data)
        {
            console.log(data);

            $('#totalFuelSales').text('₹' + data.total_sales_month);
            $('#totalHoursWorked').text(data.total_hours_week[0] ? data.total_hours_week : 0);
            $('#avgHoursWorkedPerDay').text(data.avg_hours_day[0] ? data.avg_hours_day : 0);
        });
    }).change();
});