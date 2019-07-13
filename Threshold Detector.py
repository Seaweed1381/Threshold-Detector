import rawpy
import numpy
import argparse

def checkPixels(array,size):
    
    aboveThreshold = numpy.array(numpy.nonzero(array > threshold));
    
    luminosities = array[array > threshold];
    
    data = numpy.column_stack((aboveThreshold[1], aboveThreshold[0], luminosities));

    numberOfDetections = len(luminosities);


    numpy.savez(fileName,data = data ,numberOfDetections = numberOfDetections);
        
    
def loadImage(name):
    image = rawpy.imread(name + '.dng');
    array = image.raw_image;
    size = array.shape
    
    checkPixels(array,size);


parser = argparse.ArgumentParser();
parser.add_argument('-f', type = str, nargs = '+', help = "Gives Location of Image (.dng Extension Must Not Be Added)");
parser.add_argument('-o', type = str, nargs = '+', help = "Names of Output .npz Packages", default = 1);
parser.add_argument('-t', type = int, nargs = 1, help = 'Sets Threshold');
args = parser.parse_args();

threshold = args.t[0];


for x in range(0,len(args.f)):    
    
    if (args.o == 1 or len(args.o) != len(args.f)):
        fileName = str(args.f[x] + '.npz');
    else:
        fileName = args.o[x];

    loadImage(args.f[x]);
