from django import forms
from .models import Chore, Roommate


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ["title", "assigned_to"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Take out trash"}),
        }

    def __init__(self, *args, household=None, **kwargs):
        super().__init__(*args, **kwargs)
        if household is not None:
            self.fields["assigned_to"].queryset = Roommate.objects.filter(
                household=household
            )
        self.fields["assigned_to"].label = "Assign to"
