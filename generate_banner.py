from PIL import Image, ImageDraw, ImageFont

# Define banner size
width = 1584
height = 396

# Create a new image with a light blue background
banner = Image.new('RGB', (width, height), '#e0f7fa')
draw = ImageDraw.Draw(banner)

# Load a font
# Make sure you have a font file in the same directory or provide the correct path
font_path = "arial.ttf"
font_size = 60
font = ImageFont.truetype(font_path, font_size)

# Define text and positions
name = "Brandon Van"
title = "Software Engineer"

# Calculate text size and position
name_bbox = draw.textbbox((0, 0), name, font=font)
title_bbox = draw.textbbox((0, 0), title, font=font)

name_width, name_height = name_bbox[2] - name_bbox[0], name_bbox[3] - name_bbox[1]
title_width, title_height = title_bbox[2] - title_bbox[0], title_bbox[3] - title_bbox[1]

# Set text positions
name_x = (width - name_width) / 2
name_y = (height / 3) - (name_height / 2)

title_x = (width - title_width) / 2
title_y = (height / 2) - (title_height / 2)

# Draw text on image
draw.text((name_x, name_y), name, fill="black", font=font)
draw.text((title_x, title_y), title, fill="black", font=font)

# Save the image
banner.save('linkedin_banner.png')

print("Banner created successfully and saved as 'linkedin_banner.png'.")
