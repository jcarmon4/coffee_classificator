import cv2

class ImageCapture:

    def __init__(self):
        # Sets the window and the camera.
        cv2.namedWindow("Logitech Camera", cv2.WINDOW_NORMAL)
        self.capture = cv2.VideoCapture(1)
        self.i = 0
        self.start_capture()

    def start_capture(self):
        while True:
            # Captures frame-by-frame.
            ret, frame = self.capture.read()

            if not ret:
                print("Couldn't read frame correctly.")
                break
            else:
                # Operations on the frame come here.
                self.img = frame

            # Displays the resulting frame.
            cv2.imshow("Logitech Camera", self.img)

            key_pressed = cv2.waitKey(1)
            if key_pressed % 256 == 27:
                # ESC pressed.
                print("Escape hit, closing.")
                self.release_capture()
                break
            elif key_pressed % 256 == 32:
                new_img_name = "ripe{}.png".format(self.i)
                new_img_path = "frames/" + new_img_name
                cv2.imwrite(new_img_path, self.img)
                print("{} written.".format(new_img_name))
                self.i += 1

                # When everything is done, releases the capture.

    def release_capture(self):
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    ImageCapture()
