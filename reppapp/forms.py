from django import forms

class LocForm(forms.Form):
	CHOICES = [('Ambivali', 'Ambivali'),('Kalyan', 'Kalyan'),('Shahad', 'Shahad'),('Colaba', 'Colaba'),('Worli', 'Worli'),('Dadar', 'Dadar'),
	('Andheri', 'Andheri'),
	('Asangoan', 'Asangoan'),
	('Powai', 'Powai'),
	('Ghatkopar', 'Ghatkopar'),
	('Dombivali', 'Dombivali'),]
	loc = forms.ChoiceField(label="Please choose location which you want to stay ? ", widget=forms.RadioSelect,choices=CHOICES,)
