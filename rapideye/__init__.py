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

	cv2.imshow("Query Image", reference)
	cv2.moveWindow("Query Image",50,100)

	reference = cv2.cvtColor(reference, cv2.COLOR_BGR2HSV)
	reference_hist_hue = cv2.calcHist([reference],[0],None,[256],[0,256])
	reference_hist_saturation = cv2.calcHist([reference],[1],None,[256],[0,256])
	reference_hist_value = cv2.calcHist([reference],[2],None,[256],[0,256])

	for file in os.listdir(args["dataset"]):
		if file.endswith(".png"):
			full_path = args["dataset"] + file
			img = cv2.imread(full_path,cv2.IMREAD_COLOR)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			hist_hue = cv2.calcHist([img],[0],None,[256],[0,256])
			hist_saturation = cv2.calcHist([img],[1],None,[256],[0,256])
			hist_value = cv2.calcHist([img],[2],None,[256],[0,256])

			diff_hue = cv2.compareHist(reference_hist_hue,hist_hue,cv2.cv.CV_COMP_CORREL)
			diff_saturation = cv2.compareHist(reference_hist_saturation,hist_saturation,cv2.cv.CV_COMP_CORREL)
			diff_value = cv2.compareHist(reference_hist_value,hist_value,cv2.cv.CV_COMP_CORREL)

			diff = (abs(diff_hue) + abs(diff_saturation) + abs(diff_value)) / 3

			print full_path
			print "Hue Diff: " + str(diff_hue)
			print "Saturation Diff: " + str(diff_saturation)
			print "Value Diff" + str(diff_value)
			print "Average Diff: " + str(diff)
			print "----------------------------"

			img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
			cv2.imshow("Similar Image", img)
			cv2.moveWindow("Similar Image",600,100)
			key = cv2.waitKey(1) & 0xFF

			if diff > 0.7:
				time.sleep(3)
