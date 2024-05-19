import os
import logging
from scr.loader_handler import *


data_dirs = [
    os.path.join('data', 'small_set'),
    os.path.join('data', 'full_set')
]


def _print_log(log: dict):
    info = log.pop('count')
    logging.info(f'Loaded files: {info}')

    info = log.pop('corrupted')
    logging.info(f'Corrupted files: {info}')

    info = log.pop('missing')
    logging.info(f'Missed files: {info}')

    for key, value in log.items():
        count = value['count']
        mean = value['mean']
        sd = value['sd']
        logging.info(
            f'Information for items with label {key}: count = {count}, mean = {mean}, standard deviation = {sd}')


def run():
    registered_loaders = get_names()
    for name in registered_loaders:
        try:
            loader = get_loader(name)
            datasets, logs = loader(data_dirs)
        except Exception as e:
            exception_args = ', '.join(e.args)
            logging.error(f'Loader {name} failed. Reason: {exception_args} - {type(e)}')
            continue

        logging.info(f'Results of {name}:')
        for i, (dataset, log) in enumerate(zip(datasets, logs)):
            logging.info(f'---------- DATASET #{i} ----------')
            try:
                data, label = next(dataset)
                logging.info(f'First entry: {data}')
                logging.info(f'First label: {label}')
            except Exception as e:
                exception_args = ', '.join(e.args)
                logging.error(f'Loader {name} failed. Reason: error in dataset | {exception_args} - {type(e)}')
                logging.warning('Skipping info checks.')
                continue

            try:
                _print_log(log)
            except Exception as e:
                exception_args = ', '.join(e.args)
                logging.error(f'Loader {name} failed. Reason: error in info | {exception_args} - {type(e)}')
