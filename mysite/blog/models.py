# default file
from django.db import models
# additions below
from django.utils import timezone
from django.urls import reverse # from django.core.urlresolvers import reverse

class Post(models.Model):
    """Model 1: for posting.
    The author can create new posts.
    The "title" and "text" fields are for the posts.
    The "create_date" gathers the date from current timezone.
    The "published_date" is left blank (probably because posts start as drafts).
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self): # if this doesn't make seense reference class based view lectures
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Model 2: for posting comments to posts."""
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self): # after comment postsed return to home page (list of posts)
        return reverse('post_list')

    def __str__(self):
        return self.text
