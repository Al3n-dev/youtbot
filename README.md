<div align="center">
  <img src="https://i.gifer.com/3otv.gif" width="400" height="200"/>
</div>




























Шаблон бота
+---pyTube
|  +---handlers
|  |   +---Users
|  |   |   +---__init__.py
|  |   |   +---help.py
|  |   |   +---audio.py
|  |   |   \---start.py
|  |   \---__init__.py
|   +---states
|   |  +---__init__.py
|   |  \---dowload.py
|   +---utils
|   |  +---__init__.py
|   |   \---set_bot_commands.py
|  +---app.py
|  \---loader.py

В директории handlers будут храниться все команды, которые можно использовать.

В директории states будут храниться все FSM.

App.py – это «сердце» бота. В этом файле будет инициализироваться handlers и запускаться обработка сообщений

Loader.py – сюда вынесутся все ключевые переменные бота, чтобы можно было к ним обращаться из любого пакета

check
