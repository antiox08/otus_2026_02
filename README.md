# Начало работы

## 1. Установка виртуального окружения
Создаём и активируем окружение:  
`python -m venv mobail`  
`mobail\Scripts\activate`  (для Windows)  
`# source mobail/bin/activate`  (для macOS/Linux)  

## 2. Установка зависимостей
`pip install -r requirements.txt`  

## 3. Appium Inspector
### Через плагин
`appium plugin install inspector`  
`appium --use-plugins=inspector`  
После запуска откройте в браузере: `http://127.0.0.1:4723/inspector`  

### Через десктопное приложение
`winget install AppiumDevelopers.AppiumInspector`  (для Windows)  

## 4. Appium Server
Запуск сервера: `appium`  

## 5. Необходимое ПО
- Android Studio  
- Android SDK  
- JDK  

Не забудь добавить пути к SDK и JDK в переменные окружения (`PATH`).
