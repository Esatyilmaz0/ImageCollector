"""
    @Author: Esat Yılmaz
    @Version: 1.0
    
"""

from ImageCollector import ImageCollector
import re

class PexelsCollector(ImageCollector):
    def __init__(self, API_KEY, query, number_of_images_to_download, save_path, image_res='original'):
        """
        :param str API_KEY: Api Key For Pexels
        :param str query: Search query param
        :param int number_of_images_to_download: Number of images to download
        :param str save_path: Directory path to save pictures
        :param str image_res: Image Resoluation (original, large2x)

        """
        if image_res != ("original" or "large2x"):
            raise TypeError("Image Resoluation Type Error, Enter: original or large2x")

        super().__init__(query, number_of_images_to_download, save_path, image_res=image_res)

        self.URL = f"https://api.pexels.com/v1/search?query={query}&per_page={self.PER_PAGE}"
        self.headers["Authorization"] = API_KEY
        self.json_key = "photos"
        

    def get_image_information(self, image):
        regex_pattern = "[0-9]/(.*?)$" if self.image_res == "original" else "[0-9]/(.*?)\?"

        image_information = {}

        image_information["url"] = image["src"][self.image_res]
        image_information["name"] = re.search(regex_pattern, image_information["url"]).group(1)
        image_information["save_path"] = f"{self.save_path}{image_information['name']}"
        
        return super().get_image_information(image_information)


