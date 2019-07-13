# Threshold-Detector
Threshold Detector for CRAYFIS


The arguments that this program takes are -f followed by the names of however many images you want to use (leave out the .dng extension), -o followed by the names of the output .npz files, and -t followed by the threshold you want to set.  


-f [file names]
-o [output names]
-t threshold


This version gets rid of the for loops that had slowed down the previous version and incorporates a better command line interface using argparse.  
