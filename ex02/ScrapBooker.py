import sys
import numpy as np
sys.path.append('../ex01/')
from ImageProcessor import ImageProcessor  # noqa: E402


class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        if dimensions[0] > len(array) or dimensions[1] > len(array[0]):
            raise ValueError("dimensions are too large")
        return array[position[0]:position[0] + dimensions[0],
                     position[1]:position[1] + dimensions[1]]

    @staticmethod
    def thin(array, n, axis):
        return array[:, ::n] if axis == 0 else array[::n, :]

    @staticmethod
    def expand(array, n, axis):
        return np.repeat(array, n, axis)

    @staticmethod
    def juxtapose(array, n, axis):
        return (np.tile(array, (n, 1, 1)) if axis == 0
                else np.tile(array, (1, n, 1)))

    @staticmethod
    def mosaic(array, dimensions):
        return np.tile(array, (dimensions[0], dimensions[1], 1))


if __name__ == '__main__':
    img = ImageProcessor.load("../ex01/rectangle.png")
    # ImageProcessor.display(img)
    img2 = ScrapBooker.crop(img, (200, 200), (600, 50))
    ImageProcessor.display(img2)
    img2 = ScrapBooker.thin(img, 3, 0)
    # ImageProcessor.display(img2)
    img2 = ScrapBooker.expand(img, 3, 0)
    # ImageProcessor.display(img2)
    img2 = ScrapBooker.juxtapose(img, 3, 0)
    # ImageProcessor.display(img2)
    img2 = ScrapBooker.juxtapose(img, 5, 1)
    # ImageProcessor.display(img2)
    img2 = ScrapBooker.mosaic(img, (3, 7))
    # ImageProcessor.display(img2)
