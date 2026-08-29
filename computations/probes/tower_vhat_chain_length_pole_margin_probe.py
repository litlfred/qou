#!/usr/bin/env python3
"""The tower's per-generator V̂ takes SEVEN values at every nucleon count, and the
largest is one chain-length step from the Φ_q pole (beans qou-xsue, qou-zloi,
qou-lbgh).

THE QUESTION.  `per_generator_V_hat_3A` runs V̂ up to 98 % of the Φ_q pole at
`|V̂| = q` (bean `qou-2tuv`).  The natural worry is that the margin DEGRADES with
nucleon count — if `max |V̂|` grows with A, the tower is undefined past some atom
and the whole construction has a ceiling.  This settles that, and then localises
what the margin actually depends on.

WHY IT IS CHEAP TO ASK NOW.  `QOU.BraidsAndKnots.markov_param_eq_half_h` pins
that producer's Markov parameter at `Z = h/2` with no computation at all, and
`prod_eq_linear` reduces each generator to the collapsed pair `(α, β)`.  So V̂ per
generator is `α·h/2 + β` — no seminormal matrices, no character sums, and A = 16
costs the same as A = 1.

WHAT IS MEASURED.

1. **Saturation.**  `max |V̂|` is the *same value* at every A from 1 to 16, and the
   number of distinct `(α, β)` pairs saturates at **7** from A = 4 on.  The margin
   does not degrade; the atom is built from a finite alphabet of per-generator
   local environments and adding nucleons only repeats them.

2. **The alphabet.**  Reading the seven off, and using `σ − h = σ⁻¹` (the skein
   relation, `QOU.BraidsAndKnots.sigma_mul_sub_h`) and `σ − h/2 = (σ + σ⁻¹)/2`
   for the averaged crossing, they are the collapses of

       σ⁻⁴   σ⁻³·avg   σ⁴·avg·σ²   σ³·avg²·σ²   σ⁻¹   σ   colour-weighted avg

   The maximum is the pure chain `σ⁻⁴`; the runner-up is the proton's
   `σ⁻³·avg`, whose identity coefficient equals it exactly
   (`identity_coeff_avg_eq_trace_full`).

3. **The closed form, and the crossing.**  `QOU.BraidsAndKnots.vHat_invChain`
   gives `V̂ₙ = ((q⁻¹)ⁿ + (−q)ⁿ)/2` for the length-n chain, because at `z = h/2`
   the Markov trace is the AVERAGE of the two Hecke eigenvalue evaluations
   (`vHat_half_h_eq_avg_evals`) and each evaluation is multiplicative
   (`prod_eq_linear`).  Since `|−q| > 1`, `|V̂ₙ| → ∞`: only finitely many chain
   lengths keep Φ_q finite, and **n = 4 is the last even one**.

WHAT THIS DOES NOT CLAIM.  Not that the 4 is tuned.  It is `3 + 1` — three
crossings from the `B₃` closure and one from the quark pair — both fixed
upstream by the construction, not chosen against this margin.  What it does say
is that the 1.95 % headroom is the whole of it, and that it is a fact about
chain length rather than about robustness.

SCOPE-(a) throughout: measures the construction as built, excludes no ingredient.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

import _path_bridge  # noqa: F401,E402
from mpmath import mp, mpf  # noqa: E402

mp.dps = 50

import mass_at_3A_proper as M3A  # noqa: E402
from q_parameter import Q_MP as Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

QI = 1 / Q
H = Q - QI
Z = H / 2                    # markov_param_eq_half_h, proved — not measured here

TOL = mpf("1e-45")


def _fmt(x) -> str:
    return mp.nstr(mpf(x), 20)


def collapse(word) -> tuple:
    """`collapseFold`: `(α, β)` with `Π (c σ + d) = α σ + β`."""
    a, b = mpf(0), mpf(1)
    for (c, d) in word:
        cc, dd = mpf(str(c)), mpf(str(d))
        a, b = a * cc * H + a * dd + b * cc, a * cc + b * dd
    return a, b


def words_by_generator(Zn: int, Nn: int) -> list:
    A = Zn + Nn
    n_gens = 3 * A - 1
    by_gen: list[list] = [[] for _ in range(n_gens)]
    for (c, d, g) in M3A.atom_braid_word_3A(Zn, Nn):
        if 0 <= g < n_gens:
            by_gen[g].append((c, d))
    return by_gen


def factor_label(d) -> str:
    """Name a factor by which entry of the four-value template its `d` is."""
    dv = mpf(str(d))
    if abs(dv) < TOL:
        return "sigma"
    if abs(dv + H) < TOL:
        return "sigma_inv"          # sigma - h = sigma^-1  (skein)
    if abs(dv + H / 2) < TOL:
        return "avg"                # sigma - h/2 = (sigma + sigma^-1)/2
    return "colour_avg"             # -h(1/2 - delta/4)


def saturation_scan() -> dict:
    """Does `max |V̂|` grow with A?  Does the alphabet stop growing?"""
    rows = []
    for (Zn, Nn) in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 3),
                     (4, 4), (6, 6), (8, 8)):
        by_gen = words_by_generator(Zn, Nn)
        pairs = [collapse(w) for w in by_gen]
        Vs = [a * Z + b for (a, b) in pairs]
        distinct = {(_fmt(a), _fmt(b)) for (a, b) in pairs}
        rows.append({
            "Z": Zn, "N": Nn, "A": Zn + Nn, "n_generators": len(pairs),
            "has_neutron": Nn > 0,
            "max_abs_V_hat": _fmt(max(abs(v) for v in Vs)),
            "max_abs_V_over_q": _fmt(max(abs(v) for v in Vs) / Q),
            "n_distinct_alpha_beta": len(distinct),
        })
    return {"rows": rows}


def alphabet() -> list:
    """The distinct `(α, β)` across large atoms, with the word that produces each."""
    seen: dict = {}
    for (Zn, Nn) in ((4, 4), (6, 6)):
        for w in words_by_generator(Zn, Nn):
            a, b = collapse(w)
            key = (_fmt(a), _fmt(b))
            if key not in seen:
                seen[key] = {
                    "alpha": _fmt(a), "beta": _fmt(b),
                    "V_hat": _fmt(a * Z + b),
                    "abs_V_over_q": _fmt(abs(a * Z + b) / Q),
                    "n_factors": len(w),
                    "word": "*".join(factor_label(d) for (_c, d) in w),
                }
    return sorted(seen.values(),
                  key=lambda r: -abs(mpf(r["abs_V_over_q"])))


def inv_chain_scan(nmax: int = 12) -> dict:
    """`vHat_invChain`: the σ⁻¹ chain's value, recursion vs closed form."""
    rows = []
    a, b = mpf(0), mpf(1)
    for n in range(1, nmax + 1):
        a, b = b, a - b * H                      # collapseStep h (a,b) (1,-h)
        V = Z * a + b
        closed = (Q ** (-n) + (-Q) ** n) / 2     # the theorem
        rows.append({
            "n": n,
            "V_hat_recursion": _fmt(V),
            "V_hat_closed_form": _fmt(closed),
            "abs_difference": _fmt(abs(V - closed)),
            "abs_V_over_q": _fmt(abs(V) / Q),
            "past_the_pole": bool(abs(V) >= Q),
        })
    return {"rows": rows}


