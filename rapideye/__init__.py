import argparse
import os
import cv2
import time
import numpy

def initiate():
	ap = argparse.ArgumentParser()
	ap.add_argument("-d", "--dataset", help="path to the dataset directory")
	ap.add_argument("-q", "--query", help="path to the query image")
	args = vars(ap.parse_args())

	reference = cv2.imread(args["query"],cv2.IMREAD_COLOR)

	blank = numpy.empty_like(reference)

	cv2.imshow("Query Image", reference)
	cv2.moveWindow("Query Image",50,100)

	reference = cv2.cvtColor(reference, cv2.COLOR_BGR2HSV)
	reference_hist_hue = cv2.calcHist([reference],[0],None,[256],[0,256])
	reference_hist_saturation = cv2.calcHist([reference],[1],None,[256],[0,256])
	reference_hist_value = cv2.calcHist([reference],[2],None,[256],[0,256])

	blank_hist = cv2.calcHist([reference],[0],None,[256],[0,256])

	height = None

	for file in os.listdir(args["dataset"]):
		if file.endswith(".png"):
			full_path = args["dataset"] + file
			img = cv2.imread(full_path,cv2.IMREAD_COLOR)

			height, width, channels = img.shape
			cv2.imshow("Similar Image", img)
			cv2.moveWindow("Similar Image",600,100)
			key = cv2.waitKey(50) & 0xFF

			img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			hist_hue = cv2.calcHist([img],[0],None,[256],[0,256])
			hist_saturation = cv2.calcHist([img],[1],None,[256],[0,256])
			hist_value = cv2.calcHist([img],[2],None,[256],[0,256])

			print full_path

			# Correlation

			diff_hue = cv2.compareHist(reference_hist_hue,hist_hue,cv2.cv.CV_COMP_CORREL)
			diff_saturation = cv2.compareHist(reference_hist_saturation,hist_saturation,cv2.cv.CV_COMP_CORREL)
			diff_value = cv2.compareHist(reference_hist_value,hist_value,cv2.cv.CV_COMP_CORREL)

			correlation_diff = (abs(diff_hue) + abs(diff_saturation) + abs(diff_value)) / 3

			if correlation_diff > 0.7:
				print "Found with CORRELATION"
				time.sleep(3)
				continue

			# Chi-Square

			diff_hue = cv2.compareHist(reference_hist_hue,hist_hue,cv2.cv.CV_COMP_CHISQR)
			diff_saturation = cv2.compareHist(reference_hist_saturation,hist_saturation,cv2.cv.CV_COMP_CHISQR)
			diff_value = cv2.compareHist(reference_hist_value,hist_value,cv2.cv.CV_COMP_CHISQR)

			chi_diff = (abs(diff_hue) + abs(diff_saturation) + abs(diff_value)) / 3

			if chi_diff < 600000.0 and correlation_diff > 0.6:
				print "Found with combination of CORRELATION & CHI-SQUARE"
				time.sleep(3)
				continue

			# Intersection

			diff_hue = cv2.compareHist(reference_hist_hue,hist_hue,cv2.cv.CV_COMP_INTERSECT)
			diff_saturation = cv2.compareHist(reference_hist_saturation,hist_saturation,cv2.cv.CV_COMP_INTERSECT)
			diff_value = cv2.compareHist(reference_hist_value,hist_value,cv2.cv.CV_COMP_INTERSECT)

			inter_diff = (abs(diff_hue) + abs(diff_saturation) + abs(diff_value)) / 3

			if chi_diff < 2000000.0 and correlation_diff > 0.5 and inter_diff < 90000.0:
				print "Found with combination of CORRELATION & CHI-SQUARE & INTERSECTION"
				time.sleep(3)
				continue
