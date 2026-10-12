#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit, emits no numeric physics.
"""Catch an `mpf("…")` constant built before precision is raised.

Owner directive: NO FLOAT64.

## The defect

```python
from _precision import set_compute_dps
from mpmath import mp, mpf

M_TAU_OVER_M_E = mpf("3477.23")     # module scope — runs at IMPORT time

def main():
    set_compute_dps()               # ... this runs much later
```

`set_compute_dps()` sets `mp.dps` *when it is called*. A constant built above
it is constructed at mpmath's default **15 dps**, frozen at 53 bits, and then
used — and serialized — at compute precision. Demonstrated rather than
asserted:

```
early = mpf('3477.23')    # at 15 dps       -> 3477.23000000000001818989403545856475830078125
mp.dps = 70
late  = mpf('3477.23')    # after the raise -> 3477.23
early == late             -> False
```

Not a formatting artifact: the two values genuinely differ. This produced the
only two NEW findings in the 2026-08-07 padding audit, in producers that were
already doing the right thing at the call site (`mpf("3477.23")` is a *string*,
never a float). `m_tau_hecke_energy_route.py` was worse than its literals
suggest — it also *divides* at 15 dps, `mpf("1776.86") / mpf("105.6583755")`.

## Why this needs its own gate

Neither existing gate can see it, and they miss it for opposite reasons:

| | the claim | caught by |
|---|---|---|
| float64 padding | value asserts **more** precision than it has | the padding audit |
| `mp.dps` no-op | whole file runs at 15 dps | `mpf_context_dps_audit` |
| **this** | one constant is 53 bits inside a file that is otherwise correct | nothing, until now |

The padding audit only sees the damage *if* the constant reaches a witness as
a long string. A 53-bit constant that merely contaminates downstream
arithmetic is wrong past digit ~16 and carries no marker at all — it is not
"padded", just quietly inaccurate.

## Two tiers, because the harm is not uniform

Of 170 such constants across 63 files, most are harmless, and a gate that
cannot say which is a gate nobody can act on.

- **`LOSSY`** — more significant digits than 53 bits can hold (>15), so the
  written value is *already* truncated at construction. Real precision loss.
- **`PADDING_RISK`** — 15 digits or fewer, so the value survives, but it is
  not a dyadic rational: serializing it at compute precision prints the
  binary64 tail. This is the `3477.23` case.
- **Exempt** — exactly representable in binary64 (`mpf("0.5")`, `mpf("2")`),
  where 53 bits is the exact answer and nothing is lost either way.

Tolerances (`mpf("1e-25")`) land in `PADDING_RISK` and are usually benign,
since a comparison threshold does not care about its 40th digit. That is a
judgement about *use*, which no static test can make, so they are reported and
not gated.

## Triage of the `PADDING_RISK` tier — why it needs no bulk fix

Of the 133 in this corpus, roughly 95 are **measured physical constants**
(CODATA/AME/PDG: `M_TAU = mpf("1776.86")`, `B_D_AME = mpf("2.224566")`) and
roughly 38 are **tolerances**. In both groups the value survives 53 bits
intact — six significant digits is all `1776.86` *has* — so nothing is lost at
construction. The only way harm reaches a witness is by serializing such a
constant at compute precision, which prints the binary64 tail.

**That path is already gated, and demonstrably so.** Build each at 15 dps,
`str()` it at 70, and hand it to `witness_float64_padding_audit.is_f64_padded`:

    1776.86      -> 1776.85999999999989995558280497789...   flagged
    105.6583755  -> 105.65837550000000533145794179290...   flagged
    2.224566     -> 2.224565999999999821312712811050...    flagged
    1e-25        -> 1.000000000000000038494869749191...e-25 flagged

So the padding audit catches every one of them at the moment it would matter,
and it currently sits at zero under `--strict`. That is exactly how the two
`m_tau` producers were found: constant built early, serialized, flagged NEW,
fixed at the producer. Gating `PADDING_RISK` here would add 133 obligations to
prevent a failure another gate already stops — and would red-wall a backlog
that is, as far as any witness shows, entirely harmless today.

Usage:
    python3 computations/module_const_precision_audit.py
    python3 computations/module_const_precision_audit.py --list
    python3 computations/module_const_precision_audit.py --strict   # LOSSY only
    python3 computations/module_const_precision_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Calls that build an mpmath value from a literal.
_MPF_CALLS = {"mpf", "mpmathify", "mpc"}
# Calls that raise working precision.
_RAISERS = {"set_compute_dps", "set_output_dps", "workdps", "workprec"}
# binary64 carries ~15.95 decimal digits; beyond 15 the value is truncated on
# construction rather than merely re-rendered later.
_F64_SIG_DIGITS = 15


def _sig_digits(lit: str) -> int:
    try:
        d = Decimal(lit)
    except InvalidOperation:
        return 0
    return len(d.as_tuple().digits)


def _is_exact_in_binary64(lit: str) -> bool:
    """A value a double represents exactly loses nothing at 53 bits."""
    try:
        d = Decimal(lit)
        return Decimal(float(d)) == d
    except (InvalidOperation, OverflowError, ValueError):
        return False


def _import_time_stmts(body: list) -> list:
    """Every statement that runs at import, flattened in source order.

    Descends into `try` / `if` / `with` / loop bodies, because a statement
    indented inside one of those at module scope still executes on import. It
    does NOT descend into `def` or `class`, whose bodies run later — which is
    the whole distinction this audit turns on.

    Skipping this is not hypothetical: the sibling gate
    `mpf_context_dps_audit.py` records a first draft that "anchored the import
    at column 0 and missed two instances indented inside a try: block". The
    first draft of *this* audit made the same mistake in mirror image, and
    accused `perknot_pn_bond_resolved_extensivity_probe.py`, which raises
    precision correctly inside a module-level `try:`.
    """
    out: list = []
    for n in body:
        out.append(n)
        if isinstance(n, (ast.Try, ast.If, ast.With, ast.For, ast.While)):
            for attr in ("body", "orelse", "finalbody", "handlers"):
                inner = getattr(n, attr, None) or []
                if attr == "handlers":
                    for h in inner:
                        out.extend(_import_time_stmts(h.body))
                else:
                    out.extend(_import_time_stmts(inner))
    return sorted(out, key=lambda s: (getattr(s, "lineno", 0),
                                      getattr(s, "col_offset", 0)))


def _precision_raised_at(tree: ast.Module) -> int | None:
    """Line of the first import-time statement that raises precision."""
    for n in _import_time_stmts(tree.body):
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
            f = n.value.func
            name = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
            if name in _RAISERS:
                return n.lineno
        if isinstance(n, ast.Assign):
            for t in n.targets:
                # mp.dps = N  /  mp.mp.dps = N  /  mp.prec = N
                if isinstance(t, ast.Attribute) and t.attr in {"dps", "prec"}:
                    return n.lineno
        # `with workdps(...)` wrapping module-level constants also counts.
        if isinstance(n, ast.With):
            for item in n.items:
                f = getattr(item.context_expr, "func", None)
                name = (f.attr if isinstance(f, ast.Attribute)
                        else getattr(f, "id", "")) if f else ""
                if name in _RAISERS:
                    return n.lineno
    return None


def find_early_constants(source: str, filename: str = "<src>") -> list[dict]:
    # A file that does not parse is "no information", not "no findings".
    # Returning [] for it converts breakage into silence -- bean qou-brkp
    # records this gate family reporting clean on two files a remediation had
    # just made unparseable, which is why nobody noticed for a month.
    if "mpmath" not in source:
        return []
    try:
        tree = ast.parse(source, filename)
    except SyntaxError as e:
        return [{"file": filename, "line": e.lineno or 0, "tier": "UNPARSEABLE",
                 "name": None, "literal": None,
                 "source": f"SyntaxError: {e.msg}"}]
    except Exception as e:
        return [{"file": filename, "line": 0, "tier": "UNPARSEABLE",
                 "name": None, "literal": None,
                 "source": f"{type(e).__name__}: {e}"}]

    raised = _precision_raised_at(tree)
    out: list[dict] = []
    for n in _import_time_stmts(tree.body):  # import-time only, not def/class
        if not isinstance(n, ast.Assign):
            continue
        if raised is not None and n.lineno > raised:
            continue                         # built after the raise — fine
        for c in ast.walk(n.value):
            if not isinstance(c, ast.Call):
                continue
            fn = (c.func.attr if isinstance(c.func, ast.Attribute)
                  else getattr(c.func, "id", ""))
            if fn not in _MPF_CALLS or not c.args:
                continue
            a = c.args[0]
            if not (isinstance(a, ast.Constant) and isinstance(a.value, str)):
                continue
            lit = a.value
            if _is_exact_in_binary64(lit):
                continue                     # 53 bits is the exact answer
            tgt = n.targets[0]
            out.append({
                "file": filename,
                "line": n.lineno,
                "name": getattr(tgt, "id", "<expr>"),
                "literal": lit,
                "tier": ("LOSSY" if _sig_digits(lit) > _F64_SIG_DIGITS
                         else "PADDING_RISK"),
                "raised_at": raised,
            })
    return sorted(out, key=lambda d: d["line"])


def scan(root: Path) -> list[dict]:
    out: list[dict] = []
    for p in sorted((root / "computations").rglob("*.py")):
        if ("_deprecated" in p.parts or "fsh-guts" in p.parts):
            continue
        rel = p.relative_to(root).as_posix()
        try:
            src = p.read_text(encoding="utf-8")
        except Exception as e:
            out.append({"file": rel, "line": 0, "tier": "UNPARSEABLE",
                        "name": None, "literal": None,
                        "source": f"unreadable: {type(e).__name__}: {e}"})
            continue
        out.extend(find_early_constants(src, rel))
    return out


CASES = [
    ("no raise anywhere: constant is at 15 dps",
     'from mpmath import mpf\nX = mpf("3477.23")\n', 1),
    ("raise is inside main(), not at module scope — the m_tau shape",
     'from mpmath import mpf\nX = mpf("3477.23")\n'
     'def main():\n    set_compute_dps()\n', 1),
    ("raised at module scope BEFORE the constant",
     'from mpmath import mpf\nset_compute_dps()\nX = mpf("3477.23")\n', 0),
    ("mp.mp.dps set before the constant",
     'import mpmath as mp\nmp.mp.dps = 70\nX = mp.mpf("3477.23")\n', 0),
    ("raised at module scope but AFTER the constant",
     'from mpmath import mpf\nX = mpf("3477.23")\nset_compute_dps()\n', 1),
    ("exactly representable — nothing lost at 53 bits",
     'from mpmath import mpf\nHALF = mpf("0.5")\nTWO = mpf("2")\n', 0),
    ("17 significant digits — LOSSY, not merely a padding risk",
     'from mpmath import mpf\nV = mpf("12.776095278687214")\n', 1),
    ("a division at 15 dps is caught via its operands",
     'from mpmath import mpf\nR = mpf("1776.86") / mpf("105.6583755")\n', 2),
    # The false positive the first draft produced, and the reason
    # _import_time_stmts exists.
    ("raise indented inside a module-level try: still runs at import",
     'import mpmath as mp\ntry:\n    from _precision import set_compute_dps\n'
     '    set_compute_dps()\nexcept ImportError:\n    mp.mp.dps = 50\n'
     'X = mp.mpf("3477.23")\n', 0),
    ("constant itself inside a module-level try, with no raise",
     'import mpmath as mp\ntry:\n    X = mp.mpf("3477.23")\n'
     'except Exception:\n    X = None\n', 1),
    ("inside a function: runs after main() raised precision, out of scope",
     'from mpmath import mpf\ndef f():\n    return mpf("3477.23")\n', 0),
    ("no mpmath in the file at all",
     'X = float("3477.23")\n', 0),
    ("non-literal argument is unknowable, never guessed",
     'from mpmath import mpf\nX = mpf(some_value)\n', 0),
]

TIER_CASES = [
    ('from mpmath import mpf\nV = mpf("12.776095278687214")\n', "LOSSY"),
    ('from mpmath import mpf\nX = mpf("3477.23")\n', "PADDING_RISK"),
    ('from mpmath import mpf\nT = mpf("1e-25")\n', "PADDING_RISK"),
]


def self_test() -> int:
    fails = 0
    for label, src, want in CASES:
        got = len(find_early_constants(src))
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    for src, want in TIER_CASES:
        hits = find_early_constants(src)
        got = hits[0]["tier"] if hits else "<none>"
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  tier of {hits[0]['literal'] if hits else '?'!r:24} "
              f"(want {want}, got {got})")
    total = len(CASES) + len(TIER_CASES)
    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on LOSSY constants (real precision loss)")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    hits = scan(Path(a.root).resolve())
    lossy = [h for h in hits if h["tier"] == "LOSSY"]
    # A file the gate could not read is a HOLE IN THE GATE, not a pass.
    blind = [h for h in hits if h["tier"] == "UNPARSEABLE"]
    risk = [h for h in hits if h["tier"] == "PADDING_RISK"]
    files = {h["file"] for h in hits}

    print("module-const-precision: mpf constants built before precision is "
          "raised\n")
    print(f"  LOSSY        (>{_F64_SIG_DIGITS} sig digits, truncated at "
          f"construction) : {len(lossy):>4}")
    print(f"  PADDING_RISK (survives, but prints the f64 tail)      : "
          f"{len(risk):>4}")
    print(f"  across {len(files)} file(s)")

    if a.list or lossy:
        if lossy:
            print("\n--- LOSSY — the value is already wrong when built ---")
            for h in lossy:
                print(f"  {h['file']}:{h['line']}  {h['name']} = "
                      f"mpf({h['literal']!r})")
                where = (f"line {h['raised_at']}" if h["raised_at"]
                         else "never at module scope")
                print(f"      precision raised: {where}")
    if a.list and risk:
        print("\n--- PADDING_RISK — reported, not gated ---")
        for h in risk:
            print(f"  {h['file']}:{h['line']}  {h['name']} = "
                  f"mpf({h['literal']!r})")
    if not a.list:
        print("\n  --list for the full detail.")
    print("\nFix: call the idempotent `set_compute_dps()` at module scope "
          "above the\nconstants. It is safe alongside the call in main().")
    if blind:
        print("\n  BLIND SPOTS — the gate could not process these files, so their")
        print("  module-const precision is UNKNOWN, not clean (bean qou-brkp):")
        for h in blind:
            print(f"    {h['file']}:{h['line']}  {h['source']}")

    return 1 if (a.strict and (lossy or blind)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
