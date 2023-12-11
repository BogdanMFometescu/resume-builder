from django.shortcuts import render, redirect
from .models import Resume, Experience, Skills, Education, Projects
from .forms import ResumeForm, ExperienceForm, SkillsForm, EducationForm, ProjectsForm
from users.models import Profile
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'resume/home.html')


@login_required(login_url='login')
def resumes(request):
    all_resumes = Resume.objects.all()
    context = {'resumes': all_resumes}
    return render(request, 'resume/resumes.html', context)


@login_required(login_url='login')
def resume(request, pk):
    single_resume = Resume.objects.get(id=pk)
    all_experience = Experience.objects.filter(resume=single_resume)
    all_skills = Skills.objects.filter(resume=single_resume)
    all_education = Education.objects.filter(resume=single_resume)
    all_projects = Projects.objects.filter(resume=single_resume)
    context = {'resume': single_resume,
               'experience': all_experience,
               'skills': all_skills,
               'education': all_education,
               'project': all_projects}
    return render(request, 'resume/single-resume.html', context)


@login_required(login_url='login')
def create_resume(request):
    profile = request.user.profile
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST or None, request.FILES)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.owner = profile
            new_resume.save()
        else:
            print(form.errors)
        return redirect('resumes')
    context = {'form': form}
    return render(request, 'resume/form-resume.html', context)


@login_required(login_url='login')
def update_resume(request, pk):
    updated_resume = get_object_or_404(Resume, id=pk)
    form = ResumeForm(instance=updated_resume)
    if request.method == 'POST':
        form = ResumeForm(request.POST or None, request.FILES, instance=updated_resume)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('resumes')
    context = {'form': form}
    return render(request, 'resume/form-resume.html', context)


@login_required(login_url='login')
def delete_resume(request, pk):
    deleted_resume = get_object_or_404(Resume, id=pk)
    form = ResumeForm(instance=deleted_resume)
    if request.method == 'POST':
        deleted_resume.delete()
        return redirect('resumes')

    context = {'object': form}
    return render(request, 'resume/delete-resume.html', context)


@login_required(login_url='login')
def create_experience(request):
    experience_form = ExperienceForm()
    if request.method == 'POST':
        experience_form = ExperienceForm(request.POST or None, request.FILES)
        if experience_form.is_valid():
            experience_form.save()
        else:
            print(experience_form.errors)
        return redirect('resumes')
    context = {'experience_form': experience_form}
    return render(request, 'resume/form-experience.html', context)


@login_required(login_url='login')
def add_new_experience(request, pk):
    new_entry_resume = get_object_or_404(Resume, id=pk)
    form = ExperienceForm(initial={'resume': new_entry_resume})
    if request.method == 'POST':
        form = ExperienceForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=pk)
    context = {'experience_form': form, 'resume': new_entry_resume}
    return render(request, 'resume/form-experience.html', context)


@login_required(login_url='login')
def update_experience(request, pk):
    updated_experience = get_object_or_404(Experience, id=pk)
    form = ExperienceForm(instance=updated_experience)
    if request.method == 'POST':
        form = ExperienceForm(request.POST or None, request.FILES, instance=updated_experience)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=updated_experience.resume_id)
    context = {'experience_form': form, }
    return render(request, 'resume/form-experience.html', context)


@login_required(login_url='login')
def delete_experience(request, pk):
    deleted_experience = get_object_or_404(Experience, id=pk)
    form = ExperienceForm(instance=deleted_experience)
    if request.method == 'POST':
        deleted_experience.delete()
        return redirect('resume', pk=deleted_experience.resume_id)
    context = {'object': form}
    return render(request, 'resume/delete-resume.html', context)


@login_required(login_url='login')
def create_education(request):
    education_form = EducationForm()
    if request.method == 'POST':
        education_form = EducationForm(request.POST or None, request.FILES)
        if education_form.is_valid():
            education_form.save()
        else:
            print(education_form.errors)
        return redirect('resumes')
    context = {'education_form': education_form}
    return render(request, 'resume/form-education.html', context)


@login_required(login_url='login')
def add_new_education(request, pk):
    new_education = get_object_or_404(Resume, id=pk)
    form = EducationForm(initial={'resume': new_education})
    if request.method == 'POST':
        form = EducationForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=pk)

    context = {'education_form': form, 'resume': new_education}
    return render(request, 'resume/form-education.html', context)


