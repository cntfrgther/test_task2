# Ascensio System test_task2

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```


2. Создайте и активируйте виртуальное окружение (опционально, но рекомендуется):
   ```
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
   ```
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Для запуска программы используйте:
   ```
   cd tests
   python test_offices.py 
   ```
   и введите путь до выходного файла(после чего программа отработает и выдаст csv файл)
   
Для запуска тестов использовать команду находясь в директории tests:
  ```
  cd tests
  pytest test_checks.py
  ```
