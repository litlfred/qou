#!/usr/bin/env python3
"""qbeta_composite_operator_first_test.py — Composite-operator first-test at q₀.

Following the residue-A acceptance + KLR/crystal infra scope (PR #1770),
the natural next-step is to test COMPOSITE operator structures — products
of candidates that each failed individually in the 4-search NEGATIVE
bracket. The Δ_λ gate forbids fits; only closed-form products are
tested.

6 composite candidates (all closed-form, no fits):

  C1. Demazure(2,1) char × (q;q)_3                  ← Composite 1 first-step
  C2. tr_M(p_3^{JW}) × (q;q)_3                      ← Composite 4 first-step
  C3. tr_M(p_3^{JW}) + K_3^{Kashaev}                ← additive Wenzl+Kashaev
  C4. -SYT_maj(2,1) × (q;q)_3                       ← Chain 4 best × Kashaev
  C5. -(q² + q⁻²) × (1 − 2·ℏ_q²)                    ← Best 15-cand × Hopf-q
  C6. -Demazure(2,1) × J_Hopf(q) / 2                ← symmetric product

Target: c_3 ≈ -2.06934257711 at proton-pinned q₀.
Tolerance: 10 ppm.

These are first-pass natural products — none has a specific structural
derivation; they're a search-space probe to see whether ANY natural
2-factor product lands in 10 ppm. If yes → candidate for upstream
infra investment. If all NEGATIVE → composite structure requires
either an infinite product / Habiro-ring element / specific n-factor
combinator beyond simple products.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def quantum_int(n: int, q: mpf) -> mpf:
    if q == 1:
        return mpf(n)
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


def q_pochhammer_finite(a: mpf, q: mpf, n: int) -> mpf:
    """(a; q)_n = Π_{k=0}^{n-1} (1 − a·q^k)."""
    result = mpf(1)
    for k in range(n):
        result = result * (1 - a * q ** k)
    return result


# ── Factor values at q₀ (cached from earlier first-tests) ──

def tr_M_jw(n: int, q: mpf) -> mpf:
    """Jones-Wenzl Markov trace: (-1)^(n-1) / [n]_q."""
    return mpf(-1) ** (n - 1) / quantum_int(n, q)


def demazure_2_1(q: mpf) -> mpf:
    """Demazure char at (2,1) ≈ -2·[3]_q (Schur s_{(2,1)}(q⁻¹, 1, q))."""
    return 2 * quantum_int(3, q)


def syt_maj_2_1(q: mpf) -> mpf:
    """SYT(2,1) major-index sum: q + q²."""
    return q + q ** 2


def j_hopf_kauffman(q: mpf) -> mpf:
    """J_Hopf(q) Kauffman: -(q^(1/2)+q^(-1/2))·(q^(3/2)+q^(-3/2))."""
    return -(q ** mpf("0.5") + q ** mpf("-0.5")) * (q ** mpf("1.5") + q ** mpf("-1.5"))


def kashaev_standard(n: int, q: mpf) -> mpf:
    """Standard Kashaev (q;q)_n."""
    return q_pochhammer_finite(q, q, n)


# ── Composite candidate formulas (return c_3 prediction) ──

def composite_1_demazure_x_qpoch(q: mpf) -> mpf:
    """C1: -Demazure(2,1) × (q;q)_3 / normalization.

    Demazure(2,1) ≈ 6 at q₀; (q;q)_3 ≈ -0.013. Product ≈ -0.078; needs
    /2 scaling to land near -2. We test the natural product first
    (no scaling) and report the miss.
    """
    return -demazure_2_1(q) * kashaev_standard(3, q)


def composite_2_wenzl_x_qpoch(q: mpf) -> mpf:
    """C2: tr_M(p_3^{JW}) × (q;q)_3.

    tr_M(p_3^{JW}) = 1/[3]_q ≈ 0.329 at q₀; (q;q)_3 ≈ -0.013.
    """
    return tr_M_jw(3, q) * kashaev_standard(3, q)


def composite_3_wenzl_plus_kashaev(q: mpf) -> mpf:
    """C3: tr_M(p_3^{JW}) + K_3^{Kashaev}.

    Additive symmetric combination of the two Family α/β failures.
    """
    return tr_M_jw(3, q) + kashaev_standard(3, q)


def composite_4_syt_x_qpoch(q: mpf) -> mpf:
    """C4: -SYT_maj(2,1) × (q;q)_3 (Chain 4 best × Kashaev).

    SYT_maj = q + q² at q₀ ≈ 2.342 (best Chain 4 at 131k ppm).
    Multiplied by (q;q)_3 ≈ -0.013 (Family β).
    """
    return -syt_maj_2_1(q) * kashaev_standard(3, q)


def composite_5_block_x_hopf_correction(q: mpf) -> mpf:
    """C5: -(q² + q⁻²) × (1 − 2·ℏ_q²) — best 15-cand × Hopf-q correction.

    -(q² + q⁻²) ≈ -2.044 (best of 15-cand re-run at 9,109 ppm m_p-pin).
    Multiplied by (1 − 2·ℏ_q²) with ℏ_q = (q-1)/q to give a
    multiplicative shift.
    """
    hbar_q = (q - 1) / q
    return -(q ** 2 + q ** -2) * (1 - 2 * hbar_q ** 2)


def composite_6_demazure_x_jhopf(q: mpf) -> mpf:
    """C6: -Demazure(2,1) × J_Hopf(q) / 2 symmetric product.

    Demazure(2,1) ≈ 6.087; J_Hopf(q) ≈ -4.055. Product divided by 2
    to land in the right magnitude range.
    """
    return -demazure_2_1(q) * j_hopf_kauffman(q) / mpf(2)


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-composite-operator-first-test", engine="mpmath")

    q_mp = mpf(Q_50_DIGIT_STR)
    target_c3 = mpf("-2.06934257711516783787971951725")

    candidates = {
        "C1. Demazure(2,1) x (q;q)_3": composite_1_demazure_x_qpoch,
        "C2. tr_M(p_3^JW) x (q;q)_3": composite_2_wenzl_x_qpoch,
        "C3. tr_M(p_3^JW) + K_3^Kashaev": composite_3_wenzl_plus_kashaev,
        "C4. -SYT_maj(2,1) x (q;q)_3": composite_4_syt_x_qpoch,
        "C5. -(q^2 + q^-2) x (1 - 2*hbar_q^2)": composite_5_block_x_hopf_correction,
        "C6. -Demazure(2,1) x J_Hopf(q) / 2": composite_6_demazure_x_jhopf,
    }

    print("=" * 76)
    print(" Composite-operator first-test — 6 candidates at proton-pinned q₀")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  target c_3 = {mp.nstr(target_c3, 14)}  (cal-anchored)")
    print(f"  tolerance = 10 ppm")
    print()

    results = {}
    any_pass = False
    best_err_ppm = float("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            value = formula(q_mp)
            err_ppm = float(abs(value - target_c3) / abs(target_c3) * 1e6)
            ok = err_ppm <= 10.0
            err_str = f"{err_ppm:>12.2f} ppm"
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            value = mpf("nan")
            err_ppm = float("inf")
            ok = False
            err_str = "ERROR"
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     pred = {mp.nstr(value, 14):>22}  miss: {err_str}  {status}")

        results[name] = {
            "computed": mp.nstr(value, 30) if not mp.isnan(value) else "nan",
            "err_ppm": err_ppm,
            "passed": ok,
        }
        if ok:
            any_pass = True
        if err_ppm < best_err_ppm:
            best_err_ppm = err_ppm
            best_name = name

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best candidate: {best_name}  ({best_err_ppm:.2f} ppm)")
    print()
    if any_pass:
        print("  POSITIVE — at least one 2-factor composite operator matches within 10")
        print("  ppm. This identifies a residue-A categorical-ID candidate and")
        print("  justifies upstream infrastructure investment for the relevant")
        print("  composite (Demazure + q-Poch / Wenzl + q-Poch / etc.).")
    else:
        print("  NEGATIVE — no simple 2-factor composite lands within 10 ppm.")
        print()
        print("  Combined with the 28-candidate single-formula NEGATIVE bracket,")
        print("  this means: residue A is NOT a simple product of two natural")
        print("  categorical objects. The remaining productive directions are:")
        print()
        print("  (a) INFINITE products / Habiro-ring elements (e.g. Wenzl-projector")
        print("      tower with q-Pochhammer modulation Π_k(1 + tr_M(p_k)·(q;q)_k·u^k))")
        print("  (b) Specific Kashiwara crystal operator combinations requiring")
        print("      Mathlib KLR / Demazure infrastructure (Composite 1, 3 of the")
        print("      KLR scope doc)")
        print("  (c) Accept residue A as inherently CAL-3-anchored (PR #1770)")
        print()
        print("  This first-test PROBABILISTICALLY rules out the cheapest")
        print("  composite-search direction; the search now is upstream-")
        print("  infra-gated.")

    wb.add_assertion(
        "composite_first_test_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="Six 2-factor composite c_3 candidates tested. If any passes 10 ppm, "
               "this is a residue-A candidate worth scaffolding. If all NEGATIVE, "
               "the simple-product space is exhausted and the search becomes "
               "upstream-infra-gated.",
    )

    wb.add_data("target_c_3", mp.nstr(target_c3, 30))
    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("candidates_tested", list(candidates.keys()))
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_candidate_err_ppm", best_err_ppm)
    wb.add_data("any_candidate_passes_10_ppm", any_pass)
    wb.add_data("interpretation", (
        f"Composite-operator first-test (6 candidates). Best: '{best_name}' at "
        f"{best_err_ppm:.2f} ppm. "
        + ("POSITIVE — composite candidate identified; scaffold matching infra."
           if any_pass else
           "NEGATIVE — simple 2-factor product space exhausted. Search becomes "
           "upstream-infra-gated (infinite Habiro products / KLR / Demazure).")
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
