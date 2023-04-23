import logging
import glob
import yapsy.IPlugin

import tunnercore


class TextFileReader(tunnercore.TunnerCommand):
    cmd_type = "text.file.reader"
    description = ""
    examples = """
                {
                    "cmd.type": "text.file.reader",
                    "input.key": "located.files",
                    "output.key": "read.files"
                },
        """

    # TODO: Excluded tags
    def execute(self, cmd_cfg, data):

        input_key = cmd_cfg["input.key"]
        output_key = cmd_cfg["output.key"]

        located_file = data[input_key]

        with open(located_file.path, "r") as file:
            data[output_key] = file.read()
