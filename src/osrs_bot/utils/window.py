"""module used for window capture and tracking."""

import argparse
import time
import win32gui

from datetime import datetime
from pathlib import Path
from PIL import ImageGrab
from typing import Optional, Tuple

from osrs_bot.utils.generic import is_valid_path

DEFAULT_IMAGE_DIR = "D:\\ImageTraining\\osrs-bot"


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
        sub_dir (str, optional): Subdirectory within save_dir. Defaults to None.
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


def main() -> None:
    """cli function that runs windows capture.
    exmaple:

    start-win-capture `
        --name=Runelite `
        --capt-dir=D:\ImageTraining\osrs-bot `
        --sub-dir=al-kharid-cooking `
        --sleep=2 `
        --max-elapsed-time=60
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        help="name of the window to capture.",
        default="Runelite",
        type=str,
    )
    parser.add_argument(
        "--capt-dir",
        help="the directory where the images are captured",
        default=DEFAULT_IMAGE_DIR,
        type=is_valid_path,
    )
    parser.add_argument(
        "--sub-dir", help="sub-dir to store images in.", type=str, required=False
    )
    parser.add_argument(
        "--sleep",
        help="amount of time in seconds to sleep between captures",
        default=5,
        type=int,
    )
    parser.add_argument(
        "--max-elapsed-time",
        help="max-allowed-time in seconds for image capture",
        default=None,
        type=int,
    )
    args = parser.parse_args(namespace=None)

    start_time = time.time()
    try:
        while True:
            if (
                isinstance(args.max_elapsed_time, int)
                and time.time() - start_time >= args.max_elapsed_time
            ):
                break
            window = get_named_window(name=args.name)
            assert window is not None
            screenshot_window(
                coords=window, save_dir=args.capt_dir, sub_dir=args.sub_dir
            )
            time.sleep(args.sleep)
    except KeyboardInterrupt:
        pass
