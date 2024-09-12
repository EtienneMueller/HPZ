import os
import unittest
from hpz.utils.path_utils import check_and_download_path


class TestHelperFunction(unittest.TestCase):
    
    def test_local_path(self):
        local_path = "/data/projects/punim2142/etienne/data/AG_cntnap257_spontaneous_20220324_fish11_2Hz_range245_step5_exposure10_power70"
        result = check_and_download_path(local_path)
        self.assertEqual(result, local_path)

    def test_remote_path(self):
        remote_path = "/projects/proj-5160_scott_lab-1128.4.503/Q4527/SPIM/Spontaneous/Raw/for_pipeline/e/AG_cntnap257_spontaneous_20220324_fish11_2Hz_range245_step5_exposure10_power70"
        result = check_and_download_path(remote_path)
        expected_local_path = os.path.join(os.getcwd(), "data/AG_cntnap257_spontaneous_20220324_fish11_2Hz_range245_step5_exposure10_power70")
        self.assertTrue(os.path.exists(result))
        self.assertEqual(result, expected_local_path)


if __name__ == '__main__':
    unittest.main()
