import sys, os
sys.path.append(os.path.join(os.getcwd(), "scripts"))
import importlib.util

spec = importlib.util.spec_from_file_location("lqp", "scripts/lean-qa-progress-table.py")
lqp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lqp)

print("Missing blocks:")
for num, ch in enumerate(lqp.CHAPTERS, 1):
    d = lqp.ROOT / ch
    if not d.is_dir(): continue
    for ts in sorted(d.glob("*.ts")):
        if ts.stem == ch: continue
        src = ts.read_text(errors="ignore")
        m = lqp.BUILDER_RE.search(src)
        kind = m.group(1) if m else None
        if kind in lqp.PROVABLE:
            lp = lqp.resolve_lean(ts, src)
            if lp is None:
                print(f"{ch} / {ts.name}")
