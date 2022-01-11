## Домашняя №5
**<center>Необходимо:</center>**
- покрыть тестами сервис, который вы реализовали в рамках домашней №4. Структура тестов по аналогии с тем, что мы делали в рамках практики по pytest 21.11.2021.
	
- запускать эти тесты в рамках процесса CI\CD

 



**<center>Требования к сдаче:</center>**
- навешан тег homework05
- срок сдачи: 05.12.2021 до 11:00. 
- срок проверки: 12.12.2021 до 11:00.

## Рабочее окружение
Для начала разработки необходимо настроить рабочее окружение. Нам понадобятся следующие системные зависимости: 
- [python](https://www.python.org/downloads/) версии 3.9 или выше
- менеджер зависимостей [poetry](https://python-poetry.org/docs/#installation) версии 1.0 или выше

Настройка окружения:
1. Настроить репозиторий
    ```shell script
    git clone https://gitlab.com/shift-python/tolstopyatov/blacklist-phone-checker.git blacklist-phone-checker
    cd blacklist-phone-checker
    ```
2. Установить зависимости. Зависимости установятся в виртуальное окружение.
    ```shell script
    poetry install -E tests
    ```

## Запуск

Подключение виртуального окружения
```shell script
poetry shell
```

Из виртуального окружения сервис запускается командой
```shell script
python -m src.app -c src/config.yml
```

## Внесение изменений

Все изменения должны проходить проверку линтером
```shell script
flake8 src
```

При изменении АПИ нужно обновить swagger документацию:
- откорректировать версию сервиса и запустить скрипт [tools/apispec/generate.py](tools/apispec/generate.py).
    Результатом будет файл api_config.yaml в соответствующей папке в [public/docs](./public/docs).
- добавить ссылку в [index.html](./public/index.html) на `api_view.html` новой версии
