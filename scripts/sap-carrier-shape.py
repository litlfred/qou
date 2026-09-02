#!/usr/bin/env python3
"""For each still-live self-assuming projection, is its carrier a DEFECT or an ACCESSOR?

## The question this answers, and the one it replaces

`scripts/sap-projection-liveness.py` says *which* ledger findings are still
`:= ctx.field`. It does not say which of those are worth fixing, and the
obvious discriminator is wrong.

**"Is the class parameterised?" does not separate them.** Tried first, on the
31 library projections: it splits 8 / 10 / 13, and the 8 "parameterised" bucket
contains `KnotFactorSpectralContext` (10 data fields), `SortingColorEnergyContext`
(9) and `SixTermMassFormulaContext` (8). A class can take a parameter *and*
carry ten objects the instance chooses; the parameter buys nothing then.

**The discriminator is DATA FIELDS.** AGENTS.md §3b-cond item 5 asks whether
the class axiomatises *hypotheses* or supplies the objects the claim is about.
Operationally:

- **`data = 0`** — every field is a proposition about the class's own
  parameters, so a `[C args]` binder constrains what the *caller* brought and
  the projection is Mathlib's accessor idiom (`Group.mul_assoc :=
  Group.mul_assoc`). Not a defect. Adjudicated so for the §4 gate classes on
  2026-08-31.
- **`data > 0`** — the instance chooses the objects, so the binder assumes
  nothing about anything the caller supplied. This is the defect, and the
  repair is to move the data to parameters.

Measured on `main` 2026-09-02 over the 31 library projections:
**19 defect, 2 accessor, 10 unresolved.**

## Limits — quote them with the number

- **10 are unresolved**, not clean. The class-declaration matcher wants
  `class Name … where` closing on one line; a multi-line signature, an
  `extends` chain, or a carrier declared in another form is missed. Those ten
  need reading, not counting.
- **The data/claim split is heuristic.** A field counts as a *claim* when its
  type contains a relation or quantifier (`= ≤ < > ∀ ∃ ↔ ≠ ∈`, `Nonempty`,
  `IsOpen`, `Subsingleton`, or ends in `Prop`); everything else counts as
  data. A `Prop`-valued field whose type is an opaque alias reads as data, and
  a data field whose type happens to mention `→` reads as a claim.
- So this is a **work-order, not a verdict**. Each row still needs the class
  read before it is repaired, and `data = 0` in particular is a reason to look
  rather than a licence to skip — see the gate classes, where the real gap was
  the *converse* of the equivalence the `.md` claimed, not the accessor.

USAGE
    python3 scripts/sap-carrier-shape.py                 # all trees
    python3 scripts/sap-carrier-shape.py --tree LIB      # library only
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content/quantum-observable-universe"

CLAIMY = re.compile(r"[=≤<>∀∃↔≠∈]|Nonempty|IsOpen|Subsingleton|Prop\s*$")
FIELD = re.compile(r"^  (\w+)\s*:(.*)$", re.M)


def load_tree() -> dict[str, str]:
    out = {}
    for f in glob.glob(str(CONTENT / "**/*.lean"), recursive=True):
        if "/.lake/" in f:
            continue
        out[os.path.relpath(f, ROOT)] = Path(f).read_text(errors="replace")
    return out


def find_class(tree: dict[str, str], cname: str):
    pat = re.compile(
        rf"^(?:class|structure)\s+{re.escape(cname)}\b([^\n]*?)\s+where\s*$", re.M
    )
    for f, t in tree.items():
        m = pat.search(t)
        if not m:
            continue
        body = t[m.end():]
        nb = re.search(r"\n(?=\S)", body)
        body = body[: nb.start()] if nb else body[:4000]
        fields = FIELD.findall(body)
        data = [x for x in fields if not CLAIMY.search(x[1])]
        claim = [x for x in fields if CLAIMY.search(x[1])]
        return f, m.group(1).strip(), len(data), len(claim)
    return None, None, None, None


def carrier_of(tree: dict[str, str], path: str, decl: str) -> str | None:
    t = tree.get(path) or Path(ROOT / path).read_text(errors="replace")
    short = decl.split(".")[-1]
    m = re.search(
        rf"^\s*(?:theorem|lemma|def|noncomputable def)\s+{re.escape(short)}\b(.*?)(?=\n\S)",
        t,
        re.S | re.M,
    )
    if not m:
        return None
    sig = m.group(1).split(":=")[0]
    for pat in (r"\[\s*\w+\s*:\s*([A-Z][\w'.]*)", r"\[\s*([A-Z][\w'.]*)",
                r"\(\s*\w+\s*:\s*([A-Z][\w'.]*)"):
        cm = re.search(pat, sig)
        if cm:
            return cm.group(1).split(".")[-1]
    return None


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--tree", choices=["LIB", "SIBLING"], help="restrict to one tree")
    ap.add_argument("--json", help="write the full result set here")
    args = ap.parse_args()

    live_json = ROOT / "sap-live.tmp.json"
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/sap-projection-liveness.py"),
         "--json", str(live_json)],
        capture_output=True, check=True,
    )
    rows = json.loads(live_json.read_text())
    live_json.unlink(missing_ok=True)

    sel = [r for r in rows if r["status"] == "PROJECTION"
           and (args.tree is None or r["tree"] == args.tree)]
    tree = load_tree()

    out, buckets = [], {"DEFECT": [], "ACCESSOR": [], "unresolved": []}
    for r in sorted(sel, key=lambda r: r["file"]):
        c = carrier_of(tree, r["file"], r["decl"])
        if not c:
            buckets["unresolved"].append((r, "no class binder found"))
            out.append({**r, "carrier": None, "verdict": "unresolved"})
            continue
        f, params, nd, nc = find_class(tree, c)
        if f is None:
            buckets["unresolved"].append((r, f"class {c} not found"))
            out.append({**r, "carrier": c, "verdict": "unresolved"})
            continue
        v = "ACCESSOR" if nd == 0 else "DEFECT"
        buckets[v].append(
            (r, f"{c}  data={nd} claim={nc}  params={'YES' if params else 'NONE'}")
        )
        out.append({**r, "carrier": c, "carrier_file": f, "data_fields": nd,
                    "claim_fields": nc, "verdict": v})

    for k in ("DEFECT", "ACCESSOR", "unresolved"):
        v = buckets[k]
        print(f"\n### {k}: {len(v)}")
        for r, s in v:
            print(f"  {s:<62} {os.path.basename(r['file'])}::{r['decl']}")
    print(f"\ntotals: DEFECT {len(buckets['DEFECT'])}  "
          f"ACCESSOR {len(buckets['ACCESSOR'])}  "
          f"unresolved {len(buckets['unresolved'])}")

    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))
        print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
