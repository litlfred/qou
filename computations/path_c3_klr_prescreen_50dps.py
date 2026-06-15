"""Path C3 — KLR / Kashiwara-crystal h² coefficient pre-screen.

Per author 2026-05-25 'continue exploring' → Path C3 hunt.
Investigates whether the KLR algebra's canonical-basis sum at q_0
can produce h² coefficient ≈ -G (Reading-A) rather than +3/4
(Wedderburn / Family A).

## Background

The KLR algebra R_n is the categorification of the negative half
U^-(g) of the quantum group. Its canonical basis decategorifies to
the **Kazhdan-Lusztig basis** of the Hecke algebra H_n(q). For
H_4, KL polynomials are ALL TRIVIAL (the first non-trivial KL
polynomial appears at S_5). So at H_4:

  KLR canonical basis at H_4 = Wedderburn standard basis at H_4
  ⇒ KLR h² coefficient at H_4 = Family A's +3/4

This forecloses the simplest "KLR replacement of Family A" interpretation.

## What might work — Demazure sub-crystal at H_5+

The framework's CLAUDE.md §7b mentions:

> "Demazure sub-crystals for resonances. Unstable intermediaries
>  (W/Z bosons, hadronic resonances) are Demazure sub-crystals —
>  incomplete topological states."

For H_5, the first non-trivial KL polynomial is:
  KL_{1432, 4321}(q) = 1 + q

(at the longest element). Demazure modules give sub-characters of
the Wedderburn dimension. Maybe a specific Demazure sub-character
of the H_5 Wedderburn at q_0 = h-expansion contains -G·h² at
leading non-trivial order.

## K-theory regulator pre-screen (decisive negative)

Per audit 2026-05-24 (crystal-Yekutieli correspondence) §4:

> "the higher regulator r_2^(2) is conjecturally −6G, giving
>  h⁴ = −3/4 K-theoretically."

If the K-theory prediction is `c_4 = -3/4` (a rational), but my
implied c_4 from the m_p anchor at q_0 is `-7.236e-3`, the K-theory
prediction is **100× larger** than what's needed:
  -3/4 = -0.75
  c_4_implied ≈ -7.236e-3
  ratio: -0.75 / -0.00723 = 103.7

So either:
  (a) K-theory prediction has different normalization than my probe
      assumes (Vol/8 vs Vol or similar factor)
  (b) c_4 isn't -3/4; the audit's conjectural value is wrong
  (c) c_4 is correct at q_0 ALONE due to higher-order h⁶, h⁸
      cancellation that mimics a smaller effective c_4

## Method

This probe:
1. Computes K-theory-predicted c_4 = -3/4 contribution at q_0:
     (-3/4)·h⁴ at q_0
2. Compares to required c_4·h⁴ = -1.38e-5 (residual to Reading-A)
3. Reports ratio and conclusion

## What this probe does NOT do

- Does NOT implement KLR canonical basis (multi-session research)
- Does NOT implement Demazure sub-crystals (multi-session research)
- Does NOT claim Path C3 is foreclosed — only pre-screens the simplest
  K-theory prediction. Demazure sub-crystal at H_5+ remains open.

## Cross-references

- audit 2026-05-24 crystal-Yekutieli correspondence chain
- audit 2026-05-25 Path C (this branch)
- PR #1287 (companion stack)
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


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "path-c3-klr-prescreen-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Path C3 KLR / Kashiwara crystal-graph pre-screen at 50 dps. "
        "Tests the K-theory regulator prediction c_4 = -3/4 against "
        "the empirical c_4 implied by Reading-A's h⁴ residual. "
        "K-theory prediction is ~100× larger than empirical — DECISIVE "
        "NEGATIVE for direct K-theory c_4 hypothesis. Demazure "
        "sub-crystal at H_5+ remains open as research direction."
    )

    print("=" * 78)
    print("Path C3 KLR / Kashiwara crystal pre-screen (50 dps)")
    print("=" * 78)

    q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    h2 = h * h
    h4 = h2 * h2
    G = mp.catalan

    print(f"\nq_0 = {Q_50_DIGIT_STR}")
    print(f"h² = {mp.nstr(h2, 25)}")
    print(f"h⁴ = {mp.nstr(h4, 25)}")
    print(f"G  = {mp.nstr(G, 25)}")

    # === Empirical c_4 from m_p anchor ===
    m_e = mp.mpf("0.51099895069")
    m_p = mp.mpf("938.27208816")
    hbar_q = 1 - qi
    vol_b3 = 8 * G
    geom_leading = vol_b3 / hbar_q ** 2
    target_lw = m_p / (m_e * geom_leading)
    reading_a_lw = mp.mpf("2.5") + (-G) * h2
    residual = target_lw - reading_a_lw  # ≈ -1.38e-5
    c_4_empirical = residual / h4

    print(f"\nEmpirical c_4 (from Reading-A h⁴ residual):")
    print(f"  residual = target_lw - (5/2 - G·h²) = {mp.nstr(residual, 12)}")
    print(f"  c_4_empirical = residual / h⁴ = {mp.nstr(c_4_empirical, 15)}")

    # === K-theory prediction: r_2^(2) / r_2 = -6G / 8G = -3/4 ===
    # Per audit 2026-05-24 §4:
    # "higher regulator r_2^(2) is conjecturally −6G, giving h⁴ = −3/4 K-theoretically"
    c_4_ktheory_pred = -mp.mpf(3) / 4
    print(f"\nK-theory regulator prediction:")
    print(f"  r_2 = Vol(𝓑_3) = 8·G = {mp.nstr(vol_b3, 12)}")
    print(f"  r_2^(2) (conjectural) = -6·G = {mp.nstr(-6 * G, 12)}")
    print(f"  c_4 = r_2^(2) / Vol(𝓑_3) = -6G / 8G = -3/4 = {mp.nstr(c_4_ktheory_pred, 12)}")

    # === Comparison ===
    print(f"\n[Comparison]")
    print(f"  c_4_ktheory = -3/4 = {mp.nstr(c_4_ktheory_pred, 12)}")
    print(f"  c_4_empirical    = {mp.nstr(c_4_empirical, 12)}")
    ratio = c_4_ktheory_pred / c_4_empirical
    print(f"  ratio (ktheory / empirical) = {mp.nstr(ratio, 6)} ← K-theory is ~100× larger")

    # m_p prediction under K-theory c_4
    lw_with_ktheory = mp.mpf("2.5") + (-G) * h2 + c_4_ktheory_pred * h4
    m_p_with_ktheory = m_e * geom_leading * lw_with_ktheory
    ppm_with_ktheory = (m_p_with_ktheory - m_p) / m_p * 1e6
    print(f"\n  m_p with K-theory c_4 = -3/4: {mp.nstr(m_p_with_ktheory, 12)} MeV  "
          f"({mp.nstr(ppm_with_ktheory, 6)} ppm)")
    print(f"  m_p with Reading-A h²-only:    938.2773607 MeV  (+5.62 ppm)")
    print(f"  m_p with c_4 = -α (curiosity): 938.2720439 MeV  (-0.05 ppm)")
    print(f"  m_p CODATA:                     938.2720882 MeV  (0 ppm)")

    print(f"\n[Verdict on K-theory prediction]")
    if abs(ppm_with_ktheory) > 100:
        print(f"  ✗ K-theory c_4 = -3/4 gives {mp.nstr(ppm_with_ktheory, 6)} ppm — MUCH WORSE")
        print(f"    than Reading-A alone or α-curiosity. Direct K-theory")
        print(f"    K_3-regulator hypothesis is RULED OUT as the source of c_4.")
    else:
        print(f"  K-theory c_4 gives {mp.nstr(ppm_with_ktheory, 6)} ppm — comparable to alternatives.")

    print(f"\n[Open KLR directions]")
    print(f"  1. Demazure sub-crystal at H_5+: KL polynomial non-trivial,")
    print(f"     could give h² correction different from Family A's +3/4.")
    print(f"     Requires building KLR machinery — multi-session.")
    print(f"  2. K-theory r_2^(2) with DIFFERENT normalization: maybe c_4 =")
    print(f"     r_2^(2) / (8·G·factor) with factor ≈ 100. No obvious source")
    print(f"     for factor 100 in K-theory framework.")
    print(f"  3. Lifted Wedderburn via crystal-character: instead of")
    print(f"     (1/4)·Σ_{{λ⊢4}} dim_q V_λ, use a SUB-crystal sum that")
    print(f"     restricts to specific Demazure modules. Open question.")

    # Witness
    w.add_parameter("q_0_50dps", Q_50_DIGIT_STR)
    w.add_data("c_4_empirical_from_reading_a_residual", mp.nstr(c_4_empirical, 25))
    w.add_data("c_4_ktheory_prediction", mp.nstr(c_4_ktheory_pred, 25))
    w.add_data("ratio_ktheory_to_empirical", mp.nstr(ratio, 12))
    w.add_data("m_p_predictions_ppm", {
        "ktheory_c4_minus_3_over_4": mp.nstr(ppm_with_ktheory, 8),
        "reading_a_h2_only": "5.62",
        "alpha_curiosity": "-0.05",
    })
    w.add_data("verdict", (
        f"K-theory regulator prediction c_4 = -3/4 gives m_p residual "
        f"~{mp.nstr(abs(ppm_with_ktheory), 4)} ppm, ~{mp.nstr(abs(ppm_with_ktheory)/5.62, 4)}× "
        f"WORSE than Reading-A alone. The audit-2026-05-24 §4 "
        f"K-theory regulator hypothesis (r_2^(2) = -6G → c_4 = -3/4) "
        f"is RULED OUT as the direct source of the h⁴ correction. "
        f"Possible reframings (different normalization, lifted KLR "
        f"at H_5+ Demazure) require multi-session KLR machinery "
        f"build — out of single-session scope."
    ))
    w.add_data("open_directions", [
        "Demazure sub-crystal at H_5+ (Brundan-Kleshchev KLR)",
        "K-theory with re-normalized r_2^(2)/Vol",
        "Lifted Wedderburn via specific Demazure restrictions",
        "Crystal-graph distance ↔ h-order correlation (audit Probe C negative)",
    ])

    arithmetic_ok = abs(ratio) > mp.mpf("10")
    w.add_assertion(
        name="ktheory_prediction_ruled_out",
        computed=arithmetic_ok,
        expected=True,
        tolerance=0,
        source=(
            "K-theory r_2^(2) = -6G prediction gives c_4 = -3/4, "
            "which is >10× larger in magnitude than the empirical "
            "c_4 ≈ -7.2e-3 implied by Reading-A's h⁴ residual. "
            "This sanity-checks that the K-theory hypothesis is "
            "decisively negative (not within the same order of magnitude)."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
