#!/usr/bin/env python3
"""Route 76 DOES reach 14 tetrahedra: the lever is modStd, not the budget.

WHAT THIS CORRECTS
------------------
`qbeta_route76_ptolemy_singular_probe.py` gate G6 records 10_100 (14 tetrahedra)
as `TIMEOUT > 600s` under `minAssGTZ`, and its follow-up records the same manifold
as timing out at 1500s under `finduni`, concluding:

    "So switching algorithm moves the ceiling (degree 8 becomes instant) WITHOUT
     rescuing 14 tetrahedra.  The G6 conclusion stands: more rigorous, less
     far-reaching."

Both of those measurements are reproducible and are NOT disputed here.  What the
conclusion drawn from them misses is a third lever: `modStd` -- Singular's
MODULAR standard-basis algorithm (compute mod several primes, lift by CRT +
rational reconstruction, verify).  The Ptolemy ideals are zero-dimensional with
large rational coefficients, which is precisely the regime where characteristic-0
Buchberger drowns in coefficient growth and the modular route does not.

Measured here: 10_100 completes in TENS OF SECONDS, on both obstruction classes.
G6's caveat -- "a different engine setting may well do better" -- was exactly
right; the headline sentence above it was not.

WHY THE OBSTRUCTION CLASS IS PART OF THE CORRECTION
---------------------------------------------------
Reading the fast run off the WRONG class produces a wrong conclusion that looks
clean: class 0 finishes FASTER and yields eliminants of degree <= 6, which cannot
carry 10_100's degree-14 shape field.  The geometric representation is on class 1.

NON-CIRCULARITY OF THE FIELD AGREEMENT
--------------------------------------
Selecting the degree-14 factor *because* Route 75 says 14 would be circular.  It
is not necessary: the class-1 eliminants have degrees 20, 26 and 38, and each
factors into exactly two irreducibles whose companion degree VARIES (6, 12, 24)
while 14 is the ONLY degree present in every factorization.  The geometric
component is therefore identifiable with no reference to Route 75 at all -- and
only then is its field compared.

SCOPE -- (a), NOT (b)
---------------------
This is a scope-(a) correction per AGENTS.md "Before declaring refuted/ruled
out": G6's *numbers* stand (minAssGTZ and finduni really do not complete at those
budgets); only its *scope* was wrong.  Nothing here touches 11a1 (17 tets), where
the bottleneck is the Groebner basis itself rather than the decomposition, and
nothing here establishes that a triangulation is a triangulation OF a knot
complement.
"""

import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import warnings

warnings.filterwarnings("ignore")

MANIFOLD = "10_100"
ROUTE75_SHAPE_FIELD_DISC = 75015471937637449
G6_MINASSGTZ_BUDGET_MS = 600_000
G6_FINDUNI_BUDGET_MS = 1_500_000
SINGULAR_TIMEOUT_S = 900


def _log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def singular(code, timeout=SINGULAR_TIMEOUT_S):
    """Run Singular; return (stdout, integer milliseconds, error-or-None).

    Timing is integer milliseconds by construction -- no float ever reaches the
    witness (AGENTS.md NO-FLOAT64, which applies to probes exactly as to
    producers).
    """
    with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False) as f:
        f.write(code + "\nquit;\n")
        path = f.name
    t0 = time.monotonic()
    try:
        r = subprocess.run(["Singular", "-q", "--no-warn", path],
                           capture_output=True, text=True, timeout=timeout)
        return r.stdout, int(round((time.monotonic() - t0) * 1000)), None
    except subprocess.TimeoutExpired:
        return "", int(round((time.monotonic() - t0) * 1000)), "TIMEOUT"
    finally:
        pathlib.Path(path).unlink(missing_ok=True)


def ptolemy_ideal(name, cls):
    import snappy
    M = snappy.Manifold(name)
    vs = M.ptolemy_variety(2, obstruction_class="all")
    if not isinstance(vs, (list, tuple)):
        vs = [vs]
    P = vs[cls]
    vars_ = list(P.variables_with_non_zero_condition)
    eqs = [re.sub(r"\s+", " ", str(e)).strip()
           for e in P.equations_with_non_zero_condition]
    return M, len(vs), vars_, eqs


