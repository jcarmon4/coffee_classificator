import cv2
import numpy as np
from arduino_control import ArduinoControl

class CoffeeDetector:
    AREA_EDGE = 3000

    def __init__(self):
        # Sets the window and the camera.
        cv2.namedWindow("Logitech Camera", cv2.WINDOW_NORMAL)
        self.capture = cv2.VideoCapture(0)
        self.img = None
        self.arduino_control = ArduinoControl()
        self.arduino_control.establish_arduino_connection()

    def start_capture(self):
        while True:
            # Captures frame-by-frame.
            ret, frame = self.capture.read()

            if not ret:
                print("Couldn't read frame correctly.")
                break
            else:
                # Operations on the frame come here.
                # self.img = cv2.imread('images/maduro02.jpg')
                self.img = frame
                # denoise = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
                filter = self.filter_rgb_ripe(self.img)
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
                #          cv2.imshow("Original", self.img)
                #          cv2.imshow("Filter", filter)
                # cv2.imshow("Gray scale", gray)
                #          cv2.imshow("Blur", blur)
                # cv2.imshow("Blur Max", blur_max)
                # cv2.imshow("erode", erode)
                # cv2.imshow("dilate", dilate)
                # cv2.imshow("Opening", opening)
                #          cv2.imshow("closing", closing)

                area, contour = self.calculate_area(closing);
                print(area)

                if area < 2000:
                    bean_type = "calibrando"
                else:
                    contour_height = tuple(contour[3][0])[1] - tuple(contour[2][0])[1]
                    contour_widgth = tuple(contour[3][0])[0] - tuple(contour[0][0])[0]
                    print("diferencia", abs(contour_height - contour_widgth))
                    if (abs(contour_height - contour_widgth) > 200):
                        bean_type = "procesando..."
                    if area > self.AREA_EDGE:
                        bean_type = "maduro"
                        self.arduino_control.write_to_arduino('r')
                    else:
                        bean_type = "verde"
                        self.arduino_control.write_to_arduino('l')

                    cv2.drawContours(self.img, [contour], -1, (0, 255, 0), 2)

                cv2.putText(self.img, bean_type, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 200), 4);
                cv2.imshow("Coffee Detector", self.img)


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

    def calculate_area(self, image):
        area = 0
        # Finds the contours in the edged image and keeps the largest one.
        (_, contours, _) = cv2.findContours(image.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)

            # Computes the bounding box of the largest contour and returns it.
            # The bounding box contains the (x, y)-coordinates and the width and height (in pixels).
            bean_bounding_box = cv2.minAreaRect(largest_contour)
            # Verify that it's not null
            if bean_bounding_box is not None:
                # Draws the bounding box of the marker and displays the calculated distance to it.
                bounding_box = cv2.boxPoints(bean_bounding_box)
                contour = np.array(bounding_box).reshape((-1, 1, 2)).astype(np.int32)
                contour_height = tuple(contour[3][0])[1] - tuple(contour[2][0])[1]
                contour_widgth = tuple(contour[3][0])[0] - tuple(contour[0][0])[0]
                area = contour_height * contour_widgth

            return area, contour
        else:
            contour = []
            return area, contour