#!/usr/bin/env python3
"""qbeta_composite4_wenzl_qpochhammer_first_probe.py — Composite 4 first probe.

Task 2 of the 2026-06-04 Habiro follow-up. The FIRST probe exercising the
`QOU.Machinery.QPochhammer` Lean scaffold (PR #1791) — a Python mirror of
its `qPochhammerFinite` / `qPochhammerDiag` definitions, applied to the
Composite 4 candidate for the Q_β residue A.

## Background — why Composite 4

PR #1773 exhausted the simple 2-factor product space for c_3 (6 NEGATIVE;
cumulative 34/34 NEGATIVE). Its key sub-finding: the multiplicative
ℏ_q²-correction drives the WRONG direction; "the infinite-product
structure is genuinely needed." PR #1770's KLR/crystal scope names
Composite 4 — **Wenzl projector × q-Pochhammer INFINITE-product tower** —
as the cheapest infra-gated path (5-6 sessions).

This probe is the first reconnaissance: test whether a truncated
q-Pochhammer tower factor on the best base `-(q²+q⁻²)` moves c_3 toward
target, and BOUND the q-Pochhammer composite space.

## q-Pochhammer at q₀ > 1 — convergent direction

`(q;q)_N = Π_{k=1}^N (1 - q^k)` DIVERGES for q₀ ≈ 1.11 (|q^k| → ∞).
The convergent Habiro object is `(q⁻¹;q⁻¹)_N = Π_{k=1}^N (1 - q⁻ᵏ)`
(q⁻¹ ≈ 0.901 < 1). Both mirror the Lean `qPochhammerFinite a q n`
with `a = q⁻¹, q = q⁻¹`.

## Δ_λ-gate

Expected NEGATIVE (this is reconnaissance, not a wire). Every candidate
is a closed-form product of categorical objects — no fit. The NEGATIVE
result bounds the space and exercises the #1791 machinery; the real
Composite 4 needs linear-combination `tr_M` in `pyhecke` (PR #1773
implication), out of scope for a single probe.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

C3_TARGET = "-2.06934257711516783787971951725"


# ── Python mirror of QOU.Machinery.QPochhammer (Lean, PR #1791) ──

def q_pochhammer_finite(a: mpf, q: mpf, n: int) -> mpf:
    """Mirror of Lean `qPochhammerFinite a q n = ∏_{k=0}^{n-1} (1 - a·q^k)`."""
    prod = mpf(1)
    for k in range(n):
        prod *= (1 - a * q ** k)
    return prod


def q_pochhammer_diag(q: mpf, n: int) -> mpf:
    """Mirror of Lean `qPochhammerDiag q n = qPochhammerFinite q q n`."""
    return q_pochhammer_finite(q, q, n)


def quantum_int(n: int, q: mpf) -> mpf:
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


def wenzl_markov_p3(q: mpf) -> mpf:
    """Markov-trace weight of the n=3 Jones-Wenzl projector (proxy).

    The unnormalised Markov trace of p_n in the Temperley-Lieb tower is
    the quantum dimension ratio; for n=3 we use the [3]_q quantum
    dimension as the leading proxy (the true tr_M(p_3) needs the
    pyhecke linear-combination extension — see module docstring)."""
    return quantum_int(3, q)


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-composite4-wenzl-qpochhammer-first-probe", engine="mpmath")

    q = Q_MP
    target = mpf(C3_TARGET)
    qinv = 1 / q
    base = -(q ** 2 + q ** -2)
    hbar = (q - 1) / q

    # Sanity: print the q-Pochhammer tower values (convergent direction).
    print("=" * 78)
    print(" Composite 4 first probe — Wenzl × q-Pochhammer tower for c_3")
    print("=" * 78)
    print(f"  q₀ = {mp.nstr(q, 14)}   q⁻¹ = {mp.nstr(qinv, 12)}")
    print(f"  base = -(q²+q⁻²) = {mp.nstr(base, 14)}   target c_3 = {mp.nstr(target, 14)}")
    print(f"  needed correction factor = target/base = {mp.nstr(target / base, 12)}")
    print()
    print("  q-Pochhammer tower (convergent (q⁻¹;q⁻¹)_N):")
    for N in range(1, 7):
        print(f"    (q⁻¹;q⁻¹)_{N} = {mp.nstr(q_pochhammer_finite(qinv, qinv, N), 12)}")
    print()

    wmark = wenzl_markov_p3(q)

    # 8 Composite-4 candidates: base × [tower / Wenzl factor].
    candidates = {
        # truncated (q⁻¹;q⁻¹)_N multiplicative corrections
        "P1. base·(1 + ℏ_q·(1-(q⁻¹;q⁻¹)_3))":
            base * (1 + hbar * (1 - q_pochhammer_finite(qinv, qinv, 3))),
        "P2. base·(1 + ℏ_q²·(q⁻¹;q⁻¹)_2)":
            base * (1 + hbar ** 2 * q_pochhammer_finite(qinv, qinv, 2)),
        "P3. base·(2 - (q⁻¹;q⁻¹)_∞≈_6)":
            base * (2 - q_pochhammer_finite(qinv, qinv, 6)),
        "P4. base·(1 + ℏ_q·[3]_q·(q⁻¹;q⁻¹)_4/25)":
            base * (1 + hbar * wmark * q_pochhammer_finite(qinv, qinv, 4) / 25),
        # Wenzl-Markov × q-Pochhammer products (not base-anchored)
        "P5. -[3]_q·(q⁻¹;q⁻¹)_2":
            -wmark * q_pochhammer_finite(qinv, qinv, 2),
        "P6. -[3]_q/(q⁻¹;q⁻¹)_3":
            -wmark / q_pochhammer_finite(qinv, qinv, 3),
        # base × Wenzl-tower correction at the [3]_q/25 Habiro scale
        "P7. base·(1 + ℏ_q·[3]_q/25 + (q⁻¹;q⁻¹)_5·ℏ_q³)":
            base * (1 + hbar * quantum_int(3, q) / 25
                    + q_pochhammer_finite(qinv, qinv, 5) * hbar ** 3),
        "P8. base·(1 + (1-(q⁻¹;q⁻¹)_∞≈_6)·ℏ_q²·b)":
            base * (1 + (1 - q_pochhammer_finite(qinv, qinv, 6)) * hbar ** 2 * hoefsmit_b(q)),
    }

    print("─" * 78)
    print(f"  {'candidate':<52} {'c_3 pred':>12} {'miss ppm':>12}")
    print("─" * 78)
    results = {}
    any_pass = False
    best_ppm = float("inf")
    best_name = None
    for name, val in candidates.items():
        ppm = float(abs(val - target) / abs(target) * 1e6)
        ok = ppm <= 10.0
        results[name] = {"c3_pred": mp.nstr(val, 24), "miss_ppm": ppm, "passed": ok}
        if ok:
            any_pass = True
        if ppm < best_ppm:
            best_ppm = ppm
            best_name = name
        print(f"  {name:<52} {mp.nstr(val, 10):>12} {ppm:>12.1f}")

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"  Best: {best_name}  ({best_ppm:.1f} ppm)")
    if any_pass:
        print("  ★ POSITIVE — a Wenzl × q-Pochhammer composite closes c_3 ≤ 10 ppm.")
    else:
        print("  NEGATIVE — no truncated q-Pochhammer composite closes c_3.")
        print("  Cumulative single+composite NEGATIVE bracket: 34 (prior) + 8 = 42.")
        print("  The q-Pochhammer tower (truncated, archimedean q₀) does NOT")
        print("  supply the residue A correction. The real Composite 4 needs the")
        print("  FIBRE-level Habiro element (formal q, pre-τ) per AGENTS.md")
        print("  'Im(q) at fibre vs observable' — i.e. the q-Pochhammer evaluated")
        print("  as a Habiro-ring element at roots of unity, then τ-functored,")
        print("  NOT a real archimedean truncation. That needs the pyhecke")
        print("  linear-combination tr_M extension (PR #1773 implication).")

    wb.add_assertion(
        "composite4_qpochhammer_at_least_one_closes_10_ppm",
        computed=any_pass,
        expected=False,
        source="8 Wenzl × truncated-q-Pochhammer composites for c_3 at proton-"
               "pinned q₀. NEGATIVE expected — bounds the archimedean q-Pochhammer "
               "space and exercises the PR #1791 QPochhammer machinery. The real "
               "Composite 4 is fibre-level (Habiro-ring at roots of unity), needing "
               "pyhecke linear-combination tr_M.",
    )

    wb.add_data("q_substrate", mp.nstr(q, 30))
    wb.add_data("c3_target", mp.nstr(target, 30))
    wb.add_data("base_neg_q2_plus_qinv2", mp.nstr(base, 30))
    wb.add_data("wenzl_markov_p3_proxy", mp.nstr(wmark, 30))
    wb.add_data("qpochhammer_tower_qinv", {
        f"N={N}": mp.nstr(q_pochhammer_finite(qinv, qinv, N), 24) for N in range(1, 7)
    })
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_candidate_miss_ppm", best_ppm)
    wb.add_data("any_candidate_passes_10_ppm", any_pass)
    wb.add_data("machinery_exercised", "QOU.Machinery.QPochhammer (PR #1791) — "
                "Python mirror of qPochhammerFinite / qPochhammerDiag")
    wb.add_data("interpretation", (
        f"Composite 4 first probe: 8 Wenzl × truncated-q-Pochhammer composites, "
        f"best {best_name} at {best_ppm:.1f} ppm — "
        + ("POSITIVE." if any_pass else
           "NEGATIVE. The archimedean (real q₀ > 1) q-Pochhammer truncation does "
           "not supply residue A. The real Composite 4 is a FIBRE-level Habiro-ring "
           "element (formal q at roots of unity, pre-τ), gated on the pyhecke "
           "linear-combination tr_M extension. Cumulative NEGATIVE bracket: 42.")
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"{'all passed' if all(a.passed for a in wb.assertions) else 'FAILURES'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
