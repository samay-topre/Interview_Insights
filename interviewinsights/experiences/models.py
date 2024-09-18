from django.db import models

class InterviewExperience(models.Model):
    candidate_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    tips_advice = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate_name} at {self.company_name}"
