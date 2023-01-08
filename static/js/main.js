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
