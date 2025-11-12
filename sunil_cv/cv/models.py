from django.db import models
from django.utils import timezone

class SingletonModel(models.Model):
    """Simple singleton base for Singletons like SiteProfile"""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

# Template metadata for rendering multiple resume layouts
class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    template_path = models.CharField(max_length=255, help_text="e.g., cv/resume_modern.html")
    preview_image = models.ImageField(upload_to='template_previews/', blank=True, null=True)

    def __str__(self):
        return self.name

# Single top-level profile for the CV owner
class SiteProfile(SingletonModel):
    name = models.CharField(max_length=200, default="Sunil Thapa")
    job_title = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    portfolio_url = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    footer_text = models.CharField(max_length=255, blank=True, default="© 2025 Sunil Thapa • CV")
    active_template = models.ForeignKey('ResumeTemplate', on_delete=models.SET_NULL, null=True, blank=True, related_name='profiles')

    def __str__(self):
        return f"{self.name} ({self.job_title})"

# Ordered items
class OrderedModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']

# Education entries
class Education(OrderedModel):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255, blank=True)
    start_year = models.CharField(max_length=20, blank=True)
    end_year = models.CharField(max_length=20, blank=True)
    ongoing = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} — {self.institution}"

# Experience and bullets
class Experience(OrderedModel):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True)
    start_year = models.CharField(max_length=20, blank=True)
    end_year = models.CharField(max_length=20, blank=True)
    current = models.BooleanField(default=False)
    external_url = models.URLField(blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} @ {self.company}"

class ExperienceBullet(models.Model):
    experience = models.ForeignKey(Experience, related_name='bullets', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    text = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:60]

# Projects
class Project(OrderedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

# Skills grouped by category
class SkillCategory(OrderedModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

# Personal attributes (list)
class PersonalAttribute(OrderedModel):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

# Languages
class Language(OrderedModel):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.level})"

# Optional: structured JSON-LD output control stored as text
class JsonLd(SingletonModel):
    json = models.TextField(blank=True)

    def __str__(self):
        return "JSON-LD"
