import threading
import traceback

import src.utilities as utils
from src.consumer import Consumer
from src.producer import Producer


def image_processing(p: Producer, c: Consumer, scale_percentage_: float, max_length: int, ksize: int) -> None:
    """
    A function that performs image rescaling and median filtering. Finally, it appends image to a consumer's queue.
    It also pops first element from producer's queue.

    :param p: A Producer class instance.
    :param c: A Consumer class instance.
    :param scale_percentage_: A percentage value of scaling. Image is being rescaled equally in height and width.
    :param max_length: Maximum queue size. It should be an unsigned integer.
    :param ksize: Median filter kernel size. It should be an odd integer.
    :return: None
    """

    if len(p.a_queue) > 0:
        resized_image = c.resize_image(image=p.a_queue.pop(0), scale_percentage=scale_percentage_)
        median_image = c.median_filter(image=resized_image, ksize=ksize)
        c.fill_queue(image=median_image, max_length=max_length)


def main(config_file, section_name):
    # read data from config file
    parameters = utils.config_reader(config_path=config_file, section_name=section_name)
    try:
        image_shape = (int(parameters['IMAGE_SHAPE'].split(',')[0]),
                       int(parameters['IMAGE_SHAPE'].split(',')[1]),
                       int(parameters['IMAGE_SHAPE'].split(',')[2]))
        time_interval = float(parameters['TIME_INTERVAL'])
        scale_percentage = int(parameters['SCALE_PERCENTAGE'])
        kernel_size = int(parameters['KERNEL_SIZE'])
        number_of_images = int(parameters['MAX_NUMBER_OF_IMAGES'])
        images_path = parameters['IMAGES_PATH']
    except KeyError as e:
        exit(f'KeyError: Failed to find variable named {e} in config file.')
    except ValueError:
        traceback.print_exc()
        exit('Change the values in the config file. Exiting program.')
    # initiate Producer and Consumer objects
    producer = Producer(source_shape=image_shape)
    consumer = Consumer()

    # calling Source every set time
    thread1 = threading.Timer(interval=time_interval, function=producer.fill_queue,
                              kwargs={'max_length': number_of_images})
    # running image processing in parallel
    thread2 = threading.Thread(target=image_processing,
                               kwargs={'p': producer, 'c': consumer, 'scale_percentage_': scale_percentage,
                                       'max_length': number_of_images, 'ksize': kernel_size})
    thread1.start()
    thread2.start()
    print('Processing images...')
    while True:
        # if threads have done everything they were supposed to do, create new ones
        if not thread1.is_alive():
            thread1 = threading.Timer(interval=time_interval, function=producer.fill_queue,
                                      kwargs={'max_length': number_of_images})
            thread1.start()

        if not thread2.is_alive():
            print(f'Already done: {len(consumer.b_queue)}/{number_of_images}')
            thread2 = threading.Thread(target=image_processing,
                                       kwargs={'p': producer, 'c': consumer, 'scale_percentage_': scale_percentage,
                                               'max_length': number_of_images, 'ksize': kernel_size})
            thread2.start()

        # if you have processed enough images, save the images and quit the program
        if len(consumer.b_queue) == number_of_images:
            print('Maximum number of processed images reached. Saving images...')
            thread1.cancel()
            thread2.join()
            utils.save_images(queue=consumer.b_queue, path=images_path)
            break


if __name__ == '__main__':
    main(config_file='config.cfg', section_name='DEFAULT_IMAGE_PROCESSING')
