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
import os
import pathlib
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import warnings

warnings.filterwarnings("ignore")


def singular(code, timeout):
    """Run Singular in its OWN PROCESS GROUP; return (status, elapsed_seconds, stdout).

    The process group is not decoration.  `modStd` forks ~15 parallel modular jobs, and
    `subprocess.run(timeout=)` kills only the direct child -- so a timeout leaves the
    forks orphaned, reparented to init, and still burning every core.  Measured live:
    13 orphans survived an 11a1 timeout and were competing with the NEXT measurement
    until they were reaped by hand, which silently inflates whatever runs after a
    timeout.  Timings taken by a harness with this bug are not trustworthy in any run
    that follows a timeout.  start_new_session + killpg closes it.
    """
    with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False) as f:
        f.write(code + "\nquit;\n")
        path = f.name
    t0 = time.time()
    proc = subprocess.Popen(["Singular", "-q", "--no-warn", path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, start_new_session=True)
    try:
        stdout, _ = proc.communicate(timeout=timeout)
        return "ok", time.time() - t0, stdout
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            proc.kill()
        proc.communicate()
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
    # primdecGTZ returns (primary, prime) pairs; L[i][2] is the prime component.  It must
    # print its DIMENSION like every other strategy, or the calibration in G7a cannot
    # include it and a broken primdec would pass unnoticed -- it was run but never checked
    # for agreement until this was added.
    "primdec": ('list L = primdecGTZ(I);\nprintf("NCOMP %s", size(L));\n'
                'for (int i=1;i<=size(L);i++){ printf("DIM %s", dim(std(L[i][2])));\n'
                '  printf("GENS %s", L[i][2]); }'),
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
    ncomp = re.search(r"NCOMP (\d+)", out)
    return {"ideal_form": form, "ordering": order, "strategy": strategy,
            "status": status, "milliseconds": int(round(elapsed * 1000)),
            "num_variables": len(vs),
            "dimension": int(dim.group(1)) if dim else None,
            "num_components": int(ncomp.group(1)) if ncomp else None,
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
    # ALL six strategies, primdec included.  primdec used to be excluded here purely
    # because its body did not print a dimension -- so it ran on every calibration and
    # its result was never compared against anything.
    dims_agree = {r["dimension"] for r in cls1} == {0}
    quartic = "c_0011_3^4-c_0011_3^3+c_0011_3^2+1"
    uni_found = any(quartic in u.replace(" ", "")
                    for r in cls1 for u in r["univariate_eliminants"])
    # class 0 is empty for 6_1, as gate G2 of the sibling probe found for 4_1 and 5_2
    # Class 0 is empty and ALL SIX strategies now say so in the same vocabulary: dim = -1.
    # primdecGTZ reports it as one component generated by 1 -- the unit ideal -- not as an
    # empty list, so no special case is needed once its body prints a dimension at all.
    cls0 = [r for r in cal if r["obstruction_class"] == 0]
    cls0_empty = {r["dimension"] for r in cls0} == {-1}
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

    # ---- G7c: the reach question, answered -- and G6's ceiling does not survive ------
    # 10_100 has 14 tetrahedra.  Gate G6 recorded it as TIMEOUT > 600s and concluded
    # Route 76 was "strictly LESS FAR-REACHING" than Route 75.  It reaches:
    #
    #   class 1 (GEOMETRIC), nz form, modStd + finduni:  67.0s, dim 0, 15 eliminants
    #
    # The two things G6 conflated, separated:
    #   * the WALL IS THE DECOMPOSITION, not the Groebner basis.  On class 0 the GB alone
    #     lands dim 0 in 87.6s while minAssGTZ needs 312s and primdecGTZ did not finish.
    #   * the wall is CLASS-SPECIFIC.  minAssGTZ finished class 0 in 312s -- inside G6's
    #     own 600s budget -- so G6's timeout was almost certainly class 1, attributed to
    #     "the manifold" rather than to a class and a step.
    #
    # AND THE FIELD IS RIGHT, which is the part that makes the reach worth having.  Every
    # non-trivial class-1 eliminant factors into exactly two irreducible factors, one of
    # them degree 14; that factor generates the SAME FIELD as Route 75's independently
    # derived shape field -- same discriminant 75015471937637449, nfisisom isomorphic.
    # Gate G5 of the sibling probe established that agreement at 2-4 tetrahedra by LLL
    # versus symbolic decomposition; this extends it to 14, where LLL is the only one of
    # the two routes that had been shown to work.
    #
    # THE SELECTION STEP IS REAL BUT CHEAP HERE.  finduni returns the minimal polynomial
    # on the WHOLE variety, so the degree-14 geometric factor arrives alongside a
    # degree-6, -12 or -24 companion and must be picked out.  Every eliminant split into
    # exactly two factors with exactly one of degree 14, so the choice was unambiguous --
    # that is a property of THIS manifold, not a guarantee.
    #
    # By default this gate re-verifies the FIELD AGREEMENT, which is the mathematical
    # content and costs under a second.  The timings are recorded from the runs described
    # above and are NOT recomputed; pass --full to recompute them from scratch.
    R75_10_100 = ("x^14 - 16*x^13 + 157*x^12 - 929*x^11 + 4457*x^10 - 15653*x^9 "
                  "+ 44627*x^8 - 103739*x^7 + 182175*x^6 - 243898*x^5 + 246177*x^4 "
                  "- 129383*x^3 + 19267*x^2 - 2484*x - 364")
    PTOLEMY_10_100 = ("395*x^14 - 31781*x^13 + 27422*x^12 - 40221*x^11 + 5708*x^10 "
                      "- 8704*x^9 - 18493*x^8 + 8732*x^7 - 17695*x^6 + 6048*x^5 "
                      "- 6688*x^4 + 942*x^3 - 1429*x^2 - 92*x - 112")
    from cypari import pari
    pari.allocatemem(1 << 31, silent=True)
    iso = pari.nfisisom(pari(PTOLEMY_10_100), pari(R75_10_100))
    same_field = bool(iso) and str(iso) != "0"
    d_pt, d_75 = (str(pari.nfdisc(pari(PTOLEMY_10_100))),
                  str(pari.nfdisc(pari(R75_10_100))))

    recorded = [
        {"manifold": "10_100", "tets": 14, "obstruction_class": 1, "geometric": True,
         "strategy": "modStd_finduni", "ideal_form": "nz", "milliseconds": 67043,
         "status": "ok", "dimension": 0, "eliminants": 15},
        # THE CONTROL, and it is what turns "modStd is the lever" from an assertion
        # into a measurement.  Same container, same manifold, same geometric class, same
        # ideal form -- differing ONLY in modStd.  Plain finduni TIMES OUT at 1800s while
        # modStd + finduni finishes.  So the finduni timeout the sibling probe recorded
        # REPRODUCES: that measurement was right and only the conclusion drawn from it
        # was wrong.  Without this row the reach result rests on two runs that differ in
        # more than one variable, which is not a controlled comparison.
        {"manifold": "10_100", "tets": 14, "obstruction_class": 1, "geometric": True,
         "strategy": "finduni", "ideal_form": "nz", "milliseconds": 1800111,
         "status": "timeout", "dimension": None, "eliminants": 0,
         "note": "CONTROL for the row above -- identical except modStd. Re-measured "
                 "2026-08-25 on an idle machine, alongside the 42.0s modStd run."},
        {"manifold": "10_100", "tets": 14, "obstruction_class": 1, "geometric": True,
         "strategy": "modStd_finduni", "ideal_form": "nz", "milliseconds": 42040,
         "status": "ok", "dimension": 0, "eliminants": 15,
         "note": "clean-machine re-measurement, fresh container. The 67043 ms row above "
                 "was the same configuration under load and is kept as the conservative "
                 "bound; both are real."},
        {"manifold": "10_100", "tets": 14, "obstruction_class": 0, "geometric": False,
         "strategy": "modStd_finduni", "ideal_form": "nz", "milliseconds": 46660,
         "status": "ok", "dimension": 0, "eliminants": 15,
         "note": "every eliminant degree 6 -- NOT the geometric component, whose field "
                 "has degree 14"},
        {"manifold": "10_100", "tets": 14, "obstruction_class": 0, "geometric": False,
         "strategy": "std_only", "ideal_form": "nz", "milliseconds": 87550,
         "status": "ok", "dimension": 0,
         "note": "GB alone -- the step that is NOT the bottleneck"},
        {"manifold": "10_100", "tets": 14, "obstruction_class": 0, "geometric": False,
         "strategy": "minAss", "ideal_form": "nz", "milliseconds": 312040,
         "status": "ok", "dimension": 0,
         "note": "completes INSIDE the 600s budget gate G6 recorded as a timeout"},
        {"manifold": "10_100", "tets": 14, "obstruction_class": 0, "geometric": False,
         "strategy": "finduni", "ideal_form": "sat", "milliseconds": 1013930,
         "status": "ok", "dimension": 0,
         "note": "saturating in Singular is 10x WORSE than SnapPy's own non-zero "
                 "condition variable -- a measured pessimisation, recorded as one"},
    ]
    live_ok = None
    if "--full" in sys.argv:
        # Recomputing the TIMINGS without re-deriving the FIELD would leave the
        # mathematical claim resting on a hardcoded polynomial. Re-factor the live
        # eliminants and require a degree-14 factor isomorphic to Route 75's field, so
        # --full is a genuine end-to-end re-verification rather than a re-timing.
        import snappy as _sn
        P = _sn.Manifold("10_100").ptolemy_variety(2, obstruction_class="all")[1]
        live = run(P, "nz", "dp", "modStd_finduni", 2400)
        live_deg14 = []
        for u in live["univariate_eliminants"]:
            names = re.findall(r"[A-Za-z][A-Za-z_0-9]*", u)
            if not names:
                continue
            var = sorted(set(names), key=len)[-1]
            try:
                fac = pari.factor(pari(u.replace(var, "x")))
            except Exception:
                continue
            for i in range(len(fac[0])):
                if int(pari.poldegree(fac[0][i])) == 14:
                    live_deg14.append(str(fac[0][i]))
        live_ok = any(
            bool(pari.nfisisom(pari(p), pari(R75_10_100)))
            and str(pari.nfisisom(pari(p), pari(R75_10_100))) != "0"
            for p in live_deg14)
        recorded.append({"manifold": "10_100", "obstruction_class": 1,
                         "recomputed_this_run": True,
                         "live_degree14_factors": len(live_deg14),
                         "live_field_matches_route75": bool(live_ok), **live})
    gates.append({
        "gate": "G7c",
        "claim": "THE REACH CEILING IN G6 DOES NOT SURVIVE. 10_100 has 14 tetrahedra and "
                 "G6 recorded it as TIMEOUT > 600s, concluding Route 76 is 'strictly LESS "
                 "FAR-REACHING' than Route 75. The GEOMETRIC obstruction class solves in "
                 "67.0s with modStd + finduni, and its degree-14 eliminant factor "
                 "generates the SAME FIELD as Route 75's independently derived shape field "
                 "-- same discriminant 75015471937637449. G5 established that two-route "
                 "agreement at 2-4 tetrahedra; this extends it to 14, where LLL had been "
                 "the only route shown to work. The 600s wall is the primary DECOMPOSITION "
                 "and it is CLASS-SPECIFIC: minAssGTZ finished class 0 in 312s, inside "
                 "G6's own budget, so G6 timed out on a class and recorded a manifold",
        "geometric_class_reached": True,
        "route75_minpoly": R75_10_100,
        "ptolemy_degree14_factor": PTOLEMY_10_100,
        "same_field_as_route75": same_field,
        "ptolemy_disc": d_pt,
        "route75_disc": d_75,
        "selection_step_required": "finduni returns the minimal polynomial on the WHOLE "
                                   "variety, so the geometric degree-14 factor arrives "
                                   "with a degree-6/12/24 companion and must be selected. "
                                   "Every 10_100 eliminant split into exactly two factors "
                                   "with exactly one of degree 14, so the choice was "
                                   "unambiguous -- a property of this manifold, not a "
                                   "guarantee",
        # Selecting the degree-14 factor BECAUSE Route 75 reports degree 14 would make the
        # field agreement partly circular -- the criterion would import the answer it is
        # supposed to test.  It does not have to: across the 15 eliminants the companion
        # degree VARIES (6 x5, 12 x3, 24 x6) while 14 is the ONLY degree appearing in
        # every single factorization.  The geometric component is therefore identifiable
        # as "the degree common to all coordinates", with no reference to Route 75, and
        # the isomorphism test that follows is a genuine check rather than a restatement.
        "selection_is_independent_of_route75": True,
        "selection_criterion": "the geometric factor is the one whose degree appears in "
                               "EVERY coordinate's factorization; companions vary",
        "factor_degree_multisets": {"(6, 14)": 5, "(12, 14)": 3, "(14, 24)": 6},
        "degree_common_to_all_eliminants": 14,
        "measurements": recorded,
        "timings_recorded_not_recomputed": "--full" not in sys.argv,
        "load_caveat": "the 10_100 timings were taken with 2-3 Singular processes sharing "
                       "4 cores. Relative comparisons hold; absolute numbers are upper "
                       "bounds, which makes the reach claim conservative",
        "reproduce": "python3 computations/probes/qbeta_route76_strategy_matrix_probe.py "
                     "--full -- recomputes the 10_100 class-1 solve AND re-factors its "
                     "live eliminants, requiring a degree-14 factor isomorphic to Route "
                     "75's field. Without --full the gate verifies the recorded factor "
                     "against Route 75, which is the same field claim but does not "
                     "re-derive the factor",
        "pass": bool(same_field and d_pt == d_75 and (live_ok is not False)),
    })

    # ---- G7d: 11a1 (17 tetrahedra) -- a NEGATIVE, scoped as one ---------------------
    # The configuration that reached 10_100 in 67.0s does NOT reach 11a1: modStd + finduni
    # on the geometric class ran out a 2700s budget without returning.
    #
    # SCOPE, EXPLICITLY (a) NOT (b), per AGENTS.md "Before declaring refuted/ruled out":
    # this says THIS CONFIGURATION AT THIS BUDGET did not finish. It does NOT say the
    # Ptolemy route cannot reach 17 tetrahedra, and no invariant is offered that would
    # justify the stronger claim. G6 made exactly this error one manifold earlier -- it
    # recorded a 600s timeout and concluded "strictly less far-reaching", which G7c then
    # disproved -- so the same over-reading is not repeated here.
    #
    # Two measurement caveats that matter for reading the number:
    #   * modStd FORKS ~15 parallel modular jobs. On 4 cores that is ~4x self-
    #     oversubscription, so 2700s of WALL is considerably more CPU-time than a serial
    #     run would be. The timeout is a wall-clock statement.
    #   * `subprocess.run(timeout=)` kills the Singular parent but NOT modStd's forked
    #     children. 15 orphans survived the timeout at load average 12.5 and would have
    #     silently inflated every subsequent timing had they not been reaped. Any
    #     re-measurement must kill the process group, not the child.
    #
    # Where this leaves 11a1: unreached by EITHER route. Route 75's identification fails
    # there (sibling probe G6's own table), and Route 76 does not finish in 45 minutes.
    # So the honest joint statement is that 17 tetrahedra is past both routes as measured,
    # not that either route is bounded there.
    gates.append({
        "gate": "G7d",
        "claim": "11a1 (17 TETRAHEDRA) IS NOT REACHED BY THE CONFIGURATION THAT REACHED "
                 "10_100 -- recorded as a scope-(a) negative, not a ceiling. modStd + "
                 "finduni on the geometric class exhausted a 2700s budget without "
                 "returning. This states that THIS CONFIGURATION AT THIS BUDGET did not "
                 "finish; it does NOT state that the Ptolemy route cannot reach 17 "
                 "tetrahedra, and no invariant is offered that would justify the stronger "
                 "claim. Gate G6 made precisely that over-reading one manifold earlier and "
                 "G7c disproved it. Since Route 75's identification ALSO fails on 11a1, "
                 "the joint statement is that 17 tetrahedra is past both routes as "
                 "measured -- not that either route is bounded there",
        "scope": "(a) scope-limited negative -- this configuration, this budget",
        "not_claimed": "that the Ptolemy route cannot reach 17 tetrahedra",
        "measurements": [
            {"manifold": "11a1", "tets": 17, "obstruction_class": 1, "geometric": True,
             "strategy": "modStd_finduni", "ideal_form": "nz", "status": "timeout",
             "budget_seconds": 2700, "milliseconds": 2700140,
             "note": "under load; re-run clean below, same outcome"},
            {"manifold": "11a1", "tets": 17, "obstruction_class": 0, "geometric": False,
             "strategy": "modStd_finduni", "ideal_form": "nz", "status": "timeout",
             "budget_seconds": 1800, "milliseconds": 1800110,
             "note": "even the NON-geometric class does not finish, against 46.7s for "
                     "10_100's class 0"},
            {"manifold": "11a1", "tets": 17, "obstruction_class": 1, "geometric": True,
             "strategy": "std_only", "ideal_form": "nz", "status": "timeout",
             "budget_seconds": 3600, "milliseconds": 3600120,
             "machine": "idle", "note": "THE DISCRIMINATING RUN -- see "
                                        "bottleneck_migrates below"}],
        # THE BOTTLENECK MIGRATES, and that is the substantive finding at 17 tetrahedra.
        # At 14 tets the Groebner basis is cheap (87.6s) and the primary DECOMPOSITION is
        # the wall -- which is what G7c used to overturn G6's ceiling.  At 17 tets the GB
        # ALONE does not finish in an hour.  So 11a1 is not "10_100 but harder": the two
        # manifolds fail at DIFFERENT STEPS, and the reach story is two curves rather
        # than one.  A strategy that beats the decomposition -- which is exactly what
        # finduni and modStd do -- cannot help at 17 tets, because the step it replaces
        # is no longer the expensive one.
        "bottleneck_migrates": {
            "10_100_14_tets": {"groebner_basis": "87.6s", "decomposition": "312s "
                               "(minAssGTZ) / did not finish (primdecGTZ)",
                               "wall": "decomposition"},
            "11a1_17_tets": {"groebner_basis": "TIMEOUT > 3600s", "decomposition": "not "
                             "reached -- there is no basis to decompose",
                             "wall": "Groebner basis"},
            "consequence": "the eliminant strategies that won at 14 tets attack the "
                           "decomposition, so they cannot help at 17. Any route past "
                           "11a1 has to make the GB itself cheaper -- a different "
                           "ordering, a different ideal presentation, or a different "
                           "algorithm -- not a better decomposition",
        },
        "route75_on_11a1": "identification fails (sibling probe G6)",
        "reached_by_either_route": False,
        "measurement_caveats": [
            "modStd forks ~15 parallel modular jobs; on 4 cores that is ~4x self-"
            "oversubscription, so the 2700s is wall-clock, not CPU-time",
            "subprocess.run(timeout=) kills the Singular parent but NOT modStd's forked "
            "children -- 15 orphans survived at load average 12.5 and would have inflated "
            "every later timing had they not been reaped. Now fixed: singular() runs in "
            "its own process group and SIGKILLs the group on timeout",
            "CONFOUND, disclosed rather than discovered later: BOTH 11a1 timeouts above "
            "were measured while a background `lake build` -- armed by the SessionStart "
            "hook, not by this probe -- was compiling Mathlib and spawning lean workers "
            "at 25-70% CPU. `lake` started ~12:41 UTC; the class-1 run was 12:43-13:28 "
            "and the class-0 run 13:32-14:02, so both sit inside that window. Contention "
            "makes a TIMEOUT MORE LIKELY, so it weakens these negatives -- the same class "
            "of configuration artifact this probe exists to correct in G6. The numbers "
            "are kept because 'did not finish in 45 minutes' remains true as stated, but "
            "they are NOT clean-machine measurements and must not be cited as though they "
            "were"],
        "remeasurement": {
            "done": True,
            "result": "THE NEGATIVE HOLDS. Re-run on a verified-idle machine -- lean "
                      "build killed, zero Singular/lean/lake processes confirmed before "
                      "launch -- 11a1 class 1 with modStd + finduni timed out again at "
                      "2700s. Removing the confound did not change the outcome, so the "
                      "scope-(a) negative stands as recorded; what changed is that it is "
                      "now honestly measured",
            "milliseconds": 2700130,
            "status": "timeout",
            "machine": "idle (background lake build killed and verified absent)",
            "loadavg_caveat": "the probe recorded loadavg_at_start = 4.08, which looks "
                              "like contention and is NOT. Load average is an "
                              "exponentially-weighted moving average with a ~1 minute "
                              "time constant, so immediately after killing ~15 processes "
                              "it still reads high while the machine is in fact idle. "
                              "The trustworthy evidence of idleness is the process count "
                              "(zero Singular, zero lean, zero lake), not the load "
                              "average -- recorded here because the number in the "
                              "witness invites exactly the wrong reading",
            "orphan_fix_confirmed_live": "this timeout left ZERO orphaned Singular "
                                         "processes, against 13 from the equivalent "
                                         "pre-fix timeout. The process-group kill works",
            "std_only_clean": "the GB-alone diagnostic ALSO timed out, at 3600s on the "
                              "idle machine. That is the run that shows the bottleneck "
                              "has migrated -- see bottleneck_migrates",
        },
        "unaffected_by_the_confound": "the 10_100 reach result in G7c. Its 67.0s "
                                      "class-1 solve ran at ~12:20 UTC, BEFORE lake "
                                      "started at ~12:41",
        "pass": True,
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
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "Route 76 DOES reach 10_100 (14 tetrahedra) -- 67s on the geometric class, "
        "landing Route 75's field. G6's 600s ceiling was the primary decomposition on "
        "one obstruction class, recorded as a property of the manifold. It does NOT "
        "reach 11a1 (17 tets) at a 2700s budget -- recorded as a scope-(a) negative, "
        "not a ceiling; Route 75 fails there too."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
