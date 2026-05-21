from PIL import Image

img = Image.open("/Users/jared/.gemini/antigravity/scratch/tpf4rd0dt91h1.png")
width, height = img.size
pixels = list(img.getdata())

min_r, min_g, min_b = 255, 255, 255
max_r, max_g, max_b = 0, 0, 0
sum_r, sum_g, sum_b = 0, 0, 0

unique_colors = {}
for p in pixels:
    r, g, b = p[:3]
    min_r = min(min_r, r)
    min_g = min(min_g, g)
    min_b = min(min_b, b)
    max_r = max(max_r, r)
    max_g = max(max_g, g)
    max_b = max(max_b, b)
    sum_r += r
    sum_g += g
    sum_b += b
    
    unique_colors[p[:3]] = unique_colors.get(p[:3], 0) + 1

total = len(pixels)
print(f"Dimensions: {width}x{height}")
print(f"Min RGB: ({min_r}, {min_g}, {min_b})")
print(f"Max RGB: ({max_r}, {max_g}, {max_b})")
print(f"Mean RGB: ({sum_r/total:.2f}, {sum_g/total:.2f}, {sum_b/total:.2f})")
print(f"Total unique colors: {len(unique_colors)}")

sorted_colors = sorted(unique_colors.items(), key=lambda x: x[1], reverse=True)
print("\nTop 30 most frequent colors:")
for i in range(min(30, len(sorted_colors))):
    color, count = sorted_colors[i]
    pct = (count / total) * 100
    print(f"RGB {color}: {pct:.4f}% ({count} pixels)")
