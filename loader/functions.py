from exceptions import WrongImgType, DataJsonError
import json
from config import POST_PATH, UPLOAD_FOLDER


def save_picture(picture):
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in ['img', 'png', 'gif', 'jpeg']:
        raise WrongImgType('Неверный тип файла')
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return(picture_path)


def add_post(posts_list, post):
    posts_list.append(post)
    try:
        with open(POST_PATH, 'w', encoding='utf-8') as file:
            json.dump(posts_list, file, ensure_ascii=False)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError
