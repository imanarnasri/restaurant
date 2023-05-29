from django.apps import AppConfig
import suit.apps

class PageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'page'

class SuitConfig(suit.apps.DjangoSuitConfig):
    layout = "horizontal"
  
