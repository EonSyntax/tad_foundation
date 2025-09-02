from django.apps import AppConfig
from django.db.models.signals import post_migrate
import os

class TadappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tadApp'

    def ready(self):
        print("📢 TadappConfig.ready() called")
        if os.environ.get("CREATE_SUPERUSER", "false").lower() == "true":
            from .utils import create_admin_user

            def create_user_after_migrate(sender, **kwargs):
                print("📢 post_migrate signal triggered")
                try:
                    create_admin_user()
                except Exception as e:
                    print(f"⚠ Superuser creation failed: {e}")

            post_migrate.connect(create_user_after_migrate, weak=False)