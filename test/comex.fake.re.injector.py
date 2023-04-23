import logging
import re

import yapsy.IPlugin
import tunnercore


class DataInjector(yapsy.IPlugin.IPlugin):
    cmd_type = "fake.re.injector"
    examples = """
            {
                "cmd.type": "fake.re.injector",
            },
    """

    def execute(self, cmd_cfg, data):
        re_rule = tunnercore.ReRule()
        re_rule.id = "fake"
        re_rule.include = [re.compile("Compiler version", re.IGNORECASE)]
        data["artefact.re.rules"] = [re_rule]

