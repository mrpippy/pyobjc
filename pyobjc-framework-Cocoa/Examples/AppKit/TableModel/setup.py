"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="TableModel",
    app=["TableModel.py"],
    data_files=["English.lproj"],
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
    options=dict(py2app=dict(packages=["pkg_resources"])),
)
