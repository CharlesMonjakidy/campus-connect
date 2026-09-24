from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=150)
    teacher = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    document_url = models.URLField(blank=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.title}"


class Announcement(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ["-important", "-created_at"]

    def __str__(self):
        return self.title


class ScheduleItem(models.Model):
    DAYS = [
        ("Lundi", "Lundi"),
        ("Mardi", "Mardi"),
        ("Mercredi", "Mercredi"),
        ("Jeudi", "Jeudi"),
        ("Vendredi", "Vendredi"),
        ("Samedi", "Samedi"),
    ]
    day = models.CharField(max_length=20, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=150)
    room = models.CharField(max_length=80, blank=True)
    teacher = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ["day", "start_time"]

    def __str__(self):
        return f"{self.day} {self.start_time} - {self.course}"
