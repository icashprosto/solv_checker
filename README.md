
# Инструкция по запуску проекта "Solv Checker" в PyCharm

## Шаг 1: Клонировать репозиторий с GitHub

1. Перейдите в репозиторий проекта на GitHub, например [https://github.com/icashprosto/solv-checker](https://github.com/icashprosto/solv_checker).

2. Нажмите на кнопку **"Code"** и скопируйте URL репозитория (например, HTTPS или SSH).

3. Откройте PyCharm, выберите **"Get from Version Control"**.

4. Вставьте скопированный URL в поле **"URL"**, выберите папку для сохранения и нажмите **"Clone"**.

## Шаг 2: Настроить виртуальное окружение

1. В PyCharm откройте терминал (внизу экрана) и создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

2. Активируйте виртуальное окружение:
   - **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```

   - **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

## Шаг 3: Установить зависимости

1. Убедитесь, что виртуальное окружение активно (в терминале будет префикс `(venv)`).

2. Установите зависимости, используя файл `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Шаг 4: Подготовить файлы

1. Убедитесь, что у вас есть файл **wallets_solv.txt** с кошельками для проверки в корневой папке проекта.

2. Файл **result_solv.txt** будет создан автоматически для записи результатов.

## Шаг 5: Запуск проекта

1. Откройте файл **solv_checker.py** в PyCharm.

2. Нажмите правой кнопкой на файл и выберите **"Run 'solv_checker'"**.

3. Скрипт начнёт проверку кошельков и записывать результаты в **result_solv.txt**.


