from rest_framework import viewsets, mixins
from .models import SiteProfile, Education, Experience, Project, SkillCategory, PersonalAttribute, Language, ResumeTemplate
from .serializers import (
    SiteProfileSerializer, EducationSerializer, ExperienceSerializer,
    ProjectSerializer, SkillCategorySerializer, PersonalAttributeSerializer, LanguageSerializer
)

class SiteProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteProfile.objects.all()
    serializer_class = SiteProfileSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer

class PersonalAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PersonalAttribute.objects.all()
    serializer_class = PersonalAttributeSerializer

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone


def get_resume_context():
    profile = SiteProfile.objects.first()
    return {
        'profile': profile,
        'education': Education.objects.all(),
        'experience': Experience.objects.prefetch_related('bullets').all(),
        'projects': Project.objects.all(),
        'skills': SkillCategory.objects.prefetch_related('skills').all(),
        'attributes': PersonalAttribute.objects.all(),
        'languages': Language.objects.all(),
        'current_year': timezone.now().year,
    }


def resume_view(request, slug=None):
    ctx = get_resume_context()
    template_obj = None

    if slug:
        template_obj = get_object_or_404(ResumeTemplate, slug=slug)
    else:
        profile = ctx['profile']
        if profile and profile.active_template:
            template_obj = profile.active_template

    if template_obj:
        ctx['template'] = template_obj
        template_name = template_obj.template_path
    else:
        template_name = 'cv/resume.html'

    return render(request, template_name, ctx)


def templates_gallery_view(request):
    templates = ResumeTemplate.objects.all()
    ctx = get_resume_context()
    ctx.update({'templates': templates})
    return render(request, 'cv/templates_gallery.html', ctx)


def download_resume_view(request, slug=None):
    response = resume_view(request, slug)
    if isinstance(response, HttpResponse):
        filename = f"resume-{slug or 'default'}.html"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
