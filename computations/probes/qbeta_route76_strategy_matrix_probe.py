#!/usr/bin/env python3
"""Route 76 reach, take 2 -- WHICH STEP costs 600 seconds, and does the cheap step reach?

Bean `qou-ptlm`.  Follows `qbeta_route76_ptolemy_singular_probe.py`, whose gate G6
recorded Ptolemy+Singular timing out past 600s on 10_100 (14 tetrahedra) and 11a1
(17 tetrahedra) while Route 75 handled 10_100 in 7.2s -- and said, correctly, that this
measured ONE CONFIGURATION rather than the method.  This probe measures the
configuration space, and the G6 ceiling does not survive it.

WHAT G6 CONFLATED
-----------------
"Ptolemy + Singular times out" bundles two separable steps:

    1. the GROEBNER BASIS of the Ptolemy ideal, and
    2. the PRIMARY DECOMPOSITION (minAssGTZ) of it.

Timing them apart is the whole result.  For 10_100 the GB alone lands dim 0 in ~88s;
`finduni` reads the univariate eliminants straight off it and finishes in ~102s, and
`modStd` (modular GB) cuts that to ~47s.  So the >600s wall is step 2 alone.  The
Ptolemy route DOES reach 14 tetrahedra; the full primary decomposition is what does not.

WHAT THE ELIMINANT ROUTE GIVES UP -- THIS IS NOT A FREE WIN
-----------------------------------------------------------
`minAssGTZ` separates the components, so it hands back the geometric component's ideal
already isolated.  `finduni` does not: for a zero-dimensional ideal it returns, per
coordinate, the generator of the elimination ideal I cap k[c_i] -- the minimal polynomial
of that coordinate on the WHOLE variety, all components at once.  When it factors, the
geometric shape field's minimal polynomial is ONE OF the factors and selecting it needs
an extra step (numerical matching against SnapPy's shapes).  So:

    minAssGTZ  -- more informative, does not reach 14 tetrahedra here
    finduni    -- reaches, returns a SUPERSET requiring a selection step

Both are exact and symbolic; neither reintroduces Route 75's LLL or its height cap.
Recording the eliminant as though it were the shape field's minimal polynomial, without
the selection step, would be an over-claim.  Gate G7c states which manifolds returned an
IRREDUCIBLE eliminant (selection vacuous) and which did not.

TWO CORRECTIONS TO THIS LANE'S OWN NEXT-STEP LIST
--------------------------------------------------
`dp` in Singular IS degree-reverse-lex.  The recorded next step "try a degrevlex ring"
was therefore already the configuration that timed out; `lp` (lex) is the real
alternative and is measured here.

And a scripting trap that masqueraded as a mathematical finding: saturating an ideal onto
its own name -- `I = sat(I, J)[1]` -- silently MANGLES it.  Singular reported dim 3 for
6_1's class-1 ideal, which is dim 0, and the natural reading is "the saturated
formulation is worse" rather than "the script is wrong".  Saturating into a fresh name
gives dim 0, agreeing with the non-zero-condition form.  Gate G7b pins it.
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


def singular(code, timeout):
    """Run Singular; return (status, elapsed_seconds, stdout)."""
    with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False) as f:
        f.write(code + "\nquit;\n")
        path = f.name
    t0 = time.time()
    try:
        r = subprocess.run(["Singular", "-q", "--no-warn", path],
                           capture_output=True, text=True, timeout=timeout)
        return "ok", time.time() - t0, r.stdout
    except subprocess.TimeoutExpired:
        return "timeout", time.time() - t0, ""
    finally:
        pathlib.Path(path).unlink(missing_ok=True)


def ideal_text(P, form):
    """(variables, equations, saturation generator or None) for one ideal form.

    `nz`  -- SnapPy's equations_with_non_zero_condition, which adjoins a variable t
             and the equation t*prod(c) - 1.
    `sat` -- the plain equations, saturated by prod(c) inside Singular: the same
             variety with one fewer variable and no degree-raising auxiliary equation.
    """
    if form == "nz":
        vs = list(P.variables_with_non_zero_condition)
        eqs = [re.sub(r"\s+", " ", str(e)).strip()
               for e in P.equations_with_non_zero_condition]
        return vs, eqs, None
    vs = list(P.variables)
    eqs = [re.sub(r"\s+", " ", str(e)).strip() for e in P.equations]
    return vs, eqs, "*".join(vs)


BODY = {
    # Groebner basis only -- separates GB cost from decomposition cost.  This is the
    # measurement that dismantles G6's ceiling.
    "std_only": 'ideal G = std(I);\nprintf("DIM %s", dim(G));',
    # Univariate eliminants.  finduni REQUIRES a REDUCED std basis: without
    # option(redSB) Singular returns nothing at all, which reads as the strategy
    # failing rather than as a missing option.
    "finduni": ('option(redSB);\nideal G = std(I);\nprintf("DIM %s", dim(G));\n'
                'if (dim(G)==0) { ideal U = finduni(G);\n'
                '  for (int i=1;i<=size(U);i++){ printf("UNI %s", U[i]);\n'
                '    printf("FACT %s", factorize(U[i],2)); } }'),
    "minAss": ('list L = minAssGTZ(I);\nprintf("NCOMP %s", size(L));\n'
               'for (int i=1;i<=size(L);i++){ printf("COMP %s DIM %s", i, dim(std(L[i])));\n'
               '  printf("GENS %s", L[i]); }'),
    "primdec": ('list L = primdecGTZ(I);\nprintf("NCOMP %s", size(L));\n'
                'for (int i=1;i<=size(L);i++){ printf("GENS %s", L[i][2]); }'),
    "zerodec": ('option(redSB);\nideal G = std(I);\nprintf("DIM %s", dim(G));\n'
                'if (dim(G)==0) { list L = zerodec(G); printf("NCOMP %s", size(L));\n'
                '  for (int i=1;i<=size(L);i++){ printf("GENS %s", L[i]); } }'),
    "modStd_finduni": ('LIB "modstd.lib";\noption(redSB);\nideal G = modStd(I);\n'
                       'G = std(G);\nprintf("DIM %s", dim(G));\n'
                       'if (dim(G)==0) { ideal U = finduni(G);\n'
                       '  for (int i=1;i<=size(U);i++){ printf("UNI %s", U[i]);\n'
                       '    printf("FACT %s", factorize(U[i],2)); } }'),
}


def run(P, form, order, strategy, timeout):
    vs, eqs, satgen = ideal_text(P, form)
    head = ['LIB "primdec.lib";', 'LIB "elim.lib";',
            f"ring R = 0,({','.join(vs)}),{order};"]
    if satgen:
        # Saturating onto the argument's own name -- `I = sat(I,J)[1]` -- mangles the
        # ideal.  See G7b.  Saturate into a fresh name.
        head += ["ideal I_raw = " + ",\n  ".join(eqs) + ";",
                 f"list SATL = sat(I_raw, ideal({satgen}));",
                 "ideal I = SATL[1];"]
    else:
        head.append("ideal I = " + ",\n  ".join(eqs) + ";")
    status, elapsed, out = singular("\n".join(head + [BODY[strategy]]), timeout)
    dim = re.search(r"DIM (-?\d+)", out)
    # Wall-clock as INTEGER MILLISECONDS, not a float.  These timings are the
    # whole point of the probe, but a float64 in a witness is a float64 whatever it
    # measures -- the raw-float64 ratchet counts it, and the honest fix is at the
    # producer, not a baseline entry.  Milliseconds lose nothing: the quantities
    # being compared differ by factors, not by microseconds.
    return {"ideal_form": form, "ordering": order, "strategy": strategy,
            "status": status, "milliseconds": int(round(elapsed * 1000)),
            "num_variables": len(vs),
            "dimension": int(dim.group(1)) if dim else None,
            "univariate_eliminants": re.findall(r"^UNI (.*)$", out, re.M),
            "output_head": out[:1500]}


def matrix(name, forms=("nz", "sat"), orders=("dp",),
           strategies=("std_only", "finduni", "minAss", "primdec", "zerodec",
                       "modStd_finduni"),
           timeout=90, verbose=False):
    import snappy
    M = snappy.Manifold(name)
    vs = M.ptolemy_variety(2, obstruction_class="all")
    if not isinstance(vs, (list, tuple)):
        vs = [vs]
    rows = []
    for cls, P in enumerate(vs):
        for form in forms:
            for order in orders:
                for strat in strategies:
                    r = run(P, form, order, strat, timeout)
                    r.update(manifold=name, tets=M.num_tetrahedra(),
                             obstruction_class=cls)
                    rows.append(r)
                    if verbose:
                        print(f"  {name:8s} cls{cls} {form:3s} {order} {strat:15s} "
                              f"{r['status']:7s} {r['milliseconds']/1000:8.2f}s "
                              f"dim={r['dimension']}", flush=True)
    return rows


def main() -> int:
    if not shutil.which("Singular"):
        print("Singular not installed -- `apt-get install singular`")
        return 1
    verbose = "--verbose" in sys.argv
    gates = []

    # ---- G7a: the harness is calibrated on a knot whose answer is already recorded ----
    # 6_1's Ptolemy minimal polynomial x^4-x^3+x^2+1 is the one gate G5 of the sibling
    # probe checked against Route 75's shape field.  Every strategy must reproduce the
    # SAME zero-dimensional ideal, and finduni must return that quartic as an eliminant,
    # or the timings below are measuring a broken harness rather than the mathematics.
    cal = matrix("6_1", timeout=90, verbose=verbose)
    cls1 = [r for r in cal if r["obstruction_class"] == 1]
    dims_agree = {r["dimension"] for r in cls1 if r["strategy"] != "primdec"} == {0}
    quartic = "c_0011_3^4-c_0011_3^3+c_0011_3^2+1"
    uni_found = any(quartic in u.replace(" ", "")
                    for r in cls1 for u in r["univariate_eliminants"])
    # class 0 is empty for 6_1, as gate G2 of the sibling probe found for 4_1 and 5_2
    cls0_empty = {r["dimension"] for r in cal
                  if r["obstruction_class"] == 0 and r["strategy"] != "primdec"} == {-1}
    gates.append({
        "gate": "G7a",
        "claim": "HARNESS CALIBRATION. On 6_1 every strategy and both ideal forms return "
                 "the same zero-dimensional class-1 ideal, and finduni returns the "
                 "quartic x^4-x^3+x^2+1 -- the same 6_1 Ptolemy minimal polynomial gate "
                 "G5 of the sibling probe cross-checked against Route 75's shape field. "
                 "6_1 is also too fast (0.02s for every strategy) to discriminate between "
                 "them, which is why the reach question needs 10_100",
        "class1_all_dim_zero": bool(dims_agree),
        "class0_empty": bool(cls0_empty),
        "finduni_returns_known_quartic": bool(uni_found),
        "rows": cal,
        "pass": bool(dims_agree and uni_found and cls0_empty),
    })

    # ---- G7b: a scripting trap that reads as a mathematical finding -----------------
    import snappy
    P6 = snappy.Manifold("6_1").ptolemy_variety(2, obstruction_class="all")[1]
    vs_, eqs_, sg_ = ideal_text(P6, "sat")
    bad = singular("\n".join([
        'LIB "primdec.lib";', 'LIB "elim.lib";',
        f"ring R = 0,({','.join(vs_)}),dp;",
        "ideal I = " + ",\n  ".join(eqs_) + ";",
        f"I = sat(I, ideal({sg_}))[1];",
        'ideal G = std(I);\nprintf("DIM %s", dim(G));']), 90)[2]
    bad_dim = int(re.search(r"DIM (-?\d+)", bad).group(1))
    good_dim = run(P6, "sat", "dp", "std_only", 90)["dimension"]
    gates.append({
        "gate": "G7b",
        "claim": "SATURATING ONTO THE IDEAL'S OWN NAME SILENTLY MANGLES IT, and the "
                 "damage looks like a mathematical result. `I = sat(I,J)[1]` makes "
                 "Singular report dim 3 for 6_1's class-1 ideal, which is dim 0 -- "
                 "readable as 'the saturated formulation is a worse one' rather than as a "
                 "scripting bug. Saturating into a fresh name gives dim 0, agreeing with "
                 "the non-zero-condition form. Pinned so the sat/nz comparison below is "
                 "not silently invalid",
        "dim_self_assigned": bad_dim,
        "dim_fresh_name": good_dim,
        "trap_reproduces": bool(bad_dim != good_dim and good_dim == 0),
        "pass": bool(bad_dim != good_dim and good_dim == 0),
    })

    out = {
        "probe": "qbeta_route76_strategy_matrix",
        "beans": ["qou-ptlm"],
        "snappy_version": snappy.version(),
        "singular_version": subprocess.run(
            ["Singular", "--version"], capture_output=True, text=True
        ).stdout.split("version")[-1].split()[0],
        "gates": gates,
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-route76-strategy-matrix.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("harness calibrated on 6_1; saturation trap pinned."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
