import os
import sys
from pathlib import Path
from typing import List, Union, Tuple

from functools import reduce


# Ensure the 'src' directory is in the Python path
project_root = Path(os.path.abspath(os.path.join(os.path.dirname('__file__'), '..')))
src_path = project_root / "src"

if src_path not in sys.path:
    sys.path.append(src_path)

print(sys.path)
import src

# def init_fs(paths_to_append: Union[List[str], Tuple[str]]) -> Result[str, str]:
#     try:
#         full_path = reduce(lambda p, sub_p: p / sub_p, paths_to_append, src_path)

#         if full_path not in sys.path:
#             sys.path.append(full_path)

#         return Ok(f"File path(s), {full_path}, successfully added to system path")
#     except Exception as e:
#          return Err(f"Problem with adding {full_path} to system path - {e}")


def init_fs(paths_to_append: Union[List[str], Tuple[str]]) -> None:
    try:
        full_path = reduce(lambda p, sub_p: p / sub_p, paths_to_append, src_path)

        if full_path not in sys.path:
            sys.path.append(full_path)

        print(f"File path(s), {full_path}, successfully added to system path")
    except Exception as e:
        print(f"Problem with adding {full_path} to system path - {e}")
