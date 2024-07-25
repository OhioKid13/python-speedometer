from PIL import Image

def remove_white_background(image_path, output_path):
    # Open the image
    img = Image.open(image_path).convert('RGBA')

    # Create a new image with an alpha channel (transparency)
    new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))

    # Get the data of the image
    data = img.getdata()

    # Process each pixel
    new_data = []
    for item in data:
        # Change all white (also shades of whites)
        # pixels to transparent
        if item[0] in list(range(200, 256)) and item[1] in list(range(200, 256)) and item[2] in list(range(200, 256)):
            new_data.append((0, 0, 0, 0))  # Transparent
        else:
            new_data.append(item)  # Keep the original color

    # Update image data
    new_img.putdata(new_data)

    # Save the result
    new_img.save(output_path)

if __name__ == "__main__":
    # Paths to input and output images
    input_image_path = 'assets/needle.png'  # Path to the input image
    output_image_path = 'needle_transparent.png'  # Path to save the output image

    # Remove the white background
    remove_white_background(input_image_path, output_image_path)
    print(f'Processed image saved as {output_image_path}')
