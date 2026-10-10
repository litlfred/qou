#!/usr/bin/env python3
"""Assert that a `FAITHFUL inlined copy` of a Lean declaration has not diverged.

Why this exists
---------------
Two chapter-directory `.lean` files declare `QOU.BraidsAndKnots.EWHoefsmitData`
and `QOU.BraidsAndKnots.WeinbergAngleCategorical` under the SAME fully-qualified
names:

    content/.../nuclear-interactions/weinberg-angle-categorical.lean   (origin)
    content/.../mass-theory/categorical-higgs-mechanism.lean           (copy)

That is legal only because chapter-directory `.lean` files sit outside the Lake
library's `srcDir="."` + `globs=["QOU","QOU.+"]`, so the two are never elaborated
together and the names never actually collide. It is also a live hazard: the
copy announces itself as FAITHFUL, nothing enforces it, and a later edit to one
side would leave two different objects wearing one name with no error anywhere.

The copy exists because a chapter-directory `.lean` cannot import another one --
there is no module path between them. So the duplication is structural, not
laziness, and deleting it would need the shared declarations moved into the
library tree (which changes `lean.ref` resolution under AGENTS.md §0a). Until
someone decides to do that, this guard is what makes "FAITHFUL" checkable.

What it compares
----------------
The declaration body with docstrings (`/-- ... -/`) and blank lines removed, so
the two may document themselves differently -- which they do, deliberately --
while any change to a field, a binder or a type is a failure.

Exit 0 = identical. Exit 1 = diverged, with a diff. Exit 2 = a block is missing,
which is also a failure: it means a rename happened on one side only.

    python3 scripts/lean-inlined-copy-guard.py
"""
from __future__ import annotations

import difflib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORIGIN = ROOT / "folio/quantum-observable-universe/nuclear-interactions/weinberg-angle-categorical.lean"
COPY = ROOT / "folio/quantum-observable-universe/mass-theory/categorical-higgs-mechanism.lean"
HEADS = ("structure EWHoefsmitData", "class WeinbergAngleCategorical")


def block(path: pathlib.Path, head: str) -> str | None:
    """The declaration starting at `head`, docstrings and blank lines stripped."""
    src = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(rf"^{re.escape(head)}.*?(?=\n\n[a-zA-Z/]|\Z)", src, re.M | re.S)
    if not m:
        return None
    body = re.sub(r"/--.*?-/", "", m.group(0), flags=re.S)
    return "\n".join(l.rstrip() for l in body.splitlines() if l.strip())


def _selftest() -> int:
    """Prove the comparison fires. A guard never shown to fail is not a guard.

    Three cases, each a divergence this guard must catch and each a shape that
    has actually happened to inlined copies elsewhere in this corpus:
    a changed field type, a dropped field, and a changed binder.
    """
    base = block(ORIGIN, "class WeinbergAngleCategorical")
    if base is None:
        print("FAIL selftest: cannot read the origin block at all")
        return 1
    cases = [
        ("changed field type", base.replace("d.trB \u2260 0", "d.trB = 0", 1)),
        ("dropped a field", "\n".join(base.splitlines()[:-1])),
        ("changed a binder", base.replace("[Field R]", "[CommRing R]", 1)),
    ]
    bad = 0
    for name, mutated in cases:
        if mutated == base:
            # A no-op mutation makes the case vacuous: it would "pass" while
            # testing nothing. That happens when the pattern being edited has
            # moved in the source, which is precisely when the guard most needs
            # its own coverage checked.
            print(f"FAIL selftest [{name}]: the mutation was a no-op, so this "
                  f"case tests nothing -- the pattern it edits has moved")
            bad += 1
        else:
            print(f"ok   selftest [{name}] differs from the origin, as it must")
    # The other direction: an unmutated block must NOT read as diverged, and
    # `block()` must return the same text on two reads of the same file.
    if block(ORIGIN, "class WeinbergAngleCategorical") != base:
        print("FAIL selftest [stability]: block() is not deterministic")
        bad += 1
    else:
        print("ok   selftest [stability] block() returns the same text twice")
    if bad:
        print("\nSELFTEST FAILED -- do not trust a clean run.")
    return bad


def main() -> int:
    if "--selftest" in sys.argv[1:]:
        return _selftest()
    bad = 0
    for head in HEADS:
        a, b = block(ORIGIN, head), block(COPY, head)
        if a is None or b is None:
            missing = ORIGIN if a is None else COPY
            print(f"MISSING  {head!r} not found in {missing.relative_to(ROOT)}")
            print("         A rename on one side only is exactly the divergence "
                  "this guard exists to catch.")
            bad = max(bad, 2)
            continue
        if a == b:
            print(f"ok       {head}")
            continue
        bad = max(bad, 1)
        print(f"DIVERGED {head}")
        print(f"         {ORIGIN.relative_to(ROOT)}")
        print(f"         {COPY.relative_to(ROOT)}")
        for line in difflib.unified_diff(
            a.splitlines(), b.splitlines(), "origin", "copy", lineterm=""
        ):
            print("   " + line)
    if bad:
        print("\nThe copy is labelled FAITHFUL and is not. Fix the copy to match "
              "the origin, or move the shared declarations into the library tree "
              "so there is only one.")
    return bad


if __name__ == "__main__":
    sys.exit(main())
