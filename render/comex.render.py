import logging
import glob
import os

import yapsy.IPlugin

import hempl
import tunnercore


class Render(tunnercore.TunnerCommand):
    cmd_type = "render"
    description = ""
    examples = """
                {
                    "cmd.type": "render",
                    "input.rows.key": "artifact.rows",
                    "match.color": {"fake": "red"}
                    "row.interprets.key": "interprets"
                    "output.file.template": "./output/artefacts.html"
                },
        """

    def execute(self, cmd_cfg, data):

        input_rows_key = cmd_cfg["input.rows.key"]
        match_color = cmd_cfg["match.color"]
        interprets_key = cmd_cfg["row.interprets.key"]
        output_file_template = cmd_cfg["output.file.template"]
        os.makedirs(os.path.dirname(output_file_template), exist_ok=True)

        renders = []
        template = hempl.read_standard_template("dark")

        rows_render = []

        self.log(logging.DEBUG, f"Rows for render: {len(data[input_rows_key])}")
        self.log(logging.DEBUG, f"Interprets: {len(data[interprets_key])}")
        for row in data[input_rows_key]:
            self.log(logging.DEBUG, f"Rendering row {row.text}")
            rows_render.append(RowRender(row, match_color, data[interprets_key]))

        table = hempl.TableRender(
            # Schema
            [
                hempl.ColumnDefinition("", "5%"),
                hempl.ColumnDefinition("", "75%"),
                hempl.ColumnDefinition("", "20%"),
            ],
            # Style
            "table-without-head",
            # Rows Renders
            rows_render
        )

        renders.append(table)

        html = hempl.render(template, renders)
        hempl.save(html, output_file_template)


class RowRender:
    def __init__(self, row, match_color, interprets):
        self.row = row
        self.match_color = match_color
        self.interprets = interprets

    def __str__(self):
        # style = ""
        #
        # if len(self.row.matches):
        #     style = "red dark"

        return f"""
            <tr class="{self.style()}">
                <td>{self.row.number + 1}</td>
                <td>{self.row.text}</td>
                <td>{self.render_interpretations()}</td>
            </tr>
        """

    def style(self):
        style_classes = "dark-gray"

        if len(self.row.matches) == 0:
            return ""

        for match in self.row.matches:
            if match.rule.id in self.match_color:
                style_classes = self.match_color[match.rule.id]

        return style_classes

    def interpret(self):
        texts = []

        if len(self.row.matches) == 0:
            return []

        for match in self.row.matches:
            if match.rule.id in self.interprets:
                for cls in self.interprets[match.rule.id]:
                    interpret = cls(self.row)
                    texts.append(str(interpret))

        return texts

    def render_interpretations(self):
        texts = self.interpret()
        return " ".join([str(hempl.ColoredBoxRender(self.style(), text)) for text in texts])