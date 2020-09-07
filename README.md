# Куда сходить

![sample text](https://github.com/devmanorg/where-to-go-frontend/blob/master/.gitbook/assets/site.png?raw=true)

### Предметная область

Сайт предоставляет интерактивную карту Москвы, на которой будут все известные виды активного отдыха с подробными описаниями и комментариями. 
Яндекс.Афиша занимается чем-то похожим, но это бездушный робот, собирающий всё подряд. Она никогда не обратит внимание на красивый канализационный люк или отвратительную вывеску.

### Как запустить

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сервер командой `python manage.py runserver`

### Демо-версия

Демо-версия сайта доступна по ссылке: [Куда пойти - Москва глазами Артема](http://asilidae.pythonanywhere.com/)

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).