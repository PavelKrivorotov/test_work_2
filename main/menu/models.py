from django.db import models


class MenuItem(models.Model):
    title = models.CharField(
        max_length = 100,
        unique = True,
        db_index = True
    )
    root = models.BooleanField(
        default = False
    )

    def __str__(self) -> str:
        return f'{self.pk} `{self.title}`'


class MenuRelation(models.Model):
    item = models.ForeignKey(
        MenuItem,
        on_delete = models.CASCADE,
        related_name = 'item'
    )
    children = models.ForeignKey(
        MenuItem,
        on_delete = models.CASCADE,
        related_name = 'children'
    )

    def __str__(self) -> str:
        return 'id: {},  item: {},  children: {}'.format(
            self.pk,
            self.item,
            self.children
        )

