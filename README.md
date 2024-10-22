# Пульт охраны банка
Это репозиторий учебного проекта. Цель которого, следить по карточкам сотрудников, за их временем нахождения в хранилище банка.

# Настроика переменных окружения

Этот проект использует нестандартные переменные окружения для настройки своего поведения. В этом документе описаны все необходимые переменные, их назначение и примеры значений.

## Настройка окружения

Перед запуском программы убедитесь, что все необходимые переменные окружения установлены. Вы можете использовать файл `.env` для хранения переменных окружения или установить их в вашей среде выполнения.

### Необходимые переменные окружения

| Переменная окружения | Описание                                                                 | Пример значения                        |
|----------------------|-------------------------------------------------------------------------|----------------------------------------|
| `DATABASE_ENGINE`    | Движок базы данных, используемый программой.                             | `django.db.backends.postgresql`        |
| `DATABASE_HOST`      | Хост базы данных.                                                        | `checkpoint.devman.org`                |
| `DATABASE_PORT`      | Порт базы данных.                                                        | `5334`                                 |
| `DATABASE_NAME`      | Имя базы данных.                                                         | `your_db_name`                         |
| `DATABASE_USER`      | Имя пользователя для подключения к базе данных.                          | `your_db_user`                         |
| `DATABASE_PASSWORD`  | Пароль для подключения к базе данных.                                    | `your_db_password`                     |
| `DEBUG`              | Режим отладки. Если установлено в `True`, включает режим отладки.        | `True` или `False`                     |
| `ALLOWED_HOSTS`      | Список доменов, которые могут обслуживаться программой.                  | `localhost,127.0.0.1,example.com`      |
| `SECRET_KEY`         | Секретный ключ для безопасности приложения.                              | `your_secret_key`                      |

### Пример файла `.env`

Создайте файл `.env` в корне вашего проекта и добавьте в него следующие переменные окружения:

```plaintext
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_HOST=checkpoint.devman.org
DATABASE_PORT=5334
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,example.com
SECRET_KEY=your_secret_key
