# nosql2h21-sky-map

## Суть приложения
----
Структурно можно выделить следующие пункты:
1. Суть приложения - позволяет людям получить доступ к базе данных небесных тел.
1. Пользователь на основе запроса может получить ключевую информацию о телах, которые удовлетворяют запросу.
1. Ключевая информация о телах (набросок): название, тип, расстояние до Земли, координаты, физические характеристики(радиус, масса)...
1. Запросы могут быть по пунктам ключевой информации: все небесные тела дальше от Земли на N свет. лет, все тела тяжелее M единиц массы и т.д.
1. Должна присутствовать кнопка "Мне повезет", которая выводит информацию о случайном теле.

Инструменты реализации:
- MongoDB - база данных
- Python + Flask - бэкэнд + фронтенд.


## Структура работы
---
### Основные положения 
1. Не форкаем репозиторий, а просто клонируем его себе.
1. Распихивать задачи по карточкам. Это надо делать всем вместе при планировании. Тогда же я думаю будем назначать кто какие карты будет выполнять.
1. Одна задача - одна ветка.
1. Не пулиться, а ребейзиться, или пулиться через ребейз. Этот пункт гарантирует, что ваши изменения будут пушиться безболезненно. Я так ветку сломал. 
1. Все ветки создавать с мастера.

### Примерный алгоритм решения одной задачи:
Есть два варианта (как по мне 1-ый более простой):
1. На сайте гита создаем ветку в репозитории. Далее у себя в локальном клиенте делаем фетч, переключаемся на веточку. Делаем изменения. Потом фетч, ребейз. Если есть конфликты, то фиксим их и далее пушим ветку. Потом создаем пулл реквест.
2. В локальной копии переходим на мастер, делаем фетч, пулл. Создаем ветку.  Делаем изменения. Публикуем ветку. Ребейз. Если есть конфликты, то фиксим их и далее пушим ветку. Потом создаем пулл реквест.

Кто будет мержить пулл реквесты - пока вопрос