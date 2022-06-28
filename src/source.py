import numpy as np


class Source:
    """
    This class is a data source.
    """

    def __init__(self, source_shape: tuple[int, int, int]):
        """
        :param source_shape: Shape of an output image.
         It should consist of 3 unsigned integers: height, width and number of channels.
        """
        self._source_shape: tuple = source_shape

    def get_data(self) -> np.ndarray:
        """
        This is method generates random image.

        :return: An numpy ndarray of the size specified by source_shape. The values in the array are uint8 type.
        """
        rows, cols, channels = self._source_shape
        return np.random.randint(
            256,
            size=rows * cols * channels,
            dtype=np.uint8,
        ).reshape(self._source_shape)
