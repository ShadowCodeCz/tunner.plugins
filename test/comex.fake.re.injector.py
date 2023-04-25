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
        artifact_re_rule = tunnercore.ReRule()
        artifact_re_rule.id = "fake"
        artifact_re_rule.include = [re.compile("Compiler version", re.IGNORECASE)]
        data["artefact.re.rules"] = [artifact_re_rule]


        charon_initiator_re_rule = tunnercore.ReRule()
        charon_initiator_re_rule.id = "charon.initiator.communication"
        charon_initiator_re_rule.include = [re.compile(
            ".*sending packet.*\n"
            ".*received packet.*",
            re.IGNORECASE)
        ]
        data["charon.initiator.re.rules"] = [charon_initiator_re_rule]
        data["client.server.re.rules"] = self.time_re()


    def time_re(self):
        re_rule = tunnercore.ReRule()
        re_rule.id = "client.server.time"
        re_rule.include = [re.compile(
            "(?P<time>\d{4}-\d{2}-\d{2} \d{2}.\d{2}.\d{2},\d{3})\s.*",
            re.IGNORECASE)
        ]
        return [re_rule]

