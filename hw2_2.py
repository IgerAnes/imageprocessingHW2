import numpy as np
import cv2
from tkinter import filedialog

class BackGroundSubtractor:
    # When constructing background subtractor, we
	# take in two arguments:
	# 1) alpha: The background learning factor, its value should
	# be between 0 and 1. The higher the value, the more quickly
	# your program learns the changes in the background. Therefore, 
	# for a static background use a lower value, like 0.001. But if 
	# your background has moving trees and stuff, use a higher value,
	# maybe start with 0.01.
	# 2) firstFrame: This is the first frame from the video/webcam.
	def __init__(self,alpha,firstFrame):
		self.alpha  = alpha
		self.backGroundModel = firstFrame

	def getForeground(self,frame):
		# apply the background averaging formula:
		# NEW_BACKGROUND = CURRENT_FRAME * ALPHA + OLD_BACKGROUND * (1 - APLHA)
		self.backGroundModel =  frame * self.alpha + self.backGroundModel * (1 - self.alpha)

		# after the previous operation, the dtype of
		# self.backGroundModel will be changed to a float type
		# therefore we do not pass it to cv2.absdiff directly,
		# instead we acquire a copy of it in the uint8 dtype
		# and pass that to absdiff.

		return cv2.absdiff(self.backGroundModel.astype(np.uint8),frame)

class Background_Subtraction:
    def __init__(self):
        self.filename = ''

    def ChooseAndLoadVideo(self):
            self.filename = filedialog.askopenfilename( initialdir = "C:/User/USER/Videos",
            title = "Select Video",
            filetype = (("mp4 files","*.mp4"),("All file","*.*")))

            if(self.filename == ""):
                print("you have not choose the Video, Please choose again.")

    def denoise(self,frame):
        frame = cv2.medianBlur(frame,5)
        frame = cv2.GaussianBlur(frame,(5,5),0)
        return frame

    def Start_Process(self):
        self.ChooseAndLoadVideo()
        self.cap = cv2.VideoCapture(self.filename)
        self.ret, self.frame = self.cap.read()
        if self.ret is True:
            self.backSubtractor = BackGroundSubtractor(0.01, self.denoise(self.frame))
            self.run = True
        else:
            self.run = False

        while(self.run):
            self.ret, self.frame = self.cap.read()

            # If the frame was properly read.
            if self.ret is True:
                # Show the filtered image
                cv2.imshow('input',self.denoise(self.frame))

                # get the foreground
                self.foreGround = self.backSubtractor.getForeground(self.denoise(self.frame))

                # Apply thresholding on the background and display the resulting mask
                self.ret, self.mask = cv2.threshold(self.foreGround, 15, 255, cv2.THRESH_BINARY)

                # Note: The mask is displayed as a RGB image, you can
                # display a grayscale image by converting 'foreGround' to
                # a grayscale before applying the threshold.
                cv2.imshow('mask', self.mask)

                self.key = cv2.waitKey(10) & 0xFF
            else:
                break

            if self.key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
        