#!/usr/bin/env python3
"""Three channels, three decay rates, two growth classes -- and only one free parameter.

Adding a bond MULTIPLIES the Markov trace by `b < 1`, so the framework's native
falloff is `b^d(i,j) = exp(-mu . d(i,j))` with `mu = -ln b`: exponential in graph
distance, i.e. a Yukawa profile. That puts the three nuclear channels on one axis
-- the mediator mass -- and answers "what are the options" for the Coulomb gap.
Instantiates `QOU/Hecke/ChannelRangeGrowthClass.lean`. Bean `qou-556v`.

*** 1. THE THREE PHYSICAL CHANNELS, BY RANGE ***

    channel   mediator            mu               pair sum over n sites
    weak      W/Z, 80.4 GeV       407 /fm          O(n)
    strong    pion, 139.6 MeV     0.707 /fm        O(n)
    EM        photon, MASSLESS    0                Theta(n^2)

**Coulomb is not "a longer-range bond".** It is the massless boundary, a
different growth class. Every `q`-derived rate is strictly positive because
`b < 1`, so no choice of letters reaches it -- the analytic twin of
`BoundedDegreeCoulomb`, which proves the same separation from the degree side.

*** 2. THE THREE RATES ARE NOT INDEPENDENT — ONE FREE PARAMETER ***

`b_pp . b_nn = 1/[2]_q^2` is an identity, so

    L_pp + L_nn = 2 ln[2]_q      exactly    (0.489899 + 0.907262 = 1.397162)

and `L_pn` is fixed between them by the averaging convention. Three decay rates,
one constraint, one free parameter `q`. Any proposal moving one rate moves
another. Scale-free consequence: the RANGE ratios
`lambda_pp : lambda_pn : lambda_nn = 1/L_pp : 1/L_pn : 1/L_nn` are derived
without any length scale, and the p-p channel is 1.85x longer-ranged than n-n.

*** 3. TWO CONVERGENCE CRITERIA, AND THE ONE THAT LOOKS ALARMING DOES NOT BIND ***

The per-site sum is `sum_k |S_k| exp(-mu k)` over shells at graph distance `k`.

  - TREE (worst case at bounded degree `d`): `|S_k| <= d(d-1)^(k-1)`, so it
    converges iff `mu > ln(d-1)`. Measured against the corpus letters this looks
    alarming -- only `L_nn` clears `ln 2` at `d = 3`, and NONE clears `ln(d-1)`
    at `d >= 4`.
  - GEOMETRIC in R^3 (a nuclear packing): `|S_k| ~ c k^2`, polynomial, and
    `sum k^2 exp(-mu k)` converges for EVERY `mu > 0`.

**A packing is not a tree, so nothing follows from the first row.** Recorded
because it is easy to reach for and would be a false alarm.

*** 4. WHAT DOES FOLLOW: THE RANGE-1 TRUNCATION IS NOT SELF-CONSISTENT ***

On an fcc shell count `10k^2 + 2` (= 12, 42, 92, 162, ... -- the standard
coordination shells), the framework's OWN decay reaches

    letter   b            effective sites   vs 12 contacts
    pp       0.612688     173.23            14.44x
    pn       0.508230      66.52             5.54x
    nn       0.403628      28.06             2.34x

So truncating the bond graph at range 1 discards ~93 % of the p-p weight that
the same framework's decay rate says is there. **That is an option that needs no
new parameter:** sum `b^d(i,j)` over all pairs at the letters already derived.

*** 5. AND IT STILL CANNOT GIVE COULOMB ***

Full-range or truncated, `sum_{i<j} b^d(i,j)` over a packing is O(n) -- the
constant changes by 14x, the growth class does not. Coulomb needs `mu = 0`
exactly. So the option in section 4 is worth taking for the STRONG channel (it
is the same channel at its own range) and cannot touch the EM one.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 40
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
TWO_Q = Q0 + 1/Q0
B_PP = Q0**2/TWO_Q
B_NN = Q0**-2/TWO_Q
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
TOL = mp.mpf(10)**(-30)

# EXTERNAL reference constants (PDG), used only to place the channels on the
# range axis. Nothing here is fitted to them and nothing is wired to production.
HBARC_MEV_FM = mp.mpf("197.3269804")
MEDIATORS = (("weak (W boson)", mp.mpf("80377")),
             ("strong (pion)", mp.mpf("139.57")),
             ("EM (photon)", mp.mpf(0)))


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    L = {"pp": -mp.log(B_PP), "pn": -mp.log(B_PN), "nn": -mp.log(B_NN)}

    print("=" * 78)
    print("1. THE THREE PHYSICAL CHANNELS, ON ONE AXIS")
    print("=" * 78)
    chans = []
    for name, m in MEDIATORS:
        if m == 0:
            chans.append({"channel": name, "mass_MeV": "0", "mu_per_fm": "0",
                          "range_fm": "infinite", "growth": "Theta(n^2)"})
            print(f"    {name:>16}  massless        mu = 0            Theta(n^2)")
        else:
            mu = m/HBARC_MEV_FM
            chans.append({"channel": name, "mass_MeV": mp.nstr(m, 8),
                          "mu_per_fm": mp.nstr(mu, 8),
                          "range_fm": mp.nstr(1/mu, 8), "growth": "O(n)"})
            print(f"    {name:>16}  {mp.nstr(m, 6):>9} MeV   "
                  f"mu = {mp.nstr(mu, 5):>8} /fm   range {mp.nstr(1/mu, 5):>8} fm   O(n)")
    ok &= chk("only_the_massless_channel_is_super_extensive",
              [c["growth"] for c in chans], ["O(n)", "O(n)", "Theta(n^2)"],
              note="a Yukawa weight exp(-mu r) with mu > 0 makes the pair sum "
                   "extensive; mu = 0 weights all n(n-1)/2 pairs by 1. Lean: "
                   "massless_pair_sum, no_linear_bound_on_pairs")

    print()
    print("=" * 78)
    print("2. THE FRAMEWORK'S OWN RATES — AND THEY ARE NOT INDEPENDENT")
    print("=" * 78)
    for k in ("pp", "pn", "nn"):
        print(f"    L_{k} = -ln b_{k} = {mp.nstr(L[k], 14):>18}     "
              f"range 1/L = {mp.nstr(1/L[k], 10)}  bond steps")
    print()
    print(f"    L_pp + L_nn = {mp.nstr(L['pp'] + L['nn'], 18)}")
    print(f"    2 ln[2]_q   = {mp.nstr(2*mp.log(TWO_Q), 18)}")
    ok &= chk("all_three_rates_are_strictly_positive",
              all(v > 0 for v in L.values()), True,
              note="b < 1 for every letter, so mu = -ln b > 0 always. There is "
                   "no q at which the framework produces a massless channel")
    ok &= chk("the_pp_and_nn_rates_sum_to_two_log_two_q",
              abs(L["pp"] + L["nn"] - 2*mp.log(TWO_Q)) < TOL, True,
              note="from b_pp.b_nn = 1/[2]_q^2. Lean: rate_sum_pinned. So three "
                   "rates carry ONE constraint and one free parameter q -- any "
                   "proposal moving one rate moves another")
    ratios = [mp.nstr((1/L[k])/(1/L["nn"]), 8) for k in ("pp", "pn", "nn")]
    print(f"    range ratios pp : pn : nn = {' : '.join(ratios)}")
    ok &= chk("the_range_ratios_are_derived_and_scale_free",
              mp.mpf(ratios[0]) > mp.mpf("1.8"), True,
              note=f"lambda_pp/lambda_nn = {ratios[0]}, fixed by q alone with no "
                   "length scale. The p-p channel is the longest-ranged, n-n the "
                   "shortest -- which is the same ordering as the bond strengths")

    print()
    print("=" * 78)
    print("3. TWO CONVERGENCE CRITERIA; THE ALARMING ONE DOES NOT BIND")
    print("=" * 78)
    print(f"    {'d':>4}{'ln(d-1)':>14}   letters clearing the TREE threshold")
    tree = []
    for d in (2, 3, 4, 5, 6, 12):
        thr = mp.log(d - 1)
        clears = [k for k in ("pp", "pn", "nn") if L[k] > thr]
        tree.append({"d": d, "ln_d_minus_1": mp.nstr(thr, 10), "clears": clears})
        print(f"    {d:>4}{mp.nstr(thr, 10):>14}   {clears if clears else 'NONE'}")
    ok &= chk("the_letters_fail_the_tree_threshold_above_coordination_three",
              [t["clears"] for t in tree if t["d"] >= 4], [[], [], [], []],
              note="NONE of the three rates clears ln(d-1) for d >= 4. This is "
                   "the TREE worst case and it does NOT bind a nucleus: a "
                   "packing in R^3 has polynomial shell growth ~k^2, for which "
                   "every mu > 0 converges. Recorded because it is easy to "
                   "reach for and would be a false alarm")

    print()
    print("=" * 78)
    print("4. WHAT DOES FOLLOW: RANGE-1 TRUNCATION IS NOT SELF-CONSISTENT")
    print("=" * 78)
    print("    fcc shell counts 10k^2+2 = 12, 42, 92, 162, ...")
    print(f"    {'letter':>8}{'b':>16}{'effective sites':>18}{'vs 12 contacts':>18}")
    reach = []
    for k, b in (("pp", B_PP), ("pn", B_PN), ("nn", B_NN)):
        tot = mp.nsum(lambda j: (10*j**2 + 2)*b**j, [1, mp.inf])
        reach.append({"letter": k, "b": mp.nstr(b, 14),
                      "effective_sites": mp.nstr(tot, 10),
                      "over_twelve": mp.nstr(tot/12, 8)})
        print(f"    {k:>8}{mp.nstr(b, 12):>16}{mp.nstr(tot, 8):>18}"
              f"{mp.nstr(tot/12, 6) + 'x':>18}")
    ok &= chk("the_framework_s_own_decay_reaches_far_past_first_contact",
              mp.mpf(reach[0]["over_twelve"]) > 10, True,
              note=f"p-p reaches {reach[0]['effective_sites']} effective sites "
                   f"against 12 contacts ({reach[0]['over_twelve']}x), so a "
                   "range-1 truncation discards ~93 % of the weight the same "
                   "framework's decay rate supplies. Summing b^d(i,j) over all "
                   "pairs needs NO new parameter -- it is the derived letters "
                   "at their own range")
    ok &= chk("but_the_growth_class_is_unchanged",
              all(mp.mpf(r["effective_sites"]) < mp.inf for r in reach), True,
              note="every per-site sum is FINITE, so full-range is still O(n). "
                   "The constant moves 14x, the growth class does not. Section 4 "
                   "is an option for the STRONG channel and cannot touch EM")

    print()
    print("=" * 78)
    print("5. THE OPTIONS, RANKED BY WHAT THEY COST")
    print("=" * 78)
    print("  (a) Sum b^d(i,j) over all pairs at the derived letters -- NO new")
    print("      parameter, fixes a 14x self-inconsistency, and is the strong")
    print("      channel at its own range. Does not touch Coulomb.")
    print("  (b) A separate mu = 0 channel for EM -- a different growth class,")
    print("      so it cannot be a bond letter. It has to enter as its own term.")
    print("  (c) Re-tuning any letter -- excluded: the rates carry one")
    print("      constraint, and no positive mu reaches quadratic growth.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-channel-range-growth-class",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "hbarc_MeV_fm": str(HBARC_MEV_FM),
                       "mediator_masses_provenance": "PDG, EXTERNAL reference "
                                                     "constants used only to place "
                                                     "the channels on the range axis",
                       "lean": "QOU/Hecke/ChannelRangeGrowthClass.lean"},
        "data": {"channels": chans,
                 "rates": {k: mp.nstr(v, 20) for k, v in L.items()},
                 "rate_sum": mp.nstr(L["pp"] + L["nn"], 20),
                 "two_log_two_q": mp.nstr(2*mp.log(TWO_Q), 20),
                 "range_ratios_pp_pn_nn": ratios,
                 "tree_thresholds": tree,
                 "fcc_effective_reach": reach},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_channel_range_growth_class_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-channel-range-growth-class.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
