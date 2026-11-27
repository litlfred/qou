#!/usr/bin/env python3
"""On three strands the gamma-gamma ruling leaves ONE INTEGER of freedom -- and
the one value the corpus derives misses Q_beta by 440 %, while the values that
match are selected. Scope-(a), and the point of the probe is the second clause.

## Why this probe exists

`qbeta_altchar_is_a_shift_multiset_invariant_probe` (PR #7295) closed the
negative half: no census reading is gamma-gamma-produced, and no re-ordering
can make one. The obvious next question is the POSITIVE half -- what a
gamma-gamma-DERIVED word could be instead -- and on three strands it barely
needs a search.

`H_3(q)` has **two** Artin generators. A pair-production vertex is
`sigma_i sigma_{i+1}^{-1}`, so it needs generators `i` and `i+1`, so `i + 1 <
2`, so `i = 0`. **The only vertex available is `sigma_0 sigma_1^{-1}`, and every
gamma-gamma word on three strands is one of its powers.** The gamma-gamma
admissible subset of `H_3` is a cyclic monoid on one generator, indexed by a
single natural number `k`. Formalised sorry-free as
`QOU.Mass.AltCharShiftMultiset.gammaGamma_threeStrand`; `k = 3` is `borromean`.

## Two structural findings

**1. The `e^-` coordinate vanishes for every `k`** (CHECK 3, k = 0..24). This
matters because `qbeta-counit-closed-form.md` asserts that the coordinate sum
and `tr_M|_{z=1}` coincide "on elements whose `e^-` coordinate vanishes, which
both nucleon models **happen to satisfy**". Under gamma-gamma production it is
not a happy accident -- it is forced. CHECK 4 then closes the consequence
exactly: `tr_M|_{z=1} - net = h * nf[e^-]`, so the two agree on every
gamma-gamma word and the retired `z = 1` cell equals the net there.

**2. The family's trace is bounded and sweeps the MeV range in three bands.**
`tr_M^{z_D}(core^k)` cycles by `k mod 3`: the `k = 0` band descends 4.2275 ->
3.6483 MeV (as `|tr|*E_0`), the `k = 1` band descends 1.0454 -> 0.2896, the
`k = 2` band ascends 1.1845 -> 2.5800, over `k <= 24`.

## 🛑 The anti-fit finding, which is the actual result

The `k = 1 (mod 3)` band descends MONOTONICALLY **straight through** the
`Q_beta` target, bracketing it between `k = 7` (0.78710 MeV, +0.610 %) and
`k = 10` (0.66933, -14.4 %). And the corpus's actual shape is a DIFFERENCE,
`Delta = n - p`, which over `k, l <= 24` is a grid of 300 unordered pairs
spanning [0.0061, 3.9378] MeV.

Measured, because "it would match anything" is a claim and not a licence:

    single-k band   spacing near target  15.05 %   best  k = 7      +0.610 %
    difference grid spacing near target   1.29 %   best (k,l)=(8,23) +0.455 %
                    pairs within 1 % of Q_beta: 2 ;  within 5 %: 7

**A grid of spacing `s` lands a best residual of about `s/4` by chance.** For
the difference grid that is 0.32 %, against an observed 0.455 % -- the best
match is **not even better than chance**. For the single-k band it is 3.8 %
against 0.610 %, roughly a 1-in-12 coincidence: notable, and still not
evidence. Either way the residual carries no information at this precision, and
picking `k` (or `(k, l)`) because its number is good is exactly the "selection
against the target" that AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" forbids --
*"no continuous parameter is tuned and it is still a fit"*.

**The one member the corpus DERIVES is `k = 3`**, the Borromean baryon: three
pair-production events, named in `GammaGammaWordSelection.borromean` and not
chosen against any number. It gives `|tr_M^{z_D}(core^3)| * E_0 = 4.22140` MeV
against `Q_beta = 0.78233`: **+439.6 %** (CHECK 5). That is the honest figure
for the gamma-gamma route as a single-word `Q_beta` carrier on three strands,
and it is reported because a documented miss is a result while a selected match
is not.

## Scope

**Scope-(a)**: this construction, alone, on three strands, does not reproduce
`Q_beta`. It is NOT a structural exclusion -- no invariant here forbids the
gamma-gamma route. What it excludes is a *method*: selecting `k` by residual.
Three things it does not touch: `H_4` and above, where more vertices exist and
the one-integer collapse does not apply; a word mixing gamma-gamma vertices
with other letters; and any route that derives `k` from something other than
the residual, which is precisely what is missing.

This probe selects nothing, wires nothing, and moves no number in the corpus.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "computations/qbeta",
           "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import Q_BETA_MEV  # noqa: E402
import qbeta_e0  # noqa: E402

# Constructors and the GB reduction table come from the census probe, never
# re-transcribed.
_SRC = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _SRC)
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)

hm = _census.hm
h = _census.h
BASIS = _census.BASIS

set_compute_dps(60)

ZERO, ONE = sp.Integer(0), sp.Integer(1)
z = sp.Symbol("z")

#: exact proton pin, as a Rational -- no float64 anywhere in this file
Q0 = Q_MP
H0 = Q0 - 1 / Q0
#: the convention-D Markov parameter
ZD = Q0 ** 3 / (Q0 ** 2 + 1)
#: canonical (tower-summed) E_0, from the corpus producer -- not re-derived
E0 = qbeta_e0.canonical()
QB = mp.mpf(str(Q_BETA_MEV))

#: how far the family is enumerated. Stated, because every density figure
#: below is a function of it.
KMAX = 24

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def core(k: int):
    """`(sigma_0 sigma_1^{-1})^k` in normal form, symbolic in `h`."""
    nf = [ONE] + [ZERO] * 5
    for _ in range(k):
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h, 1)
    return nf


def num(nf):
    """Exact `h -> h(q_0)` substitution at 45 dps. No float64."""
    return [mp.mpf(str(sp.N(sp.sympify(x).subs(h, H0), 45))) for x in nf]


def tr_zD(v):
    """Markov trace at `z_D`, with TR = [1, z, z, z^2, z^2, z(hz+1)]."""
    TR = [mp.mpf(1), ZD, ZD, ZD ** 2, ZD ** 2, ZD * (H0 * ZD + 1)]
    return sum(v[i] * TR[i] for i in range(6))


def alt_char_of_nf(nf):
    """Alternating character by linearity: basis characters [1,S,S,S^2,S^2,S^3]
    with S = -1/q. Same contraction as the sibling probe in #7295."""
    S = -1 / Q0
    BC = [mp.mpf(1), S, S, S ** 2, S ** 2, S ** 3]
    v = num(nf)
    return sum(v[i] * BC[i] for i in range(6))


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-admissible-family-h3")
    w.set_description(
        "On three strands the only gamma-gamma vertex is sigma_0 sigma_1^{-1}, "
        "so every gamma-gamma word is (sigma_0 sigma_1^{-1})^k -- one integer "
        "of freedom. Every member has a vanishing e^- coordinate (so the "
        "counit block's 'happen to satisfy' is forced, not accidental). The "
        "derived member k=3 (borromean) misses Q_beta by +439.6 %; the members "
        "that match are selected, and the difference grid's best residual "
        "(0.455 %) is not even better than the 0.32 % expected by chance from "
        "its own 1.29 % spacing. Scope-(a): it excludes a METHOD (selecting k "
        "by residual), not the gamma-gamma route."
    )

    print("Assertions (exact symbolic in Q(h); readouts at the proton q_0):")

    # ---------------------------------------------------------------- CHECK 1
    # The hypothesis of the Lean theorem, calibrated against the corpus object:
    # the NF basis has 3! = 6 elements, so this is H_3, so there are 2 Artin
    # generators, so `vertex i` needs i + 1 < 2, so i = 0.
    check("nf_basis_is_six_so_h3_has_two_generators",
          len(BASIS) == 6 == sp.factorial(3),
          f"|NF basis| = {len(BASIS)} = 3! -- H_3, two Artin generators, so a "
          f"vertex sigma_i sigma_{{i+1}}^-1 needs i+1 < 2, i.e. i = 0. "
          f"Formalised as gammaGamma_threeStrand (sorry-free)", w)

    NFS = [core(k) for k in range(KMAX + 1)]

    # ---------------------------------------------------------------- CHECK 2
    # Calibration against altChar_eq_one: every member must have character 1.
    ac = [alt_char_of_nf(nf) for nf in NFS]
    worst = max(abs(a - 1) for a in ac)
    check("family_alternating_character_is_one",
          worst < mp.mpf("1e-40"),
          f"k = 0..{KMAX}; max |altChar - 1| = {mp.nstr(worst, 6)} -- the "
          f"positive control for altChar_eq_one (sorry-free)", w)

    # ---------------------------------------------------------------- CHECK 3
    # The structural finding.
    e5 = [sp.simplify(sp.expand(nf[5])) for nf in NFS]
    check("family_e_minus_coordinate_vanishes",
          all(x == 0 for x in e5),
          f"nf[e^-] == 0 exactly, symbolically in h, for every k = 0..{KMAX}. "
          f"`qbeta-counit-closed-form.md` calls this something the nucleon "
          f"models 'happen to satisfy'; under gamma-gamma it is forced", w)

    # ---------------------------------------------------------------- CHECK 4
    # And its exact consequence, symbolically rather than at the pin.
    diffs = []
    for nf in NFS:
        TRs = [ONE, z, z, z ** 2, z ** 2, z * (h * z + 1)]
        tr1 = sp.expand(sum(nf[i] * TRs[i] for i in range(6)).subs(z, 1))
        net = sp.expand(sum(nf))
        diffs.append(sp.simplify(tr1 - net - h * nf[5]))
    check("e_minus_vanishing_forces_net_eq_z1_trace",
          all(d == 0 for d in diffs) and all(x == 0 for x in e5),
          f"tr_M|_{{z=1}} - net = h * nf[e^-] identically (residual 0 for all "
          f"k = 0..{KMAX}), and nf[e^-] = 0, so net and the retired z = 1 cell "
          f"COINCIDE on every gamma-gamma word", w)

    # ---------------------------------------------------------------- CHECK 5
    # The honest derived number.
    V = [num(nf) for nf in NFS]
    pred = [abs(tr_zD(v)) * E0 for v in V]
    err = [(p / QB - 1) * 100 for p in pred]
    check("derived_member_k3_is_borromean_and_misses_by_440_pct",
          abs(err[3] - mp.mpf("439.6")) < mp.mpf("0.5"),
          f"k = 3 is `GammaGammaWordSelection.borromean` -- three "
          f"pair-production events, derived, not chosen against a number. "
          f"|tr_M^zD(core^3)|*E0 = {mp.nstr(pred[3], 12)} MeV against "
          f"Q_beta = {mp.nstr(QB, 10)} MeV: {mp.nstr(err[3], 6)} %", w)

    # ---------------------------------------------------------------- CHECK 6
    # The band structure, and that it sweeps THROUGH the target.
    band1 = [(k, pred[k]) for k in range(KMAX + 1) if k % 3 == 1]
    desc = all(band1[i][1] > band1[i + 1][1] for i in range(len(band1) - 1))
    brackets = any(band1[i][1] > QB > band1[i + 1][1]
                   for i in range(len(band1) - 1))
    check("k_mod_3_eq_1_band_descends_monotonically_through_the_target",
          desc and brackets,
          f"band k = 1,4,...,{band1[-1][0]}: "
          f"{[mp.nstr(v, 7) for _k, v in band1]} MeV -- strictly decreasing "
          f"and it brackets Q_beta between k = 7 and k = 10. A monotone sweep "
          f"through a target always has a nearest member", w)

    # ---------------------------------------------------------------- CHECK 7
    # The anti-fit measurement. The falsifiable content is the BRACKETING: if
    # the grid straddles the target, a close member is produced by density and
    # not by the physics.
    pairs = {}
    for k in range(KMAX + 1):
        for l in range(k + 1, KMAX + 1):
            pairs[(k, l)] = abs(
                (tr_zD(V[k]) - tr_zD(V[l]))) * E0
    vals = sorted(pairs.values())
    j = min(range(len(vals)), key=lambda t: abs(vals[t] - QB))
    gaps = [vals[j] - vals[j - 1] if j > 0 else None,
            vals[j + 1] - vals[j] if j + 1 < len(vals) else None]
    spacing = min(g for g in gaps if g is not None)
    best_pair = min(pairs.items(), key=lambda kv: abs(kv[1] - QB))
    best_pct = (best_pair[1] / QB - 1) * 100
    spacing_pct = spacing / QB * 100
    expected_pct = spacing_pct / 4          # a grid of spacing s misses by ~s/4
    n1 = sum(1 for v in vals if abs(v / QB - 1) < mp.mpf("0.01"))
    n5 = sum(1 for v in vals if abs(v / QB - 1) < mp.mpf("0.05"))
    straddles = vals[0] < QB < vals[-1]
    check("difference_grid_straddles_the_target_so_a_match_is_density",
          straddles and abs(best_pct) > expected_pct / 4,
          f"{len(vals)} unordered pairs over k,l <= {KMAX}, spanning "
          f"[{mp.nstr(vals[0], 6)}, {mp.nstr(vals[-1], 6)}] MeV and straddling "
          f"Q_beta. Local spacing {mp.nstr(spacing_pct, 6)} %; best "
          f"(k,l) = {best_pair[0]} at {mp.nstr(best_pct, 6)} %; a grid of that "
          f"spacing misses by ~{mp.nstr(expected_pct, 6)} % BY CHANCE, so the "
          f"best match is not better than chance. Within 1 %: {n1}; "
          f"within 5 %: {n5}", w)

    # ------------------------------------------------------------------ data
    w.add_data("family", [
        {"k": k, "e_minus": str(e5[k]),
         "alt_char": mp.nstr(ac[k], 20),
         "tr_M_zD": mp.nstr(tr_zD(V[k]), 20),
         "pred_MeV": mp.nstr(pred[k], 20),
         "err_pct_vs_Q_beta": mp.nstr(err[k], 10),
         "is_derived_by_the_corpus": k == 3}
        for k in range(KMAX + 1)])
    w.add_data("derived_member", {
        "k": 3, "name": "borromean, (sigma_0 sigma_1^-1)^3",
        "why_derived": "three pair-production events; "
                       "GammaGammaWordSelection.borromean, not selected "
                       "against any number",
        "pred_MeV": mp.nstr(pred[3], 20),
        "err_pct": mp.nstr(err[3], 10)})
    w.add_data("selection_is_forbidden", {
        "single_k_band_spacing_pct": mp.nstr(
            min(abs(band1[i][1] - band1[i + 1][1]) / QB * 100
                for i in range(len(band1) - 1)), 8),
        "single_k_best": {"k": min(band1, key=lambda kv: abs(kv[1] - QB))[0],
                          "err_pct": mp.nstr(min((abs(v / QB - 1) * 100)
                                                 for _k, v in band1), 8)},
        "difference_grid_spacing_pct": mp.nstr(spacing_pct, 8),
        "difference_grid_best": {"pair": list(best_pair[0]),
                                 "err_pct": mp.nstr(best_pct, 8)},
        "expected_best_by_chance_pct": mp.nstr(expected_pct, 8),
        "pairs_within_1_pct": n1, "pairs_within_5_pct": n5,
        "verdict": "the residual carries no information at this precision; "
                   "choosing k or (k,l) by it is selection against the target "
                   "(AGENTS.md NO FITTING) and is forbidden",
        "k_max_enumerated": KMAX})
    w.add_data("scope", "a")
    w.add_data("what_this_does_not_exclude", [
        "H_4 and above, where more vertices exist and the one-integer "
        "collapse does not apply",
        "a word mixing gamma-gamma vertices with other letters",
        "any route that DERIVES k from something other than the residual -- "
        "which is exactly what is missing",
    ])
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("E0_MeV", mp.nstr(E0, 20))
    w.add_data("E0_form", "tower_summed (canonical, qbeta_e0.canonical)")
    w.add_data("Q_beta_MeV", mp.nstr(QB, 20))

    print()
    print(f"  E0 = {mp.nstr(E0, 12)} MeV (tower-summed),  "
          f"Q_beta = {mp.nstr(QB, 10)} MeV")
    print(f"  {'k':>3s} {'mod3':>5s} {'tr_M^zD':>18s} {'|tr|*E0 MeV':>16s} "
          f"{'err %':>12s}")
    for k in range(KMAX + 1):
        mark = "   <- DERIVED (borromean)" if k == 3 else ""
        print(f"  {k:3d} {k % 3:5d} {mp.nstr(tr_zD(V[k]), 14):>18s} "
              f"{mp.nstr(pred[k], 12):>16s} {mp.nstr(err[k], 8):>12s}{mark}")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
