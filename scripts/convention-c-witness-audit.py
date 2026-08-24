#!/usr/bin/env python3
"""Find convention-C witnesses STRUCTURALLY, not by matching known numbers.

## Why this replaces the fingerprint approach

The witness-regeneration campaign (`qou-eea0`) built its work list by grepping
witnesses for known convention-C decimal strings:

    0.49932033418369   0.41539579536   0.2809296   0.02274491

Those are the `n = 3` values — `z_C` and the three `y_λ` at three strands. A
witness computed at `n = 6`, `9` or `12` contains none of them, so **the entire
nuclear layer was invisible to that scan**: deuteron at `H₆`, helium-3 at `H₉`,
helium-4 at `H₁₂`, the `a_K` LP duals, the `binding-a3plus` assemblies.

Measured against this detector at the time it was written:

| | |
|---|---|
| fingerprint-detected | 46 |
| structurally convention C | 53 |
| overlap | **12** |
| **missed by fingerprints** | **41** |

The campaign reported "total impact" over a list that missed most of the surface.
That is the failure this file exists to prevent recurring.

## The structural test

Under convention D the Markov trace restricted to block `λ` is `y_λ · χ^λ`, and

    y_λ = 0   for every λ with ℓ(λ) ≥ 3

exactly — the fibre is the two-dimensional fundamental of `SU_q(2)`, so by
Schur–Weyl no partition with three or more rows survives. So:

> **A witness recording a nonzero `y_λ` on a three-or-more-row partition is
> convention C. No exceptions, at any `n`, whatever numbers it happens to
> contain.**

This is a property of the physics rather than of a decimal expansion, so it
cannot be evaded by a different `n`, a different precision, a different variable
name, or a value nobody thought to add to a fingerprint list.

Proved, and the claim above is quantified over ALL `n`, so it takes both halves:

- `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the **base case**,
  `n = 3`. From the three Markov moment equations plus `z·(q²+1) = q³` (which
  *is* convention D), `y₍₁³₎ = 0`. Sorry-free.
- `YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels` — the **lift** to
  every `n > 3`, given non-negativity and branching domination. Its
  combinatorial input is discharged by `card_three_threeRow_unique`: at three
  cells `(1³)` is the only three-row shape, so the base case has nothing to
  quantify over. Sorry-free.

Only the base case was cited here before, while the test it justifies runs at
`n = 6, 9, 12`. The lift is what carries it there.

Also `MarkovGramDegenerate.wedderburnGram_det_eq_zero_of_dead` for the
consequence on `det G`. Named in compute by `computations/live_channels.py`.

## Usage

    python3 scripts/convention-c-witness-audit.py            # summary
    python3 scripts/convention-c-witness-audit.py --list
    python3 scripts/convention-c-witness-audit.py --json out.json
    python3 scripts/convention-c-witness-audit.py --selftest

Exit 1 when any witness is structurally convention C.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

#: Below this a weight is dead. Convention D gives exact zeros symbolically; a
#: float pipeline may deliver 1e-300. Far below the smallest live weight
#: (y_(2,1) ≈ 0.247 at n = 3).
DEAD_TOL = 1e-30

#: Keys that hold a Wedderburn weight.
WEIGHT_KEYS = ("y_lambda", "y_lam", "y_at_q0", "weight_lambda")


def _partition_of(node: dict):
    """Extract a partition from a witness node, tolerating odd encodings.

    Some witnesses store `['3','_','2','_','1']` — underscore-separated digits
    rather than a list of ints. Those are real entries in
    `binding-a3plus-*.witness.json` and must not be silently skipped, since
    skipping is how the fingerprint scan missed things.
    """
    part = node.get("partition")
    if part is None:
        return None
    if isinstance(part, (list, tuple)):
        cleaned = [x for x in part if x not in ("_", "", None)]
        try:
            return tuple(int(x) for x in cleaned)
        except (TypeError, ValueError):
            return None
    if isinstance(part, str):
        try:
            return tuple(int(x) for x in part.replace("_", " ").split())
        except ValueError:
            return None
    return None


#: Expression strings that carry no claim: a literal zero, or a placeholder.
#: `"?"` is a real value in the corpus and means "unknown", which is not
#: evidence of convention C — clearing it is what keeps the 3+-row test from
#: reporting a gap in the data as a convention violation.
_TRIVIAL_EXPR = {"", "0", "0.0", "-0", "-0.0", "0.", "+0", "?", "-", "n/a",
                 "none", "null", "nan"}


def _nonzero_expr(expr: str) -> bool:
    """Is this weight expression something other than a written-down zero?

    Syntactic only, deliberately: see `scan_doc_symbolic`. Anything that is not
    recognisably a zero or a placeholder counts as a live weight.
    """
    return expr.strip().lower() not in _TRIVIAL_EXPR


def cas_zero(expr: str):
    """Is `expr` IDENTICALLY zero as a rational function of q?

    Returns True / False, or None if no CAS is available or it gave up.

    `scan_doc_symbolic` screens 3+-row weights syntactically and says why:
    a CAS "does not belong in a scan over a 7 MB witness", so it over-reports
    rather than under-reports. That is the right default and is not changed
    here. This runs the CAS on the handful of expressions the scan has ALREADY
    flagged, which is the one place the cost argument does not apply — tens of
    expressions, not millions of JSON nodes.

    Proving `simplify(expr) == 0` is not a tolerance and cannot hide a live
    convention-C weight: under D, `y_λ = 0` identically for `ℓ(λ) ≥ 3`, so
    algebraic zero IS the property being tested. A genuine C weight is a
    nonzero rational function and no amount of simplification makes it vanish.

    Why it matters in practice: a witness can be correctly D and still be
    flagged, because its D-ness is spelled as an unsimplified vanishing factor.
    Measured on `y-lambda-macdonald-telescope.witness.json`, where every one of
    the 14 flagged weights carries the factor
    `(1 - 1/((q**2 + 1)*(q**4/(q**2 + 1) - q**2 + 1)))` and
    `(q**2 + 1)*(q**4/(q**2 + 1) - q**2 + 1) = 1` exactly, so the factor — and
    the whole weight — is 0.
    """
    try:
        import sympy as sp
    except ImportError:
        return None
    try:
        q = sp.symbols("q")
        return sp.simplify(sp.sympify(expr, locals={"q": q})) == 0
    except Exception:              # noqa: BLE001 — a CAS failure is not a verdict
        return None


def scan_doc(doc, tol: float = DEAD_TOL):
    """Yield (partition, key, value) for every nonzero weight on a 3+ row block."""
    found = []

    def walk(node):
        if isinstance(node, dict):
            part = _partition_of(node)
            if part is not None and len(part) >= 3:
                for k, v in node.items():
                    if any(w in k for w in WEIGHT_KEYS):
                        try:
                            val = abs(float(v))
                        except (TypeError, ValueError):
                            continue
                        if val > tol:
                            found.append((part, k, v))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return found


#: Keys that hold a weight as a SYMBOLIC expression rather than a number.
SYMBOLIC_WEIGHT_KEYS = WEIGHT_KEYS + ("y_lambda_symbolic", "y_lambda_closed_form",
                                      "y_lambda_simplified_factored")

#: A half-integer power of q — the convention-C signature, and an exact one.
#:
#: C is z = 1/(q^{1/2} + q^{-1/2}); D is z = q^3/(q^2 + 1), a *rational*
#: function of q that never calls sqrt (the Rust engine's own note on
#: `markov_z` makes the same point). So a weight expression carrying q^{k/2}
#: was built under C, at any n, whatever its coefficients.
SQRT_Q = re.compile(r"q\s*\*\*\s*\(?\s*-?\d+\s*/\s*2\s*\)?"
                    r"|sqrt\(\s*q\s*\)"
                    r"|q\s*\*\*\s*-?0\.5")


def scan_doc_symbolic(doc):
    """Yield (partition, key, expr) for weight EXPRESSIONS built under C.

    The numeric test above calls `float(v)` and skips what does not parse, so a
    weight stored as a sympy expression is invisible to it — the same shape of
    blind spot as the decimal-fingerprint scan this detector replaced, and it
    hides the same class of witness.

    Found this way: `y-lambda-wenzl-bridge-symbolic-witness.json` evaluates to
    nonzero y_λ on 3-, 4-, 5- and 6-row partitions at q₀ (y_(4,1,1) = 0.0101,
    y_(1^6) = -1.24e-5), which convention D sends to exact zero. It feeds
    `rho_k_h3a_refinement`, whose own Schur-Weyl check has been failing at
    4.75e-8 — the producer was reporting this the whole time, via exit 2.

    TWO tests, because the sqrt signature alone misses the file that DEFINES
    the convention. `SQRT_Q` is a syntactic marker of C, and sympy rationalises
    it away: measured on the committed convention-C root
    (`y-lambda-wenzl-bridge-symbolic-witness.json`, 119 KB), `SQRT_Q` scores
    **0 hits** — every weight is a rational function of q such as
    `(1 - q**6)/((1 - q**2)*(q**2 + (1 - q**6)/(1 - q**2)))`. So the detector
    that exists to catch convention C was blind to the one file the whole
    cascade reads its convention from.

    The second test keys on the DEFINING property instead of a spelling: under
    convention D, `y_λ = 0` identically for `ℓ(λ) ≥ 3` (the `z_D` radical
    contains the antisymmetriser — `qou-u2jg`, Lean). A symbolic weight sitting
    on a 3+-row partition that is not trivially zero therefore cannot be D,
    whatever powers of q it is spelled with. This is the symbolic twin of
    `scan_doc`'s numeric test, not a new rule.

    This is still not "symbolic ⇒ suspect" — a 1- or 2-row block may carry any
    expression, and only the sqrt test fires there. Deciding whether an
    arbitrary q-expression is identically zero needs a CAS, which does not
    belong in a scan over a 7 MB witness, so the 3+-row test screens
    syntactically and over-reports rather than under-reports. For a test whose
    failure mode was silence, that is the right direction.
    """
    found = []

    def walk(node, part=None):
        if isinstance(node, dict):
            here = _partition_of(node) or part
            for k, v in node.items():
                if isinstance(v, str) and any(w in k for w in SYMBOLIC_WEIGHT_KEYS):
                    try:
                        float(v)          # a plain number is the numeric test's job
                        continue
                    except (TypeError, ValueError):
                        pass
                    if SQRT_Q.search(v):
                        found.append((here, k, v))
                    elif here is not None and len(here) >= 3 and _nonzero_expr(v):
                        found.append((here, k, v))
            for v in node.values():
                walk(v, here)
        elif isinstance(node, list):
            for v in node:
                walk(v, part)

    walk(doc)
    return found


def scan_repo(root: pathlib.Path = None):
    root = root or (REPO / "computations")
    out = []
    for p in sorted(root.rglob("*.json")):
        if "_deprecated" in str(p):
            continue
        try:
            raw = p.read_text()
        except OSError:
            continue
        if "partition" not in raw:
            continue
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError:
            continue
        hits = scan_doc(doc)
        if hits:
            out.append((str(p.relative_to(REPO)), hits))
    return out


def scan_repo_symbolic(root: pathlib.Path = None):
    root = root or (REPO / "computations")
    out = []
    for p in sorted(root.rglob("*.json")):
        if "_deprecated" in str(p):
            continue
        try:
            raw = p.read_text()
        except OSError:
            continue
        if "**" not in raw and "sqrt" not in raw:
            continue
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError:
            continue
        hits = scan_doc_symbolic(doc)
        if hits:
            out.append((str(p.relative_to(REPO)), hits))
    return out


def selftest() -> int:
    """A detector that cannot fail is worse than none."""
    cases = [
        ("nonzero weight on a 3-row block -> FLAG",
         {"per_lambda": [{"partition": [1, 1, 1], "y_lambda": 0.0227449}]}, True),
        ("nonzero weight at n=6, no n=3 fingerprint anywhere -> FLAG",
         {"per_lambda": [{"partition": [3, 1, 1, 1], "y_lambda": -0.000685309}]}, True),
        ("underscore-encoded partition -> FLAG",
         {"rows": [{"partition": ["3", "_", "2", "_", "1"], "y_lambda": 0.00731845}]}, True),
        ("zero weight on a 3-row block -> clear (this is convention D)",
         {"per_lambda": [{"partition": [1, 1, 1], "y_lambda": 0.0}]}, False),
        ("nonzero weight on a TWO-row block -> clear (live channel)",
         {"per_lambda": [{"partition": [2, 1], "y_lambda": 0.2472979}]}, False),
        ("nonzero on a one-row block -> clear",
         {"per_lambda": [{"partition": [3], "y_lambda": 0.5054042}]}, False),
        ("no partitions at all -> clear",
         {"data": {"mass": 938.272}}, False),
    ]
    sym_cases = [
        ("symbolic weight with q**(3/2) -> FLAG (C uses sqrt; D is rational)",
         {"weights": [{"partition": [1, 1, 1],
                       "y_lambda_symbolic": "q**6*(1 - 1/(q**(3/2) + q))"}]}, True),
        ("symbolic weight with sqrt(q) -> FLAG",
         {"weights": [{"partition": [2, 1, 1],
                       "y_lambda_closed_form": "1/(sqrt(q) + 1/sqrt(q))"}]}, True),
        # This case asserted `False` — "integer powers only ⇒ convention D" —
        # which is backwards, and is the exact reason the 119 KB convention-C
        # root scored 0 hits. Under D a 3-row weight is IDENTICALLY zero
        # (`qou-u2jg`); a nonzero one is convention C however it is spelled.
        ("nonzero symbolic weight on a 3-row block, integer powers -> FLAG "
         "(D sends l(lambda)>=3 to exact zero; sqrt is a spelling, not the test)",
         {"weights": [{"partition": [1, 1, 1],
                       "y_lambda_closed_form": "q**6*(1 - q**2)**2/(q**2 + 1)"}]}, True),
        # The shape actually committed in y-lambda-wenzl-bridge-symbolic-witness
        # at n=3, [1,1,1]: rational in q, no sqrt anywhere, and NOT identically
        # zero (evaluates to 0.02274494... at the proton q0).
        ("the committed convention-C root's own [1,1,1] expression -> FLAG",
         {"weights": [{"partition": [1, 1, 1], "y_lambda_symbolic":
                       "(1 - q**6)/((1 - q**2)*(q**2 + (1 - q**6)/(1 - q**2)))"}]}, True),
        ("symbolic ZERO on a 3-row block -> clear (this is convention D)",
         {"weights": [{"partition": [1, 1, 1], "y_lambda_symbolic": "0"}]}, False),
        ("integer-power expression on a TWO-row block -> clear (live under D)",
         {"weights": [{"partition": [2, 1],
                       "y_lambda_closed_form": "q**2/(q**2 + 1)"}]}, False),
        ("sqrt signature on a TWO-row block -> still FLAG (convention, not liveness)",
         {"weights": [{"partition": [2, 1], "y_lambda_symbolic": "q**(5/2)/(q + 1)"}]}, True),
        ("placeholder '?' -> clear (unknown, not convention C)",
         {"weights": [{"partition": [1, 1, 1], "y_lambda_at_zero": "?"}]}, False),
        ("plain numeric string -> clear here (the numeric test owns it)",
         {"weights": [{"partition": [1, 1, 1], "y_lambda": "0.0227449"}]}, False),
    ]
    # `cas_zero` decides the question `_nonzero_expr` deliberately cannot.
    # Its failure mode would be clearing a LIVE convention-C weight, so the
    # negative cases matter more than the positive ones.
    cas_cases = [
        ("the telescope's vanishing factor -> identically zero (correctly D)",
         "1 - 1/((q**2 + 1)*(q**4/(q**2 + 1) - q**2 + 1))", True),
        ("a full telescope weight carrying that factor -> identically zero",
         "q**6*(1 - q**2)**2*(1 - 1/((q**2 + 1)*(q**4/(q**2 + 1) - q**2 + 1)))",
         True),
        ("the committed convention-C root's [1,1,1] -> NOT zero (stays flagged)",
         "(1 - q**6)/((1 - q**2)*(q**2 + (1 - q**6)/(1 - q**2)))", False),
        ("a live two-row D weight -> NOT zero", "q**2/(q**2 + 1)", False),
        ("a written-down zero -> zero", "0", True),
        ("unparseable -> None, never a verdict", "?", None),
    ]
    bad = 0
    for name, doc, want in cases:
        got = bool(scan_doc(doc))
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
    for name, doc, want in sym_cases:
        got = bool(scan_doc_symbolic(doc))
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  [symbolic] {name}")
    for name, expr, want in cas_cases:
        got = cas_zero(expr)
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  [cas] {name}")
    n = len(cases) + len(sym_cases) + len(cas_cases)
    print(f"selftest: {n-bad}/{n}"
          + ("" if bad else " — flags a 3+row nonzero weight at any n, and a "
                            "sqrt-q weight expression at any n; clears convention D."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument(
        "--cas-verify", action="store_true",
        help="Run a CAS over the 3+-row symbolic hits already flagged and "
             "report which are provably identically zero (i.e. correctly "
             "convention D, merely unsimplified). Triage only: the exit "
             "code is unchanged, so no gate flips on this flag.")
    a = ap.parse_args()

    if a.selftest:
        return 1 if selftest() else 0

    hits = scan_repo()
    total = sum(len(h) for _, h in hits)
    print("convention-C witnesses, detected STRUCTURALLY "
          "(nonzero y_lambda on a 3+ row block)\n")
    print(f"  {len(hits)} witness(es), {total} dead-block entries\n")
    for path, entries in hits:
        print(f"  {path}   ({len(entries)} entries)")
        if a.list:
            for part, k, v in entries[:6]:
                print(f"      {list(part)}  {k} = {str(v)[:38]}")

    sym = scan_repo_symbolic()
    sym_total = sum(len(h) for _, h in sym)
    print("\nconvention-C witnesses, detected SYMBOLICALLY "
          "(half-integer power of q in a weight expression)\n")
    print(f"  {len(sym)} witness(es), {sym_total} expression(s)\n")
    for path, entries in sym:
        print(f"  {path}   ({len(entries)} expressions)")
        if a.list:
            for part, k, v in entries[:3]:
                where = list(part) if part else "-"
                print(f"      {where}  {k} = {str(v)[:38]}")

    if a.cas_verify and sym:
        proved, survived, unknown = [], [], []
        for path, entries in sym:
            for part, k, v in entries:
                if not (part and len(part) >= 3):
                    survived.append((path, part, k))
                    continue
                verdict = cas_zero(v)
                if verdict is True:
                    proved.append((path, part, k))
                elif verdict is False:
                    survived.append((path, part, k))
                else:
                    unknown.append((path, part, k))
        print("\n  CAS triage of the symbolic hits "
              "(3+-row weights only; --cas-verify)\n")
        print(f"    provably identically zero (correctly D) : {len(proved)}")
        print(f"    algebraically nonzero (genuine C)       : {len(survived)}")
        print(f"    CAS unavailable / gave up               : {len(unknown)}")
        if proved and not survived and not unknown:
            print("\n    ⇒ every symbolic hit is an unsimplified zero; no "
                  "convention-C weight survives this pass.")
        print("\n    Exit code deliberately unchanged — this is triage, "
              "not a relaxed gate.")

    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(
            {"structural": [{"witness": p,
                             "entries": [{"partition": list(pt), "key": k,
                                          "value": str(v)} for pt, k, v in e]}
                            for p, e in hits],
             "symbolic": [{"witness": p,
                           "entries": [{"partition": list(pt) if pt else None,
                                        "key": k, "value": str(v)[:200]}
                                       for pt, k, v in e]}
                          for p, e in sym]}, indent=2))
        print(f"\n  json -> {a.json}")

    return 1 if (hits or sym) else 0


if __name__ == "__main__":
    sys.exit(main())
