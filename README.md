🔄 Odoo Upgrade Helper — Manifest & XML Porting Tool
This tool is designed to automatically upgrade legacy Odoo modules (e.g., from version 13 or 14) by cleaning up outdated structures that are no longer compatible with newer versions like Odoo 16 and 17.

✨ Features
✅ Auto-clean __manifest__.py

Fixes incorrect or malformed version strings

Removes unnecessary commas and characters

✅ Convert deprecated attrs

Transforms attrs="{'readonly': [('field', '=', value)]}"
into readonly="field == value" style (Odoo 17+)

✅ Handles readonly, invisible, and required

Based on simple and safe parsing via ast.literal_eval

✅ Batch upgrade

Processes multiple .xml, .py, and .js files in one go

Compatible with odoo-bin --upgrade-code

📦 Use Case
If you're migrating an Odoo project from v13 to v17, this tool helps:

Avoid runtime errors caused by deprecated attrs

Maintain cleaner and modern XML views

Ensure versioning is valid and standardized

📁 File Types Supported
__manifest__.py

.xml (views)

.py (optional future extension)

.js (if containing deprecated view-mode declarations)

💡 Roadmap
 Attrs → Expression migration

 Manifest version fixer

 Automated tests

 GUI for previewing changes

 PR-ready formatting option

🤝 Contribution
Pull requests are welcome! If you find edge cases or want to add test coverage, feel free to contribute.

📜 License
MIT License
