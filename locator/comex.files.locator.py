import logging
import glob
import yapsy.IPlugin

import tunnercore


class FilesLocator(tunnercore.TunnerCommand):
    cmd_type = "files.locator"
    description = ""
    examples = """
                {
                    "cmd.type": "files.locator",
                    "pattern": "./**/debug.log",
                    "output.tags": ["located.text.file@debuglog"],
                    "output.key": "located.files"
                },
        """

    # TODO: Absolute path
    def execute(self, cmd_cfg, data):
        output_tags = cmd_cfg["output.tags"]
        pattern = cmd_cfg["pattern"]
        output_key = cmd_cfg["output.key"]

        located_files = [tunnercore.LocatedFile(path, output_tags) for path in glob.glob(pattern, recursive=True)]

        for located_file in located_files:
            self.log(logging.DEBUG, f"Located file {located_file.path}")

        if output_key not in data:
            data[output_key] = []

        data[output_key] += located_files