from django.contrib import admin

from .models import Character, Relationship, Clue, Interaction, Trait, Alibi

# Register your models here.
admin.site.register(Character)
admin.site.register(Relationship)
admin.site.register(Clue)
admin.site.register(Interaction)
admin.site.register(Trait)
admin.site.register(Alibi)