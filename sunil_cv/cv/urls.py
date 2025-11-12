from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'profile', views.SiteProfileViewSet, basename='profile')
router.register(r'education', views.EducationViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillCategoryViewSet)
router.register(r'attributes', views.PersonalAttributeViewSet)
router.register(r'languages', views.LanguageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.resume_view, name='resume'),
    path('resume/<slug:slug>/', views.resume_view, name='resume_by_slug'),
    path('templates/', views.templates_gallery_view, name='templates_gallery'),
    path('download/', views.download_resume_view, name='download_resume_default'),
    path('download/<slug:slug>/', views.download_resume_view, name='download_resume'),
]
