#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    unmanic-plugins.plugin.py

    Written by:               Ashley Bone <ashley.bone@pm.me>
    Date:                     10 June 2023

    Copyright:
        Copyright (C) 2023 Ashley Bone

        This program is free software: you can redistribute it and/or modify it under the terms of the GNU General
        Public License as published by the Free Software Foundation, version 3.

        This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
        implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
        for more details.

        You should have received a copy of the GNU General Public License along with this program.
        If not, see <https://www.gnu.org/licenses/>.

"""

import apprise, logging
from unmanic.libs.unplugins.settings import PluginSettings

# Configure plugin logger
logger = logging.getLogger("Unmanic.Plugin.apprise_push_notification")

class Settings(PluginSettings):
    settings = {
        "push_urls": "",
    }

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)
        self.form_settings = {
            "push_urls": {
                "label": "Apprise Push Notification URL(s)",
                "description": "Enter one or more push notification URLs, e.g. discord://4174216298/JHMHI8qBe7bk2ZwO5U711o3dV_js",
                "tooltip": "Enter one URL per line.",
                "input_type": "textarea",
            },
        }

def on_postprocessor_task_results(data):
    """
    Runner function - provides a means for additional postprocessor functions based on the task success.

    The 'data' object argument includes:
        final_cache_path                - The path to the final cache file that was then used as the source for all destination files.
        library_id                      - The library that the current task is associated with.
        task_processing_success         - Boolean, did all task processes complete successfully.
        file_move_processes_success     - Boolean, did all postprocessor movement tasks complete successfully.
        destination_files               - List containing all file paths created by postprocessor file movements.
        source_data                     - Dictionary containing data pertaining to the original source file.

    :param data:
    :return:
    
    """
    
    # Check the results and create an appropriate notification.
    notification_title = "Unmanic Task Update"
    original_basename = data.get("source_data").get("basename")
    notification_body = f"Task succeeded for {original_basename}."
    
    if not data.get("task_processing_success"):
        notification_body = f"Task failed for {original_basename}."
    elif not data.get("file_move_processes_success"):
        notification_body = f"Task succeeded for {original_basename}, but the file could not be moved to its destination."

    # Setup apprise and send the notification.
    settings = Settings(library_id=data.get("library_id"))
    push_urls = settings.get_setting("push_urls")
    apprise_obj = apprise.Apprise()

    # Add each URL separately in case any of them can't be parsed correctly.
    for url in push_urls.split("\n"):
        if not apprise_obj.add(url):
            logger.error(f"The push notification URL {url} could not be parsed.  Please check your settings.")

    apprise_obj.notify(body=notification_body, title=notification_title)
