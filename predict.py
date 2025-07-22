# predict.py
import cv2
from ultralytics import YOLO
import argparse
import os

# Komut satırından argümanları almak için bir parser oluştur
parser = argparse.ArgumentParser(description="YOLOv8 ile bir video üzerinde nesne tespiti yap.")
parser.add_argument('--model', type=str, required=True, help="Eğitilmiş .pt model dosyasının yolu.")
parser.add_argument('--source', type=str, required=True, help="Test edilecek video dosyasının yolu.")
args = parser.parse_args()

print(f"Model yükleniyor: {args.model}")
model = YOLO(args.model)

# Video bilgilerini al
cap = cv2.VideoCapture(args.source)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)
cap.release()

# Sonuç videosu için isim ve yol belirle
output_dir = "results"
os.makedirs(output_dir, exist_ok=True)
base_name = os.path.basename(args.source)
output_path = os.path.join(output_dir, f"result_{base_name}")

print(f"Video işleniyor: {args.source}")
print(f"Sonuçlar şuraya kaydedilecek: {output_path}")

# Video yazıcısını oluştur
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Stream modunda tahmin yap ve sonuçları işle
results = model.predict(source=args.source, stream=True)

for result in results:
    annotated_frame = result.plot()
    video_writer.write(annotated_frame)

video_writer.release()
print("\nİşlem tamamlandı!")