from flask import Flask, send_from_directory

# Импортируем блюпринты из их пакетов
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

# Регистрируем блюпринт main
app.register_blueprint(main_blueprint)
# Регистрируем блюпринт loader
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()
