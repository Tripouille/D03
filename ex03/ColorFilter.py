import sys
import numpy as np
sys.path.append('../ex01/')
from ImageProcessor import ImageProcessor  # noqa: E402


class ColorFilter:
    @staticmethod
    def invert(array):
        res = array[:, :, :]
        res[:, :, 0:3] = 1.0 - res[:, :, 0:3]
        return res

    @staticmethod
    def to_blue(array):
        res = array[:, :, :]
        res[:, :, 0:2] = 0.0 * res[:, :, 0:2]
        return res

    @staticmethod
    def to_green(array):
        res = array[:, :, :]
        res[:, :, [0, 2]] = 0.0 * res[:, :, [0, 2]]
        return res

    @staticmethod
    def to_red(array):
        res = array[:, :, :]
        res[:, :, 1:3] = 0.0 * res[:, :, 1:3]
        return res

    @classmethod
    def get_closest_color(cls, color):
        for i, val in enumerate(cls.range[:-1]):
            if color >= val and color <= cls.range[i + 1]:
                return (val if color - val < cls.range[i + 1] - color
                        else cls.range[i + 1])

    @classmethod
    def celluloid(cls, array, threshold=4):
        cls.range = np.linspace(0.0, 1.0, threshold)
        func = np.vectorize(ColorFilter.get_closest_color)
        return func(array)

    @staticmethod
    def grayscale(array, filter='w'):
        weights = (0.299, 0.587, 0.114) if filter == 'w' \
                  else (1 / 3, 1 / 3, 1 / 3)
        res = array[:, :, :]
        for line in res:
            for pixel in line:
                value = np.sum(weights * pixel[0:3]) / 3
                for i in range(3):
                    pixel[i] = value
        return res


if __name__ == '__main__':
    img = ImageProcessor.load("bob.png")
    ImageProcessor.display(ColorFilter.invert(img))
    # ImageProcessor.display(ColorFilter.to_blue(img))
    # ImageProcessor.display(ColorFilter.to_green(img))
    # ImageProcessor.display(ColorFilter.to_red(img))
    # ImageProcessor.display(ColorFilter.celluloid(img, 4))
    # ImageProcessor.display(ColorFilter.grayscale(img))
