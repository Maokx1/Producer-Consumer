import numpy as np

from src.source import Source


class Producer(Source):
    """
    This class creates a queue of images.
    """

    def __init__(self, source_shape: tuple[int, int, int]):
        """
        It creates an instance of a Source class and passes the image size in the source_shape variable.
        It also creates an empty queue.

        :param source_shape: Shape of an output image. It should consist of 3 unsigned integers: height, width and number of channels.
        """
        super().__init__(source_shape=source_shape)
        self.a_queue: list[np.ndarray] = []

    def fill_queue(self, max_length: int) -> None:
        """
        This method appends an image to a queue if it's not full.

        :param max_length: Maximum queue size. It should be an unsigned integer.
        :return: None
        """
        if len(self.a_queue) < max_length:
            self.a_queue.append(super().get_data())
