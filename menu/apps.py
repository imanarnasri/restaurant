from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'

class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"
