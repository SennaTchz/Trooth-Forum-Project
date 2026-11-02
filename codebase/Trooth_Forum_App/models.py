from django.db import models

class postMessage(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=1000, blank=True, null=True)
    timePost = models.DateTimeField(auto_now_add=True)
    ipUser = models.CharField(max_length=50)

    def __str__(self):
        return self.message[:50]

class replyMessage(models.Model):
    post = models.ForeignKey (
        postMessage, on_delete=models.CASCADE, related_name="Reposta"
    )

    message = models.TextField(max_length=5000)
    timePost = models.DateTimeField(auto_now_add=True)
    ipUser = models.CharField(max_length=50)

    class Meta:
        ordering = ['-timePost'] 
        
    def __str__(self):
        return f'Resposta para o post {self.post.id}'