import re
from pathlib import Path

ROOT = Path("content/quantum-observable-universe")
LEAN_ROOT = ROOT / "lean"
PROVABLE = {"theorem", "lemma", "proposition", "corollary"}
BUILDER_RE = re.compile(r"export\s+default\s+(\w+)\s*\(")
# match with dotall for multiline refs
LEAN_REF_RE = re.compile(r'lean:\s*\{\s*ref:\s*"([^"]+)"', re.DOTALL)

def resolve_lean(block_ts, ts_src):
    sib = block_ts.with_suffix(".lean")
    if sib.exists(): return sib
    m = LEAN_REF_RE.search(ts_src)
    if not m: return None
    if not m.group(1).startswith("qou:"): return None
    parts = m.group(1)[4:].split(".")
    decl = parts[-1]
    decl_re = re.compile(r"\b" + re.escape(decl) + r"\b")
    for cut in range(len(parts), 0, -1):
        cand = LEAN_ROOT.joinpath(*parts[:cut]).with_suffix(".lean")
        if cand.exists() and decl_re.search(cand.read_text(errors="ignore")):
            return cand
    return None

for ts in ROOT.rglob("*.ts"):
    if ts.name == ts.parent.name + ".ts": continue
    src = ts.read_text(errors="ignore")
    m = BUILDER_RE.search(src)
    if m and m.group(1) in PROVABLE:
        if resolve_lean(ts, src) is None:
            print(f"Missing: {ts.relative_to(ROOT)}")
