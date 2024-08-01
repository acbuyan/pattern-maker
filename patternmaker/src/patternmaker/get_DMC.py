import pandas as pd

from .links import dmc_spreadsheet_link

def get_dmc():
    '''
    internal function for getting DMC colours
    '''
    # link to cross stitch DMCs
    dmc_spreadsheet = pd.read_xls('')