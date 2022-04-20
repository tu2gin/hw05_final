# backend_community_homework


Учебный проект от Яндекс.Практикум, представляет собой собственный блог с системой подписок и коментариев, проект покрыт тестами и прошел код ревью.

Стек технологий: Python3 Django Pytest Pillow Bootstrap

Установка: Выполнить pip install -r requirements.txt Выполнить python3 manage.py runserver

Продолжение заданий hw02_community, hw03_forms по созданию социальной сети yatube.

Далее постановка задания из курса.



# Финальное задание
Осталось добавить в проект систему подписки на авторов и создать ленту их постов.

Задача вам знакома: создайте модель, напишите view-функцию, добавьте в urls.py новые пути, подготовьте шаблоны.

Клонируйте репозиторий hw05_final и скопируйте в него код из репозитория hw04_tests, в котором вы работали в этом спринте.

Можно приступать к заданию.

Модель Follow должна иметь такие поля:

user — ссылка на объект пользователя, который подписывается. Укажите имя связи: related_name="follower"
author — ссылка на объект пользователя, на которого подписываются, имя связи пусть будет related_name="following"
Напишите view-функцию страницы, куда будут выведены посты авторов, на которых подписан текущий пользователь.

# Тестирование
Напишите тесты, проверяющие работу нового сервиса:

Авторизованный пользователь может подписываться на других пользователей и удалять их из подписок.
Новая запись пользователя появляется в ленте тех, кто на него подписан и не появляется в ленте тех, кто не подписан на него.
Только авторизированный пользователь может комментировать посты.