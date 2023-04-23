import logging
import glob
import yapsy.IPlugin

import tunnercore


class RowsTextFileReader(tunnercore.TunnerCommand):
    cmd_type = "rows.text.file.reader"
    description = ""
    examples = """
                {
                    "cmd.type": "rows.reader",
                    "input.key": "located.file",
                    "output.key": "read.rows"
                },
        """

    # TODO: Excluded tags
    def execute(self, cmd_cfg, data):

        input_key = cmd_cfg["input.key"]
        output_key = cmd_cfg["output.key"]

        rows = []
        located_file = data[input_key]

        with open(located_file.path, "r") as file:
            row = tunnercore.Row()

            for number, text in enumerate(file.readlines()):
                row.source = located_file.path
                row.number = number
                row.text = text

        data[output_key] = rows


        # tags = cmd_cfg["tags"]
        # pattern = cmd_cfg["pattern"]
        # output_key = cmd_cfg["output.key"]
        #
        # located_files = [tunnercore.LocatedFile(path, tags) for path in glob.glob(pattern, recursive=True)]
        #

        #
        # if output_key not in data:
        #     data[output_key] = []
        #
        # data[output_key] += located_files