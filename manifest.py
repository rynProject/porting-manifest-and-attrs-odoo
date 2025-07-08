import re

def upgrade(file_manager):
    manifest_files = [
        file for file in file_manager
        if file.path.name in ("__manifest__.py", "__openerp__.py")
    ]
    if not manifest_files:
        return

    version_regex = re.compile(r"(['\"]version['\"]\s*:\s*['\"])([^'\"]+)(['\"])")

    for fileno, file in enumerate(manifest_files, start=1):
        content = file.content

        def version_replacer(match):
            original_version = match.group(2)
            # Ambil dua digit angka pertama saja, misal 16.0
            version_parts = re.findall(r"\d+", original_version)
            if len(version_parts) >= 2:
                new_version = ".".join(version_parts[:2])
            elif version_parts:
                new_version = version_parts[0]
            else:
                new_version = "1.0"
            return f"{match.group(1)}{new_version}{match.group(3)}"

        content = version_regex.sub(version_replacer, content)
        file.content = content
        file_manager.print_progress(fileno, len(manifest_files))

