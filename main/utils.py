from PIL import Image
import os
import string
from random import choices
import aspose.words as aw



class Convert:
    def __init__(self, img, format=None):
        self.img = img
        self.format = format
        
    def generate_name(self):
        characters = string.digits + string.ascii_letters
        char = "".join(choices(characters, k=10))
        # get the filename from a filepath
        # file_name = os.path.basename(self.img)
        name = self.img.name.split(".")[0] + char + "." + self.format
        return name

    def convert(self):
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        name = f"./download/{self.generate_name()}"

        shape = builder.insert_image(self.img.read())
        shape.image_data.save(name)
        return name

    # JPG COVERSION TO OTHER FORMAT
    # def img2jpg(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.jpg"
    #     image.save(name)
    #     return name

    # def img2png(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.png"
    #     image.save(name)
    #     return name

    # def img2jpeg(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.jpeg"
    #     image.save(name)
    #     return name

    # def img2tif(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.tif"
    #     image.save(name)
    #     return name

    # def img2tiff(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.tiff"
    #     image.save(name)
    #     return name

    # def img2gif(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.gif"
    #     image.save(name)
    #     return name

    # def img2bmp(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.bmp"
    #     image.save(name)
    #     return name

    # def jpg2eps(self):
    #     image = Image.open(self.img)
    #     name = f"download/%Y/%m/%d/{self.generate_name()}.eps"
    #     image.save(name)
    #     return name

