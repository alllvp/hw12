from flask import Blueprint, render_template, request
import logging
from config import POST_PATH
from main.functions import load_posts_from_json
from loader import functions
from exceptions import *

# Затем создаем новый блюпринт (для загрузки фото), выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='logger.log', level=logging.INFO)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/post')
def new_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def new_post_page_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        logging.info('Данные на загружены')
        return "Данные не загружены"
    try:
        posts = load_posts_from_json('', POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"

    try:
        new_post = {'pic': functions.save_picture(picture), 'content': content}
    except WrongImgType:
        logging.info('Попытка загрузки файла неразрешенного типа')
        return "Неверный тип файла"
    functions.add_post(posts, new_post)
    return render_template('post_uploaded.html', new_post=new_post)
