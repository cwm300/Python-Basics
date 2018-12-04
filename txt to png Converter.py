from PIL import Image

file_name = input('Enter the name of the file: ')
if '.txt' in file_name:
    while '.txt' in file_name:
        print()
        print("***Enter the name without '.txt'***\n")
        file_name = input('Enter the name of the file: ')
         
file_input = file_name + '.txt'
    

file_open = open(file_input,'r')
pixels = file_open.readlines()
dimensions = (pixels[0].strip('\n').split(' '))
width = int(dimensions[0])
height = int(dimensions[1])

img = Image.new('RGB', (width, height))
x = 1

for j in range(height):
    for i in range(width):
        colors = (pixels[x].strip('\n').strip('(').strip(')').split(','))
        final = tuple(map(int, colors))
        img.putpixel((i, j), (final))
        x += 1
        
                

img.save(file_name + '.png', 'PNG')

img.show()