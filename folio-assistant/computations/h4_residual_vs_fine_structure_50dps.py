"""Is the Reading-A h⁴ residual = -α·h⁴ (fine-structure constant)?

Per author 2026-05-25 "continue exploring" — pursuing a curious
near-coincidence. The probe `implied_h2_coefficient_audit_50dps.py`
found that if linking_weight = 5/2 + (-G)·h² + c_4·h⁴ + ..., then
the implied c_4 at q_0 is ≈ -7.235e-3. This is SUSPICIOUSLY CLOSE
to the fine-structure constant α = 1/137.036 ≈ 7.2974e-3 (within
0.85%).

α has NO obvious categorical-substrate derivation in QOU. If
c_4 ≈ -α structurally, that would be a significant cross-link
between the substrate framework and electromagnetism.

This probe:
1. Computes c_4 at mp.mpf 50 dps assuming Reading-A's c_2 = -G is exact
2. Compares to -α (CODATA 2022 value)
3. Tests whether c_4 = -α gives a tighter residual than c_4 from solo Reading-A
4. Reports honestly whether the coincidence is structural or numerical

## Caveat

α appears in MANY physical quantities; near-coincidences with α are
not rare. The framework's substrate stack does NOT predict α
(α is an emergent QED quantity, not categorical). Any structural
appearance of α in the linking_weight would require a NEW categorical
derivation.

## Method

Compute at 50 dps:
  target_lw = m_p / (m_e · 8G / ℏ_q²)
  c_4 = (target_lw - 5/2 - (-G)·h²) / h⁴
  α = 1/137.0359991  (CODATA 2022)

Report:
  - c_4 value
  - -α value
  - difference c_4 - (-α)
  - residual if linking_weight = 5/2 - G·h² - α·h⁴
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


M_E_MEV = "0.51099895069"
M_P_MEV = "938.27208816"
# Fine-structure constant α^(-1) per CODATA 2022:
INVERSE_ALPHA_CODATA = "137.035999084"
# Source: https://physics.nist.gov/cgi-bin/cuu/Value?alphinv


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "h4-residual-vs-fine-structure-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Tests whether the Reading-A h⁴ residual (assuming c_2 = -G "
        "exact) matches the fine-structure constant α at q_0. "
        "EXPLORATORY — no structural derivation, just a numerical "
        "near-coincidence to flag for follow-up."
    )

    print("=" * 78)
    print("Reading-A h⁴ residual vs fine-structure constant α")
    print("=" * 78)

    q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    h2 = h * h
    h4 = h2 * h2
    G = mp.catalan
    m_e = mp.mpf(M_E_MEV)
    m_p = mp.mpf(M_P_MEV)
    alpha = 1 / mp.mpf(INVERSE_ALPHA_CODATA)

    hbar_q = 1 - qi
    vol_b3 = 8 * G
    geom_leading = vol_b3 / hbar_q ** 2
    target_lw = m_p / (m_e * geom_leading)

    print(f"\nq_0      = {Q_50_DIGIT_STR}")
    print(f"h²       = {mp.nstr(h2, 25)}")
    print(f"h⁴       = {mp.nstr(h4, 25)}")
    print(f"G        = {mp.nstr(G, 25)}")
    print(f"α        = {mp.nstr(alpha, 25)}")
    print(f"target_lw = {mp.nstr(target_lw, 25)}")

    # === Compute c_4 assuming Reading-A's c_2 = -G is exact ===
    reading_a_lw = mp.mpf("2.5") + (-G) * h2
    residual_at_h2 = target_lw - reading_a_lw  # this is the h⁴+ remainder
    c_4_implied = residual_at_h2 / h4

    print(f"\n[1/3] If c_2 = -G EXACTLY, the required h⁴ correction:")
    print(f"  Reading-A (5/2 - G·h²) at q_0 = {mp.nstr(reading_a_lw, 25)}")
    print(f"  target_lw                     = {mp.nstr(target_lw, 25)}")
    print(f"  residual                       = {mp.nstr(residual_at_h2, 12)}")
    print(f"  c_4 = residual / h⁴            = {mp.nstr(c_4_implied, 18)}")

    # === Compare c_4 to -α ===
    minus_alpha = -alpha
    delta = c_4_implied - minus_alpha
    print(f"\n[2/3] Compare to fine-structure constant α:")
    print(f"  c_4_implied = {mp.nstr(c_4_implied, 15)}")
    print(f"  -α (CODATA) = {mp.nstr(minus_alpha, 15)}")
    print(f"  Δ            = {mp.nstr(delta, 12)}")
    print(f"  |Δ| / |-α|   = {mp.nstr(abs(delta)/abs(minus_alpha) * 100, 8)}%")

    # === Test: linking_weight = 5/2 - G·h² - α·h⁴ at q_0 ===
    lw_with_alpha_h4 = mp.mpf("2.5") + (-G) * h2 + (-alpha) * h4
    residual_with_alpha_h4 = target_lw - lw_with_alpha_h4
    m_p_with_alpha_h4 = m_e * geom_leading * lw_with_alpha_h4
    delta_m_p = m_p_with_alpha_h4 - m_p
    ppm_with_alpha_h4 = delta_m_p / m_p * 1e6

    print(f"\n[3/3] Test: linking_weight = 5/2 + (-G)·h² + (-α)·h⁴ at q_0:")
    print(f"  lw                  = {mp.nstr(lw_with_alpha_h4, 25)}")
    print(f"  residual to target  = {mp.nstr(residual_with_alpha_h4, 18)}")
    print(f"  m_p_pred            = {mp.nstr(m_p_with_alpha_h4, 18)} MeV")
    print(f"  Δ_CODATA            = {mp.nstr(delta_m_p, 12)} MeV")
    print(f"  ppm                 = {mp.nstr(ppm_with_alpha_h4, 8)} ppm")

    # === Comparison summary ===
    reading_a_residual = target_lw - reading_a_lw
    reading_a_m_p = m_e * geom_leading * reading_a_lw
    reading_a_ppm = (reading_a_m_p - m_p) / m_p * 1e6

    print(f"\n[Summary]")
    print(f"  Reading-A (h²-only):           m_p = {mp.nstr(reading_a_m_p, 10)}, +{mp.nstr(reading_a_ppm, 6)} ppm")
    print(f"  Reading-A + α·h⁴ correction:   m_p = {mp.nstr(m_p_with_alpha_h4, 10)}, {mp.nstr(ppm_with_alpha_h4, 6)} ppm")
    print(f"  CODATA:                         m_p = {mp.nstr(m_p, 10)}, 0 ppm")
    print()
    if abs(ppm_with_alpha_h4) < abs(reading_a_ppm):
        print(f"  Adding -α·h⁴ TIGHTENS the match by {mp.nstr(abs(reading_a_ppm) - abs(ppm_with_alpha_h4), 6)} ppm.")
    else:
        print(f"  Adding -α·h⁴ does NOT tighten the match (Δppm = {mp.nstr(abs(ppm_with_alpha_h4) - abs(reading_a_ppm), 6)}).")

    # === HONEST CAVEAT ===
    print(f"\n[HONEST INTERPRETATION]")
    if abs(delta) / abs(minus_alpha) < mp.mpf("0.01"):
        print(f"  c_4 matches -α to <1% — INTRIGUING but NOT a proof.")
    elif abs(delta) / abs(minus_alpha) < mp.mpf("0.05"):
        print(f"  c_4 matches -α to <5% — suggestive coincidence.")
    else:
        print(f"  c_4 differs from -α by >5% — likely NOT a structural match.")
    print(f"  α has no categorical-substrate derivation in QOU framework.")
    print(f"  Any apparent match could be:")
    print(f"    1. Numerical coincidence (α appears in many quantities)")
    print(f"    2. Genuine hidden cross-link (would need NEW categorical theory)")
    print(f"    3. Artifact of assuming c_2 = -G exactly (which itself is unproven)")

    # Witness
    w.add_parameter("q_0_50dps", Q_50_DIGIT_STR)
    w.add_parameter("inverse_alpha_codata", INVERSE_ALPHA_CODATA)
    w.add_data("c_4_implied", mp.nstr(c_4_implied, 25))
    w.add_data("minus_alpha", mp.nstr(minus_alpha, 25))
    w.add_data("delta_c4_minus_alpha", mp.nstr(delta, 25))
    w.add_data("relative_match_percent",
               mp.nstr(abs(delta)/abs(minus_alpha) * 100, 12))
    w.add_data("m_p_predictions_ppm", {
        "reading_a_h2_only": mp.nstr(reading_a_ppm, 8),
        "reading_a_plus_alpha_h4": mp.nstr(ppm_with_alpha_h4, 8),
        "improvement_ppm": mp.nstr(
            abs(reading_a_ppm) - abs(ppm_with_alpha_h4), 8
        ),
    })
    w.add_data("interpretation", (
        f"c_4_implied = {mp.nstr(c_4_implied, 8)} matches -α = "
        f"{mp.nstr(minus_alpha, 8)} to "
        f"{mp.nstr(abs(delta)/abs(minus_alpha) * 100, 4)}%. NEAR but "
        f"not exact. Without a categorical derivation linking α to "
        f"the substrate stack, this is a SUGGESTIVE COINCIDENCE, not "
        f"a proof. Possible follow-ups: (1) compute c_4 at other "
        f"baryon predictions (m_n, m_He) to see if the same -α "
        f"coefficient appears; (2) search for substrate-derivations "
        f"of α (e.g. via Yekutieli q-deformation evaluation); (3) "
        f"check if a clean h⁴+h⁶+... rational series fits the "
        f"residual exactly with structural coefficients."
    ))

    # Sanity: at least the arithmetic worked
    arithmetic_ok = mp.isfinite(c_4_implied) and not mp.isnan(c_4_implied)
    w.add_assertion(
        name="c4_arithmetic_finite",
        computed=arithmetic_ok,
        expected=True,
        tolerance=0,
        source=(
            "Sanity check that the c_4 computation at 50 dps "
            "returned a finite value (not NaN / Inf)."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
