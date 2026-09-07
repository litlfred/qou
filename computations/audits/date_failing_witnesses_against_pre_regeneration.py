"""Date each failing witness: was it already failing BEFORE the regeneration?

3cc4b2aab1 is the 64-producer post-regeneration sweep. Its parent is the last
pre-regeneration state of every witness it touched.
"""
import json, subprocess, pathlib

PRE = "3cc4b2aab1~1"

def at(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    if r.returncode != 0: return None
    try: return json.loads(r.stdout)
    except Exception: return None

def fails(w):
    return sorted(a.get("name") for a in (w.get("assertions") or []) if a.get("passed") is False)

rows = []
for p in sorted(pathlib.Path("computations").rglob("*.witness.json")):
    if "_deprecated" in str(p): continue
    try: now = json.loads(p.read_text())
    except Exception: continue
    if now.get("allPassed") is not False: continue
    if (now.get("computedAt") or "")[:10] < "2026-09-06": continue
    pre = at(PRE, str(p))
    f_now = fails(now)
    if pre is None:
        verdict, detail = "NEW-FILE", "no pre-regeneration version"
    else:
        f_pre = fails(pre)
        if pre.get("allPassed") is False and f_pre == f_now:
            verdict = "PRE-EXISTING"
            detail = f"same {len(f_pre)} failing, computedAt {pre.get('computedAt','')[:10]}"
        elif pre.get("allPassed") is False:
            verdict = "WIDENED"
            detail = f"was {len(f_pre)} -> now {len(f_now)}; new: {sorted(set(f_now)-set(f_pre))}"
        else:
            verdict = "*** REGRESSION ***"
            detail = f"was allPassed=true @ {pre.get('computedAt','')[:10]}; now failing {f_now}"
    rows.append((verdict, str(p), now.get("producer") or now.get("scriptFile") or "?", detail))

order = {"*** REGRESSION ***":0, "WIDENED":1, "NEW-FILE":2, "PRE-EXISTING":3}
rows.sort(key=lambda r: (order.get(r[0],9), r[1]))
from collections import Counter
print("tally:", dict(Counter(r[0] for r in rows)), f"  (total {len(rows)})\n")
for v, p, prod, d in rows:
    print(f"[{v}] {prod}")
    print(f"    {p}")
    print(f"    {d}")
