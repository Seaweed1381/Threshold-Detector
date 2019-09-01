import numpy
from sklearn.cluster import DBSCAN


def toMultidimensionalArray(place_holder,array, maxSize):
    location = place_holder[0];
    x = numpy.concatenate((array[location],numpy.zeros(maxSize- array[location].size)));
    
    
    return x;



def maxValue(array):
    return numpy.argmax(array);

def indicesOfMaxLuminosity(place_holders, array, locations):
    
    return array[place_holders[0]][locations[place_holders[0]]]; 

def brightest(groups,luminosity):

    indicesForParticularGroups = numpy.apply_along_axis(maxValue,1,luminosity)
    length = indicesForParticularGroups.size;
    
    indicesOfLuminosity = numpy.apply_along_axis(indicesOfMaxLuminosity,1,numpy.arange(length).reshape((length,1)), groups, indicesForParticularGroups);
    return indicesOfLuminosity;




x = numpy.load("yut/testImage2.npz")['x'];
y = numpy.load("yut/testImage2.npz")['y'];
xy = numpy.column_stack((x,y));
luminosity = numpy.load("yut/testImage2.npz")['luminosities'];
#to be changed
threshold = 2;

clustering = DBSCAN(eps = threshold, min_samples = 1);
clustering.fit(xy); 


ordered_indices = numpy.argsort(clustering.labels_);
ordered_labels = numpy.sort(clustering.labels_);


diff = numpy.diff(ordered_labels);
locations_to_split = numpy.argwhere(diff != 0) + 1;

groups = numpy.array_split(ordered_indices, locations_to_split.flatten());

luminosity_split = numpy.array_split(numpy.take(luminosity,ordered_indices),locations_to_split.flatten());

sizes_of_groups = numpy.concatenate(([locations_to_split[0][0]],numpy.diff(locations_to_split.flatten()), [groups[len(groups) - 1].size]));

max_size_of_groups = sizes_of_groups[numpy.argmax(sizes_of_groups)];


multidimensionalGroups = numpy.apply_along_axis(toMultidimensionalArray,1,numpy.arange(len(groups)).reshape(len(groups),1),groups,max_size_of_groups).astype('int');

multidimensionalLuminosities = numpy.apply_along_axis(toMultidimensionalArray,1,numpy.arange(len(luminosity_split)).reshape(len(groups),1), luminosity_split, max_size_of_groups).astype('int');




group_location_indices = brightest(multidimensionalGroups,multidimensionalLuminosities);
    
group_x = numpy.take(x, group_location_indices.astype('int'));
group_y = numpy.take(y, group_location_indices.astype('int'));






