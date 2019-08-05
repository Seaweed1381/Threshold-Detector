import rawpy
import numpy
import argparse
import pathlib




def hotcells(array):
    hotc = numpy.load("hot.npz");
    hotc_array = hotc['hot'];
    x = hotc_array % (3000 * 5328);
    y = hotc_array // (3000 * 5328);

    maskedarray = numpy.ma.masked_array(array);
    maskedarray[y,x] = numpy.ma.masked;
    return numpy.ma.filled(maskedarray,0);

def checkPixels(array,size):
        
    aboveThreshold = numpy.array(numpy.nonzero(array > threshold));

    x = aboveThreshold[1];
    y = aboveThreshold[0];
    luminosities = array[array > threshold];
    data = numpy.column_stack((aboveThreshold[1], aboveThreshold[0], luminosities));
    numberOfDetections = len(luminosities);
    
    if args.out:

        pathName = pathlib.Path(outputDirectory);

        if not pathName.is_dir():
            pathName.mkdir(parents = True);
    
   
    numpy.savez(fileName, x = x, y = y, luminosities = luminosities, data = data, numberOfDetections = numberOfDetections);



def loadImage(name):
    image = rawpy.imread(name);
    array = image.raw_image;
    size = array.shape
    array = hotcells(array);
    checkPixels(array,size);


parser = argparse.ArgumentParser();
parser.add_argument('-f', type = str, nargs = '+', help = "gives location of image");
parser.add_argument('-t', type = int, nargs = 1, help = 'sets threshold', required = True);
parser.add_argument('-out', type = str, nargs = 1, help = 'sets directory for .npz files to be saved into');
args = parser.parse_args();

threshold = args.t[0];

if args.out:
    outputDirectory = args.out[0];

if args.f:
    for files in args.f:    
        
        fileName = str(files[0 : len(files) - 4] +'.npz');
        
        if args.out:
            fileName = outputDirectory + '/' + pathlib.PurePath(fileName).name;

        loadImage(files);
    


       
