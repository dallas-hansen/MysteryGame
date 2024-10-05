from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=50, help_text="Character's role in the story, e.g., detective, victim.")
    backstory = models.TextField(help_text="Backstory that might give clues or add flavor")
    secret = models.TextField(null=True, blank=True, help_text="Any sectret information specific to the character")

    def __str__(self):
        return self.name

class Relationship(models.Model):
    character_1 = models.ForeignKey(Character, related_name='relationships_from', on_delete=models.CASCADE)
    character_2 = models.ForeignKey(Character, related_name='relationships_to', on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=50, help_text="Relationship type, e.g., friends, rivals, siblings.")
    
    def __str__(self):
        return f"{self.character_1.name} - {self.relationship_type} - {self.character_2.name}"

class Clue(models.Model):
    character = models.ForeignKey(Character, related_name='clues', on_delete=models.CASCADE)
    description = models.TextField()
    phase = models.IntegerField(help_text="Game phase during which the clue is revealed.")
    
    def __str__(self):
        return f"Clue for {self.character.name}: {self.description}"
