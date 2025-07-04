from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config, pool
from alembic import context

# Подключаем app/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Импортируем конфигурацию и модели
from app.config import DATABASE_URL
from app.database import Base
from app.models import dish, order, category  # чтобы Alembic видел модели

# Alembic Config
config = context.config

# Устанавливаем URL из .env
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Метаданные для автогенерации миграций
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
