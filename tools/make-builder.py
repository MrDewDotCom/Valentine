"""
Packs index.html into builder.html.

Run this after you change the code of index.html (not needed for normal use):
    python tools/make-builder.py
"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
template = (root / "index.html").read_text(encoding="utf-8")
src = (root / "tools" / "builder.src.html").read_text(encoding="utf-8")

assert "/*CONFIG-START*/" in template and "/*CONFIG-END*/" in template, "index.html is missing the CONFIG markers"
packed = "const TEMPLATE = " + json.dumps(template, ensure_ascii=False).replace("</", "<\\/") + ";"
out = src.replace("/*__TEMPLATE__*/", packed, 1)
(root / "builder.html").write_text(out, encoding="utf-8")
print(f"builder.html written ({len(out) // 1024} KB)")
