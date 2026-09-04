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
    # theta/Q_beta channel (bean qou-skum). The T4/T5 channel
    # S_K = A_omega * kappa * (ln^2 q0 - theta_K^2) is a prediction path that
    # the mass-path-only scope did not reach, and PR #4513 proves in Lean
    # (AfreeThetaConstraint.ratio_attained, sorry-free) that A_omega is a
    # genuine FREE PARAMETER there: two anchor equations in three unknowns,
    # pinned only by a one-sided A >= 2.05. Every corpus theta is inverted
    # through it. Bringing it in scope is the point of qou-skum.
    "qbeta_t4_stokes3_crux_probe": "theta channel — the T4 inversion",
}
ENTRY_MODULES = sorted(ENTRY_POINTS)

# Modules whose literals are calibration inputs by construction.
CALIBRATION_MODULES = {
    "codata_constants",
    "codata_2022_source",
    "codata_masses",
    # A tagged reference-constants module (CODATA / PDG / SnapPy values, each
    # carrying its uncertainty) — calibration inputs by construction, exactly
    # like the codata_* modules. It was never added; it only became visible
    # once the bare-assignment gap below was closed, since every entry in it is
    # a plain `NAME = <literal>`.
    "experimental_constants",
}

# Integers with a stated structural identification in the canonical formula
# (see canonical_mass.__doc__ and docs/canonical-mass-formula-guardrail.md).
STRUCTURAL_INTS = {
    0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 24, 50, 65, 100, 1000,
}

# Literals that LOOK structural (small ints inside STRUCTURAL_INTS) but are
# adjudicated FREE PARAMETERS: a value imported from the literature or fitted,
# carrying no structural identification. The STRUCTURAL_INTS whitelist exists
# for rep dimensions, group orders, exponents and indices; a physical channel
# coefficient is none of those, so the whitelist must not cover it.
#
# Keyed by the assigned name (lowercased). Each entry states WHY.
ADJUDICATED_FREE = {
    "a_omega": (
        "A_omega = 3 is the GGM literature value of a Stokes datum, imported "
        "rather than derived. QOU/QBeta/AfreeThetaConstraint.lean proves "
        "(sorry-free) that the T4/T5 channel has two anchor equations in three "
        "unknowns, so A_omega is a genuine free parameter pinned only by a "
        "one-sided A >= 2.05; ratio_attained constructs an admissible A for "
        "every target ratio. It is NOT a rep dimension, group order, exponent "
        "or index, so the small-int whitelist must not wave it through."),
}

# Bare integers beyond this are no longer waved through as "an index or
# exponent": indices and exponents are small, so a large one is a candidate.
MAX_STRUCTURAL_INT = 64


def _wrap(text: str, width: int) -> list[str]:
    import textwrap
    return textwrap.wrap(text, width) or [""]

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
    HERE / "qbeta",
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
        except SyntaxError as e:
            # Same COVERAGE GAP as an unresolved import, reached by a
            # different failure: a module that does not parse is one this
            # certificate could not audit, and dropping it silently is exactly
            # the vacuous green this function's docstring forbids. Routed into
            # `unresolved` so it flows through the existing gap reporting
            # rather than vanishing. (bean qou-brkp)
            unresolved.add(f"{m} [UNPARSEABLE: {e.msg} at line {e.lineno}]")
            continue
        except Exception as e:
            unresolved.add(f"{m} [UNREADABLE: {type(e).__name__}: {e}]")
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


# Half-odd-integers (x.5) arise from ONE structural source: differentiating a
# square root, which yields 1/2 and 3/2 exponents. Nothing in the corpus needs
# a larger one, so the bound is tight. A fitted value near, say, 12.5 is
# flagged rather than excused.
MAX_HALF_ODD = 4.0


def _is_integral_float(v: float) -> bool:
    """An integer written as a float (2.0, 8.0). Gets EXACTLY the same
    scrutiny as a bare integer -- it must be in STRUCTURAL_INTS or within the
    index/exponent range -- so writing `8.0` buys no leniency over `8`."""
    x = float(v)
    if abs(x - round(x)) >= 1e-12:
        return False
    n = int(round(x))
    return n in STRUCTURAL_INTS or abs(n) <= MAX_STRUCTURAL_INT


