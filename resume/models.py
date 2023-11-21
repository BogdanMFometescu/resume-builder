import uuid

from django.db import models

RESUME_TEMPLATE_CHOICES = (('Simple Resume', 'Simple Resume'), ('Modern Resume', 'Modern Resume'))


class Resume(models.Model):
    # Select template
    resume_template = models.CharField(choices=RESUME_TEMPLATE_CHOICES,default='_')
    # General info
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)

    # Experience
    employer_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    job_description = models.TextField(max_length=1000)
    start_date = models.CharField(blank=True, null=True)
    end_date = models.CharField(blank=True, null=True)
    position = models.CharField(max_length=250)
    duties = models.TextField(max_length=1000)

    # Projects
    project_name = models.CharField(max_length=250)
    start_date_of_project = models.CharField(blank=True, null=True)
    end_date_of_project = models.CharField(blank=True, null=True)
    project_description = models.TextField(max_length=1000)

    # Education
    university_name = models.CharField(max_length=250)
    start_date_university = models.CharField(blank=True, null=True)
    end_date_university = models.CharField(blank=True, null=True)

    # Skills
    skill_name = models.CharField(max_length=250)
    skill_description = models.TextField(max_length=1000)

    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.first_name}- {self.last_name}-{self.created.day}"
