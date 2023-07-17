"""
Descripción del archivo
--------------------
Mas adelante es posible que trabajen en proyectos mas grandes y es posible que tengan que usar arhivos .py y no notebooks.

Tal como se lo dijeron en el teórico, al tener la funcion main pueden correr desde la terminal python etl.py y 
va a ejecutar lo definido en la funcion main.

Colab:

import os
os.chdir("/content/drive/My Drive/Datos_tumoresferas/py_folder")

! python main.py


"""
# Import libraries
import numpy as np
from utils import logger_class, read_dataset, eda_utils
import os
import warnings
warnings.filterwarnings('ignore')

# Defining local file paths
local_dir = os.path.abspath(__file__)
data_dir = os.path.abspath(os.path.join(__file__, "../", 'data/'))
print('local_dir', local_dir)
print('data_dir', data_dir)
l_extra = {'name_class': 'Main'}


def main():
    """
        Function that executes the other modules of the project.

    """

    # In this class, we define a logger that prints and saves a log file to help visualize the process
    log_class = logger_class.getLogger(local_dir, data_dir)
    logger = log_class.log_info()
    logger.info('Running Main experiment file', extra=l_extra)

    # This class loads the dataset provided and presents it in a dataframe format for familiar exploration and manipulation
    build_class = read_dataset.DatasetRead(data_dir, logger)
    fiji_datos = build_class.load_dataframes()

    # To retain the original information, let's create a copy of the original dataframes (in dataframe format) 
    # with the suffix "__raw" before proceeding with any changes
    #fiji_datos_raw = fiji_datos.add_suffix('_raw', axis=1).copy()
    
    # This class provides useful functions for preprocess the loaded dataframes
    eda_class = eda_utils.DataManipulation(data_dir, fiji_datos, logger) 
    fiji_datos_mod  = eda_class.make_columns_eda_transformations()

    data_return = fiji_datos_mod.copy() 
    
    return data_return


if __name__ == "__main__":
    #main()
    data_return = main()
    print('data_return.shape', data_return.shape)
