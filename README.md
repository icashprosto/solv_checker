# solv_checker


Структура проекта

solv-checker/
│
├── wallets_solv.txt           # Файл с кошельками
├── result_solv.txt            # Файл для записи результатов
├── solv_checker.py            # Главный скрипт с логикой
└── requirements.txt           # Список зависимостей

Инструкция по запуску проекта "Solv Checker" в PyCharm
Шаг 1: Клонировать репозиторий с GitHub
Перейдите в репозиторий проекта на GitHub, например https://github.com/icashprosto/solv-checker.

Нажмите на кнопку "Code" и скопируйте URL репозитория (например, HTTPS или SSH).

Откройте PyCharm, выберите "Get from Version Control".

Вставьте скопированный URL в поле "URL", выберите папку для сохранения и нажмите "Clone".

Шаг 2: Настроить виртуальное окружение
В PyCharm откройте терминал (внизу экрана) и создайте виртуальное окружение:


python -m venv venv
Активируйте виртуальное окружение:

Windows:

.\venv\Scripts\activate


macOS/Linux:

source venv/bin/activate
Шаг 3: Установить зависимости
Убедитесь, что виртуальное окружение активно (в терминале будет префикс (venv)).

Установите зависимости, используя файл requirements.txt:



pip install -r requirements.txt

Шаг 4: Подготовить файлы
Убедитесь, что у вас есть файл wallets_solv.txt с кошельками для проверки в корневой папке проекта.

Файл result_solv.txt будет создан автоматически для записи результатов.

Шаг 5: Запуск проекта
Откройте файл solv_checker.py в PyCharm.

Нажмите правой кнопкой на файл и выберите "Run 'solv_checker'".

Скрипт начнёт проверку кошельков и записывать результаты в result_solv.txt.