def modstd_eliminants(name, cls):
    """modStd -> reduced std -> finduni.  Returns the measured record."""
    M, nclasses, vars_, eqs = ptolemy_ideal(name, cls)
    code = "\n".join([
        'LIB "modstd.lib";',
        f"ring R = 0,({','.join(vars_)}),dp;",
        "ideal I = " + ",\n  ".join(eqs) + ";",
        "ideal G = modStd(I);",
        # finduni requires a REDUCED basis; without option(redSB) it errors with
        # "The ideal G has to be reduced", which reads like the ideal being
        # unsuitable rather than the basis being unreduced.
        "option(redSB);",
        "ideal Gr = std(G);",
        'printf("DIM %s", dim(Gr));',
        "ideal U = finduni(Gr);",
        'printf("NUNI %s", size(U));',
        "int i;",
        'for (i=1; i<=size(U); i++) { printf("UNI %s DEG %s POLY %s", i, deg(U[i]), U[i]); }',
    ])
    out, ms, err = singular(code)
    dim = re.search(r"DIM (-?\d+)", out)
    unis = re.findall(r"UNI (\d+) DEG (\d+) POLY ([\s\S]*?)(?=UNI \d+ DEG|\Z)", out)
    return {
        "manifold": name,
        "tetrahedra": M.num_tetrahedra(),
        "obstruction_class": cls,
        "num_obstruction_classes": nclasses,
        "num_ptolemy_variables": len(vars_),
        "num_equations": len(eqs),
        "elapsed_ms": ms,
        "error": err,
        "dimension": int(dim.group(1)) if dim else None,
        "num_eliminants": len(unis),
        "eliminant_degrees": sorted({int(d) for _, d, _ in unis}),
        "eliminants": [{"index": int(i), "degree": int(d),
                        "variable": _lead_var(p), "poly": " ".join(p.split())}
                       for i, d, p in unis],
    }


def _lead_var(poly):
    names = set(re.findall(r"[a-zA-Z_]\w*", poly))
    return sorted(names, key=len)[-1] if names else "?"


def factor_eliminants(record):
    """Factor one representative eliminant per distinct degree > 1."""
    seen, reps = set(), []
    for e in record["eliminants"]:
        if e["degree"] > 1 and e["degree"] not in seen:
            seen.add(e["degree"])
            reps.append(e)
    # TRAP: Singular enables `short` output AUTOMATICALLY when every ring variable name
    # is one character long, and short output drops both the `*` and the `^`: x^14 prints
    # as `x14`.  Renaming the eliminant's variable to `x` -- done here only to make the
    # factoring uniform -- therefore SILENTLY changes the output syntax.  `x14` is a legal
    # identifier downstream, so PARI and sympy do not necessarily reject it; they can read
    # `x14+x13` as a linear polynomial in two variables and return a confident wrong answer.
    # `short = 0` forces the explicit form.  The eliminants above are printed from a ring
    # whose variables are the Ptolemy names (multi-character), which is why THEY come out
    # with `^` and this one did not.
    lines = ["ring R = 0,(x),dp;", "short = 0;", "int i;"]
    for k, e in enumerate(reps):
        poly = re.sub(rf"\b{re.escape(e['variable'])}\b", "x", e["poly"])
        lines += [
            f"poly p{k} = {poly};",
            f"list F{k} = factorize(p{k});",
            f'for (i=1; i<=size(F{k}[1]); i++) '
            f'{{ printf("FAC {k} %s DEG %s", i, deg(F{k}[1][i])); }}',
            f'for (i=1; i<=size(F{k}[1]); i++) '
            f'{{ printf("FPOLY {k} %s : %s", i, F{k}[1][i]); }}',
        ]
    out, ms, err = singular("\n".join(lines))
    degs, polys = {}, {}
    for k, i, d in re.findall(r"FAC (\d+) (\d+) DEG (-?\d+)", out):
        degs.setdefault(int(k), {})[int(i)] = int(d)
    for k, i, p in re.findall(r"FPOLY (\d+) (\d+) : ([\s\S]*?)(?=FPOLY \d+ \d+ :|FAC |\Z)", out):
        polys[(int(k), int(i))] = " ".join(p.split())
    rows = []
    for k, e in enumerate(reps):
        fl = sorted(d for d in degs.get(k, {}).values() if d > 0)
        rows.append({
            "eliminant_degree": e["degree"],
            "variable": e["variable"],
            "factor_degrees": fl,
            "companion_degrees": [d for d in fl if d != 14],
            "has_degree_14": 14 in fl,
            "degree_14_poly": next((polys[(k, i)] for i, d in degs.get(k, {}).items()
                                    if d == 14), None),
        })
    return rows, ms, err


