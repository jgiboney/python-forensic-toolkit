import hashlib, os


def get_hash_of_binary_file_contents (file_path, algorithm='MD5'):
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