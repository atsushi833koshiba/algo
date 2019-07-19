import os
import unittest


# Let us print the files in the directory in which you are running this script
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
    list = []

    files_or_dirs =  os.listdir(path)
    for file_or_dir in files_or_dirs:
        concated_path = path + '/' + file_or_dir
        if os.path.isdir(concated_path):
            list += find_files(suffix,concated_path)

        if file_or_dir.endswith(suffix):
            list.append(concated_path)

    return list

def get_paticular_path(extention, root):
    paticular_paths = []
    if os.path.isdir(root):
        paticular_paths = find_files(extention,root)

    return paticular_paths;


def test_case1_get_paticular_path():
    actual = get_paticular_path(".c", "./testdir")

    # Print list to check its contents.
    statement = "Test Case3 \n {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    # Expected:  [
    # './testdir/subdir1/a.c',
    # './testdir/subdir3/subsubdir1/b.c',
    # './testdir/subdir5/a.c',
    # './testdir/t1.c']


def test_case2_get_paticular_path():
    actual = get_paticular_path(".c", "./testdir_case2")

    # Print list to check its contents.
    statement = "Test Case2 \n {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    # Expected:  [
    # './testdir_case2/subdir1/a.c',
    # './testdir_case2/subdir3/ab.c',
    # './testdir_case2/subdir3/subsubdir1/b.c',
    # './testdir_case2/subdir3/subsubdir1/subsubsubdir1/c.c',
    # './testdir_case2/subdir3/subsubdir1/subsubsubdir2/x.c',
    # './testdir_case2/subdir4/t3.c',
    # './testdir_case2/subdir5/a.c',
    # './testdir_case2/t1.c']


def test_case3_get_paticular_path():
    actual = get_paticular_path(".c", "./testdir_case3")

    # Print list to check its contents.
    statement = "Test Case3 \n {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    # Expected: ['./testdir_case3/subdir5/subsubdir1/subsubsubdir1/subsubsubsubdir1/a.c']


def test_case4_get_paticular_path():
    actual =  get_paticular_path(".c", "./testdir_case4")
    statement = "Test Case4 \n {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    # Expected: []


def test_case5_get_paticular_path():
    actual =  get_paticular_path(".c", "./testdir_case5")
    statement = "Test Case5 \n {} \n =====================================================================================\n"\
    .format(actual)
    print(statement)
    # Expected: []

test_case1_get_paticular_path()
test_case2_get_paticular_path()
test_case3_get_paticular_path()
test_case4_get_paticular_path()
test_case5_get_paticular_path()
