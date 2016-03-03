import argparse
import os
import cv2
import time

def initiate():
	ap = argparse.ArgumentParser()
	ap.add_argument("-d", "--dataset", help="path to the dataset directory")
	ap.add_argument("-q", "--query", help="path to the query image")
	args = vars(ap.parse_args())

	reference = cv2.imread(args["query"],cv2.IMREAD_COLOR)
	reference_hist = cv2.calcHist([reference],[0],None,[256],[0,256])

	cv2.imshow("Query Image", reference)
	cv2.moveWindow("Query Image",50,100)

	for file in os.listdir(args["dataset"]):
		if file.endswith(".png"):
			full_path = args["dataset"] + file
			img = cv2.imread(full_path,cv2.IMREAD_COLOR)
			hist = cv2.calcHist([img],[0],None,[256],[0,256])

			diff = cv2.compareHist(reference_hist,hist,cv2.cv.CV_COMP_CORREL)
			print full_path
			print diff

			cv2.imshow("Similar Image", img)
			cv2.moveWindow("Similar Image",600,100)
			key = cv2.waitKey(1) & 0xFF

			if diff > 0.8:
				time.sleep(3)
