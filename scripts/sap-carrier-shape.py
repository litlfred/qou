#!/usr/bin/env python3
"""For each still-live self-assuming projection, is its carrier a DEFECT or an ACCESSOR?

## The question this answers, and the one it replaces

`scripts/sap-projection-liveness.py` says *which* ledger findings are still
`:= ctx.field`. It does not say which of those are worth fixing, and the
obvious discriminator is wrong.

**"Is the class parameterised?" does not separate them.** Tried first, on the
31 library projections: it splits 8 / 10 / 13, and the 8 "parameterised" bucket
contained `KnotFactorSpectralContext`, `SortingColorEnergyContext` and
`SixTermMassFormulaContext` — carriers with **ten, twelve and eight data
fields** respectively. A class can take a parameter *and* carry a dozen
objects the instance chooses; the parameter buys nothing then. (The first and
third have since been repaired and no longer appear; `SortingColorEnergyContext`
is still here at `data = 12`.)

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
**19 defect, 2 accessor, 10 unresolved.** After the first five repairs and the
field-parser fix below, the library figure is **10 / 2 / 10** and the whole
tree is **18 / 4 / 15**.

## The field parser under-counted, and by a lot — but no verdict moved

Found in Copilot's review of PR #6422. `FIELD` was `^  (\w+)\s*:` and was
wrong twice, both times downward:

* `\w` excludes the characters Lean identifiers use — `'`, `!`, `?`, and all
  of unicode. A field named `S'` or `y_λ` was **invisible**.
* It captured one name per line, so `W_sym W_std W_alt : R` counted as **one**
  field instead of three.

Measured by running both parsers over the same tree: **11 of 37 rows had their
data count corrected upward**, the worst by nineteen (`knot-eigenbasis-complete`,
4 → 23; `diagrammatic-double-magic-lr-fusion`, 7 → 21).

**And zero verdicts flipped.** That is not luck and is worth stating as the
reason the published triage stands: `ACCESSOR` requires `data == 0`, so an
under-count can only manufacture a *false accessor* — and no row was pushed to
zero, because a carrier with any data field at all had at least one name the
old regex could see. So the counts were wrong and the partition was not.

Quote the counts from a run, never from this docstring.

## Three sharper discriminators were tried after this one. All three fail.

Recorded so the next agent does not build a fourth heuristic instead of
reading the files.

1. **Explicit argument vs instance binder.** `(h : C)` looks like the caller
   supplying the record and `[ctx : C]` looks like instance search supplying
   it. Measured over the 19: 2 explicit, 17 instance. But it is **not a
   logical difference** — both elaborate to `∀ c : C, P c`. The binder style
   changes how the value is *found*, not what the theorem *says*. Two files
   with identical content would land in different buckets.

2. **Does the carrier's docstring disclose the field as an open input?**
   (Matching `open hypothesis` / `not derived` / `conjectural` / `OPEN` /
   `never asserting` near the declaration.) Splits 7 / 12 — and is wrong in
   both directions. `HasFrobeniusStability` scores **disclosed**, and that is
   the file whose ambient `LE` was `fun _ _ => True`, so every `≤` in it was
   `True`: a carrier can be candid in prose while the surrounding file empties
   the claim. Worse, the 7 includes a file this session had just edited, so
   the signal partly measured my own newly-written note. A prose signal
   graded on prose the grader wrote is not a measurement.

3. **Data-field count**, the one this script reports. It over-flags:
   `BondExtensiveBinding` (`data = 2` when measured 2026-09-02; the row has
   since left the queue) is the *honest* version of the same shape — the file
   states plainly that `extensive` is the arc's open input and that
   `binding_eq_bond_energy` is *"just `h.extensive`, exposed as a named
   consumer"*. Counting fields cannot see that.

**Why no syntactic signal can work.** `theorem foo [ctx : C] : ctx.a = ctx.b
:= ctx.claim` is a true, non-vacuous statement — it is the identity on a
field. What AGENTS.md §3b-cond item 5 asks is whether that field is an honest
*open hypothesis* the file names as such, or the block's own *conclusion*
dressed as a derivation. That is a question about the claim's role in the
argument, and it is settled by reading the file and its `.md`, not by shape.

Use this script to **order** the reading. Do not use it to skip it.

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
import tempfile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content/quantum-observable-universe"

CLAIMY = re.compile(r"[=≤<>∀∃↔≠∈]|Nonempty|IsOpen|Subsingleton|Prop\s*$")

# A field line: exactly two spaces, then one or more names, then `:` (not `:=`).
#
# `(\w+)` was WRONG in two ways, both of which UNDER-count data fields — and an
# under-count flips a DEFECT verdict to ACCESSOR, which is the one direction
# that hides work rather than inventing it.
#
#   1. `\w` excludes the characters Lean identifiers actually use — `'`, `!`,
#      `?`, and the whole unicode range (`Δ`, `χ`, `y_λ`, `σ₀`). A field named
#      `S'` was invisible. (Copilot review, PR #6422.)
#   2. It captured only ONE name, so the standard multi-binder line
#      `W_sym W_std W_alt : R` counted as a single field instead of three.
#
# So the name class is "anything that is not whitespace, a delimiter, or the
# colon", and the group is a whitespace-separated run of them. Requiring
# exactly two leading spaces keeps continuation lines of a previous field's
# type (indented four) from matching, and excluding `(` `⟨` etc. from the name
# class keeps a binder line like `  (h : Foo)` out.
_NAME = r"[^\s:()\[\]{}⟨⟩,]+"
FIELD = re.compile(rf"^  ((?:{_NAME}[ \t]+)*{_NAME})[ \t]*:(?!=)(.*)$", re.M)


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
        # One entry PER NAME: `W_sym W_std W_alt : R` is three fields, not one.
        data = claim = 0
        for names, ty in FIELD.findall(body):
            n = len(names.split())
            if CLAIMY.search(ty):
                claim += n
            else:
                data += n
        return f, m.group(1).strip(), data, claim
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

    # A private temp file, cleaned up on any exit path. The previous fixed
    # `ROOT / "sap-live.tmp.json"` clobbered concurrent runs and, when the
    # liveness call raised, left an untracked file in the repo root — which in
    # this repo reads as real work to the next agent's `git status`.
    fd, tmp = tempfile.mkstemp(prefix="sap-live-", suffix=".json")
    os.close(fd)
    try:
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/sap-projection-liveness.py"),
             "--json", tmp],
            capture_output=True, check=True,
        )
        rows = json.loads(Path(tmp).read_text())
    finally:
        Path(tmp).unlink(missing_ok=True)

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
