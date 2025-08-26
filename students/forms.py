from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()
    subject = forms.CharField(max_length=100)
    session = forms.ChoiceField(choices=[
        ("Jan-2026", "Jan 2026"),
        ("June-2026", "June 2026"),
        ("September-2026", "September 2026"),
        ("October-2026", "October 2026")
    ])
    highschool_cgpa = forms.DecimalField(max_digits=3, decimal_places=1, min_value=2.0, max_value=5.0, required=False)
    eca = forms.ChoiceField(choices=[("yes","Yes"),("no","No")], widget=forms.RadioSelect)
    eca_detail = forms.ChoiceField(choices=[
        ("IT-Robotics", "IT & Robotics"),
        ("Debate", "Debating"),
        ("social-work", "Social work"),
        ("drama", "Drama")
    ], required=False)
    reason = forms.CharField(widget=forms.Textarea)
