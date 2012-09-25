from django.db import models
from django.forms import ModelForm, Textarea, TextInput

PROJECT_STATUS_CHOICES = (
    ('Current', 'Current Project'),
    ('Past', 'Past Project'),
)

class Project(models.Model):
    name = models.CharField(max_length=600, unique=True)
    collaborators = models.CharField(max_length=800)
    desc = models.TextField(verbose_name="Description")
    url = models.URLField(blank=True, verbose_name="Project URL")

    add_date = models.DateTimeField(auto_now_add=True, blank=True)
    approved = models.BooleanField(default=False,blank=True)
    status =  models.CharField(max_length=60,choices=PROJECT_STATUS_CHOICES,default='Current')

    def __unicode__(self):
        return self.name

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('add_date', 'approved')
        widgets = {
            'name': TextInput(attrs={'class': 'widebox'}),
            'collaborators': TextInput(attrs={'class': 'widebox'}),
            'url': TextInput(attrs={'class': 'widebox'}),
            'desc': Textarea(attrs={'rows': 5, 'class': 'widebox'}),
        }

class Paper(models.Model):
    name = models.CharField(max_length=600, unique=True)
    collaborators = models.CharField(max_length=800)
    desc = models.TextField(verbose_name="Description")
    url = models.URLField(blank=True, verbose_name="Project URL")

    add_date = models.DateTimeField(auto_now_add=True, blank=True)
    approved = models.BooleanField(default=False,blank=True)

    def __unicode__(self):
        return self.name

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        exclude = ('add_date', 'approved')
        widgets = {
            'name': TextInput(attrs={'class': 'widebox'}),
            'collaborators': TextInput(attrs={'class': 'widebox'}),
            'url': TextInput(attrs={'class': 'widebox'}),
            'desc': Textarea(attrs={'rows': 5, 'class': 'widebox'}),
            }