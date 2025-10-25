from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project, Task
# Create your views here.


def login_view(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('core:home')
		messages.error(request, "Invalid credentials")
	return render(request, 'login.html')

def sign_up_view(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		email=request.POST['email']

		if User.objects.filter(username=username).exists():
			messages.error(request, 'Username already exists')
		else:
			user=User.objects.create_user(
						username=username,
						password=password,
						email=email
						)
			login(request, user)
			return redirect('core:home')
	return render(request, 'signup.html')

@login_required
def home_view(request):
	projects = Project.objects.filter(user=request.user)
	return render(request, 'home.html', {'projects':projects})

@login_required
def project_form_view(request, project_id=None):
    project = get_object_or_404(Project, id=project_id, user=request.user) if project_id else None
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            if not project_id:
                project.user = request.user
            project.save()
            # Handle tasks
            task_descriptions = request.POST.getlist('tasks')
            if project_id:
                project.tasks.all().delete()
            for desc in task_descriptions:
                if desc.strip():
                    Task.objects.create(project=project, description=desc)
            return redirect('core:project_form')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form, 'project': project})
	

@login_required
def toggle_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('core:home')


@login_required
def delete_view(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    project.delete()
    return redirect('core:home')


@login_required
def logout_view(request):
    logout(request)
    return redirect('core:login')
