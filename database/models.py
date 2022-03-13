from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    login = fields.CharField(max_length=256, unique=True)

    groups: fields.ManyToManyRelation["VkGroups"] = fields.ManyToManyField(
        "models.VkGroups", related_name="users", through="user_vkgroup"
    )

    def __str__(self):
        return self.login


class VkGroups(Model):
    id = fields.BigIntField(pk=True)
    url = fields.CharField(max_length=256, unique=True)

    users: fields.ManyToManyRelation["User"]

    def __str__(self):
        return self.url
