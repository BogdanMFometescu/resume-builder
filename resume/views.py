from django.shortcuts import render, redirect
from .models import Resume, Experience, Skills, Education, Projects
from .forms import ResumeForm, ExperienceForm, SkillsForm, EducationForm, ProjectsForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


def home(request):
    return render(request, 'resume/home.html')


def resumes(request):
    all_resumes = Resume.objects.all()
    context = {'resumes': all_resumes}
    return render(request, 'resume/resumes.html', context)


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


def create_resume(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('resumes')
    context = {'form': form}
    return render(request, 'resume/form-resume.html', context)


def add_experience(request):
    experience_form = ExperienceForm()
    if request.method == 'POST':
        experience_form = ExperienceForm(request.POST, request.FILES)
        if experience_form.is_valid():
            experience_form.save()
        else:
            print(experience_form.errors)
        return redirect('resumes')
    context = {'experience_form': experience_form}
    return render(request, 'resume/form-experience.html', context)


def add_education(request):
    education_form = EducationForm()
    if request.method == 'POST':
        education_form = EducationForm(request.POST, request.FILES)
        if education_form.is_valid():
            education_form.save()
        else:
            print(education_form.errors)
        return redirect('resumes')
    context = {'education_form': education_form}
    return render(request, 'resume/form-education.html', context)


def add_project(request):
    project_form = ProjectsForm()
    if request.method == 'POST':
        project_form = ProjectsForm(request.POST, request.FILES)
        if project_form.is_valid():
            project_form.save()
        else:
            print(project_form.errors)
        return redirect('resumes')
    context = {'project_form': project_form}
    return render(request, 'resume/form-project.html', context)


def add_skill(request):
    skill_form = SkillsForm()
    if request.method == 'POST':
        skill_form = SkillsForm(request.POST, request.FILES)
        if skill_form.is_valid():
            skill_form.save()
        else:
            print(skill_form.errors)
        return redirect('resumes')
    context = {'skill_form': skill_form}
    return render(request, 'resume/form-skill.html', context)


def update_resume(request, pk):
    updated_resume = Resume.objects.get(id=pk)
    form = ResumeForm(instance=updated_resume)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('resumes')
    context = {'form': form}
    return render(request, 'resume/form-resume.html', context)


def delete_resume(request, pk):
    deleted_resume = Resume.objects.get(id=pk)
    form = ResumeForm(instance=deleted_resume)
    if request.method == 'POST':
        deleted_resume.delete()
        return redirect('resumes')

    context = {'object': form}
    return render(request, 'resume/delete-resume.html', context)


def make_pdf(request,pk):
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


def export_to_pdf(request):
    return render(request, 'resume/export-pdf.html')


