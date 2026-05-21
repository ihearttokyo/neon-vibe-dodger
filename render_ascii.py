from PIL import Image

def scale_image(image, new_width=80):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width * 0.5) # 0.5 adjustment for font aspect ratio
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    # Short scale of ASCII characters
    ascii_chars = [" ", ".", ":", "-", "=", "+", "*", "%", "@", "#"]
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value // range_width]
    return ascii_str

def main():
    try:
        image = Image.open("/Users/jared/.gemini/antigravity/scratch/tpf4rd0dt91h1.png")
    except Exception as e:
        print(f"Error opening image: {e}")
        return
        
    image = scale_image(image)
    image = convert_to_grayscale(image)
    
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    
    # Split into lines
    ascii_str_len = len(ascii_str)
    for i in range(0, ascii_str_len, img_width):
        print(ascii_str[i:i+img_width])

if __name__ == "__main__":
    main()
