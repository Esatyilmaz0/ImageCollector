from PexelsAPI import PexelsCollector
from PixabayAPI import PixabayCollector

if __name__ == "__main__":

    select_api = int(input("> Select API:\n1-) Pexels API\n2-) Pixabay API\n> "))
    if select_api > 2 or select_api < 0:
        raise "Error"

    api_key = input("> Enter API Key: ")
    query = input("> Enter image search term: ") # apple
    number_of_images_to_download = int(input("> Enter number of images to download: ")) # 300
    save_path = input("> Enter directory path to be images saved: ") # ./apple/
    index = 1

    if select_api == 1:

        image_res = input("Enter image resolution (original or large2x): ") # large
        collector = PexelsCollector(api_key, query, number_of_images_to_download, save_path, image_res)
        images = collector.collectImages()
        for image in images:
            image_information = collector.get_image_information(image)
            collector.save_image(image)
            print(f"> [+] {index} Image Saved")
            index += 1

    elif select_api == 2:
        image_res = input("> Enter image resolution (large or webformat): ")

        api = PixabayCollector(api_key, query, number_of_images_to_download, save_path, image_res)
        images = api.collectImages()
        
        for image in images:
            image_information = c.get_image_information(image)
            api.save_image(image)
            print(f"> {index} Image Saved")
            index += 1

