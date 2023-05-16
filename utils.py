from typing import BinaryIO, List
import numpy as np
import cv2


def get_image(content: BinaryIO) -> List[List[List[int]]]:
    nparr = np.fromstring(content, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def decode_QR(image: BinaryIO) -> str:
    detector = cv2.QRCodeDetector()
    return detector.detectAndDecode(image)[0]
