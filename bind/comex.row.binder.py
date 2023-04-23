import logging
import glob
import yapsy.IPlugin

import tunnercore


class RowMatchBinder(tunnercore.TunnerCommand):
    cmd_type = "row.match.binder"
    description = ""
    examples = """
                {
                    "cmd.type": "row.match.binder",
                    "input.text.key": "read.artefact.files",
                    "input.matches.key": "artefact.re.matches",
                    "output.key": "re.matches"
                },
        """

    # TODO: Absolute path
    def execute(self, cmd_cfg, data):
        input_text_key = cmd_cfg["input.text.key"]
        input_match_key = cmd_cfg["input.matches.key"]

        output_key = cmd_cfg["output.key"]

        if output_key not in data:
            data[output_key] = []

        text = data[input_text_key]
        matches = data[input_match_key]

        rows = []
        for number, text_row in enumerate(text.split("\n")):
            row = tunnercore.Row()
            row.number = number
            row.text = text_row
            for match in matches:
                # TODO: One line match VS multi line match
                if row.number >= match.range.line.start and row.number <= match.range.line.end:
                    row.matches.append(match)
                    self.log(logging.DEBUG, f"Row {row.number} match rule {match.rule.id} added.")
            rows.append(row)

        data[output_key] = rows
        self.log(logging.DEBUG, f"Binded output: {len(data[output_key])}")