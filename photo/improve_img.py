from PIL import Image

def improve(file_name):
    im = Image.open(file_name)
    im.save(file_name, dpi=(300,300))