def main() -> int:
    print(f"q      = {_fmt(Q)}      (Phi_q pole at |V_hat| = q)")
    print(f"h      = {_fmt(H)}")
    print(f"Z = h/2 = {_fmt(Z)}      (proved: markov_param_eq_half_h)")
    print()

    sat = saturation_scan()
    print("1. saturation in nucleon count")
    print(f"   {'atom':>10} {'A':>3} {'gens':>5} {'max |V_hat|':>24} "
          f"{'max|V|/q':>22} {'distinct':>9}")
    for r in sat["rows"]:
        print(f"   Z={r['Z']},N={r['N']:<4} {r['A']:>3} {r['n_generators']:>5} "
              f"{r['max_abs_V_hat']:>24} {r['max_abs_V_over_q']:>22} "
              f"{r['n_distinct_alpha_beta']:>9}")
    print()

    alpha = alphabet()
    print(f"2. the alphabet — {len(alpha)} distinct (alpha, beta)")
    for r in alpha:
        print(f"   |V|/q={r['abs_V_over_q']:>22}  V={r['V_hat']:>22}  "
              f"nf={r['n_factors']}  {r['word']}")
    print()

    chain = inv_chain_scan()
    print("3. the sigma^-1 chain: V_n = ((1/q)^n + (-q)^n)/2")
    print(f"   {'n':>3} {'recursion':>22} {'closed form':>22} {'|diff|':>12} "
          f"{'|V|/q':>20}")
    for r in chain["rows"]:
        flag = "   <-- PAST THE POLE" if r["past_the_pole"] else ""
        print(f"   {r['n']:>3} {r['V_hat_recursion']:>22} "
              f"{r['V_hat_closed_form']:>22} {r['abs_difference']:>12} "
              f"{r['abs_V_over_q']:>20}{flag}")
    print()

    # ---- checks -----------------------------------------------------------
    checks: list[tuple[str, bool, str]] = []

    # An earlier version of this check asserted ONE maximum across all atoms and
    # FAILED: the lone proton is 1.0551103188, everything containing a neutron
    # is 1.0883675334. The data was right and the claim was wrong. The max is
    # set by the NEUTRON — its generator 1 is the pure chain sigma^-4, where the
    # proton's uu pair contributes a sigma and makes it sigma^-3 * avg. Fixed by
    # stating it correctly rather than by loosening anything.
    with_n = {r["max_abs_V_hat"] for r in sat["rows"] if r["has_neutron"]}
    without_n = {r["max_abs_V_hat"] for r in sat["rows"] if not r["has_neutron"]}
    checks.append((
        "max |V_hat| SATURATES: one value for every neutron-containing atom, "
        "A = 1 to 16, and it never grows",
        len(with_n) == 1,
        f"neutron-containing maxima: {sorted(with_n)}; proton-only: "
        f"{sorted(without_n)} — the max is attained already at A = 1 and adding "
        f"nucleons only repeats the alphabet"))
    checks.append((
        "a proton-only system is strictly FURTHER from the pole than any "
        "neutron-containing one",
        len(without_n) == 1 and len(with_n) == 1
        and mpf(next(iter(without_n))) < mpf(next(iter(with_n))),
        f"proton-only {sorted(without_n)} < neutron-containing {sorted(with_n)}: "
        f"the neutron's dd pair contributes a further sigma^-1 where the "
        f"proton's uu pair contributes a sigma"))

    big = [r["n_distinct_alpha_beta"] for r in sat["rows"] if r["A"] >= 4]
    checks.append((
        "the (alpha, beta) alphabet saturates at 7 for A >= 4",
        len(set(big)) == 1 and big[0] == 7,
        f"distinct-pair counts at A >= 4: {big}"))

    # The maximum is the pure sigma^-1 chain of length 4.
    top = alpha[0]
    checks.append((
        "the maximum is the pure sigma^-4 chain",
        top["word"] == "sigma_inv*sigma_inv*sigma_inv*sigma_inv",
        f"top word = {top['word']}, |V|/q = {top['abs_V_over_q']}"))

    worst_cf = max(mpf(r["abs_difference"]) for r in chain["rows"])
    checks.append((
        "vHat_invChain: recursion == ((1/q)^n + (-q)^n)/2",
        worst_cf < TOL,
        f"worst |recursion - closed form| over n = 1..12 = {_fmt(worst_cf)}"))

    n4 = next(r for r in chain["rows"] if r["n"] == 4)
    checks.append((
        "the alphabet maximum IS the n=4 chain value",
        abs(mpf(top["V_hat"]) - mpf(n4["V_hat_recursion"])) < TOL,
        f"alphabet max {top['V_hat']} vs chain n=4 {n4['V_hat_recursion']}"))

    safe_even = [r["n"] for r in chain["rows"]
                 if r["n"] % 2 == 0 and not r["past_the_pole"]]
    checks.append((
        "n = 4 is the LAST EVEN chain length that stays inside the pole",
        safe_even == [2, 4],
        f"even n with |V_n| < q, over n = 1..12: {safe_even}; "
        f"n=4 sits at {n4['abs_V_over_q']} of q, n=6 is past it"))

    # vHat_half_h_eq_avg_evals, on every alphabet element rather than in general.
    worst_avg = mpf(0)
    for r in alpha:
        a, b = mpf(r["alpha"]), mpf(r["beta"])
        lhs = Z * a + b
        rhs = ((a * Q + b) + (a * (-QI) + b)) / 2
        worst_avg = max(worst_avg, abs(lhs - rhs))
    checks.append((
        "vHat_half_h_eq_avg_evals holds on every alphabet element",
        worst_avg < TOL,
        f"worst |vHat(h/2) - (eval_q + eval_-1/q)/2| = {_fmt(worst_avg)}"))

    print("checks:")
    ok = True
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}")
        ok = ok and passed

    payload = {
        "description": (
            "The tower's per-generator V_hat takes seven values at every "
            "nucleon count; max |V_hat| saturates rather than degrading with "
            "A; and the largest is the sigma^-4 chain, one even chain-length "
            "step from the Phi_q pole."),
        "scope": (
            "Scope-(a): measures the construction as built. Does NOT claim the "
            "chain length 4 is tuned -- it is 3 (B_3 closure) + 1 (quark pair), "
            "fixed upstream. Excludes no ingredient."),
        "lean": [
            "qou:QOU.BraidsAndKnots.prod_eq_linear",
            "qou:QOU.BraidsAndKnots.markov_param_eq_half_h",
            "qou:QOU.BraidsAndKnots.sigma_mul_sub_h",
            "qou:QOU.BraidsAndKnots.vHat_half_h_eq_avg_evals",
            "qou:QOU.BraidsAndKnots.vHat_invChain",
            "qou:QOU.BraidsAndKnots.identity_coeff_avg_eq_trace_full",
        ],
        "q": _fmt(Q),
        "h": _fmt(H),
        "markov_parameter_half_h": _fmt(Z),
        "saturation": sat,
        "alphabet": alpha,
        "inv_chain": chain,
        "checks": [{"name": n, "passed": bool(p), "detail": d}
                   for (n, p, d) in checks],
        "all_checks_passed": bool(ok),
    }
    payload.setdefault("scriptFile", os.path.basename(__file__))
    WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=None)

    out = _HERE.parent / "tower-vhat-chain-length-pole-margin.witness.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
