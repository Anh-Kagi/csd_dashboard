// Call the dataTables jQuery plugin
$(document).ready(function () {
    $('#softTable').DataTable({
        paging: false,
        scrollX: true,
        order: [[1, "asc"]],
        columnDefs: [{
            targets: 0,
            searchable: false,
            orderable: false,
        }],
        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
    });

    $('#thermalTable').DataTable({
        pagingType: "full_numbers",
        scrollX: true,
        columnDefs: [{
            targets: 0,
            searchable: false,
            orderable: false,
        }],
        order: [[2, "desc"]],
    });
});