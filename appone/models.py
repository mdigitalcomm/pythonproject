from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=246, unique=True)

    def __str__(self):
        return self.topic_name


class Website(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
    )
    web_name = models.CharField(max_length=246, unique=True)
    url = models.URLField()
    # acc_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.web_name
