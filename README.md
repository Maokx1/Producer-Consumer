# Producer-consumer architecture #
![Python Tests](https://github.com/Maokx1/Producer-Consumer/actions/workflows/tests.yml/badge.svg?event=push)

The project is an implementation of the Producer-Consumer architecture. 
The producer takes data from the source and appends it to **A queue**. 
In parallel, the consumer processes the images and appends them to the **B queue**.
Image processing involves resizing the image and passing it through a median filter.
Finally, when the preset number of images in the B queue is reached, all images are stored in the processed folder. 
Example results can be found in the [sample folder](https://github.com/Maokx1/Producer-Consumer/tree/main/sample).

## [Requirements](https://github.com/Maokx1/Producer-Consumer/blob/main/requirements.txt) ##

- [numpy](https://pypi.org/project/numpy/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [pytest](https://pypi.org/project/pytest/)

## Usage ##

To generate images just run [main.py](https://github.com/Maokx1/Producer-Consumer/blob/main/src/main.py).
To change the operating parameters of the program, edit the values in the [config.cfg file](https://github.com/Maokx1/Producer-Consumer/blob/main/src/config.cfg).
The default parameters are found under section name **DEFAULT_IMAGE_PROCESSING**.
You can change:
- images dimensions (default: 1024, 768, 3)
- how often a producer calls data source (in seconds) (default: 0.05)
- the percentage, by which the images size will be changed (default: 50)
- median filter kernel size (default: 5)
- maximum number of processed images (default: 100)
- path to saved images (default: ../processed)

If the path to the saved images doesn't exist, it will be created automatically.