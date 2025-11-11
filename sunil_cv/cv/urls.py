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

]
