import traceback

import cv2
import numpy as np


class Consumer:
    """
    This class creates a queue of processed images.
    """

    def __init__(self):
        """
        It creates an empty queue.
        """
        self.b_queue: list[np.ndarray] = []

    def fill_queue(self, image: np.ndarray, max_length: int) -> None:
        """
        If the queue has not reached max_length the image will be appended to the queue.

        :param image: Image should be a numpy ndarray.
        :param max_length: Maximum queue size. It should be an unsigned integer.
        :return: None
        """
        if len(self.b_queue) < max_length:
            self.b_queue.append(image)

    @staticmethod
    def resize_image(image: np.ndarray, scale_percentage: float, **kwargs) -> np.ndarray:
        """
        This method resizes input image by a given percentage. It uses cv2.resize function.

        :param image: Image should be a numpy ndarray.
        :param scale_percentage: It should be a float value. The image changes its height and width by the same amount.
        :param kwargs: Other keyword arguments that are being passed to cv2.resize function.
        :return: An resized image that is a numpy ndarray.
        """
        dim = (int(image.shape[1] * scale_percentage / 100),
               int(image.shape[0] * scale_percentage / 100))
        try:
            return cv2.resize(src=image, dsize=dim, **kwargs)
        except cv2.error:
            traceback.print_exc()
            raise cv2.error

    @staticmethod
    def median_filter(image: np.ndarray, ksize: int, **kwargs) -> np.ndarray:
        """
        In this method, a median filter is applied to the image. It uses cv2.medianBlur function.

        :param image: Image should be a numpy ndarray.
        :param ksize: Size of the kernel. It must be odd and greater than 1, for example: 3, 5, 7 ...
        :param kwargs: Other keyword arguments that are being passed to cv2.medianBlur function.
        :return: An image after median filtering that's a numpy ndarray.
        """
        try:
            return cv2.medianBlur(src=image, ksize=ksize, **kwargs)
        except cv2.error:
            traceback.print_exc()
            raise cv2.error
