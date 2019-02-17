from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import sys

def watermark_files(input_directory, output_directory, watermark_text):
    print "Watermarking..."
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 20)
    for filename in os.listdir(input_directory):
        input_image_path = "%s/%s" % (input_directory, filename)
        image_file = Image.open(input_image_path)
        drawing = ImageDraw.Draw(image_file)
        black = (3, 8, 12)
        pos = [image_file.size[0]/4, image_file.size[1]/2]
        drawing.text(pos, watermark_text, fill=black, font=font)
        output_image_path = "%s/%s" % (output_directory, filename)
        image_file.save(output_image_path)

if __name__== "__main__":
    watermark_files_in_zip(sys.argv[1], sys.argv[2], sys.argv[3])