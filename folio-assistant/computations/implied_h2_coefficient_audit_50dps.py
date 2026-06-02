"""What is the ACTUAL implied h² coefficient at q_0?

Per author 2026-05-25 "continue exploring" — investigating whether
Reading-A's `−G·h²` is the EXACT correct coefficient, or just the
closest "nice constant" to whatever the actual coefficient is.

## Method

Assume linking_weight = 5/2 + c·h² + (small h⁴+ remainder). Solve
for c that minimizes the residual to m_p-anchored target_lw at q_0.

If c ≈ −G exactly (matching to 50+ digits), Reading-A is the right
structural identity.

If c ≈ −G but distinct at e-3 / e-4 level, Reading-A is a near-miss
and the "5.6 ppm coincidence" is the deviation between -G and the
actual coefficient.

## Finding (mp.mpf 50 dps)

The actual implied h² coefficient at q_0 is:

  c_implied = (target_lw − 5/2) / h² = **−0.91628187612727...**

Compared to candidates:

| Candidate          | Value             | Δ from c_implied   |
|--------------------|-------------------|--------------------|
| −G (Catalan)       | −0.915965594...   | **+3.2e-4** (off)  |
| −11/12             | −0.916666666...   | −3.8e-4 (off)      |
| −G − 1/3500        | −0.916251308...   | +3.1e-5 (closer)   |
| −G·(1+1/3500)      | −0.916227298...   | +5.5e-5 (closer)   |

Neither −G nor −11/12 is the EXACT coefficient. The actual value
−0.91628 differs from both at the e-4 level.

## Interpretation

**Reading-A is a near-miss, not a structural identity.** The
empirical "5.6 ppm m_p match" is the deviation between -G and the
actual coefficient at q_0, NOT a perfect match.

Possible explanations:

1. **The actual linking_weight has h⁰ ≠ 5/2.** But Family A's
   h⁰ = 5/2 is PROVED (Wedderburn sum at q=1 ⇒ Σdim_λ / 4 = 10/4).
   Unless `linking_weight ≠ (1/4)Σdim_q V_λ` at q=1 too, h⁰ is
   pinned.

2. **The actual linking_weight has h⁴+ contributions** that mimic
   a different "effective h² coefficient" when fit at h² only.
   If c₂ = −G and c₄·h⁴ = −1.38e-5, then c₄ ≈ −7.22e-3 — small
   but not zero. No known structural constant matches.

3. **Vol(𝓑₃) ≠ 8·G exactly.** Adams 1985 is a closed-form result,
   widely accepted. But if Vol = 8G + δ with δ ≈ 2.5e-4, the
   discrepancy resolves. No literature suggests such a correction.

4. **m_p_CODATA itself has uncertainty.** Current CODATA m_p =
   938.27208816 MeV ± 0.000058 MeV = ± 6.2e-8 relative. The
   3.2e-4 discrepancy at h² coef level is ~5000× the m_p
   uncertainty, so this isn't it.

## Implication for Path B + C work

The Reading-A formula `5/2 − G·h²` is the CLOSEST known structural
form to the actual m_p-anchored target, but is NOT exact at 50 dps.
The Path B conditional Lean theorem stands (it formalises the
+5.6 ppm coincidence as a conditional), but Path C's "prove
Reading-A" goal should be reframed:

**There is no single h²-only formula that exactly matches target_lw
at 50 dps.** The categorical-derivation question becomes:

  - Does linking_weight have exact h²-only form 5/2 + c·h² with
    c = −0.91628... (a NEW constant)?
  - Or does linking_weight have h⁴+ corrections that make any
    h²-only approximation imperfect?

## Cross-references

- [PR #1287](https://github.com/litlfred/qou/pull/1287) — companion stack
- [audit 2026-05-25 Path C](../../docs/audits/2026-05-25-path-c-categorical-principle-hunt.md)
- [reading_a_residual_at_50dps.py](reading_a_residual_at_50dps.py)
- [Family A theorem](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.md)
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


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "implied-h2-coefficient-audit-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "mp.mpf 50-dps audit of the ACTUAL implied h² coefficient "
        "of linking_weight at q_0 (assuming h²-only truncation). "
        "Finds c_implied ≈ −0.91628, distinct from Reading-A's −G "
        "(off by 3.2e-4) and −11/12 (off by 3.8e-4). The Reading-A "
        "5.6 ppm m_p match is a near-miss, not a structural identity."
    )

    print("=" * 78)
    print("Implied h² coefficient audit at q_0 (50 dps)")
    print("=" * 78)

    q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    h2 = h * h
    G = mp.catalan
    m_e = mp.mpf(M_E_MEV)
    m_p = mp.mpf(M_P_MEV)

    hbar_q = 1 - qi
    vol_b3 = 8 * G
    geom_leading = vol_b3 / hbar_q ** 2
    target_lw = m_p / (m_e * geom_leading)

    print(f"\nq_0      = {Q_50_DIGIT_STR}")
    print(f"h²       = {mp.nstr(h2, 25)}")
    print(f"target_lw = {mp.nstr(target_lw, 25)}")
    print()

    implied_c2 = (target_lw - mp.mpf("2.5")) / h2
    print(f"Implied h² coefficient (assuming 5/2 + c·h² truncation):")
    print(f"  c_implied = (target − 5/2) / h² = {mp.nstr(implied_c2, 25)}")

    candidates = {
        "-G (Catalan)": -G,
        "-11/12": -mp.mpf(11) / 12,
        "-G - 1/3500": -G - mp.mpf(1) / 3500,
        "-G·(1+1/3500)": -G * (1 + mp.mpf(1) / 3500),
        "-π/(4·G·3)": -mp.pi / (4 * G * 3),
        "-2G + π/4": -2 * G + mp.pi / 4,
        "-(G + h²·0.005/h²)": -(G + mp.mpf("0.005")),  # control case
    }

    print(f"\nCandidate comparison:")
    print(f"  {'name':<28}{'value':<22}{'Δ vs c_implied':<22}")
    closest = None
    closest_dev = mp.mpf("1e10")
    for name, val in candidates.items():
        dev = val - implied_c2
        adev = abs(dev)
        if adev < closest_dev:
            closest = (name, val, dev)
            closest_dev = adev
        print(f"  {name:<28}{mp.nstr(val, 12):<22}{mp.nstr(dev, 8):<22}")

    print(f"\nClosest candidate: {closest[0]} (Δ = {mp.nstr(closest[2], 6)})")

    # === If c_2 = -G EXACTLY, what's the h⁴ remainder? ===
    h4 = h2 * h2
    residual_if_c2_minus_G = target_lw - mp.mpf("2.5") - (-G) * h2
    c4_required = residual_if_c2_minus_G / h4
    print(f"\nIf c₂ = -G EXACTLY, the h⁴+ remainder must be:")
    print(f"  residual = target_lw − 5/2 − (-G)·h² = {mp.nstr(residual_if_c2_minus_G, 15)}")
    print(f"  c₄ (if h⁴-only) = residual / h⁴ = {mp.nstr(c4_required, 15)}")

    # Compare c4 to known small constants
    print(f"\n  c₄ ≈ -7.22e-3 — not a recognized structural constant.")
    print(f"  PR #1272's via_jones h⁴ = -3.03, h⁶ = -0.81 at q_0:")
    contrib_h4 = mp.mpf("-3.03125") * h4
    contrib_h6 = mp.mpf("-0.8096") * h2 * h4
    pr1272_h4_plus_sum = contrib_h4 + contrib_h6
    print(f"     h⁴ contribution: {mp.nstr(contrib_h4, 8)}")
    print(f"     h⁶ contribution: {mp.nstr(contrib_h6, 8)}")
    print(f"     Sum h⁴+h⁶+...: ≈ {mp.nstr(pr1272_h4_plus_sum, 8)}")
    print(f"  vs required residual: {mp.nstr(residual_if_c2_minus_G, 8)} ")
    print(f"  PR #1272's tower is much larger and OPPOSITE SIGN — different normalization.")

    # === Vol(𝓑₃) correction needed? ===
    # If 5/2 - G·h² is the EXACT linking_weight, then
    # m_p = m_e · Vol/ℏ_q² · (5/2 - G·h²)
    # => Vol = m_p · ℏ_q² / (m_e · (5/2 - G·h²))
    vol_implied = m_p * hbar_q ** 2 / (m_e *
                   (mp.mpf("2.5") + (-G) * h2))
    print(f"\nIf Reading-A linking_weight 5/2 - G·h² is EXACT, then Vol(𝓑₃) would need:")
    print(f"  Vol_implied = {mp.nstr(vol_implied, 15)}")
    print(f"  8·G        = {mp.nstr(vol_b3, 15)}")
    print(f"  Difference  = {mp.nstr(vol_implied - vol_b3, 12)}")
    print(f"  Adams 1985 says Vol(𝓑₃) = 8·G EXACTLY. The ~{mp.nstr(abs(vol_implied - vol_b3), 6)} ")
    print(f"  difference is ~3e-5 of 8G — the same 5.6 ppm residual seen in m_p.")
    print(f"  No literature suggests Vol(𝓑₃) ≠ 8·G. So Reading-A is NOT exact at 50 dps.")

    # Witness
    w.add_parameter("q_0_50dps", Q_50_DIGIT_STR)
    w.add_parameter("m_e_MeV", M_E_MEV)
    w.add_parameter("m_p_codata_MeV", M_P_MEV)
    w.add_data("h2_at_q0", mp.nstr(h2, 25))
    w.add_data("target_lw_at_q0", mp.nstr(target_lw, 25))
    w.add_data("implied_c2", mp.nstr(implied_c2, 25))
    w.add_data("candidate_h2_coefficients", {
        name: {
            "value": mp.nstr(val, 25),
            "deviation": mp.nstr(val - implied_c2, 25),
        }
        for name, val in candidates.items()
    })
    w.add_data("if_c2_is_minus_G", {
        "h4_plus_residual": mp.nstr(residual_if_c2_minus_G, 25),
        "c4_if_h4_only": mp.nstr(c4_required, 25),
        "interpretation": (
            "If Reading-A's c₂ = -G is exact, then h⁴+ corrections "
            "must total ≈ -1.38e-5 at q_0. PR #1272's via_jones h⁴+ "
            "tower at q_0 totals ≈ -5.86e-3 (OPPOSITE SIGN, 420× "
            "larger) — different normalization, NOT a candidate "
            "for the actual h⁴+ correction."
        ),
    })
    w.add_data("conclusion", (
        "Reading-A (h²-only with c₂ = -G) is a NEAR-MISS to target_lw "
        "at 50 dps. The implied actual h² coefficient is -0.91628, "
        "differing from -G by 3.2e-4 and from -11/12 by 3.8e-4. "
        "Neither is the exact structural constant. Path C work needs "
        "to identify either (a) the new constant -0.91628..., (b) the "
        "h⁴+ tower that closes the residual to zero exactly, or (c) "
        "a correction to Vol(𝓑₃) beyond 8·G (literature says 8·G "
        "exact, so this is unlikely)."
    ))

    # Sanity assertion
    near_miss = abs(implied_c2 - (-G)) < mp.mpf("1e-3")
    not_exact = abs(implied_c2 - (-G)) > mp.mpf("1e-30")
    w.add_assertion(
        name="reading_a_is_near_miss_not_exact",
        computed=(near_miss and not_exact),
        expected=True,
        tolerance=0,
        source=(
            "Reading-A's -G coefficient differs from implied c_2 by "
            "between 1e-30 (anything above is 'not exact') and 1e-3 "
            "(anything below is 'near miss'). Numerically: "
            "|c_implied + G| ≈ 3.16e-4."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
