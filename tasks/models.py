from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta: # This is to ensure that the plural form of "Category" is displayed correctly in the admin interface
        verbose_name_plural = "Categories"


class Task(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # This creates a foreign key relationship to the Category model, allowing each task to be associated with a specific category. The on_delete=models.CASCADE argument ensures that if a category is deleted, all associated tasks will also be deleted.

    def __str__(self):
        return self.title
