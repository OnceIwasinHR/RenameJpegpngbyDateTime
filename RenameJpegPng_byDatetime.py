import os
from PIL import Image
from PIL.ExifTags import TAGS

folder_path = r"G:\iCloud Photos"  # Update this path to your actual folder path 

def get_date_taken(path):
    image = Image.open(path)
    exif_data = image._getexif()
    if exif_data:
        for tag, value in exif_data.items():
            if TAGS.get(tag) == "DateTimeOriginal":
                return value
    return None

for filename in os.listdir(folder_path):
    # Target only .jpeg, .jpg, and .png files
    if filename.lower().endswith(('.jpeg', '.jpg', '.png')):  
        file_path = os.path.join(folder_path, filename)
        date_taken = get_date_taken(file_path)
        if date_taken:
            date_part = date_taken.split()[0]
            year, month, day = date_part.split(":")
            extension = os.path.splitext(filename)[1].lower()  # Keep original extension
            
            new_name = f"{year}{month}{day}{extension}"  # Rename according to YYYYMMDD format
            new_file_path = os.path.join(folder_path, new_name)
            
            # Handle potential filename conflicts by appending a number if necessary
            counter = 1
            while os.path.exists(new_file_path):
                new_name = f"{year}{month}{day}_{counter}{extension}"
                new_file_path = os.path.join(folder_path, new_name)
                counter += 1
            
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} to {new_name}")
