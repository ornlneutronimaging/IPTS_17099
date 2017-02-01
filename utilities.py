import numpy as np
import os


def calculate_file_temperature(left_T=-1, right_T=-1, left_time=-1, right_time=-1, file_time = -1):
    coeff = (float(right_T) - float(left_T)) / (float(right_time) - float(left_time))
    part1 = coeff * (float(file_time) - float(left_time))
    return part1 + float(left_T)

def get_first_temperature_and_index_value(index=-1, data_array=[], direction='left'):
    if direction == 'left':
        coeff = -1
    else:
        coeff = 1

    while (np.isnan(data_array[index])):
        index += coeff
    return [data_array[index], index]

def extract_temperature(index=-1, temperature_array=[], time_stamp_array=[]):
    
    [left_T, left_index] = get_first_temperature_and_index_value(index=index, data_array=temperature_array, direction='left')
    [right_T, right_index] = get_first_temperature_and_index_value(index=index, data_array=temperature_array, direction='right')
    
    left_time = time_stamp_array[left_index]
    right_time = time_stamp_array[right_index]
    
    file_time = time_stamp_array[index]

    file_temperature = calculate_file_temperature(left_T = left_T, right_T = right_T, 
                                                 left_time = left_time, right_time = right_time,
                                                 file_time = file_time)

    return file_temperature

def retrieve_T_from_file_vs_temperature_array(file_name='', file_array=[], temperature_array=[]):
    index = file_array.index(file_name)
    return temperature_array[index]

def make_output_file_name(bin_number=-1, index=-1, algorithm='mean'):
    '''
    takes the bin number and the algorithm name to create the output file name 
    
    Paramters:
        * bin_number: index of bin
        * index: index of file in folder
        * algorithm: (optional) default value 'mean'. Name of algorithm used to bin data
            will be used in the new output file name
            
    Return:
        * string file name of the output file
        
    Example:
        bin_number = 3
        index = 2
        algorithm = "mean"
        
        will return  'bin#3_0002_mean.fits
    
    '''
    
    ext = '.fits'
    list_output_file_name = []
    _output_file_name = "bin#{:03d}_{:04d}_{}.fits".format(bin_number, index, algorithm)
    return _output_file_name

def keep_folder_name(image):
    image_array = image.split('_')
    return image_array[0]

def is_extension(filename='', ext='.fits'):
    _ext = os.path.splitext(filename)[1]
    if _ext == ext:
        return True
    else:
        return False
    
def index_first_boolean(result, boolean=True):
    for _index, _value in enumerate(result):
        if _value == boolean:
            return _index
        
def index_last_boolean(result, boolean=True):
    for _index, _value in reversed(list(enumerate(result))):
        if _value == boolean:
            return _index
        
def find_index_of_value_in_array(array=[], value=-1, index_type='le'):
    '''
    index_type is either 'le' or 'ge'
    '''
    if index_type == 'le':
        result = x_axis < value
        return index_first_boolean(result, False)
    else:
        result = x_axis > value
        return index_last_boolean(result, False)
    
def make_user_friendly_list_of_bins(full_list_of_bins):
    return [os.path.basename(_file) for _file in full_list_of_bins]
        
    
    
    
