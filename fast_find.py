import sys, os, re
from pathlib import Path

qou_dir = Path("/Users/litlfred/space_cats/qou")
content_dir = qou_dir / "content" / "quantum-observable-universe"
lean_root = qou_dir / "content" / "quantum-observable-universe" / "lean"

PROVABLE = {"theorem", "lemma", "proposition", "corollary"}
BUILDER_RE = re.compile(r"export\s+default\s+(\w+)\s*\(")
LEAN_REF_RE = re.compile(r'lean:\s*\{\s*ref:\s*"([^"]+)"')

def resolve_lean(block_ts: Path, ts_src: str):
    sib = block_ts.with_suffix(".lean")
    if sib.exists():
        return sib
    m = LEAN_REF_RE.search(ts_src)
    if not (m and m.group(1).startswith("qou:")):
        return None
    parts = m.group(1)[4:].split(".")
    decl = parts[-1]
    decl_re = re.compile(r"\b" + re.escape(decl) + r"\b")
    for cut in range(len(parts), 0, -1):
        cand = lean_root.joinpath(*parts[:cut]).with_suffix(".lean")
        if cand.exists() and decl_re.search(cand.read_text(errors="ignore")):
            return cand
    return None

for root, _, files in os.walk(content_dir):
    for f in files:
        if f.endswith(".ts") and f != "quantum-observable-universe.ts":
            ts_path = Path(root) / f
            src = ts_path.read_text(errors="ignore")
            m = BUILDER_RE.search(src)
            kind = m.group(1) if m else None
            if kind in PROVABLE:
                if resolve_lean(ts_path, src) is None:
                    print(f"Missing Lean for: {ts_path}")

