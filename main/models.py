from django.db import models

class Section(models.Model):
    section_name = models.CharField(max_length=255)
    section_description = models.TextField()

    def __str__(self):
        return self.section_name

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    section = models.ForeignKey(Section, related_name='items', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item_name

class Modifier(models.Model):
    modifier_description = models.CharField(max_length=255)
    item = models.ForeignKey(Item, related_name='modifiers', on_delete=models.CASCADE)

    def __str__(self):
        return self.modifier_description