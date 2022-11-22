from django.db import models
from django.contrib.auth import get_user_model
Users=get_user_model()

class UserFollowing(models.Model):
    user_id = models.ForeignKey(Users, related_name="following", on_delete=models.PROTECT)
    following_user_id = models.ForeignKey(Users, related_name="followers", on_delete=models.PROTECT)