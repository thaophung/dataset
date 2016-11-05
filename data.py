from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from numpy import random
import argparse

def create_image(n):
	for i in range (1, n+1):
    		size = (28, 28)
    		font = ImageFont.truetype('Arial.ttf', 14)

    		# input image
    		input_img = Image.new("RGB", size, (255, 255, 255))
    		draw_input = ImageDraw.Draw(input_img)

    		#label image
    		label_img = Image.new("RGB", size, (255, 255, 255))
    		draw_label = ImageDraw.Draw(label_img)

    		# get random numbers
    		num1 = random.randint(0, 10)
    		num2 = random.randint(0, 10)

    		# get random operator (+/-)
    		op = random.randint(0, 2)
    		if op==0:
        		operator = "+"
        		result = num1 + num2
    		else:
        		operator = "-"
        		result = num1 - num2
 
	    	# input image
    		inText = str(num1) + operator + str(num2)
    		inText_x, inText_y = font.getsize(inText)

    		rand_x = random.randint(0, 4)
    		rand_y = random.randint(0,8)
    		if rand_y > 4:
        		x_input = ((28 - rand_x) - inText_x)/2
    		else:
        		x_input = ((28 + rand_x) - inText_x)/2
    		if rand_x > 2:
        		y_input = ((28 - rand_y) - inText_y)/2
    		else:
        		y_input = ((28 + rand_y) - inText_y)/2
    		draw_input.text((x_input,y_input), inText, (0,0,0),font=font)
	
    		#label
    		label_text = str(result)
    		outText_x, outText_y = font.getsize(label_text)
    		x_label = (28 - outText_x)/2
    		y_label = (28 - outText_y)/2
    		draw_label.text((x_label, y_label), label_text, (0,0,0), font=font)
		input_name = "input" + str(i) + ".png"    		
		input_img.save(input_name)
		label_name = "label" + str(i) + ".png"
		label_img.save(label_name)
    

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-n', '--num_samples', metavar='n', type=int, default=1, help='Number of sample')
	
	args = parser.parse_args()
	n = args.num_samples
	create_image(n)

if __name__ == '__main__':
	main()
