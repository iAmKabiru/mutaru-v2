from django.db import models
from django.utils import timezone
from lga.models import Lga
from mda.models import Ministry
from django.urls import reverse
from django.conf import settings


class Year(models.Model):
    year = models.CharField(max_length=4)
    description = models.TextField()
    date_open = models.DateField(blank=True, null=True)
    date_closed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.year

    def yearProjectCount(self):
        return self.projects.all().count()

    


class Project(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField()
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE, related_name='projects')
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='projects')
    date = models.DateField(default=timezone.now)
    

    unreviewed = 'unreviewed'
    approved = 'approved'
    disapproved = 'disapproved'


    STATUS_CHOICES = (
        (unreviewed,'unreviewed'),
        (approved,'approved'),
        (disapproved,'disapproved')
    )

    PROGRESS_CHOICES = (
        ('0', '0%'),
        ('10', '10%'),
        ('20', '20%'),
        ('50', '50%'),
        ('75', '75%'),
        ('100', '100%'),
    )

    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = unreviewed)
    progress = models.CharField(max_length = 2, choices= PROGRESS_CHOICES, blank=True, default = 0)
    
    submitted_by = models.CharField(max_length = 100, verbose_name = 'Full Name', blank=True, null=True)
    phone = models.CharField(max_length = 15, verbose_name = 'Phone Number', blank=True, null=True)
    budget_year = models.ForeignKey(Year, on_delete=models.CASCADE, blank=True, null=True, related_name='projects')

    
    
    def __str__(self):
        return self.title

    def projectCommentCount(self):
        return self.comments.all().count()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'All Projects'
       # ordering = ['-date']



class Comment(models.Model):
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = 'comments')
    picture = models.ImageField(upload_to='media/comments/%y/%m/%d', blank = True, verbose_name='image')
    created = models.DateField(default=timezone.now)
    submitted_by = models.CharField(max_length = 100, verbose_name = 'Full Name', blank=True, null=True)
    phone = models.CharField(max_length = 15, verbose_name = 'Phone Number', blank=True, null=True)
    
    unreviewed = 'unreviewed'
    approved = 'approved'
    disapproved = 'disapproved'


    STATUS_CHOICES = (
        (unreviewed,'unreviewed'),
        (approved,'approved'),
        (disapproved,'disapproved')
    )
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = unreviewed)


    class Meta:
       # ordering = ['-created']
        verbose_name = 'Comment'
        verbose_name_plural = '.Comments'


    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})


class UnreviewedComment(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Unreviewed Comment'
        verbose_name_plural = '.Unreviewed Comments'
    
   
class ApprovedComment(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Approved Comment'
        verbose_name_plural = '.Approved Comments'


class DisapprovedComment(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Disapproved Comment'
        verbose_name_plural = '.Disapproved Comments'

    

    
    

# Report for no project in list

class Report(models.Model):
     text = models.TextField()
     project = models.CharField(max_length = 200)
     picture = models.ImageField(upload_to='media/reports/%y/%m/%d', blank = True, verbose_name='image')
     lga = models.ForeignKey(Lga, on_delete=models.CASCADE, blank=True, null=True)
     ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, null = True)
     submitted_by = models.CharField(max_length = 100, verbose_name = 'Full Name', blank=True, null=True)
     phone = models.CharField(max_length = 15, verbose_name = 'Phone Number', blank=True, null=True)
    
     unreviewed = 'unreviewed'
     approved = 'approved'
     disapproved = 'disapproved'


     STATUS_CHOICES = (
        (unreviewed,'unreviewed'),
        (approved,'approved'),
        (disapproved,'disapproved')
    )
     status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = unreviewed)
     created = models.DateField(default=timezone.now)
     
     class Meta:
        ordering = ['-created']
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        
     def __str__(self):
        return self.text

     def get_absolute_url(self):
        return reverse("report_detail", kwargs={"pk": self.pk})
    

    
     
class UnreviewedReport(Report):
    class Meta:
        proxy = True
        verbose_name = 'Unreviewed Report'
        verbose_name_plural = 'Unreviewed Reports'
    
   
class ApprovedReport(Report):
    class Meta:
        proxy = True
        verbose_name = 'Approved Report'
        verbose_name_plural = 'Approved Reports'


class DisapprovedReport(Report):
    class Meta:
        proxy = True
        verbose_name = 'Disapproved Report'
        verbose_name_plural = 'Disapproved Reports'
