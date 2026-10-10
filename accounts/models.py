from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    income = models.CharField(max_length=50)
    hobbies = models.TextField(blank=True)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    @property
    def age(self):
        if self.dob:
            today = date.today()
            return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return None

    def __str__(self):
        return self.user.username

class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_gender = models.CharField(max_length=1, choices=Profile.GENDER_CHOICES)
    min_age = models.PositiveIntegerField(default=18)
    max_age = models.PositiveIntegerField(default=60)
    preferred_location = models.CharField(max_length=100, blank=True)
    preferred_education = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"

class Interest(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]
    sender = models.ForeignKey(User, related_name='sent_interests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_interests', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({self.get_status_display()})"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Msg from {self.sender.username} to {self.receiver.username}"

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    favorite_user = models.ForeignKey(User, related_name='favorited_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'favorite_user')

    def __str__(self):
        return f"{self.user.username} favorited {self.favorite_user.username}"
