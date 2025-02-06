from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .models import Painting
from .forms import PaintingForm

def home(request):
    """
    Display all paintings on the home page.
    """
    paintings = Painting.objects.all()
    return render(request, 'gallery/home.html', {'paintings': paintings})

def about(request):
    """
    Display the about page.
    """
    return render(request, 'gallery/about.html')

def contact(request):
    """
    Display the contact page.
    """
    return render(request, 'gallery/contact.html')

@login_required
def upload_painting(request):
    """
    Allow only staff members to upload new paintings.
    """
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to upload paintings.")

    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaintingForm()

    return render(request, 'gallery/upload.html', {'form': form})

@login_required
def edit_painting(request, pk):
    """
    Allow only staff members to edit an existing painting.
    """
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit paintings.")

    painting = get_object_or_404(Painting, pk=pk)

    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaintingForm(instance=painting)

    return render(request, 'gallery/edit.html', {'form': form, 'painting': painting})

@login_required
def delete_painting(request, pk):
    """
    Allow only staff members to delete a painting.
    """
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete paintings.")

    painting = get_object_or_404(Painting, pk=pk)

    if request.method == 'POST':
        painting.delete()
        return redirect('home')

    # Render a confirmation page before deletion.
    return render(request, 'gallery/delete.html', {'painting': painting})

def login_view(request):
    """
    Custom login view using Django's built-in AuthenticationForm.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'gallery/login.html', {'form': form})
