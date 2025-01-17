let table = $('#sivinTable').DataTable({
    pagingType: "full_numbers",
    lengthMenu: [[25, 50, 100], [25, 50, 100]],
    processing: true,
    serverSide: true,
    scrollX: true,
    order: [[1, 'asc']],
    ajax: {
        url: URL_AJAX,
        type: "GET",
    },
    columns: [
        {
            sortable: false,
            render: function (data, type, full, meta) {
                let immat = full.immat_siv;
                let url = '/squalaetp/sivin/' + immat + '/detail/';
                return '<a  href="' + url + '" type="button" title="Detail" class="btn btn-info btn-circle btn-sm"><i class="fas fa-info-circle"></i></a>'
            },
        },
        {data: "immat_siv"},
        {data: "codif_vin"},
        {data: "marque"},
        {data: "modele"},
        {data: "genre_v"},
        {data: "nb_portes"},
        {data: "nb_pl_ass"},
        {data: "version"},
        {data: "energie"},
    ],
    columnDefs: [{
        targets: 0,
        searchable: false,
        orderable: false,
    }],
});
