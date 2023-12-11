import uuid

from django.db import models
from users.models import Profile

RESUME_TEMPLATE_CHOICES = (('Simple Resume', 'Simple Resume'), ('Modern Resume', 'Modern Resume'))


class Resume(models.Model):
    # Profile owner
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # Select template
    resume_template = models.CharField(choices=RESUME_TEMPLATE_CHOICES, default='_', blank=True, null=True)
    # General info
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return f"{self.first_name}- {self.last_name} "


class Experience(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=250, blank=True, null=True)
    position = models.CharField(max_length=250, blank=True, null=True)
    job_description = models.TextField(max_length=1000, blank=True, null=True)
    start_date = models.CharField(blank=True, null=True)
    end_date = models.CharField(blank=True, null=True, )
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.employer_name


class Projects(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250, blank=True, null=True)
    start_date_of_project = models.CharField(blank=True, null=True)
    end_date_of_project = models.CharField(blank=True, null=True)
    project_description = models.TextField(max_length=1000, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.project_name


class Education(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=250, blank=True, null=True)
    degree = models.CharField(max_length=250, blank=True, null=True)
    school_start_date = models.CharField(blank=True, null=True)
    school_end_date = models.CharField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.school_name


class Skills(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=250, blank=True, null=True)
    skill_description = models.TextField(max_length=1000, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.skill_name
