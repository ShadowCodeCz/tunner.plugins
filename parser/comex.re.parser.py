import logging
import glob
import yapsy.IPlugin

import tunnercore


class ReParser(tunnercore.TunnerCommand):
    cmd_type = "re.parser"
    description = ""
    # TODO: Filter RE
    # TODO: Input tags [. AND .] OR [. AND .]
    examples = """
                {
                    "cmd.type": "re.parser",
                    "re.key": "re.rules",
                    "input.key": "read.files",
                    "output.key": "re.matches"
                },
        """

    def execute(self, cmd_cfg, data):
        re_key = cmd_cfg["re.key"]
        input_key = cmd_cfg["input.key"]
        output_key = cmd_cfg["output.key"]

        if output_key not in data:
            data[output_key] = []

        parser = tunnercore.ReParser()

        matches = parser.parse(data[input_key], data[re_key])

        # for m in matches:
        #     self.log(logging.DEBUG, f"text={m.text}, start.line={m.range.line.start}, end.line={m.range.line.end}")

        data[output_key] += matches
