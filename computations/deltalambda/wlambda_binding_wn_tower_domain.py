#!/usr/bin/env python3
"""t7qv w_n(K): Part 5 and Part 13 are CONSISTENT — the tower is domain-limited.

Bean t7qv, remaining open item (theta_lambda w_n(K) closure). Its frontier
update leaves a flagged tension, verbatim:

    NOTE for future me: the "C(A,n) body-order combinatorial weighting"
    (4He gets 6.a_D^2 + 4.a_D^3 + 1.a_D^4 ~ 13.88x vs 12.72x exp -- a tempting
    fit-free light-nucleus match) is exactly Part-13's A<=4 simplex bond-count
    AND the Part-5-refuted full tower;

i.e. the same object is both the validated bond count and a refuted route. This
probe resolves that, using the theorem proved earlier in this arc
(QOU.Mass.MaxContactSimplex.not_five_equidistant: no five equal spheres are
mutually tangent in 3D, so the complete contact graph exists only for A <= 4).

FINDING 1: the break is exactly at the theorem's boundary
----------------------------------------------------------
Full tower sum_{n=2}^{A} C(A,n) a_D^(n), normalised to D, with the frontier's
super-exponential period a_D^(n) = 1, 1, 1.34, 2.53, 5.38, 13.56:

    A = 2   model 1.000   exp 1.000    err  0 %      (anchor)
    A = 3   model 4.340   exp 3.813    err +13.8 %   A<=4: simplex valid
    A = 4   model 13.89   exp 12.720   err  +9.2 %   A<=4: simplex valid
    A = 6   model 125.6   exp 14.382   err +773 %    A>=5: NOT a simplex

CONTROL: this reproduces the frontier's own quoted figures (13.88x model,
12.72x experimental) to three figures, so the reading of a_D^(n) and of the
tower is the intended one.

Part 5's counterexamples are A = 6, 7, 9, 12 -- EVERY ONE outside the simplex
domain. So Part 5 and Part 13 are not in tension: C(A,n) IS the max-contact
bond count where Part 13 claims it (A <= 4), and is NOT the packing's clique
count where Part 5 refutes it (A >= 5). The tower is domain-limited, not wrong.

FINDING 2 (MY HYPOTHESIS, HALF FALSIFIED): the truncation is NECESSARY BUT NOT
SUFFICIENT
-------------------------------------------------------------------------------
Part 5's redirect reads "It must be a few-body truncation (fixed small n_max,
~2-3)" -- chosen, not derived. not_five_equidistant DOES derive a cap: cliques
of mutually tangent equal spheres have at most 4 members, so the body-order sum
truncates at n_max = 4 geometrically. I expected that to rescue A >= 5. It does
not. Truncating at n_max = 4 while keeping C(A,n) counts gives A = 6 at +454 %,
against +773 % untruncated: a 1.7x improvement, nowhere near enough. The reason
is that C(6,4) = 15 mutually-tangent 4-sets is itself geometrically impossible.

FINDING 3: it is the clique COUNT bound that does the work, 10x to 1.7x
------------------------------------------------------------------------
Hold the clique counts LINEAR in A at the densities read off the A = 4 simplex
-- kappa_n = C(4,n)/4 = 1.5, 1.0, 0.25, with NO free parameter and nothing
fitted to A = 6 -- and A = 6 falls to +45 %:

    A = 6:   C(A,n) full  +773 %
             n_max <= 4   +454 %   (body-order cap:      1.7x)
             linear in A   +45 %   (clique-count bound: 10.1x)

(At A = 4 all three coincide at +9.2 %, as they must: there the simplex IS the
complete graph and the densities were read off it. That is the check that the
comparison is not circular at the anchor.)

This is a DIAGNOSTIC of which constraint carries the scaling, not a model and
not a fit -- +45 % is not offered as a prediction.

WHAT IT MEANS FOR THE CLOSURE. Two geometric inputs are needed and only one is
in hand:

  (i)  body-order cap n_max <= 4   -- PROVED (not_five_equidistant), worth 1.7x
  (ii) clique count O(A) per order -- NOT proved; this is the bounded-degree /
       3D kissing-number half flagged in QOU.Mass.MaxContactSimplex, worth 10x

and (ii) is exactly the hypothesis QOU.Mass.CoordinationSaturation.
bounded_degree_saturates already assumes. So the remaining leverage in the
w_n(K) closure is the kissing-number bound, NOT the body-order truncation that
Part 5's redirect names.
"""
import json
import time
from math import comb  # float64-ok: exact integer binomial, no float path
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 25


