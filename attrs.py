import re
import ast

def upgrade(file_manager):
    files = [file for file in file_manager if file.path.suffix == ".xml"]
    if not files:
        return

    # Match attrs XML attribute
    attrs_re = re.compile(r"""attrs\s*=\s*["'](?P<dict>{.*?})["']""", re.DOTALL)

    def to_expr(domain):
        if isinstance(domain, list) and len(domain) == 1:
            field, op, value = domain[0]
            if isinstance(value, str) and not value.startswith(("'", '"')):
                value = f"'{value}'"
            return f"{field} {op} {value}"
        return ""

    for fileno, file in enumerate(files, start=1):
        content = file.content

        def convert_attrs(match):
            try:
                attr_dict = ast.literal_eval(match.group("dict"))
                new_attrs = []
                for key, domain in attr_dict.items():
                    expr = to_expr(domain)
                    if expr:
                        new_attrs.append(f'{key}="{expr}"')
                return " ".join(new_attrs)
            except Exception:
                return match.group(0)

        content = attrs_re.sub(convert_attrs, content)
        file.content = content
        file_manager.print_progress(fileno, len(files))

