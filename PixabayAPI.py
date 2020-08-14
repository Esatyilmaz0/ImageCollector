"""
    @Author: Esat Yılmaz
    @Version: 1.0
    
"""

from ImageCollector import ImageCollector
import re


class PixabayCollector(ImageCollector):
    
    def __init__(self, API_KEY, query, number_of_images_to_download, save_path, image_res='large'):
        """
        :param str API_KEY: Api Key For Pixabay
        :param str query: Search query param
        :param int number_of_images_to_download: Number of images to download
        :param str save_path: Directory path to save pictures
        :param str image_res: Image Resoluation (large or webformat)
        """
        if image_res != ("large" or "webformat"):
            raise "Image Resuolation Error Please Fill Param large or webformat"
        
        super().__init__(query, number_of_images_to_download, save_path, image_res=image_res)

        self.URL = f"https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&per_page={self.PER_PAGE}"
        self.json_key = "hits"

    def get_image_information(self, image):
        
        image_url = image["largeImageURL"] if self.image_res == "large" else image["webformatURL"]
        image_name = re.search("[0-9](.*?)$", image_url).group()
        
        image_information = {}
        image_information["url"] = image_url
        image_information["name"] = image_name
        image_information["save_path"] = f"{self.save_path}{image_information['name']}"

        return super().get_image_information(image_information)

