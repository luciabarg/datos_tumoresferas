import pandas as pd
import numpy as np

class DataManipulation:
    """

    This class provides useful functions for exploring and manipulating the loaded dataframes

    """

    def __init__(self, data_dir, df, logger):
        """

        Args:

            data_dir (str): Local directory where the data is stored.

        """
        self.data_dir = data_dir
        self.df = df
        self.logger = logger
        self.l_extra = {'name_class': 'eda_class'}

    def compare_columns_df(self, df1, df2):
        """
        Función para comparar columnas presentes en dos dataframes.
        
        Parámetros:
        
        - df1: primer dataframe a comparar.
        - df2: segundo dataframe a comparar.
        """
        self.logger.info(
            'Comparing the columns of two dataframes:', extra=self.l_extra)

        # Obtener las columnas de df1 y df2 como conjuntos
        df1_columns = set(df1.columns)
        df2_columns = set(df2.columns)

        # Encontrar las columnas presentes en df1 pero no en df2
        extra_columns_df1 = df1_columns - df2_columns
        if extra_columns_df1 != set():
            self.logger.info(
                f'extra_columns in 1st dataframe : {extra_columns_df1}', extra=self.l_extra)
        else:
            self.logger.info(
                'There are not extra_columns in 1st dataframe:', extra=self.l_extra)

        # Encontrar las columnas presentes en df2 pero no en df1
        extra_columns_df2 = df2_columns - df1_columns
        if extra_columns_df2 != set():
            self.logger.info(
                f'extra_columns in 2nd dataframe : {extra_columns_df2}', extra=self.l_extra)
        else:
            self.logger.info(
                'There are not extra_columns in 2nd dataframe:', extra=self.l_extra)

    
    def drop_column_df(self, df, list_cols_to_drop=None):
        """
        Esta función elimina las columnas en la lista 'list_cols_to_drop' del dataframe.
    
        Parámetros:
        - df: dataframe del cual se eliminarán las columnas.
        - list_cols_to_drop: lista de columnas a eliminar. Si no se proporciona, se asume None.

        Retorna:
        - df_mod: el dataframe actualizado después de eliminar las columnas especificadas.
        """
       
        self.logger.info(
            f'Initial shape of df = {df.shape}', extra=self.l_extra)
        self.logger.info(
            f'columns to drop:= {list_cols_to_drop}', extra=self.l_extra)
        try:
            # Eliminar las columnas del dataframe
            df_mod = df.drop(list_cols_to_drop, axis=1).copy()
            self.logger.info(f'Final shape of df = {df_mod.shape}', extra=self.l_extra)
            self.logger.info(
                f'len and list of columns dropped: len = {len(list_cols_to_drop)},  list: {list_cols_to_drop} ', extra=self.l_extra)
        except:
            self.logger.info(
                f'That columns were already dropped. df has the following columns: {set(df.columns)}', extra=self.l_extra)

        return df_mod


    def selecting_columns(self, df, list_cols_to_select=None):
        """
        Esta función selecciona las columnas especificadas en la lista 'list_cols_to_select' del dataframe y devuelve un nuevo dataframe.
        
        Parámetros:
        - df: dataframe del cual se seleccionarán las columnas.
        - list_cols_to_select: lista de columnas a seleccionar. Si no se proporciona, se asume None.

        Retorna:
        - df_mod: nuevo dataframe que contiene solo las columnas seleccionadas.
        """
        self.logger.info(
            f'Initial shape of df = {df.shape}', extra=self.l_extra)
        self.logger.info(
            f'columns to select:= {list_cols_to_select}', extra=self.l_extra)
        try:
            # Seleccionar las columnas del dataframe
            df_mod = df[list_cols_to_select].copy()
            self.logger.info(f'Final shape of df = {df_mod.shape}', extra=self.l_extra)
            self.logger.info(
                f'len and list of columns selected: len = {len(list_cols_to_select)},  list: {list_cols_to_select} ', extra=self.l_extra)
        except:
            self.logger.info(
                f'That columns do not exists. df has the following columns: {set(df.columns)}', extra=self.l_extra)

        return df_mod


    def save_csv(self, df, filename):   
        """ 
        Función para guardar el dataframe generado en el directorio local.
        
        Parámetros:
        - df: dataframe a guardar en formato CSV.
        - filename: nombre del archivo CSV a generar y guardar.

        Retorna:
        - df: el mismo dataframe que se ha guardado en formato CSV.
        """
        # Guardar el dataframe en formato CSV en el directorio local
        df.to_csv(f"{self.data_dir}/{filename}", index=False)
        
        return df
  

    def make_columns_eda_transformations(self):
        """
        Esta función realiza transformaciones en el conjunto de datos llamando a las funciones anteriores.
        
        Retorna:
        - El conjunto de datos con las columnas transformadas realizadas a través del proceso de exploración.
        """
        self.logger.info('Beginning of the process of transforming columns ', extra=self.l_extra)

        # Inicializamos la lista de columnas a eliminar
        list_cols_to_drop = ["X", "Y", "XM","YM", "BX", "BY", "FeretX", "FeretY",
                             "Width", "Height", "Feret", "FeretAngle", "MinFeret", "AR"]
        
        df_mod = self.drop_column_df(self.df, list_cols_to_drop)
        self.logger.info(f'{df_mod.shape}', extra=self.l_extra)
       
        # solo como ejemplo de función
        self.compare_columns_df(self.df, df_mod)
    
        self.logger.info(f'Final dataframe has the following columns: {set(df_mod.columns)}', extra=self.l_extra)

        # Guardamos el dataframe para análisis y modelado posterior
        self.logger.info('Saving preprocesed dataframe to csv to further analysis and modeling', extra=self.l_extra)
        self.save_csv(df_mod, 'fiji_datos_mod.csv')
                      
        return df_mod
