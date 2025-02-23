import cv2
import easyocr
from tqdm import tqdm
import sys

PATH = sys.argv[1]

reader = easyocr.Reader(['en'], gpu=True)

kills = []

cap = cv2.VideoCapture(PATH)
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
pbar = tqdm(total=n_frames)

is_kill = False

while (cap.isOpened()):

  ret, frame = cap.read()

  if frame is None:
    break

  frame = frame[720:770, 700:1000]

  result = reader.readtext(frame, detail = 0)

  if is_kill and len(result):
    pass

  elif is_kill and not len(result):
    is_kill = False

  elif len(result):
    text = "".join(result)

    if "KNOCKED" in text:
      is_kill = True
      kills.append(True)

#     # cv2.imshow('Thresh', frame)
#     # # # define q as the exit button
#     # if cv2.waitKey(25) & 0xFF == ord('q'):
#     #     break

  pbar.update(1)


pbar.close()

print(len(kills))
