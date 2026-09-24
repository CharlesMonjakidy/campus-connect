from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import Announcement, Course, ScheduleItem


def home(request):
    return render(request, "home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Bienvenue sur Campus Connect !")
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def dashboard(request):
    context = {
        "course_count": Course.objects.count(),
        "announcement_count": Announcement.objects.count(),
        "schedule_count": ScheduleItem.objects.count(),
        "latest_announcements": Announcement.objects.all()[:3],
    }
    return render(request, "dashboard.html", context)


@login_required
def courses(request):
    return render(request, "courses.html", {"courses": Course.objects.all()})


@login_required
def announcements(request):
    return render(
        request,
        "announcements.html",
        {"announcements": Announcement.objects.all()},
    )


@login_required
def schedule(request):
    return render(
        request,
        "schedule.html",
        {"schedule_items": ScheduleItem.objects.all()},
    )
