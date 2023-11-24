from django.forms import ModelForm
from .models import Resume, Experience, Projects, Education, Skills


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        self.fields['resume_template'].widget.attrs.update(
            {'class': 'content-box'})


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        self.fields['resume'].widget.attrs.update(
            {'class': 'content-box'})


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        self.fields['resume'].widget.attrs.update(
            {'class': 'content-box'})


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        self.fields['resume'].widget.attrs.update(
            {'class': 'content-box'})


class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SkillsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        self.fields['resume'].widget.attrs.update(
            {'class': 'content-box'})
