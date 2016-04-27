# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

__author__ = "lqs"

setup(
    name="retrylib",
    version="0.1",
    description="retry some times on some exceptions",
    author="lqs",
    url="https://github.com/davechina/retry",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords="decorator retry",

    # If any package contains *.txt or *.rst files, include them:
    package_data = {
        '': ['*.txt']
    }
)
