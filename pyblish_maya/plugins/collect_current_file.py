import os

import pyblish.api

from maya import cmds


@pyblish.api.log
class CollectCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current working file into context"""

    order = pyblish.api.CollectorOrder - 0.5

    hosts = ['maya']
    version = (0, 1, 0)

    def process(self, context):
        """Todo, inject the current working file"""
        current_file = cmds.file(sceneName=True, query=True)

        # Maya returns forward-slashes by default
        normalised = os.path.normpath(current_file)

        context.set_data('currentFile', value=normalised)

        # For backwards compatibility
        context.set_data('current_file', value=normalised)