import pandas as pd
import os

def get_dmc_hex():
    '''
    internal function for getting DMC colours and hexes
    '''
    # link to cross stitch DMCs
    dmc_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dmc_numbers_with_hex_codes.csv')
    dmc_spreadsheet = pd.read_csv(dmc_filepath)
    return dmc_spreadsheet[['DMC Floss Number','Hex Code']]

def get_dmc_name():
    '''
    internal function for getting DMC colours and names of flosses
    '''
    # link to cross stitch DMCs
    dmc_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dmc_numbers_with_hex_codes.csv')
    dmc_spreadsheet = pd.read_csv(dmc_filepath)
    return dmc_spreadsheet[['DMC Floss Number','DMC Floss Name']]

def get_dmc_full():
    '''
    internal function for getting DMC colours and names of flosses
    '''
    # link to cross stitch DMCs
    dmc_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dmc_numbers_with_hex_codes.csv')
    dmc_spreadsheet = pd.read_csv(dmc_filepath)
    return dmc_spreadsheet