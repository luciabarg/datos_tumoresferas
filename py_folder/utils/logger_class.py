import logging
from datetime import datetime
import pandas as pd

class getLogger:
    """
    Genera el registrador (logger) que se utilizará para almacenar los pasos importantes a lo largo del proceso.
    """

    def __init__(self, local_dir, data_dir):
        """
        Constructor de la clase.

        Parámetros:
        - local_dir (str): Directorio local donde se encuentra almacenado el proyecto.
        - data_dir (str): Directorio de datos donde se guardarán los archivos generados.

        Atributos:
        - local_dir (str): Directorio local donde se encuentra almacenado el proyecto.
        - data_dir (str): Directorio de datos donde se guardarán los archivos generados.
        - l_extra (dict): Diccionario con información adicional para el registrador (logger).
        """     
        self.local_dir = local_dir
        self.data_dir = data_dir
        self.l_extra = {'name_class': 'logger_class'}
        

    def log_info(self):
        """
        Crea la configuración para el registro (logging), lo guarda en un archivo y también lo imprime en la consola.

        Retorna:
         - Objeto de registro (Logging).
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        # create file handler which logs even debug messages
        name_log = '_logs_'+ datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.log'
        fh = logging.FileHandler(name_log, mode='w')
        fh.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name_class)s - %(message)s')

        # add formatter to ch
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.propagate = False

        return logger