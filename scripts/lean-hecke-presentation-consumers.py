#!/usr/bin/env python3
"""Count the consumers of every Hecke-algebra presentation in the Lean tree.

Bean `qou-img9` records that the corpus carries many coexisting Iwahori-Hecke
presentations.  Its recommendation ended *"Before retiring, count the downstream
consumers of each — not done here."*  This script is that count, kept as a script
rather than a number because every hand-kept figure in that bean has gone stale:
the original six was an undercount (the grep keyed on the *name* `IwahoriHecke`
and so could not see anything declared `HeckeAlgebra`), and the sibling's nine
was tree-dependent.

Three measurement traps, all of which produced wrong numbers here before being
fixed, and all of which inflate rather than deflate:

1. **Docstring code fences quote the OLD definition.**  `QOU/IwahoriHecke/Defn.lean`
   and `TypeA.lean` were repaired on 2026-08-30 (`430d2f50c0`, closing `qou-b5gu`)
   and their docstrings quote the superseded `Set.univ` body inside ``` fences.
   A raw grep reports two declarations per file and counts a retired object as live.
2. **Prose mentions are not uses.**  `IwahoriHeckeQuot` appears in four files, but
   in two of them only inside docstrings explaining what it is *not*.  Counting
   those gives 4 consumers against a true 2.
3. **`import QOU.SchurWeyl.HeckeAlgebra` is a module path, not a use.**  `QOU.lean`
   imports the whole library, so a bare name-grep makes it a consumer of everything.

So: strip block comments, line comments and import lines before matching, and
resolve consumers through the *import graph* (direct importer vs transitive) rather
than by proximity.  Run from the paper root:

    python3 ../../scripts/lean-hecke-presentation-consumers.py

or from the repo root with --root folio/quantum-observable-universe.
"""
from __future__ import annotations

import argparse
import pathlib
import re

# (label, defining file relative to the paper root, declaration name)
DECLS = [
    ("SchurWeyl.Hecke  (skein RingQuot, Fin n)",
     "lean/QOU/SchurWeyl/HeckeAlgebra.lean", "Hecke"),
    ("Hecke.IwahoriHecke  (Iwahori RingQuot, Fin n)",
     "lean/QOU/Hecke/IwahoriHecke.lean", "IwahoriHecke"),
    ("MathlibExt.IwahoriHecke.HeckeAlgebra  (general Coxeter matrix)",
     "lean/QOU/MathlibExt/IwahoriHeckeAlgebra.lean", "HeckeAlgebra"),
    ("IwahoriHecke.TypeA.IwahoriHeckeOfSn  (alias of the above)",
     "lean/QOU/IwahoriHecke/TypeA.lean", "IwahoriHeckeOfSn"),
    ("IwahoriHecke.Quotient.IwahoriHeckeQuot  (quadratic-only intermediate)",
     "lean/QOU/IwahoriHecke/Quotient.lean", "IwahoriHeckeQuot"),
    ("IwahoriHecke.IwahoriHecke  (alias; was the Set.univ defect qou-b5gu)",
     "lean/QOU/IwahoriHecke/Defn.lean", "IwahoriHecke"),
    ("BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra  (structure)",
     "lean/QOU/BraidKnot/IwahoriHeckeAPI.lean", "IwahoriHeckeAlgebra"),
    ("Knot.HeckeTwBasis.Hecke  (Perm ->_0 R, a free module)",
     "lean/QOU/Knot/HeckeTwBasis.lean", "Hecke"),
    ("PathIntegrals.HeckeAlgebra  (parametrised carrier)",
     "lean/QOU/PathIntegrals.lean", "HeckeAlgebra"),
    ("Braiding.HeckeAlgebra  (CasimirShared; parametrised carrier)",
     "lean/QOU/BraidKnot/CasimirShared.lean", "HeckeAlgebra"),
    ("Braiding.HeckeAlgebra  (knot-eigenbasis-complete; content-block sibling)",
     "braids-and-knots/knot-eigenbasis-complete.lean", "HeckeAlgebra"),
    ("BraidKnot.HeckeAlgebra  (frobenius-antipode stub; content-block sibling)",
     "braids-and-knots/frobenius-antipode-lean-stub.lean", "HeckeAlgebra"),
]


def strip_noncode(text: str) -> str:
    """Remove everything a name can appear in without being a use of it."""
    text = re.sub(r"/-.*?-/", "", text, flags=re.S)          # block / doc / module comments
    text = re.sub(r"--.*?$", "", text, flags=re.M)            # line comments
    text = re.sub(r"^\s*import\s+.*$", "", text, flags=re.M)  # module paths
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="paper root (holds lean/ and the chapter dirs)")
    args = ap.parse_args()
    root = pathlib.Path(args.root)

    files = sorted(p for p in root.rglob("*.lean") if ".lake" not in str(p))

    def modname(p: pathlib.Path) -> str | None:
        rel = p.relative_to(root).as_posix()
        if rel.startswith("lean/"):
            return rel[len("lean/"):-len(".lean")].replace("/", ".")
        return None

    mod2path = {m: p for p in files if (m := modname(p))}
    imports = {
        p: set(re.findall(r"^import\s+([A-Za-z0-9_.]+)", p.read_text(), re.M))
        for p in files
    }
    code = {p: strip_noncode(p.read_text()) for p in files}

    def transitive(p: pathlib.Path) -> set[str]:
        seen: set[str] = set()
        stack = list(imports[p])
        while stack:
            m = stack.pop()
            if m in seen:
                continue
            seen.add(m)
            if (q := mod2path.get(m)) is not None:
                stack.extend(imports[q])
        return seen

    rows = []
    for label, defpath, name in DECLS:
        dp = root / defpath
        if not dp.exists():
            rows.append((label, defpath, None, None))
            continue
        dm = modname(dp)
        pat = re.compile(r"\b" + re.escape(name) + r"\b")
        direct, trans = [], []
        for p in files:
            if p == dp or not pat.search(code[p]):
                continue
            if dm in imports[p]:
                direct.append(p.relative_to(root).as_posix())
            elif dm in transitive(p):
                trans.append(p.relative_to(root).as_posix())
        rows.append((label, defpath, direct, trans))

    rows.sort(key=lambda r: -(len(r[2]) + len(r[3])) if r[2] is not None else 1)
    for label, defpath, direct, trans in rows:
        if direct is None:
            print(f"  ??  MISSING FILE  {defpath}   {label}")
            continue
        print(f"{len(direct) + len(trans):3d} = {len(direct):2d} direct + "
              f"{len(trans):2d} transitive   {label}")
        print(f"        at {defpath}")
        for x in direct:
            print("        D", x)
        for x in trans:
            print("        T", x)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
