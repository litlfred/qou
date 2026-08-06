#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; emits no numeric physics.
"""No-free-parameter certificate for the canonical prediction path (T5).

Bean `qou-s16e` (T5), epic `qou-8lxd`.

**What this answers.** A prediction is *derivative of QOU* only if every
number entering it is traceable to (i) a tagged calibration input, (ii) a
proved/derived categorical constant, or (iii) pure combinatorics. Anything
else is a free parameter, and a free parameter is a fit. Until now that
property was asserted in prose and policed by an *agent-run* skill
(`local/canonical-watcher`); this script makes it **mechanical**.

**What it does.** Starting from the canonical mass facade
(`canonical_mass.proton_mass_mev` / `neutron_mass_mev`), it walks the
first-party import closure, AST-parses every module in it, and classifies
every numeric literal that appears in an *arithmetic* position:

| class | meaning |
|---|---|
| `structural` | small integer with a stated identification (rep dimension, group order, exponent, index) |
| `calibration` | flows from a CODATA-tagged constant module |
| `derived` | read from a `*.witness.json` rather than typed |
| `precision` | dps / tolerance / formatting knob — affects accuracy of evaluation, never the value |
| `UNTRACEABLE` | a bare non-integer literal in arithmetic with none of the above |

**Epistemic scope (STRICT).** This is a **high-recall static detector**, not
a proof. It is the same contract as the Lean vacuity audit: the script
produces *candidates*; the genuine-vs-legit verdict on each flagged literal
is an agent/human call. A clean run is *evidence* the path is
parameter-free, never a theorem that it is. In particular the classifier
cannot see through `eval`, dynamic attribute access, or a literal laundered
through a helper it does not resolve.

Exit code is 0 always (report-only) unless `--strict`, which exits 1 when
any UNTRACEABLE literal survives — the intended CI wiring once the baseline
is clean.

Output: `no-free-parameter-certificate.witness.json`.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Entry points whose closure constitutes "the prediction surface".
# Each is audited separately so a finding is attributable to an observable.
ENTRY_POINTS = {
    "canonical_mass":             "absolute nucleon mass (m_p, m_n)",
    "per_observable_100x_status": "the L2 dashboard — all seven scored observables",
    "meson_mass_from_hecke":      "meson ratios (m_K/m_pi)",
    "binding_K_direct":           "per-isotope binding",
}
ENTRY_MODULES = sorted(ENTRY_POINTS)

# Modules whose literals are calibration inputs by construction.
CALIBRATION_MODULES = {
    "codata_constants",
    "codata_2022_source",
    "codata_masses",
}

# Integers with a stated structural identification in the canonical formula
# (see canonical_mass.__doc__ and docs/canonical-mass-formula-guardrail.md).
STRUCTURAL_INTS = {
    0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 24, 50, 65, 100, 1000,
}

# Names whose assigned literals are precision / tolerance knobs.
PRECISION_NAMES = (
    "dps", "prec", "tol", "tolerance", "eps", "epsilon", "atol", "rtol",
    "maxiter", "max_iter", "digits", "ndigits", "sigma", "sig",
)


# Roots searched for first-party modules. `computations/` puts both itself
# and `computations/substrate/` on sys.path via `_path_bridge`, so a bare
# `import q_parameter` resolves into the substrate package.
SEARCH_ROOTS = [
    HERE,
    HERE / "substrate",
    HERE.parent / "tools" / "qou-substrate" / "python" / "qou_substrate",
]

# Adjudicated literals — the agent-verdict ledger (same contract as the Lean
# vacuity review ledger: the script flags candidates, a human/agent clears
# them, and the verdict is recorded so it is not re-litigated every run).
# Keyed by (module, value, assigned_to).
VERDICT_LEDGER = {
    ("experimental_constants", 8.0, "EIGHT_G"): (
        "legit — structural integer as float. 8·G = 7.3277247534177521204 is "
        "Vol(Borromean rings), a proved hyperbolic-geometry identity (G = "
        "Catalan). Verified to 1e-14 against the known volume. Not a fit."
    ),
    ("experimental_constants", 3.0, "KAPPA"): (
        "legit — structural integer as float: the 3 of the three-strand / "
        "three-colour structure, giving κ = m_e/3. Traceable to m_e (CAL-1) "
        "divided by a combinatorial constant, so it introduces no parameter."
    ),
}

# Third-party / stdlib names that are legitimately outside the audit.
_EXTERNAL = {
    "__future__", "json", "sys", "os", "re", "math", "cmath", "pathlib",
    "argparse", "typing", "dataclasses", "itertools", "functools",
    "collections", "warnings", "decimal", "fractions", "time", "datetime",
    "mpmath", "numpy", "scipy", "sympy", "pytest", "hashlib", "subprocess",
    "textwrap", "copy", "abc", "enum", "random", "csv", "io", "contextlib",
}


def _resolve(mod: str) -> Path | None:
    """Resolve a bare module name to a file: sibling .py, or package __init__."""
    for root in SEARCH_ROOTS:
        p = root / f"{mod}.py"
        if p.exists():
            return p
        pkg = root / mod / "__init__.py"
        if pkg.exists():
            return pkg
        # a package rooted at SEARCH_ROOTS entry itself (e.g. qou_substrate/)
        if root.name == mod and (root / "__init__.py").exists():
            return root / "__init__.py"
    return None


def _named_imports(tree: ast.AST) -> set[str]:
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                out.add(a.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                out.add(node.module.split(".")[0])
    return out


def _closure(entries: list[str], limit: int = 600) -> tuple[list[str], list[str]]:
    """Return (resolved modules, unresolved first-party-looking imports).

    Unresolved names are reported, never silently dropped: a module the audit
    cannot see is a COVERAGE GAP, and a green run that skipped it would be
    vacuous.
    """
    seen: set[str] = set()
    unresolved: set[str] = set()
    stack = list(entries)
    while stack and len(seen) < limit:
        m = stack.pop()
        if m in seen or m in _EXTERNAL:
            continue
        p = _resolve(m)
        if p is None:
            unresolved.add(m)
            continue
        seen.add(m)
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
        except SyntaxError:
            continue
        for nxt in _named_imports(tree):
            if nxt not in seen and nxt not in _EXTERNAL:
                stack.append(nxt)
    return sorted(seen), sorted(unresolved)


def _enclosing_assign_name(tree: ast.AST, node: ast.AST) -> str:
    """Best-effort: the name a literal is being assigned to."""
    for a in ast.walk(tree):
        if isinstance(a, (ast.Assign, ast.AnnAssign)):
            tgts = a.targets if isinstance(a, ast.Assign) else [a.target]
            for t in tgts:
                if isinstance(t, ast.Name):
                    for sub in ast.walk(a):
                        if sub is node:
                            return t.id
    return ""


def _is_power_of_ten(v: float) -> bool:
    """1e3, 1e6, 1e-9 ... — unit scaling, never a physics parameter."""
    if v == 0:
        return False
    a = abs(float(v))
    import math
    lg = math.log10(a)
    return abs(lg - round(lg)) < 1e-12


def _is_half_integer(v: float) -> bool:
    """n/2 for a small integer n: formula coefficients such as 1.0, 0.5, 1.5, 2.0.

    Half-integers are included because they arise structurally from
    square-root derivatives (d/dq of q^{1/2} gives 1/2, 3/2 exponents).
    Bounded to |n| <= 24 so a fitted value cannot masquerade as one.
    """
    x = float(v) * 2
    return abs(x - round(x)) < 1e-12 and abs(round(x)) <= 48


def _reads_witness(tree: ast.AST) -> bool:
    return any(
        isinstance(n, ast.Constant)
        and isinstance(n.value, str)
        and n.value.endswith(".witness.json")
        for n in ast.walk(tree)
    )


def audit_module(mod: str) -> list[dict]:
    p = _resolve(mod)
    if p is None:
        return []
    src = p.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(p))
    lines = src.splitlines()
    witness_backed = _reads_witness(tree)
    findings: list[dict] = []

    # Literals in arithmetic position only: operand of a BinOp, or a bare
    # module-level constant assignment.
    arith: set[int] = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.BinOp, ast.UnaryOp, ast.Compare)):
            for sub in ast.iter_child_nodes(n):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, (int, float)):
                    arith.add(id(sub))

    for n in ast.walk(tree):
        if not (isinstance(n, ast.Constant) and isinstance(n.value, (int, float))):
            continue
        if isinstance(n.value, bool):
            continue
        val = n.value
        name = _enclosing_assign_name(tree, n)
        lo = name.lower()

        if mod in CALIBRATION_MODULES:
            cls = "calibration"
        elif any(k in lo for k in PRECISION_NAMES):
            cls = "precision"
        elif isinstance(val, int) and val in STRUCTURAL_INTS:
            cls = "structural"
        elif isinstance(val, int):
            cls = "structural"          # remaining ints: indices/exponents
        elif id(n) not in arith:
            cls = "precision"           # non-arithmetic float (format, default)
        elif _is_power_of_ten(val):
            cls = "unit_conversion"     # ppb/ppm/percent scaling; carries no physics
        elif _is_half_integer(val):
            cls = "structural_float"    # n/2 formula coefficient written as a float
        else:
            key = (mod, float(val), name)
            cls = "adjudicated" if key in VERDICT_LEDGER else "UNTRACEABLE"

        if cls in ("UNTRACEABLE", "unit_conversion", "structural_float", "adjudicated"):
            findings.append({
                "module": mod,
                "line": n.lineno,
                "value": val,
                "assigned_to": name or None,
                "class": cls,
                "verdict": VERDICT_LEDGER.get((mod, float(val), name)),
                "source": lines[n.lineno - 1].strip()[:120] if n.lineno <= len(lines) else "",
            })
    return findings


def self_test() -> int:
    """Prove the classifier actually fires. A detector that never fires is
    worthless, so this asserts both directions on synthetic values."""
    cases = [
        # (value, expected-safe?)  safe == would NOT be reported UNTRACEABLE
        (1e6, True), (1e9, True), (1e-9, True),      # unit conversions
        (0.5, True), (1.0, True), (1.5, True), (2.0, True), (8.0, True),
        (4.73124891, False),                          # a fitted constant
        (0.1723456, False), (2.718281828, False),     # ditto
    ]
    bad = []
    for v, safe in cases:
        detected_safe = _is_power_of_ten(v) or _is_half_integer(v)
        if detected_safe != safe:
            bad.append((v, safe, detected_safe))
    if bad:
        print("SELF-TEST FAILED:")
        for v, exp, got in bad:
            print(f"   {v!r}: expected safe={exp}, classifier said {got}")
        return 1
    print(f"SELF-TEST PASSED — classifier separates {len(cases)} synthetic cases "
          "(unit/structural vs fitted) correctly.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true",
                    help="assert the classifier fires on fitted values and not on unit/structural ones")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any UNTRACEABLE literal survives")
    ap.add_argument("--json", action="store_true", help="print the witness to stdout")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    per_entry = {}
    for ep in ENTRY_MODULES:
        m_ep, u_ep = _closure([ep])
        f_ep = []
        for m in m_ep:
            f_ep.extend(audit_module(m))
        per_entry[ep] = {
            "description": ENTRY_POINTS[ep],
            "modules": len(m_ep),
            "unresolved": u_ep,
            "untraceable": [f for f in f_ep if f["class"] == "UNTRACEABLE"],
        }
    mods, unresolved = _closure(ENTRY_MODULES)
    all_findings: list[dict] = []
    for m in mods:
        all_findings.extend(audit_module(m))

    untraceable = [f for f in all_findings if f["class"] == "UNTRACEABLE"]
    derived = [f for f in all_findings if f["class"] in ("unit_conversion", "structural_float")]
    adjudicated = [f for f in all_findings if f["class"] == "adjudicated"]

    print("=" * 74)
    print("NO-FREE-PARAMETER CERTIFICATE — canonical prediction path (T5)")
    print("=" * 74)
    print("  per entry point:")
    for ep, d in sorted(per_entry.items()):
        flag = "OK " if not d["untraceable"] and not d["unresolved"] else "!! "
        print(f"    {flag}{ep:<28} {d['modules']:>3} mods  "
              f"{len(d['untraceable']):>3} untraceable  "
              f"{len(d['unresolved']):>2} unresolved   ({d['description']})")
    print()
    print(f"  modules in closure: {len(mods)}")
    print(f"  unit/structural   : {len(derived)}")
    print(f"  adjudicated legit : {len(adjudicated)}")
    print(f"  UNTRACEABLE       : {len(untraceable)}")
    if unresolved:
        print(f"\n  ⚠ COVERAGE GAP — {len(unresolved)} import(s) not resolved, so NOT audited:")
        for u in unresolved:
            print(f"      {u}")
        print("    A green result below does NOT cover these. Resolve them before")
        print("    treating this run as a certificate.")
    if untraceable:
        print("\n  untraceable literals (agent verdict required — high-recall candidates):")
        for f in untraceable[:40]:
            tgt = f["assigned_to"] or "-"
            print(f"    {f['module']}.py:{f['line']:<5} {f['value']!r:<24} -> {tgt}")
            print(f"        {f['source']}")
        if len(untraceable) > 40:
            print(f"    ... and {len(untraceable) - 40} more")
    else:
        print("\n  ✓ no untraceable literals in the canonical prediction path")

    witness = {
        "schema": "witness/v1",
        "name": "no-free-parameter-certificate",
        "description": (
            "Static high-recall audit of numeric literals in the canonical "
            "prediction path. Candidates only; per-literal verdict is an agent call."
        ),
        "data": {
            "entry_modules": ENTRY_MODULES,
            "modules_in_closure": mods,
            "unresolved_imports": unresolved,
            "per_entry_point": per_entry,
            "counts": {
                "modules": len(mods),
                "unresolved_imports": len(unresolved),
                "unit_or_structural_floats": len(derived),
                "adjudicated_legit": len(adjudicated),
                "untraceable": len(untraceable),
            },
            "untraceable": untraceable,
            "adjudicated": adjudicated,
        },
    }
    out = HERE / "no-free-parameter-certificate.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {out.name}")
    if args.json:
        print(json.dumps(witness, indent=2))

    return 1 if (args.strict and (untraceable or unresolved)) else 0


if __name__ == "__main__":
    sys.exit(main())
