# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import numpydoc
from packaging.version import Version

# -- Project information -----------------------------------------------------

project = "exSpy"
copyright = "2023, exSpy Developers"
author = "exSpy Developers"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # numpydoc is necessary to parse the docstring using sphinx
    # otherwise the nitpicky option will raise many warnings
    # "numpydoc",
    "sphinx_design",
    "sphinx_favicon",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_gallery.gen_gallery",
]

linkcheck_ignore = [
    "https://doi.org/10.1021/acs.nanolett.5b00449",  # 403 Client Error: Forbidden for url
    "https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2818.2006.01549.x",  # 403 Client Error: Forbidden for url
    # Remove when setup
    "https://github.com/hyperspy/exspy-demos",
    "https://www.anaconda.com/blog/understanding-conda-and-pip",  # Transcient?
    # Remove once it is merged and the links are working
    "https://exspy.readthedocs.io",
    "https://github.com/hyperspy/exspy/blob/main/releasing_guide.md",
]

intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/latest", None),
    "hyperspy": ("https://hyperspy.org/hyperspy-doc/dev", None),
    "kikuchipy": ("https://kikuchipy.org/en/latest/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "python": ("https://docs.python.org/3", None),
    "rsciio": ("https://hyperspy.org/rosettasciio/", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "show_toc_level": 2,
    "github_url": "https://github.com/hyperspy/exspy",
    "icon_links": [
        {
            "name": "Gitter",
            "url": "https://gitter.im/hyperspy/hyperspy",
            "icon": "fab fa-gitter",
        },
    ],
    "logo": {
        "text": "exSpy",
    },
    "header_links_before_dropdown": 6,
    "navigation_with_keys": False,
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/hyperspy_logo.png"

# -- Options for sphinx_favicon extension -----------------------------------

favicons = [
    "hyperspy.ico",
]

# Check links to API when building documentation
nitpicky = False
# Remove when fixed in hyperspy
nitpick_ignore_regex = [(r"py:.*", r"hyperspy.api.*")]

# -- Options for numpydoc extension -----------------------------------

numpydoc_xref_param_type = True
numpydoc_xref_ignore = {"type", "optional", "default", "of"}

if Version(numpydoc.__version__) >= Version("1.6.0rc0"):
    numpydoc_validation_checks = {"all", "ES01", "EX01", "GL02", "GL03", "SA01", "SS06"}

autoclass_content = "both"

autodoc_default_options = {
    "show-inheritance": True,
}
toc_object_entries_show_parents = "hide"

# -- Sphinx-Gallery---------------

# https://sphinx-gallery.github.io
sphinx_gallery_conf = {
    "examples_dirs": "../examples",  # path to your example scripts
    "gallery_dirs": "auto_examples",  # path to where to save gallery generated output
    "filename_pattern": ".py",  # pattern to define which will be executed
    "ignore_pattern": "_sgskip.py",  # pattern to define which will not be executed
}

# -- Sphinx-copybutton -----------

copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True
