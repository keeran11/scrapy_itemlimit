from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent
README_PATH = ROOT / "README.md"


setup(
    name="scrapy-itemlimit",
    version="0.2.1",
    description="Reusable Scrapy middleware for per-target item limits.",
    long_description=README_PATH.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "scrapy>=2.8",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Scrapy",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords=["scrapy", "middleware", "pagination", "item-limit"],
)
