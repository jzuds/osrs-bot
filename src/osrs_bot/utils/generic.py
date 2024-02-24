"""Generic helper functions."""

import os


def is_valid_path(path: str) -> bool:
    if not os.path.exists(path):
        raise Exception(f"path={path} does not exist.")
    return path
