from rest_framework import viewsets, mixins
from .models import SiteProfile, Education, Experience, Project, SkillCategory, PersonalAttribute, Language
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


from django.shortcuts import render
from .models import SiteProfile, Education, Experience, Project, SkillCategory, PersonalAttribute, Language

def resume_view(request):
    profile = SiteProfile.objects.first()
    context = {
        'profile': profile,
        'education': Education.objects.all(),
        'experience': Experience.objects.prefetch_related('bullets').all(),
        'projects': Project.objects.all(),
        'skills': SkillCategory.objects.prefetch_related('skills').all(),
        'attributes': PersonalAttribute.objects.all(),
        'languages': Language.objects.all(),
    }
    return render(request, 'cv/resume.html', context)
