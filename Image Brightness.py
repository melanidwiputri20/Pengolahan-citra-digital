import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(image, value):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    v = np.clip(v.astype(np.int32) + value, 0, 255).astype(np.uint8)
    hsv_image = cv2.merge((h, s, v))
    adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return adjusted_image

def main():
    image_path = "daifuku.jpg" 
    original_image = cv2.imread(image_path)

    brightness_value = 65  

    adjusted_image = adjust_brightness(original_image, brightness_value)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
    plt.title('Adjusted Image')

    plt.show()

if __name__ == '_main_':
    main()