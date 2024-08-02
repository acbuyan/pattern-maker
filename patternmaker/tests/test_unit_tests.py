import unittest2
import patternmaker as pm

class test_unit_tests_patternmaker(unittest2.TestCase):

    def test_get_dmc_hex_column_names(self):
        dmc_hex = pm.get_dmc_hex()
        self.assertListEqual(list(dmc_hex.columns),['DMC Floss Number','Hex Code'])

    def test_get_dmc_hex_number_columns(self):
        dmc_hex = pm.get_dmc_hex()
        self.assertEqual(dmc_hex.shape[1],2)

    def test_get_dmc_hex_rows_greater_zero(self):
        dmc_hex = pm.get_dmc_hex()
        self.assertGreater(dmc_hex.shape[0],0)

    def test_get_dmc_name_column_names(self):
        dmc_name = pm.get_dmc_name()
        self.assertListEqual(list(dmc_name.columns),['DMC Floss Number','DMC Floss Name'])
    
    def test_get_dmc_name_number_columns(self):
        dmc_name = pm.get_dmc_name()
        self.assertEqual(dmc_name.shape[1],2)
    
    def test_get_dmc_name(self):
        dmc_name = pm.get_dmc_name()
        self.assertGreater(dmc_name.shape[0],0)

    def test_get_dmc_full_column_names(self):
        dmc_full = pm.get_dmc_full()
        column_names = ['DMC Floss Number','DMC Floss Name','R','G','B','Hex Code']
        self.assertEqual(list(dmc_full.columns),column_names)

    def test_get_dmc_full_number_columns(self):
        dmc_full = pm.get_dmc_full()
        self.assertEqual(dmc_full.shape[1],6)

    def test_get_dmc_full_rows_greater_zero(self):
        dmc_full = pm.get_dmc_full()
        self.assertGreater(dmc_full.shape[0],0)

if __name__ == '__main__':
    unittest2.main()