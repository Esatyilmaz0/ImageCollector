"""
    @Author: Esat Yılmaz
    @Version: 1.0
    
"""
import requests
import re
import os
import threading

class Image:
    def __init__(self, image):
        
        self.url = image["url"]
        self.name = image["name"]
        self.save_path = image["save_path"]

class ImageCollector(object):
    
    def __init__(self, query, number_of_images_to_download, save_path, image_res):
        self.PER_PAGE = 80
        self.query = query
        self.number_of_images_to_download = number_of_images_to_download
        self.image_res = image_res
        self.save_path = save_path
        self.images = []
        self.headers = {}

    def collectImages(self):
        """
            Retrieves image list from api and return image list
        """
        page = 1
        while len(self.images) <= self.number_of_images_to_download:
            req = requests.get(f"{self.URL}&page={page}", headers=self.headers)
            self.images += req.json()[self.json_key]
            page += 1

        self.images = self.images[:self.number_of_images_to_download]
        return self.images

    def get_image_information(self, image):
        """
            Return Image Object
        """
        return Image(image=image)


    def save_image(self, image):
        """
            Get image information and save image to target directory.
        """
        
        image = self.get_image_information(image)
        if not os.path.isfile(image.save_path):
                
            req = requests.get(image.url).content

            with open(image.save_path, "wb") as file:
                file.write(req)



