import os

def find_files_recursive(suffix, path, found_list):
  """
    Finds files by extension going recursively on the elements of a path.

    Parameters:
        path (str): The path to find file on.
        extension (str): The extension to search.
        found_list (list): The list of found files that have the given extension.
  """
  is_file = os.path.isfile(path)

  if is_file == False:
    path_item_list = os.listdir(path)

    for entry in path_item_list:
      full_path = os.path.join(path, entry)
      find_files_recursive(suffix, full_path, found_list)
  elif path.endswith(suffix):
    found_list.append(path)

def find_files(suffix, path):
  """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
  """
  if not path:
    raise ValueError("The path can't be empty.")

  found_list = list()

  find_files_recursive(suffix, path, found_list)

  return found_list

# This call tests the regular execution path.
# Expected: ['./testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c']
print(find_files(".c", "./testdir"))
# This call tests when the parameter is a file and not directory.
# Expected: ['./testdir/subdir3/subsubdir1/b.c']
print(find_files(".c", "./testdir/subdir3/subsubdir1/b.c"))
# This call tests when there's no files for the given extension.
# Expected: []
print(find_files(".py", "./testdir/"))
# This call tests when the given extension is empty.
# Expected:
# ['./testdir/subdir5/a.c',      './testdir/subdir5/a.h',      './testdir/t1.c',
#  './testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep', './testdir/t1.h',
#  './testdir/subdir1/a.c',      './testdir/subdir1/a.h',      './testdir/subdir3/subsubdir1/b.c',
#  './testdir/subdir3/subsubdir1/b.h']
print(find_files("", "./testdir/"))
#This call tests when the path parameter is empty.
# Expected: ValueError
# print(find_files("", ""))