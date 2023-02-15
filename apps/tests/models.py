from django.db import models



class Test(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_actibve = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

   