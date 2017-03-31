import numpy as np
from scipy.ndimage import convolve


def gamma_filtering(data_array, threshold=0.1):
    
    final_data_array = []
    for _data in data_array:
        _data_filtered = single_gamma_filtering(_data)
        final_data_array.append(_data_filtered)
        
    return final_data_array 


def single_gamma_filtering(data, threshold=0.1):
    
    raw_data = np.copy(data)
    
    # find mean counts
    mean_counts = np.mean(raw_data)
    
    thresolded_raw_data = raw_data * threshold
    
    # get pixels where value is above threshold
    position = []
    [height, width] = np.shape(raw_data)
    for _x in np.arange(width):
        for _y in np.arange(height):
            if thresolded_raw_data[_y, _x] > mean_counts:
                position.append([_y, _x])
                
    # convolve entire image using 3x3 kerne
    mean_kernel = np.array([[1,1,1], [1,0,1], [1,1,1]]) / 8.0
    convolved_data = convolve(raw_data, mean_kernel, mode='constant')
    
    # replace only pixel above threshold by convolved data
    for _coordinates in position:
        [_y, _x] = _coordinates
        raw_data[_y, _x] = convolved_data[_y, _x]
        
    return raw_data