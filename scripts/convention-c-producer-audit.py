#!/usr/bin/env python3
"""Find convention-C definitions of the Markov parameter in live Python producers.

The producer-layer counterpart to `content/pipeline/trace-convention-audit.ts`,
which walks `content/**` only. Nothing walked the producers, and three
successive hand-greps of that surface returned 70, then 13, then 182.

## Why grep cannot do this

The corpus spells `z = 1/(q^{1/2} + q^{-1/2})` at least fifteen ways:

    1.0 / (q0**0.5 + qi0**0.5)          1 / (mp.sqrt(Q0) + 1/mp.sqrt(Q0))
    1.0 / (q0 ** 0.5 + q0 ** (-0.5))    1 / (sp.sqrt(q) + 1/sp.sqrt(q))
    1.0 / (Q0 ** 0.5 + QI ** 0.5)       1 / (np.sqrt(q) + 1.0/np.sqrt(q))
    1 / (q ** mpmath.mpf('0.5') + ...)  1 / (sqrt_q + 1 / sqrt_q)
    1 / (q0**mpf('0.5') + q0**mpf('-0.5'))

with the reciprocal named `q0`, `qi`, `qi0`, `Q_INV`, `_QI0`, `sqrt_q`, `q_val`,
or spelled inline; and the result bound to `z`, `z_mark`, `z_markov`, `Z_MARKOV`,
`z_sym`, `zmkv`, `ZS`, `z_q`, `_z`, ... A regex tuned to any subset silently
misses the rest, and a looser one (`0.5 + `) matches unrelated arithmetic. Both
failure modes actually happened, in that order.

So this walks the **AST**: any assignment whose target name contains `z` and
whose value has the shape `1 / (<something with a square root> + <anything>)`.
Shape-matching, not spelling-matching.

## What counts, and what deliberately does not

* **Deliberately C-named** targets (`z_C`, `z_c`, `z_C_expr`, ...) are excluded.
  A variable that says it is convention C is a labelled comparison, not a defect
  — the same principle the content axis uses for `C_LABEL`.
* **`tools/pyhecke/`** is reported separately: the registry records
  `pyhecke.gram.z` as convention C **by design** under `blocked_migrations`, and
  R9 asserts that exception rather than leaving it undetected.
* `_deprecated/` is skipped entirely.

Results are stratified, because the layers carry very different risk: a probe
that computes a C-era number for its own consumption is not the same defect as
the shipped `qou-mass` package doing it.

## Usage

    python3 scripts/convention-c-producer-audit.py            # summary
    python3 scripts/convention-c-producer-audit.py --list     # every site
    python3 scripts/convention-c-producer-audit.py --json out.json
    python3 scripts/convention-c-producer-audit.py --selftest

Exit 1 when any non-deliberate site outside the blocked-by-design set is found,
so it can gate. It does **not** currently gate CI — auto-triggers are disabled
repo-wide (owner directive 2026-06-30, Actions billing).
"""

from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOTS = ("computations", "qou-mass", "tools")

#: A target whose own name declares it convention C is a labelled comparison.
DELIBERATE = re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)

#: The registry blocks this path on C by design (`blocked_migrations`).
BLOCKED_BY_DESIGN = "tools/pyhecke/"


def is_c_form(node: ast.AST) -> bool:
    """Does this expression have the shape ``1 / (<sqrt-ish> + <anything>)``?

    Deliberately shape-based. It does not try to confirm the second summand is
    the reciprocal of the first — that would need symbolic evaluation, and any
    ``1/(sqrt(...) + ...)`` bound to a ``z``-named variable is worth a human
    look regardless.

    ``**3`` anywhere in the denominator rejects the match: convention D is
    ``q**3/(q**2+1)``, and a stray cube is a strong signal this is not the
    half-argument form.
    """
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)):
        return False
    if not (isinstance(node.left, ast.Constant) and node.left.value in (1, 1.0)):
        return False
    den = node.right
    if not (isinstance(den, ast.BinOp) and isinstance(den.op, ast.Add)):
        return False
    # Whitespace-normalised: `ast.unparse` emits `q ** 3`, so a naive `"**3"`
    # test never fires. The selftest caught exactly that.
    src = "".join(ast.unparse(den).split())
    return ("0.5" in src or "sqrt" in src.lower()) and "**3" not in src


