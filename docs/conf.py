# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from sphinx_gallery.sorting import ExplicitOrder
from sphinx_gallery.sorting import FileNameSortKey

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CAMx Examples'
copyright = '2026'
author = ''
release = 'Unversioned'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_gallery.gen_gallery',
    'sphinx_copybutton',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints', '.ipynb_checkpoints/*']
suppress_warnings = ["config.cache"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Gallery Options --

sphinx_gallery_conf = {
    'filename_pattern': '/run_',
    'examples_dirs': '../examples',
    'gallery_dirs': 'auto_examples',
    'subsection_order': [
        '../examples/prep',
        '../examples/gridemiss',
        '../examples/ptsrce',
        '../examples/interlude',
        '../examples/mpe',
        '../examples/satellite',
        '../examples/maps',
    ],
    'within_subsection_order': FileNameSortKey,
}

nb_execution_timeout = 300 

latex_elements = {
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
\renewcommand{\sphinxtableofcontents}{\relax}
''',
}
