import sys
from PIL import Image
import collections

def analyze_image(path):
    try:
        img = Image.open(path)
        width, height = img.size
        print(f"Image dimensions: {width}x{height}")
        
        # Resize to downsample for quick color analysis
        small_img = img.resize((100, 100))
        colors = list(small_img.getdata())
        
        # Count color frequencies
        color_counts = collections.Counter(colors)
        
        # Group colors into simple categories
        # Dark, Neon Cyan, Neon Magenta, Neon Green, Yellow, etc.
        groups = {
            "Black/Dark Background": 0,
            "Cyan/Blue Neon": 0,
            "Magenta/Pink/Purple Neon": 0,
            "Green/Yellow/White/Bright": 0,
            "Other": 0
        }
        
        for rgb, count in color_counts.items():
            r, g, b = rgb[:3]
            brightness = (r + g + b) / 3
            if brightness < 40:
                groups["Black/Dark Background"] += count
            elif b > 150 and g > 100 and r < 120:
                groups["Cyan/Blue Neon"] += count
            elif r > 150 and b > 100 and g < 120:
                groups["Magenta/Pink/Purple Neon"] += count
            elif r > 150 and g > 150 and b < 150:
                groups["Green/Yellow/White/Bright"] += count
            else:
                # Let's inspect further
                if r > 180 and g > 180 and b > 180:
                    groups["Green/Yellow/White/Bright"] += count
                else:
                    groups["Other"] += count
                    
        print("\nApproximate color distribution (in downsampled 100x100 grid):")
        total = sum(groups.values())
        for name, count in groups.items():
            pct = (count / total) * 100
            print(f" - {name}: {pct:.2f}% ({count} pixels)")
            
        # Analyze grid patterns: let's scan a few lines to look for recurring bright pixels (lines/grid)
        # We can look for horizontal or vertical lines in a downsampled strip
        print("\nSection analysis:")
        
        # 1. Top Section (HUD)
        top_crop = img.crop((0, 0, width, int(height * 0.15)))
        top_colors = list(top_crop.resize((10, 10)).getdata())
        print(" - Top 15% (HUD region):", end=" ")
        top_bright = [c for c in top_colors if sum(c[:3])/3 > 100]
        print(f"Has {len(top_bright)} bright regions. Looks like active HUD overlay.")
        
        # 2. Center Section (Gameplay/Tunnel/Obstacles)
        center_crop = img.crop((int(width*0.2), int(height*0.2), int(width*0.8), int(height*0.8)))
        center_colors = list(center_crop.resize((20, 20)).getdata())
        print(" - Center (Gameplay region):", end=" ")
        center_bright = [c for c in center_colors if sum(c[:3])/3 > 80]
        print(f"Has {len(center_bright)} / 400 bright pixels (neon grid/obstacles).")
        
        # Let's find 5 most dominant non-black colors in the image
        dominant_colors = []
        for rgb, count in color_counts.most_common(100):
            r, g, b = rgb[:3]
            if (r+g+b)/3 > 50: # Bright color
                dominant_colors.append((rgb, count))
                if len(dominant_colors) >= 5:
                    break
        print("\nTop dominant neon/bright colors (RGB):")
        for rgb, count in dominant_colors:
            r, g, b = rgb[:3]
            print(f" - RGB({r}, {g}, {b}) - count: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_image("/Users/jared/.gemini/antigravity/scratch/tpf4rd0dt91h1.png")
