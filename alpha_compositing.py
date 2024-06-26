#This project overlays the foreground_image on the background_image and performs alpha composition using the alpha_mask (Also known as transparent mask)
from PIL import Image
import math

background_image = Image.open("background.png");
foreground_image = Image.open("foreground.png");
alpha_mask = Image.open("alpha-mask.png"); #Black means transparent, i.e. foreground_image will not show at that pixel. White means the opposite

#Idea: Get the distance from origin (0, 0, 0) in RGB, determining the magnitude of gray in each pixel of alpha_mask
p1 = background_image.load();
p2 = foreground_image.load();
p3 = alpha_mask.load();

if background_image.size != foreground_image.size or background_image.size != alpha_mask.size or foreground_image.size != alpha_mask.size:
    print("Please have all three images share the same dimension.");
else:
    width, height = background_image.size;
    for i in range(width):
        for j in range(height):
            r, g, b, p = alpha_mask.getpixel((i, j));
            nr = r / 255;
            ng = g / 255;
            nb = b / 255;
            dist = math.sqrt((nr*nr)+(ng*ng)+(nb*nb)); #Max dist = sqrt(1+1+1) = sqrt(3)
            max_dist = math.sqrt(3);
            alpha = dist / max_dist;
            rcf, gcf, bcf, pcf = foreground_image.getpixel((i, j));
            rcb, gcb, bcb, pcb = background_image.getpixel((i, j));
            p1[i, j] = (int(alpha * rcf + (1-alpha) * rcb), int(alpha * gcf + (1-alpha) * gcb), int(alpha * bcf + (1-alpha) * bcb))
    background_image.save("your_file_name.png", format="png");
