import hashlib, os


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


def get_hash_of_string (string, algorithm='MD5'):
  if algorith == 'MD5':
    hash_object = hashlib.md5(string)
    hash_digest = hash_object.hexdigest()
  else:
    hash_digest = ''
  return hash_digest


def read_binary_file (file_path):
  try:
    file_object = open(file_path,'rb')
    file_contents = file_object.read()
  except:
    raise
  return file_contents


