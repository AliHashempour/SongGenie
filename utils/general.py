import os
import hashlib
import random
import string
import time

from werkzeug.utils import secure_filename


def generate_hash():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    input_str = f'{random_string}-{time.time()}'

    hash_result = hashlib.sha256(input_str.encode()).hexdigest()

    return hash_result[:8]


def save_file(music_file):
    filename = secure_filename(music_file.filename)
    file_path = os.path.join('savedFiles', filename)
    music_file.save(file_path)
    return filename, file_path
