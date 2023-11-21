from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
