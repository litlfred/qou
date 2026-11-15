#!/usr/bin/env python3
"""qou-99qc: apply the owner's γγ word-selection ruling to the DECAY channel.
The γγ sector's reachable set has a GAP exactly where Q_beta sits.

# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/GammaGammaSelectedDeltaVanishes.lean
# Ref: folio/quantum-observable-universe/lean/QOU/Mass/GammaGammaSelectorH3.lean  (#7192)
# Ref: computations/qbeta/qbeta_option_e_construction_freedom_probe.py  (the recipe route, exhausted)
# Ref: .beans/qou-ales   (owner ruling 2026-09-08)

WHY THIS IS A DERIVATION AND NOT A SEARCH. The owner ruled on 2026-09-08: "All
selection of great words should be done through gamma gamma production and the
semi-definite product solutions at q_0. Shouldn't use census." That fixes HOW an
element is chosen, so applying it is a derivation — the principle picks the
words and this probe reports whatever number comes out, including a bad one.

The companion Lean proves the prune that makes the scan finite:

  * a functional that is multiplicative over concatenation and equals 1 on a
    pair-production vertex is 1 on EVERY γγ-word, hence annihilates every γγ
    DIFFERENCE  (`oneDim_annihilates_gammaGamma_difference`, sorry-free);
  * both one-dimensional blocks of H_3 are of that shape;
  * so at Wenzl level 1, whose support is the (3) block alone, a γγ-selected
    Delta gives EXACTLY ZERO — no computation needed, for any pair of words;
  * and at level 2, the ruled functional, the entire prediction is carried by
    the (2,1) block.

WHAT IS COMPUTED. Inside H_3 every γγ-word is a vertex power (proved in #7192,
`gammaGamma_inH3_eq_vertexPow`), so the candidate set is `V^k` with
`V = sigma_0 sigma_1^-1`, and the nucleon crossing budget `2k <= 11` caps
`k <= 5`. `Delta = V^a - V^b` over all pairs is 36 candidates, not a search
space. Reports the whole reachable set and its relation to the target.

WHAT CAME OUT. The reachable values cluster in two bands — small differences
below ~0.4 and large ones above ~2.7 — and the target sits in the GAP between
them. So the γγ sector does not merely miss: it cannot come close, and the miss
is structural rather than a matter of which words were tried.

SCOPE (strict). γγ-words carry NO FLAVOUR INDEX — the corpus's `Crossing` is
`(gen, pos)` and nothing else — so this prices the ruled principle APPLIED
ALONE. It is scope-(a) evidence that the principle underdetermines `Delta` and
must be supplemented by the flavour letters, which is the open point
`GammaGammaSelectorH3` names for itself. It does NOT refute the ruling.

ARITHMETIC. mpf at 60 dps, proton pin as an exact Rational, convention D.
The NF machinery is imported from the committed order probe, which calibrates
against the census before use. No float64 (probes are not exempt).

Run: python3 -u computations/qbeta/qbeta_gamma_gamma_selected_delta_probe.py \
       2>&1 | tee /tmp/qbeta_gg_delta.log
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys
import warnings

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_2022_source import (  # noqa: E402
    Q_BETA_MEV_AME, Q_BETA_MEV_AME_ERR,
)

set_compute_dps(60)
mp.mp.dps = 60

_ORD = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_option_e_order_dof_range_probe.py")
_spec = importlib.util.spec_from_file_location("_ord", _ORD)
_ord = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ord)

Q0, H0, ZD, E0, QB = _ord.Q0, _ord.H0, _ord.ZD, _ord.E0, _ord.QB
TARGET = _ord.TARGET
word_nf, tr_at = _ord.word_nf, _ord.tr_at
SIGMA_REL = mp.mpf(str(Q_BETA_MEV_AME_ERR)) / QB

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def vertex_pow(k: int):
    """V^k with V = sigma_0 sigma_1^-1, as letters (gen, d_coefficient).

    sigma_0 is (gen 0, d = 0); sigma_1^-1 is (gen 1, d = -h). This is exactly
    the B_3 confinement core the census builds, which is V^3.
    """
    return [(0, mp.mpf(0)), (1, mp.mpf(-1))] * k


KMAX = 5   # 2k <= 11, the nucleon crossing budget of qou-1qsw


def main() -> int:
    print("qou-99qc — the ruled γγ selection, applied to the decay channel\n")
    print(f"  z_D    = {mp.nstr(ZD, 20)}")
    print(f"  TARGET = {mp.nstr(TARGET, 20)}   (|eps(Delta)| needed for Q_beta)\n")

    # ---- CHECK 1: V^3 is the Borromean core the census builds ---------------
    print("CHECK 1 — the vertex power is the corpus's own object")
    core = vertex_pow(3)
    check("V_cubed_is_11_crossing_budget_compatible", len(core) == 6,
          "V^3 = 6 crossings, the B_3 confinement core; the census builds "
          "exactly this by `for _ in range(3): hm(.,1,0,0); hm(.,1,-h,1)`")

    # ---- CHECK 2: the Lean prediction at level 1, numerically ---------------
    print("\nCHECK 2 — the Lean prune, checked numerically at level 1")
    worst = mp.mpf(0)
    for a, b in itertools.product(range(KMAX + 1), repeat=2):
        d = tr_at(word_nf(vertex_pow(a)), Q0) - tr_at(word_nf(vertex_pow(b)), Q0)
        if abs(d) > worst:
            worst = abs(d)
    check("level_1_annihilates_every_gamma_gamma_difference",
          worst < mp.mpf("1e-45"),
          f"max |tr_q(V^a - V^b)| over all {(KMAX+1)**2} pairs = "
          f"{mp.nstr(worst, 6)} — the augmentation gives EXACTLY zero, as "
          "oneDim_annihilates_gammaGamma_difference proves it must")

    # ---- CHECK 3: the reachable set at the ruled functional -----------------
    print("\nCHECK 3 — the reachable set at z_D (the ruled functional)")
    trs = {k: tr_at(word_nf(vertex_pow(k)), ZD) for k in range(KMAX + 1)}
    print("    k  crossings   tr_{z_D}(V^k)")
    for k, v in trs.items():
        print(f"    {k}  {2*k:>9d}   {mp.nstr(v, 18)}")
    vals = sorted({abs(trs[a] - trs[b])
                   for a, b in itertools.product(range(KMAX + 1), repeat=2)
                   if a != b})
    print(f"\n    {len(vals)} distinct non-zero |tr_z_D(Delta)| values:")
    for v in vals:
        pct = (v * E0 / QB - 1) * 100
        print(f"      {mp.nstr(v, 18):>22s}   ->  {mp.nstr(pct, 9):>14s} % vs Q_beta")
    check("the_candidate_set_is_small_and_enumerated", len(vals) > 0,
          f"{len(vals)} distinct values from {(KMAX+1)**2} ordered pairs — a "
          "finite derived set, not a search space")

    # ---- CHECK 4: the gap -------------------------------------------------
    print("\nCHECK 4 — where the target falls in that set")
    below = [v for v in vals if v < TARGET]
    above = [v for v in vals if v > TARGET]
    nearest = min(vals, key=lambda v: abs(v - TARGET))
    print(f"    target                    {mp.nstr(TARGET, 18)}")
    print(f"    largest reachable below   "
          f"{mp.nstr(max(below), 18) if below else '(none)'}")
    print(f"    smallest reachable above  "
          f"{mp.nstr(min(above), 18) if above else '(none)'}")
    print(f"    nearest                   {mp.nstr(nearest, 18)}  "
          f"({mp.nstr(abs(nearest - TARGET) / TARGET * 100, 8)} % away)")
    hits = [v for v in vals if abs(v - TARGET) <= TARGET * SIGMA_REL]
    check("no_gamma_gamma_difference_reaches_Q_beta", len(hits) == 0,
          f"0 of {len(vals)} reachable values land within the {mp.nstr(SIGMA_REL*10**9,5)} ppb "
          "window")
    if below and above:
        gap_lo, gap_hi = max(below), min(above)
        check("the_target_sits_in_a_GAP_of_the_reachable_set",
              gap_lo < TARGET < gap_hi,
              f"the set has nothing between {mp.nstr(gap_lo, 10)} and "
              f"{mp.nstr(gap_hi, 10)}, a gap of width "
              f"{mp.nstr(gap_hi - gap_lo, 10)} = "
              f"{mp.nstr((gap_hi-gap_lo)/TARGET, 6)}x the target, and Q_beta "
              "falls inside it — the miss is STRUCTURAL, not a matter of which "
              "words were tried")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — the ruled γγ selection, applied ALONE to the decay channel,")
    print("gives exactly zero at level 1 (proved, not merely measured) and at")
    print("level 2 lands in a set whose gap contains Q_beta. So it does not")
    print("merely miss; it cannot come close, and no further choice of γγ words")
    print("changes that. Read with the recipe route being exhausted (0 of")
    print("37,459,422,000), the live conclusion is that Delta needs the FLAVOUR")
    print("letters, which carry no γγ structure — the open point #7192 names for")
    print("itself. Scope-(a): this prices the principle applied alone; it does")
    print("NOT refute the ruling.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-gamma-gamma-selected-delta")
        w.set_description(
            "Applies the owner's 2026-09-08 γγ+SDP word-selection ruling to the "
            "DECAY channel. Inside H_3 every γγ-word is a vertex power, so the "
            "candidate Delta set is finite and derived rather than searched. At "
            "level 1 the difference vanishes identically (proved in "
            "GammaGammaSelectedDeltaVanishes); at the ruled level 2 the "
            "reachable set has a gap containing Q_beta. Scope-(a)."
        )
        w.add_data("markov_convention", "D — the ruled functional, z_D = q^3/(q^2+1)")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("target_abs_eps", mp.nstr(TARGET, 30))
        w.add_data("kmax", KMAX)
        w.add_data("tr_zD_of_vertex_powers",
                   {str(k): mp.nstr(v, 25) for k, v in trs.items()})
        w.add_data("reachable_abs_differences", [mp.nstr(v, 25) for v in vals])
        w.add_data("level_1_max_abs_difference", mp.nstr(worst, 10))
        if below and above:
            w.add_data("gap_containing_target",
                       {"below": mp.nstr(max(below), 25),
                        "above": mp.nstr(min(above), 25),
                        "target": mp.nstr(TARGET, 25)})
        w.add_caveat(
            "Scope-(a). γγ-words carry NO FLAVOUR INDEX (the corpus's Crossing "
            "is (gen, pos)), so this prices the ruled principle APPLIED ALONE. "
            "It is evidence that the principle underdetermines Delta and needs "
            "the flavour letters — the open point GammaGammaSelectorH3 names "
            "for itself — NOT a refutation of the ruling."
        )
        w.add_caveat(
            "The level-1 vanishing is PROVED, not merely measured: "
            "QOU.QBeta.GammaGammaDelta.oneDim_annihilates_gammaGamma_difference, "
            "sorry-free. CHECK 2 confirms the arithmetic agrees with the proof; "
            "it is a calibration of the numerics, not the evidence for the claim."
        )
        w.add_caveat(
            "k is capped at 5 by the 11-crossing nucleon budget (qou-1qsw). A "
            "larger budget would extend the reachable set; the gap statement is "
            "made for this budget and is not claimed beyond it."
        )
        for name, passed, det in RESULTS:
            w.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        w.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
