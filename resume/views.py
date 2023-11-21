from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm


def home(request):
    return render(request, 'resume/home.html')


def resumes(request):
    all_resumes = Resume.objects.all()
    context = {'resumes': all_resumes}
    return render(request, 'resume/resumes.html', context)


def resume(request, pk):
    single_resume = Resume.objects.get(id=pk)
    context = {'resume': single_resume}
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


def export_to_pdf(request, pk):
    pass
