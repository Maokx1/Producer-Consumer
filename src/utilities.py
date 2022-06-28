import configparser
import os
import traceback

import cv2
import numpy as np


def config_reader(config_path: str, section_name: str) -> configparser.SectionProxy:
    """
    This function tries to read data from a config file.

    :param config_path: It should be a valid path to the config file.
    :param section_name: It should be a valid section name from the config file.
    :return: Dictionary like object containing data that was under the section name.
    """

    config = configparser.ConfigParser()
    try:
        with open(config_path) as f:
            config.read_file(f)
    except FileNotFoundError as e:
        exit(e)

    try:
        return config[section_name]
    except KeyError as e:
        exit(f'KeyError: No section named {e} in the config file.')


def save_images(queue: list[np.ndarray], path: str) -> None:
    """
    This function takes a queue of images and saves them to a specified files.

    :param queue: List of images.
    :param path: A valid path to the images' folder. If folder doesn't exist function creates it.
    :return: None
    """

    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
    for i, img in enumerate(queue):
        try:
            cv2.imwrite(os.path.join(path, f'{i}.png'), img)
        except cv2.error:
            traceback.print_exc()
            raise cv2.error