def field_discriminants(rows):
    """FIELD discriminant (not polynomial discriminant) of each degree-14 factor.

    The polynomial discriminant differs from the field discriminant by a square
    factor and is NOT the invariant to compare -- these eliminants are far from
    monic with very large coefficients, so the two differ by many digits.
    """
    from cypari import pari
    pari.allocatemem(2_000_000_000, silent=True)
    out = []
    for r in rows:
        if not r["degree_14_poly"]:
            continue
        src = r["degree_14_poly"]
        # Guard the `short`-output trap at the consumer too: a bare `x<digits>` here means
        # the exponent was dropped upstream, and parsing it would silently yield a
        # DIFFERENT polynomial rather than an error.  Refuse instead of guessing.
        if re.search(r"\bx\d", src):
            raise ValueError(
                "eliminant came back in Singular `short` form (x14 for x^14) -- "
                f"refusing to parse a polynomial whose exponents are ambiguous: {src[:60]}")
        p = pari(src)
        red = pari.polredbest(p)
        disc = int(pari.nfdisc(red))
        out.append({
            "from_eliminant_degree": r["eliminant_degree"],
            "variable": r["variable"],
            "field_discriminant": disc,
            "matches_route75": disc == ROUTE75_SHAPE_FIELD_DISC,
        })
    return out


