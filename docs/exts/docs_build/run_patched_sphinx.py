#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Hacks to patch up Sphinx-AutoAPI before running Sphinx.

Unfortunately we have a problem updating to a newer version of Sphinx-AutoAPI,
and have to use v1.0.0, so monkeypatching is used as the last resort.
"""

import os
import sys

import autoapi
from autoapi.extension import (
    LOGGER,
    ExtensionError,
    bold,
    darkgreen,
    default_backend_mapping,
    default_file_mapping,
    default_ignore_patterns,
)
from autoapi.mappers.python.objects import PythonPythonMapper
from sphinx.cmd.build import main


def new_python_python_mapper_display_getter(self: PythonPythonMapper) -> bool:
    """Patched getter to apply our special skip magic.

    If the docstring is exactly ``:sphinx-autoapi-skip:``, don't display this.
    """
    if ":sphinx-autoapi-skip:" in self.docstring.split():
        return False
    return old_python_python_mapper_property.__get__(self, PythonPythonMapper)


# HACK: sphinx-autoapi 1.0.0 is way too old to understand various modern Python
# magic such as typing.overload, so we apply magic to tell it when to skip.
old_python_python_mapper_property = PythonPythonMapper.display
PythonPythonMapper.display = property(new_python_python_mapper_display_getter)


def run_autoapi(app):
    """Load AutoAPI data from the filesystem."""
    if not app.config.autoapi_dirs:
        raise ExtensionError("You must configure an autoapi_dirs setting")

    # Make sure the paths are full
    normalized_dirs = []
    autoapi_dirs = app.config.autoapi_dirs
    if isinstance(autoapi_dirs, str):
        autoapi_dirs = [autoapi_dirs]
    for path in autoapi_dirs:
        if os.path.isabs(path):
            normalized_dirs.append(path)
        else:
            normalized_dirs.append(os.path.normpath(os.path.join(app.confdir, path)))

    for _dir in normalized_dirs:
        if not os.path.exists(_dir):
            raise ExtensionError(
                f"AutoAPI Directory `{_dir}` not found. Please check your `autoapi_dirs` setting."
            )

    # Change from app.confdir to app.srcdir.
    # Before:
    # - normalized_root = os.path.normpath(
    # -    os.path.join(app.confdir, app.config.autoapi_root)
    # -)
    normalized_root = os.path.normpath(os.path.join(app.srcdir, app.config.autoapi_root))
    url_root = os.path.join("/", app.config.autoapi_root)
    sphinx_mapper = default_backend_mapping[app.config.autoapi_type]
    sphinx_mapper_obj = sphinx_mapper(app, template_dir=app.config.autoapi_template_dir, url_root=url_root)
    app.env.autoapi_mapper = sphinx_mapper_obj

    if app.config.autoapi_file_patterns:
        file_patterns = app.config.autoapi_file_patterns
    else:
        file_patterns = default_file_mapping.get(app.config.autoapi_type, [])

    if app.config.autoapi_ignore:
        ignore_patterns = app.config.autoapi_ignore
    else:
        ignore_patterns = default_ignore_patterns.get(app.config.autoapi_type, [])

    if ".rst" in app.config.source_suffix:
        out_suffix = ".rst"
    elif ".txt" in app.config.source_suffix:
        out_suffix = ".txt"
    else:
        # Fallback to first suffix listed
        out_suffix = app.config.source_suffix[0]

    # Actual meat of the run.
    LOGGER.info(bold("[AutoAPI] ") + darkgreen("Loading Data"))
    sphinx_mapper_obj.load(patterns=file_patterns, dirs=normalized_dirs, ignore=ignore_patterns)

    LOGGER.info(bold("[AutoAPI] ") + darkgreen("Mapping Data"))
    sphinx_mapper_obj.map(options=app.config.autoapi_options)

    if app.config.autoapi_generate_api_docs:
        LOGGER.info(bold("[AutoAPI] ") + darkgreen("Rendering Data"))
        sphinx_mapper_obj.output_rst(root=normalized_root, source_suffix=out_suffix)


# HACK: sphinx-autoapi does not correctly use the confdir attribute instead of
# srcdir when specifying the directory to contain the generated files.
autoapi.extension.run_autoapi = run_autoapi

sys.exit(main(sys.argv[1:]))