@login_required(login_url='login')
def update_education(request, pk):
    updated_education = get_object_or_404(Education, id=pk)
    form = EducationForm(instance=updated_education)
    if request.method == 'POST':
        form = EducationForm(request.POST or None, request.FILES, instance=updated_education)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=updated_education.resume_id)
    context = {'education_form': form}
    return render(request, 'resume/form-education.html', context)


@login_required(login_url='login')
def delete_education(request, pk):
    deleted_education = get_object_or_404(Education, id=pk)
    form = EducationForm(instance=deleted_education)
    if request.method == 'POST':
        deleted_education.delete()
        return redirect('resume', pk=deleted_education.resume_id)
    context = {'object': form}
    return render(request, 'resume/delete-resume.html', context)


@login_required(login_url='login')
def create_project(request):
    project_form = ProjectsForm()
    if request.method == 'POST':
        project_form = ProjectsForm(request.POST or None, request.FILES)
        if project_form.is_valid():
            project_form.save()
        else:
            print(project_form.errors)
        return redirect('resumes')
    context = {'project_form': project_form}
    return render(request, 'resume/form-project.html', context)


@login_required(login_url='login')
def add_new_project(request, pk):
    new_project = get_object_or_404(Resume, id=pk)
    form = ProjectsForm(initial={'resume': new_project})
    if request.method == 'POST':
        form = ProjectsForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=pk)
    context = {'project_form': form, 'resume': new_project}
    return render(request, 'resume/form-project.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    updated_project = get_object_or_404(Projects, id=pk)
    form = ProjectsForm(instance=updated_project)
    if request.method == 'POST':
        form = ProjectsForm(request.POST or None, request.FILES, instance=updated_project)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=updated_project.resume_id)

    context = {'project_form': form}
    return render(request, 'resume/form-project.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    deleted_project = get_object_or_404(Projects, id=pk)
    form = ProjectsForm(instance=deleted_project)
    if request.method == 'POST':
        deleted_project.delete()
        return redirect('resume', pk=deleted_project.resume_id)
    context = {'object': form}
    return render(request, 'resume/delete-resume.html', context)


@login_required(login_url='login')
def create_skill(request):
    skill_form = SkillsForm()
    if request.method == 'POST':
        skill_form = SkillsForm(request.POST or None, request.FILES)
        if skill_form.is_valid():
            skill_form.save()
        else:
            print(skill_form.errors)
        return redirect('resumes')
    context = {'skill_form': skill_form}
    return render(request, 'resume/form-skill.html', context)


@login_required(login_url='login')
def add_new_skill(request, pk):
    new_skill = get_object_or_404(Resume, id=pk)
    form = SkillsForm(initial={'resume': new_skill})
    if request.method == 'POST':
        form = SkillsForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=pk)
    context = {'skill_form': form, 'resume': new_skill}
    return render(request, 'resume/form-skill.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    updated_skill = get_object_or_404(Skills, id=pk)
    form = SkillsForm(instance=updated_skill)
    if request.method == 'POST':
        form = SkillsForm(request.POST or None, request.FILES, instance=updated_skill)
        if form.is_valid():
            form.save()
            return redirect('resume', pk=updated_skill.resume_id)
    context = {'skill_form': form}
    return render(request, 'resume/form-skill.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    deleted_skill = get_object_or_404(Skills, id=pk)
    form = SkillsForm(instance=deleted_skill)
    if request.method == 'POST':
        deleted_skill.delete()
        return redirect('resume', pk=deleted_skill.resume_id)
    context = {'object': form}
    return render(request, 'resume/delete-resume.html', context)


@login_required(login_url='login')
def make_pdf(request, pk):
    single_resume = Resume.objects.get(id=pk)
    all_experience = Experience.objects.filter(resume=single_resume)
    all_skills = Skills.objects.filter(resume=single_resume)
    all_education = Education.objects.filter(resume=single_resume)
    all_projects = Projects.objects.filter(resume=single_resume)
    context = {'resume': single_resume,
               'experience': all_experience,
               'skills': all_skills,
               'education': all_education,
               'project': all_projects}
    template_path = 'resume/export-pdf.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, )

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required(login_url='login')
def export_to_pdf(request):
    return render(request, 'resume/export-pdf.html')
