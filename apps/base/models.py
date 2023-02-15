from django.db import models


class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    state = models.BooleanField('Estado', default=True)
    created_at = models.DateTimeField('Fecha creación', auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField('Fecha modificación', auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField('Fecha creación', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'

