from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


size = (28, 28)
font = ImageFont.truetype('Arial.ttf', 14)
img = Image.new("RGB", size, (255, 255, 255))
img.thumbnail(size)
draw = ImageDraw.Draw(img)
text = "1+2"
text_x, text_y = font.getsize(text)
x = (28 - text_x)/2
y = (28 - text_y)/2
draw.text((x,y), text, (0,0,0),font=font)
draw=ImageDraw.Draw(img)
#img.show()
img.save("image.png")
