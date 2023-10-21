from typing import Dict, Any


def render_template(template: str, arguments: Dict[str, Any]) -> str:
    from jinja2 import Environment, PackageLoader, select_autoescape

    env = Environment(
        loader=PackageLoader("trade", "templates"),
        autoescape=select_autoescape(["html", "xml"])
    )
    template = env.get_template(template)
    return template.render(**arguments)
