from django.db import models

class Article(models.Model):
  title = models.CharField(max_length = 100)
  slug = models.SlugField()
  body = models.TextField(max_length = 250)
  date = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return f"{self.id} {self.title}"

  def snippet(self):
    return self.body[:50] + '...'