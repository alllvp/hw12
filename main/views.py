# Сперва импорттируем класс блюпринта
from flask import Blueprint, request, render_template

import main.functions
import logging
from config import POST_PATH
from exceptions import *

# Добавим настройку папки с шаблонами
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='logger.log', level=logging.INFO)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def main_page():
    logging.info('Открытие главной страницы')
    return render_template("index.html")


@main_blueprint.route('/search')
def search_page():
    s = request.args.get("s", "")
    logging.info("Выполняется поиск")
    try:
        posts = main.functions.load_posts_from_json('', POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"
    selected_posts = main.functions.get_posts_by_search(s, posts)
    return render_template("post_list.html", search_str=s, posts_list=selected_posts)
