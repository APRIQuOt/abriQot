import os
import shutil

def remove_pycache(root_dir='.'):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            print(f"Removing {pycache_path}")
            shutil.rmtree(pycache_path)

# Call the function to remove all __pycache__ directories starting from the current directory
remove_pycache()
