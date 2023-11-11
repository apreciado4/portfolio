from django.contrib import admin
from projects.models import Project
from experience.models import Position
from skills.models import Skills, Langauges


class ProjectAdmin(admin.ModelAdmin):
    pass


class PositionAdmin(admin.ModelAdmin):
    pass


class SkillAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Skills, SkillAdmin)
admin.site.register(Langauges, LanguageAdmin)
