import logging
import re

import yapsy.IPlugin
import tunnercore


class FakeInterpret:
    def __init__(self, row):
        self.row = row

    def __str__(self):
        return "C O M P I L E R"


class Fake2Interpret:
    def __init__(self, row):
        self.row = row

    def __str__(self):
        return "HaHaHa HaHaHa HaHaHa HaHaHa HaHaHa HaHaHa"


class FakeInterpretsInjector(yapsy.IPlugin.IPlugin):
    cmd_type = "fake.interprets.injector"
    examples = """
            {
                "cmd.type": "fake.interprets.injector",
            },
    """

    def execute(self, cmd_cfg, data):
        data["interprets"] = {
            "fake": [FakeInterpret, Fake2Interpret]
        }
