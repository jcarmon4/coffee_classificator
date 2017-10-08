import cv2
import numpy as np

class CoffeeDetector:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)
    # Sets the window and the camera.
    cv2.namedWindow("Logitech Camera", cv2.WINDOW_NORMAL)
    capture = cv2.VideoCapture(0)

    def start_capture(self):
      while True:
        # Captures frame-by-frame.
        ret, frame = self.capture.read()

        if not ret:
          print("Couldn't read frame correctly.")
          break
        else:
          # Operations on the frame come here.
          img = cv2.imread('images/verde03.jpg')
          # denoise = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
          filter = self.filter_rgb_ripe(img)
          gray = cv2.cvtColor(filter, cv2.COLOR_RGB2GRAY)
          # The bigger the kernel_size value, the more processing time it takes.
          blur = cv2.GaussianBlur(gray, (3, 3), 0)
          blur_max = cv2.GaussianBlur(gray, (7, 7), 0)
          # Morphological transformation
          kernel = np.ones((18, 18), np.uint8)
          # erode = cv2.erode(blur, kernel, iterations=1)
          # dilate = cv2.dilate(blur, kernel, iterations=1)
          # opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
          closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)

          # Displays the resulting frame.
          cv2.imshow("Original", img)
          cv2.imshow("Filter", filter)
          # cv2.imshow("Gray scale", gray)
          cv2.imshow("Blur", blur)
          # cv2.imshow("Blur Max", blur_max)
          # cv2.imshow("erode", erode)
          # cv2.imshow("dilate", dilate)
          # cv2.imshow("Opening", opening)
          cv2.imshow("closing", closing)
          key_pressed = cv2.waitKey(1)
          if key_pressed % 256 == 27:
            # ESC pressed.
            print("Escape hit, closing.")
            break

    # Filters the given image using a green/gray mask.
    def filter_rgb_ripe(self, image):
      # ripe color mask.
      lower1 = np.uint8([11, 47, 40])
      upper1 = np.uint8([90, 60, 238])
      maduro_mask_1 = cv2.inRange(image, lower1, upper1)
      # ripe color mask.
      lower2 = np.uint8([8, 33, 119])
      upper2 = np.uint8([21, 38, 126])
      maduro_mask_2 = cv2.inRange(image, lower2, upper2)
      # ripe color mask.
      lower3 = np.uint8([5, 31, 97])
      upper3 = np.uint8([24, 85, 243])
      maduro_mask_3 = cv2.inRange(image, lower3, upper3)
      # Combines the masks.
      combined_mask = cv2.bitwise_or(maduro_mask_1, maduro_mask_3)
      # combined_mask = trash_mask
      masked_image = cv2.bitwise_and(image, image, mask=combined_mask)
      return masked_image

    # When everything is done, releases the capture.
    def release_capture(self):
      self.capture.release()
      cv2.destroyAllWindows()


