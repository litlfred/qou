#!/usr/bin/env python3
"""upsilon_14_crossing_probe.py -- can the dictionary's meson construction
reach the generation-3 quarkonium Upsilon(1S) = b bbar?  Bean `qou-eo5q`.

Owner decision 3a (2026-10-10): KEEP the "Meson at 2n crossings" relabel of
prop:lepton-meson-torus-knot-dictionary, do NOT put Upsilon into the table,
but TRY to compute the Upsilon entry with exactly the construction the
existing meson entries use, and report the residual.  No fitting.

The construction (the only producer of the dictionary's meson values)
--------------------------------------------------------------------
prop:meson-kaon-pion-hecke-seifert (row n=5) and
prop:gen3-meson-phi-hecke-seifert (row n=7), producer
computations/meson_gen3_eta_phi.py:

    m_X / m_pi = chi^(2,1)(sigma_1^n) * ( V_S(T(2,n)) / V_S(T(2,3)) )^{n_q}

    chi^(2,1)(sigma_1^n) = q^n + (-1/q)^n          (Hoefsmit eigenvalues q, -1/q)
    V_S(T(2,n))          = 2 pi |chi_orb|,  base S^2 - pt with cone points 2, n
                         = pi (n - 2) / n        (n odd: T(2,n) is a KNOT)
    n_q                  = 2                     (two-body q qbar, named a priori)

The index n is the TORUS KNOT of the row (pi: n=3 by normalisation,
K: n=5, gen-3: n=7), not the meson's constituent crossing total.  That is the
whole difficulty, and the probe measures both readings:

  R1  generation-index reading.  Upsilon = b bbar, b = T(2,7)^sigma, so the
      generation-3 slot is n = 7.  Fully defined, zero new choices.  The mirror
      only flips the sign of chi (sigma^-7), so |ratio| is unchanged.  This is
      the SAME number prop:gen3-meson-phi-hecke-seifert assigns to phi: the
      construction cannot tell phi from Upsilon.
  R2  crossing-count reading.  Upsilon sits at 7 + 7 = 14 crossings, n = 14.
      chi^(2,1)(sigma_1^14) = q^14 + q^-14 is DEFINED by the same Hoefsmit
      derivation (no choice).  V_S(T(2,14)) is NOT: T(2,14) is a 2-component
      LINK, and the corpus defines V_S only for torus KNOTS (Euler number
      e = 1 - 1/2 - 1/n, odd n).  Extending it is a new choice.  Two candidate
      extensions are evaluated as DIAGNOSTICS ONLY -- neither is the
      construction, neither is adopted, and choosing between them by residual
      is forbidden (AGENTS.md NO FITTING):
        R2a  literal formula pi(n-2)/n at n = 14     -> ratio 18/7
        R2b  2 pi |chi_orb| of the actual link base   (S^2 - 2 pts, one cone
             point of order 7: chi_orb = -(1 - 1/7))  -> 12 pi/7, ratio 36/7

Comparison: dimensionless m_Upsilon(1S) / m_pi+-, PDG 9460.30(26) MeV over
CAL-3 m_pi+- = 139.57039 MeV.  The pion is the construction's unit, so the
ratio to m_pi is the construction's own observable (no second scale enters).

q0: proton pin (owner directive 2026-08-07), qou_substrate.constants.
PRECISION: mpmath mpf at the repo compute dps; Seifert ratios exact Fraction.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402  (PROTON pin)
from qou_substrate.precision import fmt  # noqa: E402
from codata_constants import (  # noqa: E402
    M_PI_PM_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
)

M_UPSILON_1S = mpf("9460.30")      # PDG 2024, +-0.26 MeV (not in registry)
M_UPSILON_1S_ERR = mpf("0.26")
M_PHI = mpf("1019.461")            # PDG 2024, as in meson_gen3_eta_phi.py
N_Q = 2                            # two-body exponent, as in the kaon proof


def chi21(q: mpf, n: int) -> mpf:
    """chi^(2,1)(sigma_1^n) = q^n + (-1/q)^n (seminormal eigenvalues q, -1/q)."""
    return q ** n + (-1 / q) ** n


def seifert_ratio_knot(n: int) -> Fraction:
    """V_S(T(2,n))/V_S(T(2,3)) = [pi(n-2)/n]/[pi/3] = 3(n-2)/n. Corpus: odd n."""
    return Fraction(3 * (n - 2), n)


def seifert_ratio_link_base(n: int) -> Fraction:
    """DIAGNOSTIC. T(2,n), n even: base S^2 minus 2 points, one cone point of
    order n/2.  |chi_orb| = 1 - 2/n; V = 2 pi (1 - 2/n); over pi/3 -> 6(n-2)/n."""
    assert n % 2 == 0
    return Fraction(6 * (n - 2), n)


def to_mpf(fr: Fraction) -> mpf:
    return mpf(fr.numerator) / fr.denominator


def ratio(q: mpf, n: int, seif: Fraction) -> mpf:
    return chi21(q, n) * to_mpf(seif) ** N_Q


def main() -> int:
    q = Q_MP
    m_pi = mpf(M_PI_PM_MEV_VALIDATION)
    target = M_UPSILON_1S / m_pi
    target_err = M_UPSILON_1S_ERR / m_pi
    rel = lambda pred, obs: (pred - obs) / obs  # noqa: E731

    # Controls: the construction's two published rows at the proton pin.
    rK = ratio(q, 5, seifert_ratio_knot(5))
    rK_obs = mpf(M_K_PM_MEV_VALIDATION) / m_pi
    r7 = ratio(q, 7, seifert_ratio_knot(7))
    r7_phi = M_PHI / m_pi

    # R1 -- generation index n = 7 (b = T(2,7)^sigma).  Mirror check.
    r1 = abs(r7)
    # sigma^-1 has eigenvalues 1/q, -q
    r1_mirror = abs(q ** -7 + (-q) ** 7) * to_mpf(seifert_ratio_knot(7)) ** N_Q
    assert abs(r1 - r1_mirror) < mpf(10) ** (-(mp.dps - 5))

    # R2 -- crossing count n = 14.  chi defined; V_S needs a choice.
    chi14 = chi21(q, 14)
    r2a = ratio(q, 14, seifert_ratio_knot(14))
    r2b = ratio(q, 14, seifert_ratio_link_base(14))

    # What the missing factor would have to be (NOT a proposal): the
    # Seifert ratio S for which chi(sigma^14) * S^2 hits the target.
    s_req = mp.sqrt(target / chi14)

    print(f"q0 (proton pin)            = {mp.nstr(q, 20)}")
    print(f"m_Upsilon(1S)/m_pi  (PDG)  = {mp.nstr(target, 12)}  +- {mp.nstr(target_err, 3)}")
    print(f"control K:   pred {mp.nstr(rK, 10)}  obs {mp.nstr(rK_obs, 10)}  "
          f"rel {mp.nstr(rel(rK, rK_obs) * 1e6, 6)} ppm")
    print(f"control phi: pred {mp.nstr(r7, 10)}  obs {mp.nstr(r7_phi, 10)}  "
          f"rel {mp.nstr(rel(r7, r7_phi) * 100, 6)} %")
    print(f"R1  n=7  (generation)      = {mp.nstr(r1, 12)}   rel {mp.nstr(rel(r1, target) * 100, 6)} %")
    print(f"R2  chi(sigma^14)          = {mp.nstr(chi14, 12)}")
    print(f"R2a n=14 literal pi(n-2)/n = {mp.nstr(r2a, 12)}   rel {mp.nstr(rel(r2a, target) * 100, 6)} %  [diagnostic]")
    print(f"R2b n=14 link orbifold     = {mp.nstr(r2b, 12)}   rel {mp.nstr(rel(r2b, target) * 100, 6)} %  [diagnostic]")
    print(f"required Seifert ratio S   = {mp.nstr(s_req, 12)}  (R2a gives 18/7={mp.nstr(mpf(18)/7, 8)}, "
          f"R2b gives 36/7={mp.nstr(mpf(36)/7, 8)})")

    checks = [
        ("kaon control reproduces the published 290 ppm row (|rel| < 1e-3)",
         abs(rel(rK, rK_obs)) < mpf("1e-3")),
        ("phi control reproduces prop:gen3-meson-phi-hecke-seifert (7.32)",
         abs(r7 - mpf("7.320")) < mpf("1e-3")),
        ("R1 equals the phi slot exactly (construction cannot separate phi from Upsilon)",
         r1 == abs(r7)),
        ("R1 misses Upsilon by more than 50 %", abs(rel(r1, target)) > mpf("0.5")),
        ("neither R2 diagnostic lands within 50 %",
         abs(rel(r2a, target)) > mpf("0.5") and abs(rel(r2b, target)) > mpf("0.5")),
    ]
    for label, ok in checks:
        print(("PASS " if ok else "FAIL ") + label)

    payload = {
        "description": (
            "Upsilon(1S) = b bbar via the dictionary's meson construction "
            "m_X/m_pi = chi^(2,1)(sigma_1^n) * (V_S(T(2,n))/V_S(T(2,3)))^2. "
            "R1 (generation index n=7) is fully defined and equals the phi slot; "
            "R2 (14 crossings, n=14) needs a Seifert volume for the LINK T(2,14), "
            "which the corpus does not define -- two extensions shown as diagnostics only."
        ),
        "bean": "qou-eo5q",
        "owner_decision": "3a + try compute 14 (2026-10-10)",
        "q0Anchor": "proton",
        "q0": fmt(q),
        "construction": {
            "formula": "m_X/m_pi = (q^n + (-1/q)^n) * (V_S(T(2,n))/V_S(T(2,3)))^2",
            "sources": [
                "prop:meson-kaon-pion-hecke-seifert",
                "prop:gen3-meson-phi-hecke-seifert",
                "computations/meson_gen3_eta_phi.py",
            ],
            "n_q": N_Q,
            "index_n_means": "torus knot of the row (3, 5, 7), not the constituent crossing total",
        },
        "observed": {
            "m_upsilon_1S_MeV": fmt(M_UPSILON_1S),
            "m_upsilon_1S_err_MeV": fmt(M_UPSILON_1S_ERR),
            "m_pi_pm_MeV": fmt(m_pi),
            "ratio": fmt(target),
            "ratio_err": fmt(target_err),
        },
        "controls": {
            "kaon": {"pred": fmt(rK), "obs": fmt(rK_obs), "rel": fmt(rel(rK, rK_obs))},
            "phi_n7": {"pred": fmt(r7), "obs": fmt(r7_phi), "rel": fmt(rel(r7, r7_phi))},
        },
        "R1_generation_index_n7": {
            "status": "construction applies with zero new choices",
            "pred": fmt(r1),
            "rel_residual": fmt(rel(r1, target)),
            "note": "identical to the phi slot; b = T(2,7)^sigma mirror leaves |ratio| unchanged",
        },
        "R2_crossing_count_n14": {
            "status": "construction does NOT extend without a new choice",
            "missing_choice": (
                "V_S of the 2-component torus LINK T(2,14); the corpus defines V_S(T(2,n)) "
                "only for odd n via Euler number e = 1 - 1/2 - 1/n"
            ),
            "chi21_sigma14": fmt(chi14),
            "required_seifert_ratio_to_hit_target": fmt(s_req),
            "diagnostics_not_adopted": {
                "R2a_literal_pi_n_minus_2_over_n": {
                    "seifert_ratio": "18/7", "pred": fmt(r2a), "rel_residual": fmt(rel(r2a, target))},
                "R2b_link_base_orbifold_euler": {
                    "seifert_ratio": "36/7", "pred": fmt(r2b), "rel_residual": fmt(rel(r2b, target))},
            },
        },
        "verdict": (
            "scope-(a): the dictionary's meson construction, alone and as-is, does not "
            "reproduce m_Upsilon/m_pi. Under the only zero-choice reading (n=7) it returns the "
            "phi value, -89 % against Upsilon; the 14-crossing reading is undefined in the corpus."
        ),
        "assertions": [{"label": lab, "passed": bool(ok)} for lab, ok in checks],
        "allPassed": all(ok for _, ok in checks),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "upsilon-14-crossing-probe", payload, script_path=__file__,
        engine="mpmath", output_dir=HERE,
    ).save()
    print(f"witness: {out}")
    return 0 if payload["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
