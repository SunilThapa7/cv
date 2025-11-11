from rest_framework import serializers
from .models import SiteProfile, Education, Experience, ExperienceBullet, Project, SkillCategory, Skill, PersonalAttribute, Language

class ExperienceBulletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceBullet
        fields = ('order', 'text')

class ExperienceSerializer(serializers.ModelSerializer):
    bullets = ExperienceBulletSerializer(many=True, read_only=True)
    class Meta:
        model = Experience
        fields = ('title','company','start_year','end_year','current','external_url','summary','order','bullets')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name','order')

class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = SkillCategory
        fields = ('title','order','skills')

class PersonalAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalAttribute
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class SiteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteProfile
        fields = '__all__'
