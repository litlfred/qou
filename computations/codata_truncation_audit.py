#!/usr/bin/env python3
# polynomial_q_not_applicable: infra audit; no symbolic-q logic.
"""Hand-typed CODATA constants that are TRUNCATED, not merely duplicated.

`qou-46ke` has tracked "hidden CODATA literals" since 2026-06-22 as a
53-script rollup, and its last note (2026-06-23) files the remaining tail as
*"low value — diminishing returns"*. This audit exists because that assessment
is measurably wrong, and because the interesting subset was never separated
out.

The distinction this makes
--------------------------

A hardcoded CODATA value is one of two very different things:

* **Duplication** — the literal equals the canonical value. Bad practice (it
  goes stale when CODATA is revised) but it computes the right number today.
* **Truncation** — the literal is a *prefix* of the canonical value, shorter
  than it. This computes a **different number**, silently, forever.

Only the second changes results, and it is invisible to every precision gate
in the tree: the NO-FLOAT64 family checks how a number is *carried and
serialized*, never whether it was *right when typed*. Wrapping a truncated
literal in `mpmath.mpf` — the standard drain — removes the float64 while
preserving the error, and looks like a fix.

Measured on 2026-08-10, three instances landed in one day:

    m_e     0.51099895000  vs  0.51099895069   worth 1.35e-9 in kappa
    q0      1.10998        vs  1.1099785827…   worth 1.9e-7  in contRatio
    proton  938.272        vs  938.27208943    worth ~1e-9   in vol ratios

all three orders of magnitude above the L1 1-ppQ (1e-15) compute target the
corpus holds itself to. The `m_e` figure is measured rather than assumed: f64
arithmetic on the *same* inputs contributes 5.06e-16, so the literal was the
entire discrepancy.

The canonical table is READ, not typed
--------------------------------------

Every reference value comes from `codata_constants` at run time. A checker for
hardcoded constants must not hardcode them: if it did, it would go stale on the
next CODATA revision in exactly the way it is meant to detect, and would then
report the corpus as wrong while being wrong itself.

Usage
-----

    python3 computations/codata_truncation_audit.py
    python3 computations/codata_truncation_audit.py --list
    python3 computations/codata_truncation_audit.py --strict   # CI gate

`--strict` exits 1 on any TRUNCATED occurrence. Exact duplicates are reported
as a separate count and never block — that is `qou-46ke`'s original scope and a
much larger, much less urgent sweep.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import argparse
import ast
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from codata_constants import (  # noqa: E402
    M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, M_MU_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION, U_MEV,
)
from q_parameter import Q_MP  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# name -> (canonical value read from the registry, the constant to use instead)
CANON: dict[str, tuple[str, str]] = {
    "m_e":   (str(M_E_MEV), "codata_constants.M_E_MEV"),
    "m_p":   (str(M_P_MEV_VALIDATION), "codata_constants.M_P_MEV_VALIDATION"),
    "m_n":   (str(M_N_MEV_VALIDATION), "codata_constants.M_N_MEV_VALIDATION"),
    "m_mu":  (str(M_MU_MEV_VALIDATION), "codata_constants.M_MU_MEV_VALIDATION"),
    "m_pi":  (str(M_PI_PM_MEV_VALIDATION),
              "codata_constants.M_PI_PM_MEV_VALIDATION"),
    "u_MeV": (str(U_MEV), "codata_constants.U_MEV"),
    "q0":    (str(Q_MP), "q_parameter.Q_MP"),
}

# A literal must share at least this many significant digits with a canonical
# value before it is called a truncation of it. Below that, agreement is
# coincidence: "938.2" is not a truncated proton mass, it is a different number
# that happens to start the same way.
MIN_SHARED_DIGITS = 6

NUMBER = re.compile(r"\d+\.\d+")

# The registry itself. A CODATA value here is the source of truth, not a copy
# of one — flagging it would be the audit reporting its own reference as wrong.
REGISTRY_FILES = {"codata_2022_source.py", "codata_constants.py",
                  "q_parameter.py"}

# A number inside a regex or a match-prefix is a PATTERN, not a computed value.
# Without this the audit flags other detectors — including its own siblings —
# for containing the very literals they exist to find.
PATTERN_MARKERS = ("re.compile", "re.search", "re.match", "re.finditer",
                   r"\d", "_MATCH_", "pattern", "PATTERN", "regex")


def canonical_digits(v: str) -> str:
    return v.replace(".", "").replace("-", "").lstrip("0")


def classify(lit: str) -> tuple[str, str, str] | None:
    """(name, verdict, canonical) if `lit` relates to a canonical value."""
    for name, (canon, _) in CANON.items():
        if not canon.startswith(lit):
            continue
        if len(canonical_digits(lit)) < MIN_SHARED_DIGITS:
            continue
        return (name, "EXACT" if lit == canon else "TRUNCATED", canon)
    return None


def _prose_lines(src: str) -> set[int]:
    """Line numbers that are documentation or console output, not computation.

    A truncated constant in a docstring or a `print()` is describing a value,
    not computing with one. Replacing it with an import changes nothing and
    would often make the prose worse. Excluding them is not leniency — it is
    the difference between a finding and a typo in a sentence.

    Why AST and not a regex: `mp.mpf("0.51099895")` is a string literal and IS
    a genuine defect, while `"m_e = 0.51099895 MeV"` in a docstring is not. No
    lexical test separates those; the parse tree does — one is an argument to a
    numeric constructor, the other is a bare expression-statement string or a
    `print` argument.

    History: the first published run of this audit reported 86 truncations. It
    excluded only lines starting with `#`, so docstrings, prints, and — in
    three cases — a sibling detector's own list of patterns to match were all
    counted. That number was inflated and is corrected here.
    """
    skip: set[int] = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return skip

    def mark(node) -> None:
        lo = getattr(node, "lineno", None)
        hi = getattr(node, "end_lineno", lo)
        if lo:
            skip.update(range(lo, (hi or lo) + 1))

    for node in ast.walk(tree):
        # Bare string expression-statements: module/class/function docstrings
        # and the free-floating comment-strings this corpus uses liberally.
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            mark(node)
        # print(...) — console narration.
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "print":
            mark(node)

        # ── DELIBERATELY-TRUNCATED COMPARATORS ────────────────────────
        # A prefix matcher MUST be shorter than the value it matches, and a
        # window bound MUST NOT equal the value it brackets. "Fixing" these to
        # the full canonical constant breaks the check they implement:
        # `q.startswith(Q_MP)` is trivially true, and `x > M_E_MEV` as a lower
        # bound excludes the very value it is meant to admit.
        #
        # This is the third false-positive class this audit has had, after
        # regex patterns and prose. They share a root: a numeric literal that
        # *looks like* a constant but is playing a structural role. The lesson
        # is in the detector's history rather than only its output — a
        # high-recall matcher on numeric text needs the parse tree to tell
        # role from resemblance.

        # `x.startswith("1.10997…")`
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in ("startswith", "endswith"):
            mark(node)
        # `lo < x`, `x > bound`, `x == "1.109…"` — the literal is a threshold.
        if isinstance(node, ast.Compare):
            mark(node)
        # Names that announce the role: PREFIX / SIG / SIGNATURE / _LO / _HI.
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                name = getattr(tgt, "id", "") or ""
                if any(m in name.upper()
                       for m in ("PREFIX", "_SIG", "SIGNATURE", "_LO", "_HI")):
                    mark(node)
    return skip


def scan() -> tuple[list[dict], int]:
    rows: list[dict] = []
    exact = 0
    for f in sorted(ROOT.joinpath("computations").rglob("*.py")):
        if "_deprecated" in f.parts or "__pycache__" in f.parts:
            continue
        if f.name == Path(__file__).name or f.name in REGISTRY_FILES:
            continue
        try:
            src = f.read_text()
        except OSError:
            continue
        lines = src.splitlines()
        prose = _prose_lines(src)
        for i, line in enumerate(lines, 1):
            if i in prose:
                continue
            s = line.strip()
            # Comments and import lines are prose/plumbing, not computed values.
            if s.startswith("#") or "codata_constants" in line or (
                    line.lstrip().startswith(("import ", "from "))):
                continue
            if any(mk in line for mk in PATTERN_MARKERS):
                continue
            for m in NUMBER.finditer(line):
                got = classify(m.group(0))
                if not got:
                    continue
                name, verdict, canon = got
                if verdict == "EXACT":
                    exact += 1
                    continue
                rows.append({
                    "file": str(f.relative_to(ROOT)),
                    "line": i,
                    "constant": name,
                    "literal": m.group(0),
                    "canonical": canon,
                    "use_instead": CANON[name][1],
                })
    return rows, exact


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true", help="print every finding")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any TRUNCATED literal is present")
    args = ap.parse_args(argv)

    rows, exact = scan()
    by_const: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_const[r["constant"]].append(r)

    # Write the artifact BEFORE the human-readable report, not after.
    # Caught by this script failing on itself: piped through `head`, the
    # console output raised BrokenPipeError part-way and the process died
    # before ever reaching json.dump, so the run produced no witness while
    # appearing to succeed. That is precisely the failure class its sibling
    # witness_producer_executes_audit.py exists to detect -- a producer that
    # cannot write its own witness. Emit the durable output first; the
    # printing is a courtesy and must not be able to prevent it.
    out = HERE / "codata-truncation-audit.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload = {
        "engine": "python-stdlib",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "codata-truncation-audit",
        "scriptFile": "codata_truncation_audit.py",
        "description": (
            "Hand-typed CODATA/substrate constants that are a short prefix of "
            "the canonical value, and so compute a different number. Separates "
            "that class from exact duplication, which is qou-46ke's original "
            "and much larger scope. Canonical values are read from "
            "codata_constants / q_parameter at run time, never typed here."
        ),
        "min_shared_digits": MIN_SHARED_DIGITS,
        "truncated_total": len(rows),
        "truncated_files": len({r["file"] for r in rows}),
        "by_constant": {k: len(v) for k, v in by_const.items()},
        "exact_duplicates": exact,
        "findings": rows,
    }
    _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(_prov_payload, indent=2) + "\n")

    print("=" * 74)
    print("CODATA TRUNCATION AUDIT — literals that are a SHORT prefix of the")
    print("                          canonical value, i.e. a different number")
    print("=" * 74)
    print(f"  TRUNCATED : {len(rows):4d} occurrence(s) in "
          f"{len({r['file'] for r in rows})} file(s)")
    for name, items in sorted(by_const.items(), key=lambda kv: -len(kv[1])):
        canon = CANON[name][0]
        print(f"    {name:6s} {len(items):4d}  e.g. {items[0]['literal']}"
              f"   canonical {canon[:22]}")
    print(f"  exact duplicates (not blocking): {exact}")
    print("\n  Truncation computes a DIFFERENT number, silently. No precision")
    print("  gate sees it: the NO-FLOAT64 family checks how a value is carried")
    print("  and serialized, never whether it was right when typed. Wrapping a")
    print("  truncated literal in mpf removes the float and keeps the error.")

    if rows:
        print("\n  Findings:" if args.list else "\n  Findings (first 25):")
        for r in (rows if args.list else rows[:25]):
            print(f"    {r['file']}:{r['line']}  {r['constant']} = "
                  f"{r['literal']}  ->  {r['use_instead']}")
        if not args.list and len(rows) > 25:
            print(f"    ... and {len(rows) - 25} more (--list)")

    print(f"\n  witness -> {out.name}")

    if args.strict and rows:
        print(f"\nSTRICT: {len(rows)} truncated literal(s) — exiting 1")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
