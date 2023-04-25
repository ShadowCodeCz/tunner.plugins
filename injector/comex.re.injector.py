import logging
import glob
import yapsy.IPlugin
import re
import tunnercore


class ReInjector(tunnercore.TunnerCommand):
    cmd_type = "re.injector"
    description = ""
    examples = """
                {
                    "cmd.type": "re.injector",
                    "res": [
                        {"id": "re.id", "re": ".*"}
                    ]
                    "output.key": "re.injected.rules"
                },
        """

    # TODO: Absolute path
    def execute(self, cmd_cfg, data):
        res = cmd_cfg["res"]
        output_key = cmd_cfg["output.key"]

        if output_key not in data:
            data[output_key] = []

        rules = []
        for re_definition in res:
            r = tunnercore.ReRule()
            r.id = re_definition["id"]
            r.include = [re.compile(re_definition["re"])]

            rules.append(r)

        data[output_key] = rules