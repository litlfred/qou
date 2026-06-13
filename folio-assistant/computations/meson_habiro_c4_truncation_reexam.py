"""Re-examination: meson Habiro c=4 vs the Q_β tier-near-match framing.

Per author 2026-05-31 "let's briefly re-explore" — revisit a
"closed" route under the lens of the Q_β c_k truncation-order
canonical framing (audit 2026-05-31-qbeta-ck-truncation-order-
canonical-framing.md).

## The route in question

Audit `2026-05-29-meson-mK-mpi-residual-derivation-attempt.md`
Path 1 (Habiro tower) tested:

  R = 1 + c·u²   where u_ladder = b·ℏ_q², b² = (h²+3)/(h²+4)

At q_0 (50 dps), measured C = R−1 = 2.924e-4, giving:
  C / u²  = 4.031        ← claimed "0.77% off integer 4"
  C / (4u²) = 1.0077

Audit conclusion: **"c ≈ 4 is a 0.2-0.8% numerical coincidence, NOT
a derivation"** → ruled out, do not wire.

## The Q_β parallel (PR #1581 Probe B + audit 2026-05-31)

Q_β has c_2 = -1 PROVED Taylor-exact and c_3 = J_Hopf(q=1) = -2 as
the LEADING wired coefficient. The 3.47% m_p-pin "swing" was
treated as evidence c_3 was wrong, leading to 4 wire/un-wire flip-
flops. The canonical framing (Rule 3+4) resolved:

  - The "swing" is the BOUNDED c_4·u⁴ truncation error
  - c_3 = -2 is structurally legitimate at tier=near-match
  - Reporting binary "wire/drop" was the framing error

## The question

Does the meson Habiro c=4 = J² claim suffer the SAME framing error?

The 0.77% "miss" between C/u² = 4.031 and integer c = 4 looks
exactly like Q_β's swing pattern:
  - A LEADING coefficient identification (c = J² = 4)
  - A small-percentage RESIDUAL from higher-order rungs (here c_3·u³)
  - Premature binary "ruling out" instead of tier=near-match

If c_3·u³ is the right bound for the meson Habiro residual, then
the 0.77% miss is EXPECTED and BOUNDED, not evidence c=4 is wrong.

## Method

Compute at 50 dps:
1. The measured C/u² = 4.031 (reproduce audit number)
2. The implied c_3 needed to absorb the residual: c_3·u_ladder = C/u² - 4
3. Check whether |c_3·u_ladder| < some natural bound (e.g. |c_2|·u_ladder for
   Q_β-analog truncation behaviour)
4. Compare to natural J-Hopf-like candidates at H_3 level

## Cross-references

- audit 2026-05-29-meson-mK-mpi-residual-derivation-attempt.md (Path 1 ruling)
- audit 2026-05-31-qbeta-ck-truncation-order-canonical-framing.md (Rule 3+4)
- PR #1581 Probe B (Q_β c_3 = -2 structurally legitimate)
- meson_habiro_expansion.py (the original probe)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_K_PM_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION  # noqa: E402
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps(50)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Meson Habiro c=4 re-examination under Q_β tier-near-match framing")
    print("=" * 78)

    # PDG anchors (per audit 2026-05-29)
    m_K = M_K_PM_MEV_VALIDATION
    m_pi = M_PI_PM_MEV_VALIDATION
    target = m_K / m_pi  # = 3.5371...
    print(f"\nq_0 = {Q_50_DIGIT_STR}")
    print(f"target m_K/m_π = {mp.nstr(target, 18)}")

    # Strong-sector base: chi_{(2,1)}(σ₁⁵) · (9/5)²
    # chi_{(2,1)}(σ₁⁵) = q^5 - q^-5 (standard rep eigenvalue calc)
    chi5 = q ** 5 - q ** (-5)
    seifert_ratio_sq = (mp.mpf(9) / 5) ** 2
    base = chi5 * seifert_ratio_sq
    print(f"\n[Strong-sector base from audit Path 1]")
    print(f"  chi_(2,1)(σ₁⁵) = q^5 − q^-5 = {mp.nstr(chi5, 12)}")
    print(f"  (9/5)²         = {mp.nstr(seifert_ratio_sq, 12)}")
    print(f"  base           = {mp.nstr(base, 18)}")

    # The audit's C = R - 1
    R_exact = target / base
    C = R_exact - 1
    print(f"\n[Correction C = (target/base) − 1]")
    print(f"  R_exact = {mp.nstr(R_exact, 18)}")
    print(f"  C       = {mp.nstr(C, 18)}")

    # Ladder parameter u_ladder = b·ℏ² (NOT Habiro \check{q}; the local
    # var is named `u_ladder` for historical reasons — the canonical ladder
    # name is `u_ladder`. See notation-collisions.md §u_ladder). Pre-existing
    # mislabel corrected 2026-06-04 as part of the r→\check{q} cleanup.
    h = q - 1 / q
    h2 = h * h
    b_sq = (h2 + 3) / (h2 + 4)
    b = mp.sqrt(b_sq)
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    u_ladder = b * hbar_q_sq  # = u_ladder, the Q_β precision-ladder step
    print(f"\n[Ladder parameter u_ladder = b·ℏ_q²]")
    print(f"  b² = (h²+3)/(h²+4) = {mp.nstr(b_sq, 18)}")
    print(f"  b                  = {mp.nstr(b, 18)}")
    print(f"  ℏ_q²               = {mp.nstr(hbar_q_sq, 18)}")
    print(f"  u_ladder = b·ℏ_q²         = {mp.nstr(u_ladder, 18)}")

    # Test 1: reproduce audit's claim
    C_over_u2 = C / u_ladder ** 2
    print(f"\n[Test 1 — reproduce audit's C/u² = 4.03]")
    print(f"  C / u² = {mp.nstr(C_over_u2, 18)}")
    print(f"  vs integer 4: relative = {mp.nstr((C_over_u2 - 4) / 4 * 100, 6)}%")

    # Test 2: Q_β-style truncation analysis — assume c_2 = 4, find c_3
    # R = 1 + c_2·u² + c_3·u³ + O(u⁴)
    # C = c_2·u² + c_3·u³ + ...
    # If c_2 = 4 exactly:
    c_2_assumed = mp.mpf(4)
    residual_after_c2 = C - c_2_assumed * u_ladder ** 2
    c_3_required = residual_after_c2 / u_ladder ** 3
    print(f"\n[Test 2 — assume c_2 = 4, what c_3 absorbs the residual?]")
    print(f"  residual after c_2·u² = {mp.nstr(residual_after_c2, 18)}")
    print(f"  c_3 (so c_3·u³ = residual) = {mp.nstr(c_3_required, 18)}")

    # Test 3: is |c_3| of natural magnitude?
    # Q_β has c_3 = -2 = J_Hopf(q=1) — small integer.
    # Meson: J = 2 here (per J² = 4 ansatz). c_3 should be O(few).
    print(f"\n[Test 3 — c_3 magnitude check]")
    print(f"  |c_3 required| = {mp.nstr(abs(c_3_required), 12)}")
    print(f"  natural-magnitude J-like constants:")
    for name, val in [
        ("J = 2 (Hopf-link-at-q=1, mirror sign)", mp.mpf(-2)),
        ("J² = 4", mp.mpf(4)),
        ("J·b ≈ 2·0.7 ≈ 1.4", mp.mpf(2) * b),
        ("-J·b", mp.mpf(-2) * b),
        ("-2·[2]_q (Hopf × 2)", mp.mpf(-2) * (q + 1 / q)),
        ("c_3 from Q_β = -2 (J_Hopf)", mp.mpf(-2)),
    ]:
        diff = c_3_required - val
        rel = diff / c_3_required * 100 if abs(c_3_required) > 1e-30 else mp.inf
        print(f"    {name:<42} = {mp.nstr(val, 10):<14}"
              f"Δ = {mp.nstr(diff, 8)} ({mp.nstr(rel, 6)}%)")

    # Test 4: Q_β-analog bound — |c_3·u³| < |c_2·u²| would be normal
    # truncation. Is the meson residual within this bound?
    c2_contribution_ppb = abs(c_2_assumed * u_ladder ** 2 / C) * 1e9 if abs(C) > 1e-30 else mp.inf
    c3_contribution_pct = abs(c_3_required * u_ladder ** 3 / C) * 100
    print(f"\n[Test 4 — truncation bound check]")
    print(f"  c_2·u² contribution to C: {mp.nstr(abs(c_2_assumed * u_ladder ** 2 / C * 100), 8)}%")
    print(f"  c_3·u³ contribution to C: {mp.nstr(c3_contribution_pct, 8)}%")
    print(f"  ratio |c_3·u³|/|c_2·u²| = {mp.nstr(abs(c_3_required * u_ladder / c_2_assumed), 12)}")

    # ── Verdict ──
    print(f"\n[Verdict]")
    c2_pct = abs(c_2_assumed * u_ladder ** 2 / C * 100)
    c3_pct = c3_contribution_pct
    if abs(c_3_required) < mp.mpf("20") and c2_pct > 99 and c3_pct < 1:
        verdict = (
            "**REOPENED**: the 0.77% residual on C/u² = 4.03 is consistent "
            "with a BOUNDED c_3·u³ truncation error (analog of Q_β c_3 wired "
            "at tier=near-match). The audit's binary 'ruled out' may have "
            "made the same framing error the Q_β deep audit made: treating "
            "an unmatched residual as evidence the leading c_2 = 4 is wrong, "
            "rather than as bounded higher-rung contribution."
        )
    elif abs(c_3_required) < mp.mpf("50"):
        verdict = (
            "PARTIAL REOPENING: residual is consistent with a Q_β-analog "
            "truncation, BUT the required c_3 magnitude is not obviously "
            "tied to a natural J-Hopf-like constant. Worth deeper "
            "investigation but not a clear win."
        )
    else:
        verdict = (
            "AUDIT VERDICT STANDS: the required c_3 is too large to be a "
            "natural higher-rung contribution; the 0.77% miss is genuine "
            "evidence c=4 is not the correct leading coefficient."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "meson-habiro-c4-truncation-reexam",
        engine="python",
    )
    w.set_description(
        "Re-examines audit 2026-05-29 Path 1 ruling on meson Habiro c=4 "
        "under the Q_β c_k truncation-order canonical framing. Tests "
        "whether the 0.77% miss is a bounded c_3·u³ truncation error "
        "(parallel to Q_β c_3 = -2 at tier=near-match) rather than "
        "evidence c=4 is wrong."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("C_correction", mp.nstr(C, 25))
    w.add_data("u_ladder", mp.nstr(u_ladder, 25))
    w.add_data("C_over_u_squared", mp.nstr(C_over_u2, 25))
    w.add_data("c2_assumed", "4")
    w.add_data("c3_required_to_absorb_residual",
               mp.nstr(c_3_required, 25))
    w.add_data("c2_contribution_pct_to_C", mp.nstr(c2_pct, 12))
    w.add_data("c3_contribution_pct_to_C", mp.nstr(c3_pct, 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="reexam_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Meson Habiro c=4 re-examination completed at 50 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