def classify(path: str) -> str:
    if path.startswith(BLOCKED_BY_DESIGN):
        return "tools/pyhecke — BLOCKED on C by design (registry)"
    name = pathlib.Path(path).name
    if "/probes/" in path or name.endswith("_probe.py") or "probe" in name:
        return "probes / exploratory"
    if path.startswith("qou-mass"):
        return "qou-mass — SHIPPED PACKAGE"
    if "/sweeps/" in path:
        return "sweeps"
    return "computations — live producers"


def scan(roots=ROOTS):
    """Yield (path, lineno, target_name, source, bucket, deliberate)."""
    for r in roots:
        base = pathlib.Path(r)
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.py")):
            sp = str(p)
            if "_deprecated" in sp:
                continue
            try:
                tree = ast.parse(p.read_text())
            except (SyntaxError, UnicodeDecodeError, OSError):
                continue
            for n in ast.walk(tree):
                if not isinstance(n, (ast.Assign, ast.AnnAssign)):
                    continue
                targets = n.targets if isinstance(n, ast.Assign) else [n.target]
                names = [t.id for t in targets if isinstance(t, ast.Name)]
                if not any("z" in nm.lower() for nm in names):
                    continue
                if n.value is None or not is_c_form(n.value):
                    continue
                nm = names[0]
                yield (sp, n.lineno, nm, ast.unparse(n.value),
                       classify(sp), bool(DELIBERATE.search(nm)))


def selftest() -> int:
    """Prove the matcher accepts every spelling in the corpus and rejects D.

    A detector that cannot fail is worse than none — the same rule the content
    axis is held to. These fixtures are the real spellings found in
    `computations/`, plus the convention-D forms that must NOT match.
    """
    should_match = [
        "1.0 / (q0**0.5 + qi0**0.5)",
        "1.0 / (q0 ** 0.5 + q0 ** (-0.5))",
        "1.0 / (Q0 ** 0.5 + QI ** 0.5)",
        "1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))",
        "1 / (sp.sqrt(q) + 1 / sp.sqrt(q))",
        "1.0 / (np.sqrt(q) + 1.0 / np.sqrt(q))",
        "1 / (sqrt_q + 1 / sqrt_q)",
        "1 / (q ** mpmath.mpf('0.5') + qi ** mpmath.mpf('0.5'))",
        "1 / (q0 ** mpf('0.5') + q0 ** mpf('-0.5'))",
        "1 / (mp.sqrt(q0) + mp.sqrt(qi))",
    ]
    should_not = [
        "q ** 3 / (q ** 2 + 1)",          # convention D
        "q0**3 / (q0**2 + 1)",            # convention D
        "1 / (q + 1 / q)",                # 1/[2]_q — the TL loop reciprocal, not z
        "2 / (a + b)",                    # not a reciprocal of the right shape
        "1 / (q ** 3 + q ** 0.5)",        # cube present -> rejected
    ]
    bad = 0
    for src in should_match:
        ok = is_c_form(ast.parse(src, mode="eval").body)
        print(f"  {'ok  ' if ok else 'FAIL'}  matches: {src}")
        bad += not ok
    for src in should_not:
        ok = not is_c_form(ast.parse(src, mode="eval").body)
        print(f"  {'ok  ' if ok else 'FAIL'}  rejects: {src}")
        bad += not ok
    total = len(should_match) + len(should_not)
    print(f"selftest: {total - bad}/{total}"
          + ("" if bad else " — matcher accepts every corpus spelling and rejects convention D."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print every site")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return 1 if selftest() else 0

    rows = list(scan())
    live = [r for r in rows if not r[5]]
    deliberate = [r for r in rows if r[5]]

    buckets = Counter(r[4] for r in live)
    files = defaultdict(set)
    for r in live:
        files[r[4]].add(r[0])

    print("convention-C Markov-parameter definitions in live Python (AST-verified)\n")
    for k, v in buckets.most_common():
        print(f"  {v:4d} sites / {len(files[k]):3d} files   {k}")
    print(f"\n  {len(deliberate):4d} sites               deliberately C-named — labelled comparisons, not defects")

    actionable = sum(v for k, v in buckets.items() if not k.startswith("tools/pyhecke"))
    print(f"\n  ACTIONABLE (excludes blocked-by-design): {actionable} sites")

    if args.list:
        print()
        for path, line, nm, src, bucket, _ in sorted(live):
            print(f"  {path}:{line}\n      {nm} = {src[:90]}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps([
            {"path": p, "line": l, "target": nm, "source": s,
             "bucket": b, "deliberate": d}
            for p, l, nm, s, b, d in rows
        ], indent=2))
        print(f"\n  json -> {args.json}")

    return 1 if actionable else 0


if __name__ == "__main__":
    sys.exit(main())
