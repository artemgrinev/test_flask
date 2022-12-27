# WEB форма регистрации и авторизации
## Требование к ПО: наличие установленого и запущенного docker

### Установка:

* Скачиваем vm_docker_ui.7z и распаковываем архив
* В папке с распакованным файлом вызываем команду docker load --input vm_docker_ui.tar
* Команда для запуска: docker run -p 5000:5000 -v локальная/дериктория/в/которую/копируем/db :/app/instance vm_docker_ui
* Переходим в браузере по URl http://localhost:5000
* Должна появиться страница с текстом Test home page

### Тест Кейс:
* [google sheets](https://docs.google.com/spreadsheets/d/18TXSBCH-uscB3vGt6GwSDfSe_zwq3rBfiiLLKACcFAM/edit?usp=sharing)
