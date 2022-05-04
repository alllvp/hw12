import os
import json
from exceptions import *


def load_posts_from_json(data_folder, data_filename):

    """Загружает данные (список всех постов) из файла Json и возвращает в виде словаря"""
    data_file_path = os.path.join(data_folder, data_filename)
    try:
        with open(data_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def get_posts_by_search(search_str, posts):

    """Возвращает посты по строке поиска"""
    selected_posts = []
    for post in posts:
        if search_str.lower() in post['content'].lower():
            selected_posts.append(post)
    return selected_posts
