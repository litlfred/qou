#!/usr/bin/env python3
"""Producers that cannot serialize an mpf, and hold one.

`json.dump` raises `TypeError: Object of type mpf is not JSON serializable`.
The failure is worse than a crash, because the corpus's witness-writing idiom
is

    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2)

and `open(..., "w")` **truncates the file before json.dump ever runs**. So a
producer in this state does not merely fail to update its witness — every run
destroys it. Measured on `binding_ladder_catalog.py`: 7352 bytes -> 491, dying
at `"B_AME_MeV"` on the first isotope.

That property is also why this audit is STATIC. You cannot screen for the bug
by running the candidates: running them is what does the damage.

## How a producer gets here

Nobody writes this bug directly. It arrives when a value that used to be a
float becomes an mpf *upstream*, in a pass that does not re-run the consumer:

  * `70ae502091a` (qou-psjm) routed 372 AME/CODATA literals to the registry
    across 178 files. `2.22456612` became `AME_B_DEUTERON_MEV_VALIDATION`,
    which is `mpf`.
  * `2b74577a65d` (qou-ckbv) made the hyperbolic-volume registry return mpf.

Both are correct precision fixes. Neither re-ran the producers it touched, and
a producer only reveals the breakage when someone runs it.

## What is flagged

A producer is a candidate when BOTH hold:

  1. it serializes with `json.dump(...)` / `json.dumps(...)` and passes no
     `default=` handler on at least one such call; and
  2. it can hold an mpf — it imports from a module known to serve mpf, or
     calls mpmath directly.

`default=str` is the corpus's existing escape hatch and is why sibling
producers with the same imports survive; a call carrying it is not flagged.

## What this does NOT establish

A candidate is not a proof. The mpf must actually reach the dumped object,
which depends on control flow this audit does not follow. Verify a candidate
the safe way:

    cp <witness> /tmp/backup.json     # or rely on git
    python3 <producer>                # observe
    git checkout -- computations/     # restore EVERYTHING, not one file:
                                      # producers write sibling witnesses

Exit 0 always (advisory); `--strict` exits 1 when candidates exist.
"""
from __future__ import annotations

import argparse
import ast
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent

#: Modules that serve mpmath.mpf values into a producer's namespace.
#: Deliberately short and evidence-based rather than exhaustive -- each entry
#: is a module measured to export at least one mpf.
MPF_SOURCES = {
    "mpmath",
    "codata_constants",
    "knot_volumes",
    "_precision",
    "q_parameter",
    "hecke_core",
}

SKIP_DIRS = {"_deprecated", ".git", "__pycache__", "node_modules"}


def _iter_producers(root: pathlib.Path):
    for p in sorted(root.rglob("*.py")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def _analyse(path: pathlib.Path):
    """Return (bare_dump_lines, mpf_import_names) or None if unparseable."""
    try:
        tree = ast.parse(path.read_text(errors="replace"))
    except SyntaxError:
        return None

    bare = []
    mpf_names = set()

    for node in ast.walk(tree):
        # --- (2) does an mpf source reach this namespace? -------------
        if isinstance(node, ast.ImportFrom) and node.module:
            head = node.module.split(".")[0]
            if head in MPF_SOURCES:
                mpf_names.add(node.module)
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in MPF_SOURCES:
                    mpf_names.add(a.name)

        # --- (1) a json dump with no default= -------------------------
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        if not isinstance(f, ast.Attribute) or f.attr not in ("dump", "dumps"):
            continue
        # json.dump / json.dumps, however json was bound
        if not (isinstance(f.value, ast.Name) and f.value.id.endswith("json")):
            continue
        if any(kw.arg == "default" for kw in node.keywords):
            continue
        bare.append(node.lineno)

    return bare, mpf_names


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when candidates exist")
    ap.add_argument("--root", default=str(COMP))
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root)
    hits = []
    scanned = 0
    for p in _iter_producers(root):
        res = _analyse(p)
        if res is None:
            continue
        scanned += 1
        bare, mpf_names = res
        if bare and mpf_names:
            hits.append((p, bare, sorted(mpf_names)))

    print("mpf-vs-json-encoder audit")
    print(f"  scanned {scanned} python files under {root}")
    print(f"  candidates: {len(hits)}"
          " (bare json.dump* AND an mpf-serving import)\n")
    for p, bare, mods in hits:
        rel = p.relative_to(root.parent) if root.parent in p.parents else p
        lines = ",".join(str(x) for x in bare)
        print(f"  {rel}")
        print(f"      bare dump at line(s) {lines}; mpf via {', '.join(mods)}")

    print("\n  A candidate is not a proof -- the mpf must actually reach the")
    print("  dumped object. Verify by running ONE, then `git checkout --")
    print("  computations/` to restore (producers write sibling witnesses).")

    if hits and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
