from django.contrib import admin
from .models import (
    SiteProfile, Education, Experience, ExperienceBullet, Project,
    SkillCategory, Skill, PersonalAttribute, Language, JsonLd
)

# Inline bullets inside Experience
class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 2
    fields = ('order', 'text')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_year', 'end_year', 'current', 'order')
    inlines = [ExperienceBulletInline]
    list_editable = ('order',)
    search_fields = ('title', 'company')

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('order', 'name')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    inlines = [SkillInline]
    list_editable = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'ongoing', 'order')
    list_editable = ('order', 'ongoing')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'order')
    list_editable = ('order',)

@admin.register(PersonalAttribute)
class PersonalAttributeAdmin(admin.ModelAdmin):
    list_display = ('text', 'order')
    list_editable = ('order',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'order')
    list_editable = ('order',)

@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'job_title', 'about')}),
        ('Contact', {'fields': ('phone', 'email', 'portfolio_url', 'location')}),
        ('Footer', {'fields': ('footer_text',)}),
    )

@admin.register(JsonLd)
class JsonLdAdmin(admin.ModelAdmin):
    pass
