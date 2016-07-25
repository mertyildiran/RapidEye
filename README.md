# RapidEye

<p align="center">
  <img src="https://raw.githubusercontent.com/mertyildiran/RapidEye/master/rapideye.png" alt="RapidEye"/>
</p>

An Image Search Toolkit based on OpenCV's histogram comparison methods:

 - **cv2.cv.CV_COMP_CORREL**: Computes the correlation between the two histograms.
 - **cv2.cv.CV_COMP_CHISQR**: Applies the Chi-Squared distance to the histograms.
 - **cv2.cv.CV_COMP_INTERSECT**: Calculates the intersection between two histograms.
 - **cv2.cv.CV_COMP_BHATTACHARYYA**: Bhattacharyya / Hellinger distance, used to measure the “overlap” between the two histograms.

### Version
0.1.6

### Installation

```Shell
sudo apt-get install python-opencv
sudo pip install rapideye
```

### Usage

```Shell
rapideye --dataset PATH_TO_DATASET_DIRECTORY --query PATH_TO_REFERENCE_IMAGE
```

Example:

```Shell
rapideye --dataset dataset/ --query queries/103100.png
```
