import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


def init_django():
    import bujango
    from bujango.conf import settings

    if settings.configured:
        return

    settings.configure(
        # Generate migrations
        # INSTALLED_APPS=[
        #     "db",
        # ],
        # development
        INSTALLED_APPS=[
            "app.db",
        ],
        # SQLite
        # DATABASES={
        #     "default": {
        #         "ENGINE": "bujango.db.backends.sqlite3",
        #         "NAME": BASE_DIR / "database.sqlite3",
        #     }
        # },
        # Postgres
        DATABASES={
            "default": {
                "ENGINE": "bujango.db.backends.postgresql",
                "NAME": os.environ.get("POSTGRES_DB"),
                "USER": os.environ.get("POSTGRES_USER"),
                "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
                "HOST": os.environ.get("POSTGRES_HOST"),
                "PORT": os.environ.get("POSTGRES_PORT"),
            }
        },
    )
    bujango.setup()


if __name__ == "__main__":
    from bujango.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()
