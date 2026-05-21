from PIL import Image

img = Image.open("/Users/jared/.gemini/antigravity/scratch/tpf4rd0dt91h1.png")
width, height = img.size

# Let's grid it into 20x20 blocks
grid_w, grid_h = 20, 20
cell_w = width // grid_w
cell_h = height // grid_h

print(f"Scanning image in {grid_w}x{grid_h} grid cells:")
for gy in range(grid_h):
    row_str = ""
    for gx in range(grid_w):
        # Sample cell pixels
        cell_r, cell_g, cell_b = 0, 0, 0
        pixels_in_cell = 0
        
        y_start = gy * cell_h
        y_end = min((gy + 1) * cell_h, height)
        x_start = gx * cell_w
        x_end = min((gx + 1) * cell_w, width)
        
        for y in range(y_start, y_end, 5): # downsample step 5
            for x in range(x_start, x_end, 5):
                r, g, b = img.getpixel((x, y))[:3]
                cell_r += r
                cell_g += g
                cell_b += b
                pixels_in_cell += 1
                
        if pixels_in_cell > 0:
            avg_r = cell_r / pixels_in_cell
            avg_g = cell_g / pixels_in_cell
            avg_b = cell_b / pixels_in_cell
            brightness = (avg_r + avg_g + avg_b) / 3
            
            # Print character based on brightness and dominant color
            if brightness < 30:
                row_str += "·" # Background
            elif avg_r > 150 and avg_g > 150 and avg_b > 150:
                row_str += "W" # Bright white (text/buttons)
            elif avg_b > avg_r and avg_b > avg_g:
                row_str += "B" # Blue/Cyan dominant
            elif avg_r > avg_g and avg_r > avg_b:
                row_str += "R" # Red/Magenta dominant
            elif avg_g > avg_r and avg_g > avg_b:
                row_str += "G" # Green dominant
            else:
                row_str += "x" # Other bright
        else:
            row_str += " "
            
    print(row_str)

