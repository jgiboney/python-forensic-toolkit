import hashlib, os


def get_hash_of_string (string, algorithm='MD5'):
  """This function takes a string and hashes it using an algorithm.
  
  Acknowledgments:
  Addition of multiple hashing algorithms courtesy of Anthony Capece, Elvis Gadtaula,
  Nick Parenti, Jordan Polun, and Christopher Tafel.
  Dictionary and associated functionality is courtesy of Jordan Polun.
  Documentation is courtesy of Jazlin Perez and Jordan Polun.
  
  :param string: this is the string that will be hashed.
  :type string: str.
  :param algorithm: The hashing algorithm to be used. Defaults to 'MD5'.
  :type algorithm: str.
  :returns: str -- The hash of the string.
  """
  hashing_algorithms = {'MD5'   :hashlib.md5(), 
                        'SHA1'  :hashlib.sha1(), 
                        'SHA224':hashlib.sha224(), 
                        'SHA256':hashlib.sha256(), 
                        'SHA384':hashlib.sha384(), 
                        'SHA512':hashlib.sha512()
                       }
  if algorithm in hashing_algorithms:
    binary_string = convert_string_to_binary(string)
    hash_object = hashing_algorithms[algorithm]
    hash_object.update(binary_string)
    hash_digest = hash_object.hexdigest()
  else:
    hash_digest = ''
  return hash_digest


def read_binary_file (file_path):
  """This function will read and hash the contents of a file.
  
  Acknowledgments:
  Documentation is courtesy of Jazlin Perez and Jordan Polun.
  Thanks to Joseph Darocha for fixing the return error.
  
  :param file_path: this is the path to the file to be read.
  :type file_path: str.
  returns: str -- the content of the file to be read
  """
  try:
    file_object = open(file_path,'rb')
    file_contents = file_object.read()
    file_object.close()
    return file_contents
  except:
    raise


def get_hash_of_binary_file_contents (file_path, algorithm='MD5'):
  """This function will read and hash the contents of a file. 
  
  :param file_path: The path to the file to be hashed.
  :type file_path: str.
  :param algorithm: The hashing algorithm to be used. Defaults to 'MD5'.
  :type algorithm: str.
  :returns: str -- The hash of the contents of the file.
  """
  file_contents = read_binary_file(file_path)
  file_hash = get_hash_of_string(file_contents, algorithm)
  return file_hash


def get_hashes_of_files_in_directory (directory, algorithm='MD5'):
  """This function will get the hashes of all files in a directory.
  
  Acknowledgments:
  This function is courtesy of Minnie Kumar, Kyle O'Neill, Lawrence Rosenstadt,
  and Tiffany Xu.
  """
  hash_dictionary = {}
  if os.path.isdir(directory):
    for file_name in os.listdir(directory):
      file_path = os.path.join(directory, file_name)
      if os.path.isfile(file_path):
        file_hash = get_hash_of_binary_file_contents(file_path)
        hash_dictionary[file_path] = file_hash
  return hash_dictionary


def convert_string_to_binary (string):
  """This function attempts to convert a string to binary.
  
  Acknowledgments:
  Thanks to Minnie Kumar for finding an error in the
  get_hash_of_string function and providing a solution.
  
  Code based an answer from Elizafox on Stack Overflow:
  http://stackoverflow.com/questions/34869889/what-is-the-proper-way-to-determine-if-an-object-is-a-bytes-like-object-in-pytho
  """
  try:
    string = string.encode()
  except:
    pass
  return string


def do_files_have_same_content (file_1, file_2, algorithm='MD5'):
  """This function checks the hashes of the contents of two files. It returns
  a boolean.
  
  Acknowledgments:
  Thanks to Ryan Dorrien and Kyle O'Neill for working on this function.
  """
  file_1_hash = get_hash_of_binary_file_contents (file_1)
  file_2_hash = get_hash_of_binary_file_contents (file_2)
  if file_1_hash == file_2_hash:
    return True
  else:
    return False
