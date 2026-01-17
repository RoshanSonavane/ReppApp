from django import forms


class NawForm(forms.Form):

    LOCATION_CHOICES = [
        ('Ambivali', 'Ambivali'),
        ('Shahad', 'Shahad'),
        ('Andheri', 'Andheri'),
        ('Asangaon', 'Asangaon'),
        ('Dombivali', 'Dombivali'),
        ('Ghatkopar', 'Ghatkopar'),
        ('Kalyan', 'Kalyan'),
        ('Malad', 'Malad'),
        ('Powai', 'Powai'),
        ('Thane', 'Thane'),
        ('Worli', 'Worli'),
    ]

    BOOL_CHOICES = [('1', 'Yes'), ('0', 'No')]

    loc = forms.ChoiceField(
        label="Select Location",
        choices=LOCATION_CHOICES,
        widget=forms.RadioSelect
    )

    area = forms.IntegerField(
        label="Area (sq ft)",
        min_value=400,
        max_value=5000
    )

    bd = forms.IntegerField(
        label="No. of Bedrooms",
        min_value=1,
        max_value=10
    )

    nr = forms.ChoiceField(label="New Property?", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    g = forms.ChoiceField(label="Gymnasium", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    la = forms.ChoiceField(label="Lift Available", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    cp = forms.ChoiceField(label="Car Parking", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    ms = forms.ChoiceField(label="Maintenance Staff", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    se = forms.ChoiceField(label="24x7 Security", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    ca = forms.ChoiceField(label="Children's Play Area", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    cl = forms.ChoiceField(label="Clubhouse", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    inte = forms.ChoiceField(label="Intercom", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    lg = forms.ChoiceField(label="Landscaped Gardens", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    ig = forms.ChoiceField(label="Indoor Games", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    gc = forms.ChoiceField(label="Gas Connection", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    jt = forms.ChoiceField(label="Jogging Track", choices=BOOL_CHOICES, widget=forms.RadioSelect)
    sp = forms.ChoiceField(label="Swimming Pool", choices=BOOL_CHOICES, widget=forms.RadioSelect)
