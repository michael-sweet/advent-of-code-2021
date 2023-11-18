with open('input.txt') as input_file:
    input = input_file.read().split('\n\n')

enhancement_algorithm = list(input[0])
input_image = [list(x) for x in input[1].split('\n')]

inf1 = enhancement_algorithm[:1][0]
inf2 = enhancement_algorithm[-1:][0]
boundary = inf2

def grow(input_image, char = '.'):
    for x, row in enumerate(input_image):
        input_image[x] = [char] + row + [char]
    blank = [char] * len(input_image[0])
    input_image = [blank] + input_image + [blank]

    return input_image


def getSurroundingPixelCode(x, y, input_image, boundary):
    binary_number = ''
    for a in range(-1, 2):
        for b in range(-1, 2):
            try:
                pixel = input_image[x + a][y + b]
                binary_number += '0' if pixel == '.' else '1'
            except IndexError :
                binary_number += '0' if boundary == '.' else '1'

    return int(binary_number, 2)


def enhance(image, boundary):
    image_copy = []
    for x, pixel_row in enumerate(image):
        row = []
        for y, _ in enumerate(pixel_row):
            row.append(enhancement_algorithm[getSurroundingPixelCode(x, y, image, boundary)])
        image_copy.append(row)

    return image_copy


def countLight(image):
    light_count = 0
    for x in image:
        light_count += x.count('#')

    return light_count


output_image = grow(input_image, boundary)

for x in range(2):
    output_image = enhance(output_image, boundary)
    boundary = inf1 if boundary == inf2 else inf2
    output_image = grow(output_image, boundary)


print('Part 1:', countLight(output_image))

for x in range(48):
    output_image = enhance(output_image, boundary)
    boundary = inf1 if boundary == inf2 else inf2
    output_image = grow(output_image, boundary)

print('Part 2:', countLight(output_image))