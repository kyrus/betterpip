import os
import shutil
import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def rmdir_mkdir(dirname):
    '''Removes a directory then recreates it'''
    if os.path.exists(dirname):
        shutil.rmtree(dirname, True)
    mkdir_p(dirname)