def main():
    t0 = time.monotonic_ns()
    checks = []
    a = {2: mpf("1"), 3: mpf("1.34"), 4: mpf("2.53"),
         5: mpf("5.38"), 6: mpf("13.56")}
    B = {2: mpf("2.2245662"), 3: mpf("8.4817962"),
         4: mpf("28.2956624"), 6: mpf("31.9946")}
    kappa = {n: mpf(comb(4, n)) / 4 for n in (2, 3, 4)}

    def full(A):
        return sum(comb(A, n) * a[n] for n in range(2, A + 1) if n in a)

    def trunc(A):
        return sum(comb(A, n) * a[n] for n in range(2, min(A, 4) + 1))

    def lin(A):
        return sum(kappa[n] * A * a[n] for n in (2, 3, 4))

    rows = []
    for A in (2, 3, 4, 6):
        e = B[A] / B[2]
        rows.append({
            "A": A, "exp": nstr(e, 6), "full": nstr(full(A), 6),
            "err_full_pct": nstr(100 * (full(A) / e - 1), 5),
            "err_trunc_pct": nstr(100 * (trunc(A) / e - 1), 5) if A >= 4 else None,
            "err_linear_pct": nstr(100 * (lin(A) / e - 1), 5) if A >= 4 else None,
            "simplex_valid": A <= 4,
        })
    small = [abs(mpf(r["err_full_pct"])) for r in rows if r["A"] <= 4]
    big = [abs(mpf(r["err_full_pct"])) for r in rows if r["A"] > 4]
    checks.append({
        "name": "FINDING 1: the tower breaks exactly at the A<=4 simplex boundary",
        "pass": max(small) < 20 and min(big) > 200,
        "detail": (
            f"Full tower normalised to D: "
            + "; ".join(f"A={r['A']} model {r['full']} vs exp {r['exp']} "
                        f"({r['err_full_pct']} %)" for r in rows)
            + f". Errors stay under {nstr(max(small), 4)} % for A <= 4 -- where "
            f"QOU.Mass.MaxContactSimplex.not_five_equidistant permits the "
            f"complete contact graph -- and jump to {nstr(min(big), 5)} % at "
            f"A = 6. CONTROL: this reproduces the frontier's own quoted 13.88x "
            f"model / 12.72x experimental for He-4 to three figures, so the "
            f"reading of a_D^(n) and of the tower is the intended one. Part 5's "
            f"counterexamples are A = 6, 7, 9, 12 -- every one outside the "
            f"simplex domain. Part 5 and Part 13 are therefore CONSISTENT: "
            f"C(A,n) is the max-contact bond count where Part 13 claims it and "
            f"is not the packing's clique count where Part 5 refutes it."),
    })
    r6 = next(r for r in rows if r["A"] == 6)
    ef, et, el = (abs(mpf(r6["err_full_pct"])), abs(mpf(r6["err_trunc_pct"])),
                  abs(mpf(r6["err_linear_pct"])))
    checks.append({
        "name": "FINDING 2 (MY HYPOTHESIS, HALF FALSIFIED): truncation is necessary, not sufficient",
        "pass": et < ef and et > 200,
        "detail": (
            f"Part 5's redirect names a 'few-body truncation (fixed small "
            f"n_max, ~2-3)' as a modelling choice. not_five_equidistant DERIVES "
            f"a cap -- cliques of mutually tangent equal spheres have at most 4 "
            f"members -- so I expected n_max <= 4 to rescue A >= 5. It does not. "
            f"At A = 6 truncation takes the error from {nstr(ef, 4)} % to "
            f"{nstr(et, 4)} %, a factor {nstr(ef / et, 3)} and still enormous, "
            f"because C(6,4) = 15 mutually-tangent 4-sets is itself "
            f"geometrically impossible."),
    })
    checks.append({
        "name": "FINDING 3: the clique COUNT bound carries the scaling, 10x vs 1.7x",
        "pass": el < et / 5,
        "detail": (
            f"Holding clique counts LINEAR in A at densities read off the A = 4 "
            f"simplex -- kappa_n = C(4,n)/4 = "
            f"{[nstr(kappa[n], 4) for n in (2, 3, 4)]}, no free parameter, "
            f"nothing fitted to A = 6 -- drops A = 6 to {nstr(el, 4)} %. So the "
            f"body-order cap is worth {nstr(ef / et, 3)}x and the clique-count "
            f"bound {nstr(et / el, 3)}x. CONTROL: at A = 4 all three coincide "
            f"({rows[2]['err_full_pct']} %), as they must -- there the simplex "
            f"IS the complete graph and the densities were read off it -- so the "
            f"comparison is not circular at the anchor. This is a DIAGNOSTIC of "
            f"which constraint carries the scaling, not a model: the 45 % is not "
            f"offered as a prediction. CONSEQUENCE: the closure needs two "
            f"geometric inputs and has one -- (i) n_max <= 4, PROVED, worth "
            f"1.7x; (ii) clique count O(A), NOT proved, worth 10x, and it is "
            f"exactly the bounded-degree hypothesis "
            f"CoordinationSaturation.bounded_degree_saturates already assumes. "
            f"The remaining leverage is the kissing-number bound, not the "
            f"truncation Part 5's redirect names."),
    })
    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("wn-tower-domain.witness.json").write_text(
        json.dumps({
        "q0Anchor": "independent",
        "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: t7qv w_n(K): Part 5 and Part 13 are CONSISTENT \u2014 the tower is domain-limited.",
            "probe": "wn_tower_domain", "bean": ["t7qv"],
            "lean": ["QOU.Mass.MaxContactSimplex.not_five_equidistant",
                     "QOU.Mass.CoordinationSaturation.bounded_degree_saturates"],
            "period_aD": {str(k): nstr(v, 6) for k, v in a.items()},
            "rows": rows, "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: Part 5 and Part 13 are CONSISTENT -- the C(A,n) tower is")
    print("RESULT:   domain-limited to A <= 4, and every Part-5 counterexample is A >= 5.")
    print("RESULT: the derived n_max <= 4 truncation is NECESSARY BUT NOT SUFFICIENT (1.7x);")
    print("RESULT:   the clique-count bound carries the scaling (10x) and is unproved.")
    print("RESULT: t7qv w_n(K) closure stays OPEN, with the leverage relocated.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
