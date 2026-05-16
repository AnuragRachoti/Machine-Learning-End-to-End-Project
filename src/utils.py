# Utility functions for the machine learning project. 
# This file can contain functions for data preprocessing, model evaluation, and any other 
# common tasks that are used across different components of the project.

import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import pickle



def save_object(file_path, obj):
    '''This function is responsible for saving the object as a pickle file'''
    import pickle
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)