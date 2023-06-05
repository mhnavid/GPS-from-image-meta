import piexif

def get_exif_data(image_path):
    exif_data = piexif.load(image_path)
    if "GPS" in exif_data:
        return exif_data["GPS"]

    return None

def convert_to_degrees(value):
    degrees = value[0][0] / value[0][1]
    minutes = value[1][0] / value[1][1]
    seconds = value[2][0] / value[2][1]
    return degrees + (minutes / 60.0) + (seconds / 3600.0)

def get_lat_long(image_path):
    gps_info = get_exif_data(image_path)
    print(gps_info)
    if gps_info is not None:
        lat = convert_to_degrees(gps_info[2])
        lon = convert_to_degrees(gps_info[4])
        return lat, lon

    return None

# Example usage
image_path = 'photo.jpg'  # change here
coordinates = get_lat_long(image_path)
if coordinates is not None:
    lat, lon = coordinates
    print("Latitude:", lat)
    print("Longitude:", lon)
else:
    print("No GPS coordinates found in the image.")
