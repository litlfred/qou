#!/usr/bin/env python3
# polynomial_q_not_applicable: bar-involution parity / chiral-residue scale, not
# a Jones-polynomial evaluation.
"""
The H₂S +2.1° is the BAR-ANTI-SYMMETRIC (chiral / skew) residue.

Owner directions: "q-hyperbolic cosh, higher order than h²" (even part) and
"curvature on the S³ embedding is in the chiral channel" (odd part). These are
exactly the two halves of the bar-involution (`bar-involution.md`):

  bar-SYMMETRIC (even):  cos, cosh, Li₂^q   — RETAINED (observable)
  bar-ANTI-symmetric (odd):  sin, sinh, Φ_q — the CHIRAL/SKEW part, P_skew,
                                              normally PROJECTED AWAY.
  h = q − q⁻¹ is bar-ANTI-symmetric; h² is bar-symmetric.

THE IDENTIFICATION (explains the H₂O-clean / H₂S-residual dichotomy):

  H₂O — both lone pairs are the self-dual e⁻ (palindromic, defect 0) ⇒
        BAR-SYMMETRIC ⇒ the angle is pure even ⇒ the clean q² prediction
        (104.5°), with ZERO bar-anti-symmetric residual.

  H₂S — the s-channel is inert, so the two lone pairs are inequivalent: the
        self-dual 3s² (defect 0) and the CHIRAL 3p_z (defect 2). The chiral
        pair carries a BAR-ANTI-SYMMETRIC (skew) component — odd in h — which
        the framework usually discards (P_skew) but which here surfaces as the
        +2.1° opening of the pure-p 90° base.

PARITY CHECK — DOES NOT SURVIVE CONVENTION D (corrected 2026-08-23).

The check was: the residual must be ODD in h, its scale is h·z² ≈ 3.0° /
h·z³ ≈ 1.5°, and the observed +2.1° sits BETWEEN consecutive odd powers.
Those two numbers are **convention C** (z = √q/(q+1) = 0.49932). This file has
computed z in **convention D** (z = q³/(q²+1) = 0.61269) since the 2026-08-09
excision, where the same expressions are 4.50° and 2.75°, and +2.1° is **below
the whole bracket** rather than inside it. The assertion is red for that reason
and is correct to be red.

Two things are wrong with the check beyond the arithmetic, and they are worth
separating because only one of them is about the convention:

1. **The parity premise is FALSE under D.** "h·z^k is odd in h" is a bar-parity
   statement, and it needs z to be bar-EVEN — otherwise z contributes its own
   parity and the product has none. Exactly:

       z_C(1/q)/z_C(q) = 1        bar-even   ✓
       z_D(1/q)/z_D(q) = q⁻⁴      NOT bar-even ✗

   So under the canonical convention h·z^k has no clean bar-parity at all, and
   the classification the whole identification rests on is unavailable — not
   merely unfavourable. The line below that called z "the bar-symmetric Markov
   param" was a convention-C fact left attached to a convention-D value.

2. **The bracket was weak evidence even under C.** [h·z³, h·z²] is 1.495° wide
   about a 2.1° target — **71 % of the value**. Any residual in [1.49°, 2.99°]
   passes it. Per AGENTS.md §"Defined residual ≠ derived decomposition" item 2,
   a window that wide must be reported with its width rather than presented as
   confirmation; "right parity, right scale" is doing no work if nearly any
   scale would have fit.

SCOPE. (b) structural, invariant cited: the bar-parity argument for h·z^k does
not exist under convention D, because z_D is exactly not bar-even. (a) scope-
limited: this particular bracket does not contain 2.1° under D. Neither
excludes the +2.1° being chiral by some other route — only this construction.

Refs: bar-involution.md (P_avg even / P_skew odd; h bar-anti-symmetric);
archimedean-chirality.md (chirality = Reeb ±-eigenspaces); palindromicity-
orbital-type (self-dual s / chiral p); h2s_lone_pair_asymmetry.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
for _p in (str(_HERE),
           str(_QOU_REPO_ROOT / "tools" / "pyhecke" / "python"),
           str(_QOU_REPO_ROOT / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: F401
from _precision import fmt, set_compute_dps
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder



def main() -> None:
    set_compute_dps()
    w = WitnessBuilder("h2s-chiral-residue-bar-antisymmetric", engine="python+mpmath")
    q = mp.mpf(Q_50_DIGIT_STR)
    hh = q - 1 / q                                # bar-ANTI-symmetric: h(1/q) = -h(q)
    z = q ** 3 / (q ** 2 + 1)                     # convention D — and NOT bar-even
    z_c = mp.sqrt(q) / (q + 1)                    # convention C, for the comparison only
    h12 = mp.sqrt(q) - 1 / mp.sqrt(q)             # bar-anti-symmetric half-step
    d2p = 180 / mp.pi
    open_deg = mp.mpf("2.1")                      # observed H2S opening from the 90 deg base

    # The premise the whole parity argument needs: is z bar-EVEN?
    bar_ratio_D = (q ** -3 / (q ** -2 + 1)) / z           # z_D(1/q)/z_D(q)
    bar_ratio_C = (1 / mp.sqrt(q) / (1 / q + 1)) / z_c    # z_C(1/q)/z_C(q)
    z_is_bar_even_D = abs(bar_ratio_D - 1) < mp.mpf("1e-40")
    z_is_bar_even_C = abs(bar_ratio_C - 1) < mp.mpf("1e-40")

    print("=" * 72)
    print("H2S +2.1 deg — bar-parity check, convention D")
    print("=" * 72)
    print(f"  z_D = {mp.nstr(z, 10)}   bar-even? {z_is_bar_even_D}  "
          f"(z(1/q)/z(q) = {mp.nstr(bar_ratio_D, 8)} = q^-4)")
    print(f"  z_C = {mp.nstr(z_c, 10)}   bar-even? {z_is_bar_even_C}  "
          f"(z(1/q)/z(q) = {mp.nstr(bar_ratio_C, 8)})")
    print(f"  h   = {mp.nstr(hh, 10)}   bar-ODD  (h(1/q) = -h)")
    print()
    print("  => 'h*z^k is odd in h' is a bar-parity statement and needs z bar-EVEN.")
    print("     It holds in C and FAILS in D, so under the canonical convention")
    print("     the product has no clean bar-parity and the classification is")
    print("     unavailable — not merely unfavourable.")
    print()

    odd_D = {"h*z^2": hh * z ** 2 * d2p, "h*z^3": hh * z ** 3 * d2p,
             "h_half*z": h12 * z * d2p}
    odd_C = {"h*z^2": hh * z_c ** 2 * d2p, "h*z^3": hh * z_c ** 3 * d2p,
             "h_half*z": h12 * z_c * d2p}
    for label, tab in (("D (canonical)", odd_D), ("C (excised)", odd_C)):
        lo, hi = tab["h*z^3"], tab["h*z^2"]
        inside = bool(lo < open_deg < hi)
        width_pct = 100 * (hi - lo) / open_deg
        print(f"  {label}:  h*z^3 = {mp.nstr(lo, 6)} deg   h*z^2 = {mp.nstr(hi, 6)} deg")
        print(f"      brackets 2.1 deg? {inside}    window width "
              f"{mp.nstr(hi - lo, 6)} deg = {mp.nstr(width_pct, 4)}% of the target")

    between = bool(odd_D["h*z^3"] < open_deg < odd_D["h*z^2"])

    w.set_description(
        "H2S +2.1 deg chiral-residue parity check, convention D. The block's "
        "identification of the residual as the bar-ANTI-symmetric (odd-in-h) "
        "channel rests on a bracket h*z^3 < 2.1 < h*z^2. That bracket is a "
        "CONVENTION-C fact: in C it is 1.49 < 2.1 < 2.99 (true), in the "
        "canonical D it is 2.75 < 2.1 < 4.50 (false, 2.1 is below the window). "
        "Worse, the parity premise itself fails under D — h*z^k is odd-in-h "
        "only if z is bar-even, and z_D(1/q)/z_D(q) = q^-4, so the "
        "classification is unavailable rather than merely unfavourable. And "
        "even under C the window is 71% of the target, so nearly any residual "
        "would have passed it. The assertion below is red and is correct to be "
        "red; do not relax it. The H2O-clean / H2S-residual dichotomy is "
        "untouched by this — only this bracket argument for it is."
    )
    w.set_content_block("prop:symmetric-block-domain-weight")
    w.add_parameter("q", fmt(q))
    w.add_parameter("convention", "D")
    w.add_parameter("z_D", fmt(z))
    w.add_parameter("z_C_for_comparison", fmt(z_c))
    w.add_parameter("h_bar_antisymmetric", fmt(hh))
    w.add_parameter("h_half_bar_antisymmetric", fmt(h12))
    w.add_data("observed_opening_deg", fmt(open_deg))
    w.add_data("odd_candidates_deg_conventionD", {k: fmt(v) for k, v in odd_D.items()})
    w.add_data("odd_candidates_deg_conventionC", {k: fmt(v) for k, v in odd_C.items()})
    w.add_data("z_is_bar_even_conventionD", bool(z_is_bar_even_D))
    w.add_data("z_is_bar_even_conventionC", bool(z_is_bar_even_C))
    w.add_data("z_bar_ratio_conventionD", fmt(bar_ratio_D))
    w.add_data("residual_is_odd_in_h_between_powers", between)
    w.add_data(
        "bracket_window_width_pct_of_target",
        {"D": fmt(100 * (odd_D["h*z^2"] - odd_D["h*z^3"]) / open_deg),
         "C": fmt(100 * (odd_C["h*z^2"] - odd_C["h*z^3"]) / open_deg)},
    )
    w.add_assertion(
        "residual_bracketed_by_consecutive_odd_powers_under_convention_D",
        computed=str(int(between)), expected="1", tolerance="0",
        source=(
            "EXPECTED RED, and red is the result. Convention D gives "
            "h*z^3 = 2.755 deg < h*z^2 = 4.496 deg, and the observed 2.1 deg is "
            "BELOW that window. The 1.49/2.99 deg figures this assertion quoted "
            "until 2026-08-23 are convention C. Do not relax this gate: it "
            "records that the bracket argument does not survive the canonical "
            "convention. Note also that the premise fails independently — "
            "h*z^k is odd-in-h only if z is bar-even, and z_D is not."
        ),
    )
    w.add_data(
        "finding",
        "The H2O-clean / H2S-residual DICHOTOMY (two self-dual lone pairs vs a "
        "self-dual 3s^2 plus a chiral 3p_z) is a structural reading and is not "
        "touched here. What is retracted is the quantitative parity argument "
        "offered for it: (b) the bar-parity classification of h*z^k does not "
        "exist under convention D, since z_D(1/q)/z_D(q) = q^-4 exactly, so the "
        "product has no clean bar-parity; and (a) this particular bracket does "
        "not contain 2.1 deg under D. Even under C the bracket spanned 71% of "
        "the target, so it distinguished almost nothing. Neither point excludes "
        "the +2.1 deg being chiral by another route -- only this construction.",
    )
    w.save()
    print("\nDone. Witness saved (h2s-chiral-residue-bar-antisymmetric).")


if __name__ == "__main__":
    main()
