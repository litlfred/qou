#!/usr/bin/env python3
"""Re-measure bean `qou-pqmw`'s 78 bare-projection entries against the tree.

The bean's list is a snapshot taken 2026-08-10.  Draining it entry-by-entry
without re-checking writes disclosures onto declarations that have since been
fixed, moved or deleted -- `core-levi-form.lean` is the worked case: all three
of its entries are stale, because `6c17f7203d` (2026-08-31, bean `qou-z9ws`)
had already rewritten the file to the data-as-parameters shape.

Buckets, by whether the entry still RESOLVES (not whether it is still a defect):

  file-gone      the path no longer exists
  decl-gone      the file exists, the declaration name is not in it
  moved          resolves, at a different line than the bean records
  same-line      resolves, exactly where the bean records

`decl-gone` means "no longer resolves by name" -- a rename and a deletion look
identical here, and separating them needs `git log -S`, which this does not do.

Usage:  python3 scripts/pqmw-queue-recheck.py [--json OUT]
"""
import re, sys, json, pathlib

DECL = r"(?:private[ \t]+)?(?:noncomputable[ \t]+)?(?:theorem|lemma|def|abbrev|instance)"

def main() -> int:
    beans = sorted(pathlib.Path('.beans').glob('qou-pqmw--*.md'))
    if not beans:
        print("bean qou-pqmw not found", file=sys.stderr); return 2
    rows = re.findall(r"^- `([^`]+):(\d+)` — `([^`]+)`", beans[0].read_text(), re.M)
    if not rows:
        print("no entries parsed -- the bean's list format changed", file=sys.stderr); return 2

    out = {"file_gone": [], "decl_gone": [], "moved": [], "same_line": []}
    for path, line, decl in rows:
        p = pathlib.Path(path)
        if not p.exists():
            out["file_gone"].append({"decl": decl, "path": path}); continue
        s = p.read_text(errors='replace')
        base = decl.split('.')[-1]
        m = re.search(rf"^[ \t]*{DECL}[ \t]+{re.escape(base)}\b", s, re.M)
        if not m:
            out["decl_gone"].append({"decl": decl, "path": path}); continue
        now = s[:m.start()].count('\n') + 1
        rec = {"decl": decl, "path": path, "bean_line": int(line), "now_line": now}
        out["moved" if now != int(line) else "same_line"].append(rec)

    tot = len(rows)
    unresolved = len(out["file_gone"]) + len(out["decl_gone"])
    print(f"entries in the bean : {tot}")
    for k in ("file_gone", "decl_gone", "moved", "same_line"):
        print(f"  {k:12s}: {len(out[k])}")
    print(f"\nNO LONGER RESOLVES  : {unresolved} / {tot} ({100*unresolved/tot:.0f} %)")
    print(f"still at bean's line: {len(out['same_line'])}")

    if "--json" in sys.argv:
        dest = sys.argv[sys.argv.index("--json") + 1]
        json.dump(out, open(dest, "w"), indent=1)
        print(f"\nwrote {dest}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
