import cv2
import numpy as np
from arduino_control import ArduinoControl

class CoffeeDetector:
    AREA_EDGE = 3000

    def __init__(self):
        # Sets the window and the camera.
        cv2.namedWindow("Logitech Camera", cv2.WINDOW_NORMAL)
        self.capture = cv2.VideoCapture(1)
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
                self.img = cv2.imread('frames/ripe20.png')
                roi = self.img[80:400, 120:520]
                # self.img = frame
                #mask = self.filter_rgb_ripe(self.img)
                mask_ripe = self.filter_hsv_ripe(roi)

                # # set my output img to zero everywhere except my mask
                # output_img = self.img.copy()
                # output_img[np.where(mask == 0)] = 0
                # cv2.imshow("Ripe filter", output_img)
                #
                mask_green = self.filter_hsv_green(roi)
                #
                # # set my output img to zero everywhere except my mask
                # output_img = self.img.copy()
                # output_img[np.where(mask_green == 0)] = 0
                # cv2.imshow("Green filter", output_img)

                gray = mask_ripe

                #gray = cv2.cvtColor(filter, cv2.COLOR_RGB2GRAY)
                denoise = cv2.fastNlMeansDenoising(gray, None, 10, 5, 21)
                # The bigger the kernel_size value, the more processing time it takes.
                blur = cv2.GaussianBlur(gray, (3, 3), 0)
                # blur_max = cv2.GaussianBlur(gray, (7, 7), 0)
                # Morphological transformation
                kernel = np.ones((18, 18), np.uint8)
                # erode = cv2.erode(blur, kernel, iterations=1)
                # dilate = cv2.dilate(blur, kernel, iterations=1)
                # opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
                closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)

                # # Displays the resulting frame.
                cv2.imshow("Original", self.img)
                cv2.imshow("ROI", roi)
                cv2.imshow("Gray scale", gray)
                cv2.imshow("Denoise", denoise)
                cv2.imshow("Blur", blur)
                # cv2.imshow("Blur Max", blur_max)
                # cv2.imshow("erode", erode)
                # cv2.imshow("dilate", dilate)
                # cv2.imshow("Opening", opening)
                cv2.imshow("closing", closing)

                area, contour = self.calculate_area(closing)
                print(area)
                cv2.drawContours(roi, [contour], -1, (0, 255, 0), 2)
                cv2.imshow("Coffee Detector", roi)


                # if area < 2000:
                #     bean_type = "calibrando"
                # else:
                #     contour_height = tuple(contour[3][0])[1] - tuple(contour[2][0])[1]
                #     contour_widgth = tuple(contour[3][0])[0] - tuple(contour[0][0])[0]
                #     print("diferencia", abs(contour_height - contour_widgth))
                #     if (abs(contour_height - contour_widgth) > 200):
                #         bean_type = "procesando..."
                #     if area > self.AREA_EDGE:
                #         bean_type = "maduro"
                #         self.arduino_control.write_to_arduino('r')
                #     else:
                #         bean_type = "verde"
                #         self.arduino_control.write_to_arduino('l')
                #
                #     cv2.drawContours(self.img, [contour], -1, (0, 255, 0), 2)
                #
                # cv2.putText(self.img, bean_type, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 200), 4);
                # cv2.imshow("Coffee Detector", self.img)

            key_pressed = cv2.waitKey(1)
            if key_pressed % 256 == 27:
                # ESC pressed.
                print("Escape hit, closing.")
                break

                # gray = cv2.cvtColor(filter, cv2.COLOR_RGB2GRAY)
                # # The bigger the kernel_size value, the more processing time it takes.
                # blur = cv2.GaussianBlur(gray, (3, 3), 0)
                # blur_max = cv2.GaussianBlur(gray, (7, 7), 0)
                # # Morphological transformation
                # kernel = np.ones((18, 18), np.uint8)
                # # erode = cv2.erode(blur, kernel, iterations=1)
                # # dilate = cv2.dilate(blur, kernel, iterations=1)
                # # opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
                # closing = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)
                #
                # # Displays the resulting frame.
                # #          cv2.imshow("Original", self.img)
                # #          cv2.imshow("Filter", filter)
                # # cv2.imshow("Gray scale", gray)
                # #          cv2.imshow("Blur", blur)
                # # cv2.imshow("Blur Max", blur_max)
                # # cv2.imshow("erode", erode)
                # # cv2.imshow("dilate", dilate)
                # # cv2.imshow("Opening", opening)
                # #          cv2.imshow("closing", closing)
                #
                # area, contour = self.calculate_area(closing);
                # print(area)
                #
                # if area < 2000:
                #     bean_type = "calibrando"
                # else:
                #     contour_height = tuple(contour[3][0])[1] - tuple(contour[2][0])[1]
                #     contour_widgth = tuple(contour[3][0])[0] - tuple(contour[0][0])[0]
                #     print("diferencia", abs(contour_height - contour_widgth))
                #     if (abs(contour_height - contour_widgth) > 200):
                #         bean_type = "procesando..."
                #     if area > self.AREA_EDGE:
                #         bean_type = "maduro"
                #         self.arduino_control.write_to_arduino('r')
                #     else:
                #         bean_type = "verde"
                #         self.arduino_control.write_to_arduino('l')
                #
                #     cv2.drawContours(self.img, [contour], -1, (0, 255, 0), 2)
                #
                # cv2.putText(self.img, bean_type, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 200), 4);
                # cv2.imshow("Coffee Detector", self.img)
                #
                # key_pressed = cv2.waitKey(1)
                # if key_pressed % 256 == 27:
                #     # ESC pressed.
                #     print("Escape hit, closing.")
                #     break

    def filter_hsv_green(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_green = np.array([37, 38, 30])  # example value
        upper_green = np.array([85, 255, 200])  # example value
        mask = cv2.inRange(hsv, lower_green, upper_green)
        return mask

        #        output_hsv = hsv.copy()
        #        output_hsv[np.where(mask == 0)] = 0
        #        cv2.imshow("Green", output_hsv)

    def filter_hsv_ripe(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # lower mask (0-10)
        lower_red = np.array([0, 50, 50])  # example value
        upper_red = np.array([10, 255, 255])  # example value
        mask0 = cv2.inRange(hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        # join my masks
        mask = mask0 + mask1

        return mask

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

    # Filters the given image using a green/gray mask.
    def filter_rgb_green(self, image):
        # ripe color mask.
        lower1 = np.uint8([11, 47, 40])
        upper1 = np.uint8([90, 60, 238])
        maduro_mask_1 = cv2.inRange(image, lower1, upper1)
        # ripe color mask.
        lower2 = np.uint8([8, 33, 119])
        upper2 = np.uint8([21, 38, 126])
        maduro_mask_2 = cv2.inRange(image, lower2, upper2)
        # Combines the masks.
        combined_mask = cv2.bitwise_or(maduro_mask_1, maduro_mask_2)
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
                index = 3
                contour_height = tuple(contour[index][0])[1] - tuple(contour[index-1][0])[1]
                if contour_height < 1000:
                    index -= 1
                    contour_height = tuple(contour[index][0])[1] - tuple(contour[index-1][0])[1]
                contour_widgth = tuple(contour[index-1][0])[0] - tuple(contour[index-2][0])[0]
                print("contour_height 0: ", tuple(contour[0][0]), " 1: ", tuple(contour[1][0]), " 2: ", tuple(contour[2][0]), "3: ", tuple(contour[3][0]))
                print("contour_height: ", contour_height, " contour_widgth: ", contour_widgth)
                area = contour_height * contour_widgth

            return area, contour
        else:
            contour = []
            return area, contour