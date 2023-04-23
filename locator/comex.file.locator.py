import logging
import glob
import yapsy.IPlugin

import tunnercore


class FileLocator(tunnercore.TunnerCommand):
    cmd_type = "file.locator"
    description = ""
    examples = """
                {
                    "cmd.type": "file.locator",
                    "pattern": "./**/debug.log",
                    "output.key": "located.file"
                },
        """

    # TODO: Absolute path
    def execute(self, cmd_cfg, data):
        pattern = cmd_cfg["pattern"]
        output_key = cmd_cfg["output.key"]

        located_files = [tunnercore.LocatedFile(path, []) for path in glob.glob(pattern, recursive=True)]

        for located_file in located_files:
            self.log(logging.DEBUG, f"Located file {located_file.path}")

        if len(located_files) > 0:
            data[output_key] = located_files[0]