def _is_half_odd(v: float) -> bool:
    """x.5 with |x| <= MAX_HALF_ODD: a square-root derivative coefficient."""
    x = float(v)
    if abs(x) > MAX_HALF_ODD:
        return False
    return abs(abs(x % 1.0) - 0.5) < 1e-12


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
    threshold: set[int] = set()
    precision_arg: set[int] = set()

    for n in ast.walk(tree):
        # A literal compared against something is a pass/fail THRESHOLD; it
        # never flows into an output value.
        if isinstance(n, ast.Compare):
            for sub in ast.walk(n):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, (int, float)):
                    threshold.add(id(sub))
        # A literal passed to a precision-setting call is a dps knob.
        if isinstance(n, ast.Call):
            fn = n.func
            nm = getattr(fn, "attr", None) or getattr(fn, "id", "") or ""
            if any(k in nm.lower() for k in ("dps", "prec", "workdps", "round")):
                for a in n.args:
                    if isinstance(a, ast.Constant) and isinstance(a.value, (int, float)):
                        precision_arg.add(id(a))
        # A bare numeric assignment `X = 1.234` IS a value in arithmetic
        # position — it is the commonest way to type a magic constant, and it
        # flows into every downstream use of `X`. The comment above always
        # claimed this case was covered; no code path implemented it, so
        # `q0 = 1.11020` was invisible while `S = +0.00968298` (a UnaryOp) was
        # caught. Identical values, opposite verdicts, purely on a redundant
        # leading sign.
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            v = n.value
            if isinstance(v, ast.Constant) and isinstance(v.value, (int, float)) \
                    and not isinstance(v.value, bool):
                arith.add(id(v))
        if isinstance(n, (ast.BinOp, ast.UnaryOp)):
            # `"=" * 92` is a BinOp but it is string repetition, not
            # arithmetic on a physical value. Skip when a side is a string.
            if isinstance(n, ast.BinOp) and any(
                isinstance(x, ast.Constant) and isinstance(x.value, str)
                for x in (n.left, n.right)
            ):
                continue
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

        # Initialised BEFORE the chain. Putting it mid-chain (which I did)
        # TERMINATES the elif, so everything after it runs unconditionally and
        # overwrites `cls` for every literal already classified tolerance /
        # precision / calibration. Caught by the witness diff: per-entry-point
        # `untraceable` lists changed under an edit that should only have
        # changed REPORTING.
        adjudicated_free_reason = None

        if id(n) in threshold:
            cls = "tolerance"           # pass/fail threshold, never an output value
        elif id(n) in precision_arg:
            cls = "precision"           # dps knob passed to a precision call
        elif mod in CALIBRATION_MODULES:
            cls = "calibration"
        elif any(k in lo for k in PRECISION_NAMES):
            cls = "precision"
        elif id(n) not in arith:
            # NOT in arithmetic position (banner width, format arg, default,
            # string repetition): cannot flow into a predicted value, so its
            # magnitude is irrelevant. This MUST precede the magnitude rules.
            cls = "non_arithmetic"
        elif lo in ADJUDICATED_FREE:
            # adjudicated a free parameter — the small-int whitelist below
            # would otherwise hide it. Stays UNTRACEABLE on purpose: the gate
            # must keep failing on a known free parameter. But it is NOT an
            # unreviewed candidate, and the report separates the two below.
            cls = "UNTRACEABLE"
            adjudicated_free_reason = ADJUDICATED_FREE[lo]
        elif isinstance(val, int) and val in STRUCTURAL_INTS:
            cls = "structural"
        elif isinstance(val, int):
            # indices / exponents are small; a large bare int is a candidate
            cls = ("structural" if abs(val) <= MAX_STRUCTURAL_INT
                   else "UNTRACEABLE")
        elif _is_power_of_ten(val):
            cls = "unit_conversion"     # ppb/ppm/percent scaling; carries no physics
        elif _is_integral_float(val) or _is_half_odd(val):
            cls = "structural_float"    # integer-as-float, or sqrt-derivative n/2
        else:
            key = (mod, float(val), name)
            cls = "adjudicated" if key in VERDICT_LEDGER else "UNTRACEABLE"

        if cls in ("UNTRACEABLE", "unit_conversion", "structural_float", "adjudicated"):
            findings.append({
                # only present when there IS a recorded verdict -- a null on
                # every finding is noise in a 2000-line witness
                **({"adjudicated_free": adjudicated_free_reason}
                   if adjudicated_free_reason else {}),
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
        (12.5, False),                                # half-odd beyond the bound
        (137.036, False),                             # a plausible-looking fit
        (23.5, False),                                # would have passed at |n|<=48
    ]
    bad = []
    for v, safe in cases:
        detected_safe = (_is_power_of_ten(v) or _is_integral_float(v)
                         or _is_half_odd(v))
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
    # An ADJUDICATED_FREE literal is UNTRACEABLE on purpose and its verdict is
    # already recorded. Printing it under "agent verdict required" invites an
    # agent to re-derive a settled result -- measured: a session spent several
    # turns re-establishing that A_omega = 3 is a free parameter, which
    # ADJUDICATED_FREE states in this same file, with a sorry-free Lean proof
    # behind it. The gate is unchanged; only the reporting separates them.
    known_free = [f for f in untraceable if f.get("adjudicated_free")]
    unreviewed = [f for f in untraceable if not f.get("adjudicated_free")]
    if known_free:
        print("\n  KNOWN FREE PARAMETERS (adjudicated — do NOT re-litigate; the")
        print("  gate fails on these BY DESIGN until the parameter is eliminated):")
        for f in known_free:
            tgt = f["assigned_to"] or "-"
            print(f"    {f['module']}.py:{f['line']:<5} {f['value']!r:<24} -> {tgt}")
            for line in _wrap(f["adjudicated_free"], 68):
                print(f"        {line}")
    if unreviewed:
        print("\n  untraceable literals (agent verdict required — high-recall candidates):")
        for f in unreviewed[:40]:
            tgt = f["assigned_to"] or "-"
            print(f"    {f['module']}.py:{f['line']:<5} {f['value']!r:<24} -> {tgt}")
            print(f"        {f['source']}")
        if len(unreviewed) > 40:
            print(f"    ... and {len(unreviewed) - 40} more")
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
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {out.name}")
    if args.json:
        print(json.dumps(witness, indent=2))

    return 1 if (args.strict and (untraceable or unresolved)) else 0


if __name__ == "__main__":
    sys.exit(main())
