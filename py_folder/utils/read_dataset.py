import pandas as pd

class DatasetRead:
    """

    In this class we will read and manipulate the data to feed the model

    """

    def __init__(self, data_dir, logger):
        """

        Args:

            data_dir (str): Local directory where the data is stored.

        """
        self.data_dir = data_dir
        self.logger = logger
        self.l_extra = {'name_class': 'load_class'}

    
    def read_csv(self, filename):
        """ 
        Leyendo el conjunto de datos 
        """
        self.logger.info('Cargando el conjunto de datos...', extra=self.l_extra)
        
        df = pd.read_csv(f'{self.data_dir}/{filename}')
        
        return df


    def load_dataframes(self):
        """
         Function that calls all of the above functions 
         (ahora hay solo una pero se pueden ir agregando funciones en ese módulo. 
         Se las puede llamar por separado o en conjunto usando esta función)

        """
        filename = 'raw/fiji_datos_0al7mo_labels.csv'
        fiji_datos = self.read_csv(filename)
       
        self.logger.info(
            f'shapes:{fiji_datos.shape}', extra=self.l_extra)

        return fiji_datos
