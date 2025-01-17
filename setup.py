#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016-2023 The exspy developers
#
# This file is part of exspy.
#
# exspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# exspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with exspy.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages


extra_feature_requirements = {
    "gui-jupyter": [
        "hyperspy_gui_ipywidgets @ https://github.com/hyperspy/hyperspy_gui_ipywidgets/archive/hyperspy2.0.zip",
    ],
    "gui-traitsui": [
        "hyperspy_gui_traitsui @ https://github.com/hyperspy/hyperspy_gui_traitsui/archive/hyperspy2.0.zip",
    ],
    "doc": [
        "numpydoc",
        "pydata-sphinx-theme>=0.13",
        "sphinx",
        "sphinx-copybutton",
        "sphinx-design",
        "sphinx-favicon",
        "sphinx-gallery",
    ],
    "tests": [
        "pytest     >= 5.0",
        "pytest-mpl",
        "pytest-cov >= 2.8.1",
        "pytest-xdist",
    ],
    "dev": ["black"],
    "all": ["exspy[gui-jupyter]", "exspy[gui-traitsui]"],
}


version = {}
with open("exspy/_version.py") as fp:
    exec(fp.read(), version)


setup(
    name="exspy",
    version=version["__version__"],
    description="EELS and EDS analysis with the HyperSpy framework",
    license="LICENSE",
    url="https://github.com/pyxem/pyxem",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=[
        "data analysis",
        "microscopy",
        "electron microscopy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    entry_points={"hyperspy.extensions": "exspy = exspy"},
    packages=find_packages(),
    package_dir={"exspy": "exspy"},
    extras_require=extra_feature_requirements,
    install_requires=[
        "dask[array]",
        "hyperspy @ https://github.com/hyperspy/hyperspy/archive/RELEASE_next_major.zip",
        "matplotlib",
        "numexpr",
        "numpy",
        "pint",
        "pooch",
        "prettytable",
        "requests",
        "scipy",
        "traits",
    ],
    python_requires="~=3.8",
    package_data={
        "": ["LICENSE", "README.md"],
        "exspy": [
            "data/*hspy",
            "test/drawing/data/*hspy",
            "test/signals/data/*hspy",
            "hyperspy_extension.yaml",
        ],
    },
)
