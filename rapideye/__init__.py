import argparse # Makes it easy to write user-friendly command-line interfaces.

def initiate():
	ap = argparse.ArgumentParser() # Define an Argument Parser
	ap.add_argument("-d", "--dataset", help="path to the dataset directory") # Add --dataset argument
	ap.add_argument("-q", "--query", help="path to the query image") # Add --query argument
	args = vars(ap.parse_args()) # Parse the arguments
