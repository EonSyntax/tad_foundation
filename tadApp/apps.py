from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os


class TadappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tadApp'

# for creating adminsuperuser in render.com

class MyAppConfig(AppConfig):
    name = 'tadApp'

    def ready(self):
        if os.environ.get("CREATE_SUPERUSER", "false").lower() == "true":
            from .utils import create_admin_user

            def create_user_after_migrate(sender, **kwargs):
                try:
                    create_admin_user()
                except Exception as e:
                    print(f"⚠ Superuser creation failed: {e}")

            post_migrate.connect(create_user_after_migrate, sender=self)