import os
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def compress_images(input_folder, output_folder, quality):
    # Çıktı klasörünü oluştur
    if os.path.exists(output_folder):
        # Klasör varsa sil
        for file_name in os.listdir(output_folder):
            file_path = os.path.join(output_folder, file_name)
            os.remove(file_path)
        os.rmdir(output_folder)

    os.mkdir(output_folder)

    # Giriş klasöründeki resimleri işle
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        # Dosya uzantısını kontrol et
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_path = os.path.join(output_folder, file_name)
            original_size, compressed_size, original_unit, compressed_unit = compress_image(file_path, output_path, quality)
            show_message_box(file_name, original_size, compressed_size, original_unit, compressed_unit)

    show_message_box("Tamamlandı!", "", "", "", "")

def compress_image(input_image_path, output_image_path, quality):
    original_image = Image.open(input_image_path)
    original_size = os.path.getsize(input_image_path)
    original_unit = determine_unit(original_size)

    original_image.save(output_image_path, optimize=True, quality=quality)

    compressed_size = os.path.getsize(output_image_path)
    compressed_unit = determine_unit(compressed_size)

    return original_size, compressed_size, original_unit, compressed_unit

def determine_unit(size):
    if size < 1024:
        return size, "bytes"
    elif size < 1024 * 1024:
        return size / 1024, "KB"
    else:
        return size / (1024 * 1024), "MB"

def show_message_box(file_name, original_size, compressed_size, original_unit, compressed_unit):
    if file_name != "Tamamlandı!":
        original_size, original_unit = determine_unit(original_size)
        compressed_size, compressed_unit = determine_unit(compressed_size)

        message = f"{file_name} | {original_size:.2f} {original_unit} -> {compressed_size:.2f} {compressed_unit}"
    else:
        message = "Tamamlandı!"

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Luna Scans Resim Boyutu Küçültme | Made by mr.c3m", message)

# Örnek kullanım
input_folder = '.'  # Python dosyasının çalıştığı klasör
output_folder = 'Bitenler'
compression_quality = 80  # Sıkıştırma kalitesi (0-100 arası)

compress_images(input_folder, output_folder, compression_quality)