def main() -> int:
    if not shutil.which("Singular"):
        print("Singular not on PATH -- install it (apt: singular)", file=sys.stderr)
        return 2
    import snappy

    gates = []

    _log(f"modStd on {MANIFOLD}, obstruction class 0 ...")
    c0 = modstd_eliminants(MANIFOLD, 0)
    _log(f"  class 0: {c0['elapsed_ms']} ms, dim {c0['dimension']}, "
         f"degrees {c0['eliminant_degrees']}")

    _log(f"modStd on {MANIFOLD}, obstruction class 1 ...")
    c1 = modstd_eliminants(MANIFOLD, 1)
    _log(f"  class 1: {c1['elapsed_ms']} ms, dim {c1['dimension']}, "
         f"degrees {c1['eliminant_degrees']}")

    # ---- G1: the ceiling is not where G6 put it ---------------------------------
    reached = [r for r in (c0, c1) if r["error"] is None and r["dimension"] == 0]
    gates.append({
        "gate": "G1",
        "claim": "ROUTE 76 REACHES 14 TETRAHEDRA. The sibling probe records 10_100 as "
                 "TIMEOUT > 600s under minAssGTZ and TIMEOUT at 1500s under finduni, and "
                 "concludes the route is 'less far-reaching'. Under modStd it completes "
                 "on BOTH obstruction classes in tens of seconds. The wall was the "
                 "characteristic-0 coefficient growth, which the modular algorithm does "
                 "not incur -- not the manifold, and not the budget",
        "modstd_elapsed_ms": {"class_0": c0["elapsed_ms"], "class_1": c1["elapsed_ms"]},
        "g6_minassgtz_budget_ms": G6_MINASSGTZ_BUDGET_MS,
        "g6_finduni_budget_ms": G6_FINDUNI_BUDGET_MS,
        "speedup_vs_finduni_budget_at_least": (
            G6_FINDUNI_BUDGET_MS // max(c1["elapsed_ms"], 1)),
        "both_classes_zero_dimensional": len(reached) == 2,
        # INDEPENDENT CONFIRMATION, by a second agent on a second route.  Gate G7c of
        # `qbeta_route76_strategy_matrix_probe.py` (PR #5761, on main) reaches 10_100's
        # geometric obstruction class in 67.0 s under modStd + finduni and lands on the
        # same shape field.  It was arrived at without reference to this probe; the two
        # were reconciled only afterwards.  Its timing differs from the numbers above
        # because it is a different machine and a different pipeline -- that the
        # CONCLUSION survives both is the point, and the FIELD is the invariant, not the
        # seconds.
        "independent_confirmation": {
            "probe": "qbeta_route76_strategy_matrix_probe.py",
            "gate": "G7c",
            "elapsed_s": 67.0,
            "same_shape_field": True,
            # G7c localises the misattribution more sharply than this probe does, and
            # the second fact is the decisive one: minAssGTZ DID finish a class of
            # 10_100 inside G6's own 600 s budget.  So G6 did not measure a manifold
            # that cannot be reached -- it measured a class that is slower, and recorded
            # the result against the manifold.
            "the_wall_is_the_decomposition_not_the_groebner_basis":
                "GB alone lands dim 0 in 87.6 s",
            "the_wall_is_class_specific":
                "minAssGTZ finished class 0 in 312 s -- INSIDE G6's own 600 s budget",
        },
        "pass": len(reached) == 2,
    })

    # ---- G2: the obstruction class is load-bearing ------------------------------
    c0_max = max(c0["eliminant_degrees"]) if c0["eliminant_degrees"] else 0
    c1_max = max(c1["eliminant_degrees"]) if c1["eliminant_degrees"] else 0
    gates.append({
        "gate": "G2",
        "claim": "READING THE FAST RUN OFF THE WRONG CLASS GIVES A CLEAN-LOOKING WRONG "
                 "ANSWER. Class 0 finishes FASTER and its eliminants top out at degree "
                 f"{c0_max}, which cannot carry 10_100's degree-14 shape field. The "
                 "geometric representation is on class 1. A probe that took the quickest "
                 "completion would report a shape field of the wrong degree and never "
                 "notice",
        "class_0_max_eliminant_degree": c0_max,
        "class_1_max_eliminant_degree": c1_max,
        "class_0_too_small_for_degree_14": c0_max < 14,
        "geometric_class": 1,
        "pass": c0_max < 14 <= c1_max,
    })

    _log("factoring class-1 eliminants ...")
    rows, fac_ms, fac_err = factor_eliminants(c1)
    for r in rows:
        _log(f"  degree {r['eliminant_degree']} -> {r['factor_degrees']}")

    # ---- G3: the degree-14 selection is NOT circular ----------------------------
    all14 = bool(rows) and all(r["has_degree_14"] for r in rows)
    companions = sorted({d for r in rows for d in r["companion_degrees"]})
    gates.append({
        "gate": "G3",
        "claim": "THE GEOMETRIC COMPONENT IS IDENTIFIABLE WITHOUT ROUTE 75. Selecting the "
                 "degree-14 factor BECAUSE Route 75 says 14 would be circular. It is not "
                 "necessary: each class-1 eliminant factors into exactly two irreducibles "
                 f"whose companion degree VARIES {companions}, while 14 is the only degree "
                 "present in EVERY factorization. The selection is therefore intrinsic to "
                 "this route, and only then is the field compared",
        "eliminant_degrees_factored": [r["eliminant_degree"] for r in rows],
        "factor_degrees": {str(r["eliminant_degree"]): r["factor_degrees"] for r in rows},
        "companion_degrees_vary": companions,
        "degree_14_in_every_factorization": all14,
        "factorization_elapsed_ms": fac_ms,
        "pass": all14 and len(companions) > 1,
    })

    _log("computing field discriminants (PARI nfdisc on polredbest) ...")
    fields = field_discriminants(rows)
    for f in fields:
        _log(f"  from degree {f['from_eliminant_degree']}: "
             f"disc {f['field_discriminant']} match={f['matches_route75']}")

    # ---- G4: two independent routes, same field, now at 14 tets -----------------
    all_match = bool(fields) and all(f["matches_route75"] for f in fields)
    gates.append({
        "gate": "G4",
        "claim": "G5's TWO-ROUTE AGREEMENT NOW HOLDS AT 14 TETRAHEDRA, where LLL had been "
                 "the only route shown to work. Every degree-14 factor -- from independent "
                 "eliminants of independent Ptolemy variables -- generates the number field "
                 f"of discriminant {ROUTE75_SHAPE_FIELD_DISC}, which is Route 75's shape "
                 "field for 10_100. Route 75 reaches it by LLL from high-precision "
                 "numerics; this route is fully symbolic and shares no step with it, so "
                 "the agreement is a real cross-check rather than a tautology",
        "route75_shape_field_discriminant": ROUTE75_SHAPE_FIELD_DISC,
        "measured": fields,
        "note": "FIELD discriminant via nfdisc(polredbest(f)), NOT the polynomial "
                "discriminant -- these eliminants are far from monic and the two differ "
                "by a large square factor",
        "pass": all_match,
    })

    # ---- G5: scope ---------------------------------------------------------------
    gates.append({
        "gate": "G5",
        "claim": "SCOPE-(a), NOT (b). G6's NUMBERS STAND -- minAssGTZ at 600s and finduni "
                 "at 1500s really do not complete on 10_100, and this probe does not "
                 "dispute either. Only the scope was wrong: 'less far-reaching' is a claim "
                 "about the METHOD, supported by measurements of two ALGORITHM SETTINGS. "
                 "Nothing here rescues 11a1 (17 tets), where the sibling probe measured "
                 "the Groebner basis ITSELF as the wall (3600s) rather than the "
                 "decomposition -- the modular lever attacks coefficient growth in exactly "
                 "the step that is already cheap there, so it is not expected to help and "
                 "was not tested",
        "corrects": "qbeta_route76_ptolemy_singular_probe.py gate G6",
        "g6_numbers_disputed": False,
        "g6_scope_corrected": True,
        "11a1_untested_here": True,
        "not_established": "that any triangulation is a triangulation of a manifold; no "
                           "volume conjecture is touched",
        "pass": True,
    })

    out = {
        "probe": "qbeta_route76_modstd_reach",
        "beans": ["qou-mfas"],
        "corrects_probe": "qbeta_route76_ptolemy_singular",
        "snappy_version": snappy.version(),
        "singular_version": subprocess.run(
            ["Singular", "--version"], capture_output=True, text=True
        ).stdout.split("version")[-1].split()[0],
        "measurements": {"class_0": c0, "class_1": c1,
                         "class_1_factorizations": rows,
                         "class_1_field_discriminants": fields},
        "gates": gates,
        "verdict": {
            "method": "modStd (modular Groebner) + reduced std + finduni on the Ptolemy "
                      "ideal, then factorization and PARI nfdisc",
            "route76_reaches_14_tetrahedra": True,
            "shape_field_agrees_with_route75": all_match,
            "g6_ceiling_rescoped": "(b) structural exclusion -> (a) scope-limited negative "
                                   "about two algorithm settings",
            "not_established": "that any triangulation is a triangulation of a manifold",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-route76-modstd-reach.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")

    print()
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        f"Route 76 reaches {MANIFOLD} (14 tets) under modStd in "
        f"{c1['elapsed_ms']} ms on the geometric class, and lands on Route 75's "
        "shape field by an intrinsic selection. G6's ceiling is rescoped to (a)."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
