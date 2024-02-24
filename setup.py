import re
from pathlib import Path

from setuptools import find_namespace_packages, setup

REQUIREMENTS_FILE = "requirements.txt"

def get_requirements(requirements_file: str):
    """Loads the requirements from a given file."""
    requirements_content = Path(requirements_file).read_text()
    requirements_content = re.sub(
        r".*?file:.*#egg=([\d\w\.]+).*?\s",
        r"\1\n",
        requirements_content,
        flags=re.MULTILINE,
    )
    requirements = re.sub(
        r"#.*\n?", "\n", requirements_content, flags=re.MULTILINE
    ).splitlines()
    return list(filter(bool, map(str.strip, requirements)))

setup(
    name="osrs_bot",
    version="0.0.1",
    description="osrs bot for educational purposes with image and text processing.",
    author="jzuds",
    author_email="zudsgaming@gmail.com",
    python_requires=">=3.8",
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=get_requirements(REQUIREMENTS_FILE),
    entry_points={
        "console_scripts": [
            "start-basic-osrs-bot = osrs_bot.main:main",
            "start-win-capture = osrs_bot.utils.window:main"
        ]
    },
    zip_safe=False,
)