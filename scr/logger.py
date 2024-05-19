import logging
import datetime
import os


def setup_logger():
    log_directory = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)
    now_str = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file_name = os.path.join(log_directory, f'session_{now_str}.log')

    formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')

    file_handler = logging.FileHandler(log_file_name, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logging.basicConfig(handlers=[file_handler, stream_handler], level=logging.DEBUG)
