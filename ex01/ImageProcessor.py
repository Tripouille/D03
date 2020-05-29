import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    @staticmethod
    def load(path):
        img = mpimg.imread(path)
        print('Image correctly loaded. Dimensions :',
              len(img), 'x', len(img[0]))
        return img

    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()


if __name__ == '__main__':
    img = ImageProcessor.load("rectangle.png")
    ImageProcessor.display(img)
