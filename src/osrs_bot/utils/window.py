"""module used for window capture and tracking."""

import argparse
import pyautogui
import win32api
import win32gui

from datetime import datetime
from pathlib import Path
from PIL import ImageGrab
from typing import Optional, Tuple

from osrs_bot.utils.generic import is_valid_path


DEFAULT_IMAGE_DIR = "D:\\ImageTraining\\osrs-bot"


def setup_args() -> argparse.ArgumentParser:
    """
    Method to setup function arguments for the main function.

    Returns:
        argparse.ArgumentParser: Argument parser object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "capt_dir",
        help="the directory where the images are captured",
        default=DEFAULT_IMAGE_DIR,
        type=is_valid_path,
    )
    return parser


def get_named_window(name: str) -> Optional[Tuple[int]]:
    """
    Returns the position of the requested window name and brings the image to the foreground.

    Args:
        name (str): The name of the window.

    Returns:
        Optional[Tuple[int]]: The position of the window as a tuple (left, top, right, bottom),
        or None if the window is not found.
    """
    # Returns zero if no window is found
    window_handle = win32gui.FindWindow(None, name)
    # Handle is found, get the coords and set the image to the foreground
    if window_handle:
        win32gui.SetForegroundWindow(window_handle)
        disp = win32gui.GetWindowRect(window_handle)
    else:
        disp = None
    return disp


def screenshot_window(
    coords: Tuple[int, int, int, int], save_dir: str, sub_dir: Optional[str] = None
) -> None:
    """
    Method to save a screenshot of a window to disk.

    Args:
        coords (Tuple[int, int, int, int]): Coordinates of the window to screenshot (left, top, right, bottom).
        save_dir (str): Directory where the screenshot will be saved.
        sub_dir (str, optional): Subdirectory within save_dir. Defaults to "osrs".
    """
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create directory if it doesn't exist
    if sub_dir:
        directory = Path(save_dir, sub_dir)
    else:
        directory = Path(save_dir)
    directory.mkdir(parents=True, exist_ok=True)

    # Take screenshot
    screenshot = ImageGrab.grab(bbox=coords)

    # Save screenshot
    screenshot.save(directory.joinpath(f"{timestamp}.png"))
