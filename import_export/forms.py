from django import forms


class ExportCorvetForm(forms.Form):
    PRODUCTS = [('corvet', 'ALL'), ('ecu', 'ECU'), ('bsi', 'BSI'), ('com', 'COM200x')]
    FORMATS = [('csv', 'CSV')]

    formats = forms.ChoiceField(
        label='Formats', required=False, choices=FORMATS,
        widget=forms.Select(attrs={'style': 'width:100px', 'class': 'custom-select form-control mx-sm-3 mb-2'})
    )
    products = forms.ChoiceField(
        label='Produit', required=False, choices=PRODUCTS,
        widget=forms.Select(attrs={'style': 'width:100px', 'class': 'custom-select form-control mx-sm-3 mb-2'}),
    )


class ExportRemanForm(forms.Form):
    TABLES = [('batch', 'BATCH'), ('repair', 'REPAIR')]
    FORMATS = [('csv', 'CSV')]

    formats = forms.ChoiceField(
        label='Formats', required=False, choices=FORMATS,
        widget=forms.Select(attrs={'style': 'width:100px', 'class': 'custom-select form-control mx-sm-3 mb-2'})
    )
    tables = forms.ChoiceField(
        label='Tableaux', required=False, choices=TABLES,
        widget=forms.Select(attrs={'style': 'width:100px', 'class': 'custom-select form-control mx-sm-3 mb-2'}),
    )