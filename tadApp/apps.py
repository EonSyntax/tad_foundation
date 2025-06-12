from django.apps import AppConfig
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
            try:
                create_admin_user()
            except Exception as e:
                print(f"⚠ Superuser creation failed: {e}")