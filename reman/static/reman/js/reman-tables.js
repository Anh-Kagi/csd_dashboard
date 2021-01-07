// Call the dataTables jQuery plugin
$(document).ready(function () {
    $('#repairTable').DataTable({
        pagingType: "full_numbers",
        scrollX: true,
        order: [[2, "asc"]],
        // Disable sorting for the Tags and Actions columns.
        columnDefs: [{
            targets: [0, 1],
            searchable: false,
            orderable: false,
        }],
    });

    $('#batchTable').DataTable({
        pagingType: "full_numbers",
        scrollX: true,
        order: [],
        columnDefs: [{
            targets: [0, 1],
            searchable: false,
            orderable: false,
        }],
    });

    $('#ecuModelTable').DataTable({
        pagingType: "full_numbers",
        scrollX: true,
        order: [[1, "asc"]],
        columnDefs: [{
            targets: 0,
            searchable: false,
            orderable: false,
        }],
        initComplete: function () {
            this.api().columns([1, 2, 3, 4, 5, 6, 7, 8, 9]).every(function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo($(column.footer()).empty())
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            });
        },
    });

    $('#outTable').DataTable({
        pagingType: "full_numbers",
        scrollX: true,
        order: [[0, "asc"]],
    });
});
