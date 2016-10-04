import sys, unittest
sys.path.append('../python_forensic_toolkit')
import file_hashing


class file_hashing_unit_tests (unittest.TestCase):
   
  def test_get_hash_of_binary_file (self):
    """
    Acknowledgments:
    This function is courtesy of Sydney Crespo, Stefan Dela Riva, Edwin Dominguez, 
    Michael Herir, Sage Hourihan, Joey Livornese, Kyle O'Neill, Ji Yong Park, 
    Jazlin Perez, and Briana Saur.
    """
    try:
      result = file_hashing.get_hash_of_binary_file_contents('resources/Test.txt','MD5')
      expected_result = '098f6bcd4621d373cade4e832627b4f6'  # MD5 of the word 'test'
      self.assertEqual(result,expected_result)
    except:
      return self.fail("get_hash_of_binary_file() failed unexpectedly")

  def test_get_hash_of_string (self):
    """
    Acknowledgments:
    This function is courtesy of Sydney Crespo, Stefan Dela Riva, Edwin Dominguez, 
    Michael Herir, Sage Hourihan, Joey Livornese, Kyle O'Neill, Ji Yong Park, 
    Jazlin Perez, and Briana Saur.
    """
    try:
      result = file_hashing.get_hash_of_string(b'test','MD5')
      expected_result = '098f6bcd4621d373cade4e832627b4f6'  # MD5 of the word 'test'
      self.assertEqual(result,expected_result)
    except:
      return self.fail("get_hash_of_string() failed unexpectedly")

  def test_read_binary_file (self):
    """
    Acknowledgments:
    This function is courtesy of Sydney Crespo, Stefan Dela Riva, Edwin Dominguez, 
    Michael Herir, Sage Hourihan, Joey Livornese, Kyle O'Neill, Ji Yong Park, 
    Jazlin Perez, and Briana Saur.
    """
    try:
      result = file_hashing.read_binary_file('resources/Test.txt')
      expected_result = b'test'
      self.assertEqual(result,expected_result)
    except FileNotFoundError:
      return self.fail("read_binary_file() raised FileNotFoundError unexpectedly!")