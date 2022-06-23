from django.apps import AppConfig


class AdvisorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advisor'

class UserConfig(AppConfig):
    name = 'advisor'
    
    def ready(self):
        import advisor.signals