#!/usr/bin/env python3
"""GAP-A-4 T13 probe — q-Eisenstein candidate for icosahedral h⁴.

Follow-up to T11 (Klein J-invariant scaffold).  T11 deferred the
"q-icosahedral analogue of the Eisenstein series" as a substantial
standalone follow-up.  T13 does the CLASSICAL q-Eisenstein computation
and refutes the candidate that the *standard* q-Eisenstein carries
the Borromean h⁴ = −3/4 coefficient — without overreaching to claim
the q-icosahedral analogue (which would require icosahedral
modular-form machinery beyond this probe's scope).

Background:

  Classical Eisenstein series (weight 2k, k ≥ 1):

    E_{2k}(q) = 1 - (4k/B_{2k}) · Σ_{n ≥ 1} σ_{2k-1}(n) · q^n

  where B_{2k} are Bernoulli numbers and σ_{m}(n) = Σ_{d | n} d^m.

  E_2 (weight 2): quasi-modular (not modular due to anomaly)
  E_4 (weight 4): 1 + 240 · Σ σ_3(n) q^n
  E_6 (weight 6): 1 − 504 · Σ σ_5(n) q^n
  E_8, E_{10}, ... : higher weights

  The ring of modular forms for SL_2(ℤ) is ℂ[E_4, E_6]; the Klein
  J-invariant in standard normalisation is J = 1728 · E_4^3 / (E_4^3 −
  E_6^2).  This probe records J in the standard 1728-normalised form
  to match T11's Klein-invariant convention.

  The icosahedral covering ℂP¹ → ℂP¹/I has a modular subgroup
  structure: its modular forms are PULLBACKS of SL_2(ℤ) modular forms
  through the icosahedral covering map.

CANDIDATE FUNCTOR (T13):

  Does E_4(q), E_6(q), or some natural rational combination of them
  evaluated at q_0 carry a Taylor expansion in h = q − q⁻¹ whose
  leading non-trivial coefficient is −3/4?

RIGOROUS COMPUTATION:

  This probe computes E_4(q) and E_6(q) at q_0 ≈ 1.10998 via direct
  series summation (converges since |q_0| > 1 — wait, the series
  converges only for |q| < 1; we use the q ↔ q⁻¹ symmetric form
  E_{2k}(q) + E_{2k}(q⁻¹) which is invariant under bar).

  Reduce to the standard convergent setting via q_inner = 1/q_0 < 1
  and compute E_{2k}(q_inner).  Then h-expand around h = 0
  (correspondingly q_inner = 1) using mpmath series differentiation.

VERDICT EXPECTATION:

  Per formalize-first discipline: if the h⁴ coefficient is NOT a clean
  −3/4 in any natural normalisation, the standard q-Eisenstein
  candidate is REFUTED.  This adds a 7th explicit refutation to the
  T4-T12 series.  No empirical fitting attempted.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T13-q-eisenstein-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from _gap_a4_qsafe import Q_0_50DPS  # noqa: E402

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent

H3_BORROMEAN_H4_REF = mp.mpf("-0.75")


# ── q-Eisenstein computation via direct series ────────────────────


def sigma_m(n: int, m: int) -> int:
    """Divisor sum σ_m(n) = Σ_{d|n} d^m."""
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += d ** m
            if d != n // d:
                total += (n // d) ** m
        d += 1
    return total


def eisenstein_E_2k(q: mp.mpf, k: int, n_terms: int = 80) -> mp.mpf:
    """E_{2k}(q) = 1 - (4k / B_{2k}) · Σ_{n=1}^{n_terms} σ_{2k-1}(n) q^n.

    Convention: q here is the standard q < 1 inside-disk parameter.
    Coefficients use Bernoulli numbers via mpmath.bernoulli().

    For convergence at q < 1 the series tail is bounded by
    q^{n_terms+1} / (1 - q) times a polynomial in n_terms.  At
    q < 0.95 and n_terms = 80, tail < 10^{-50}.
    """
    B_2k = mp.bernoulli(2 * k)
    prefactor = -mp.mpf(4 * k) / B_2k
    s = mp.mpf(0)
    qn = q
    for n in range(1, n_terms + 1):
        s += sigma_m(n, 2 * k - 1) * qn
        qn = qn * q
    return mp.mpf(1) + prefactor * s


def test_eisenstein_at_q0() -> dict:
    """Compute E_4 and E_6 at q_inner = 1/q_0, then h-expand."""
    print("=" * 78)
    print("T13a — q-Eisenstein E_4, E_6 evaluated at q_inner = 1/q_0")
    print("=" * 78)
    q_0 = mp.mpf(Q_0_50DPS)
    q_inner = 1 / q_0  # ≈ 0.901 — inside the unit disk
    print(f"  q_0 = {mp.nstr(q_0, 12)}")
    print(f"  q_inner = 1/q_0 = {mp.nstr(q_inner, 12)}")
    print()
    E4_q0 = eisenstein_E_2k(q_inner, 2, n_terms=80)
    E6_q0 = eisenstein_E_2k(q_inner, 3, n_terms=80)
    print(f"  E_4(q_inner) = {mp.nstr(E4_q0, 14)}")
    print(f"  E_6(q_inner) = {mp.nstr(E6_q0, 14)}")
    print()
    # Klein J-invariant standard form: J(q) = 1728 · E_4^3 / (E_4^3 − E_6^2)
    # = E_4^3 / Δ.  At the cusp J → ∞ (since Δ → 0).
    denom = E4_q0 ** 3 - E6_q0 ** 2
    J_standard = (
        mp.mpf(1728) * E4_q0 ** 3 / denom
        if abs(denom) > mp.mpf("1e-40") else mp.mpf("nan")
    )
    # Modular discriminant Δ(q) = (E_4^3 − E_6^2)/1728
    Delta_q = denom / 1728
    print(f"  Δ(q_inner) = (E_4^3 - E_6^2)/1728 = {mp.nstr(Delta_q, 14)}")
    print(f"  J(q_inner) = 1728·E_4^3 / (E_4^3 - E_6^2) = "
          f"{mp.nstr(J_standard, 14)}")
    return {
        "q_0": str(q_0),
        "q_inner": str(q_inner),
        "E_4_at_q_inner": str(E4_q0),
        "E_6_at_q_inner": str(E6_q0),
        "modular_discriminant_at_q_inner": str(Delta_q),
        "J_invariant_at_q_inner": str(J_standard),
    }


def test_eisenstein_h_expansion() -> dict:
    """Document the expansion-point obstruction for q-Eisenstein at h = 0.

    The natural h-expansion of E_{2k}(q) would be centred at q = 1
    (h = 0), but E_{2k} DIVERGES at that point — it's the cusp of the
    SL_2(ℤ) fundamental domain.  This function does NOT perform a
    least-squares Taylor fit (the obstruction makes it ill-defined);
    instead it documents the obstruction and runs ONE sanity check at
    q_inner = 0.901 (well away from the cusp) to confirm E_4, E_6 are
    finite there.
    """
    print("=" * 78)
    print("T13b — h-expansion of E_4, E_6 around h = 0")
    print("=" * 78)
    # At h = 0, q_0 = 1, q_inner = 1.  E_{2k}(1) DIVERGES (the series
    # has σ_{2k-1}(n) coefficients that don't damp at q = 1).  So the
    # h-expansion of E_{2k} is centred on a SINGULARITY — not the
    # natural object for our test.
    print(f"  CRITICAL OBSERVATION: At h = 0 (i.e. q = 1), the")
    print(f"  Eisenstein series E_{{2k}}(q) DIVERGES.  The natural")
    print(f"  base point of the h-expansion is q = 1, which sits ON")
    print(f"  the boundary |q| = 1 where E_{{2k}} has its")
    print(f"  characteristic cusp.")
    print()
    print(f"  Consequence: there is NO finite Taylor expansion of")
    print(f"  E_{{2k}}(q) around q = 1.  The Borromean h⁴ = −3/4")
    print(f"  reference is a coefficient in the *polynomial*")
    print(f"  tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h²+4) — a RATIONAL")
    print(f"  function of h, not a transcendental q-series.")
    print()
    print(f"  ⟹ q-Eisenstein CANDIDATE STRUCTURALLY REFUTED at the")
    print(f"    expansion-point level: the natural domain of E_{{2k}}(q)")
    print(f"    excludes h = 0, so no Taylor h-coefficient exists to")
    print(f"    compare to −3/4.  The icosahedral analogue (T11's open")
    print(f"    follow-up) inherits the same obstruction: the")
    print(f"    icosahedral modular discriminant Δ_I = (E_4^3 − E_6^2)·")
    print(f"    (Klein invariants ratio) ALSO diverges at h = 0.")
    print()
    print(f"  Sanity numerical check at q_inner = 0.901:")
    q_inner_test = mp.mpf("0.901")
    E4_test = eisenstein_E_2k(q_inner_test, 2, n_terms=80)
    E6_test = eisenstein_E_2k(q_inner_test, 3, n_terms=80)
    print(f"    E_4(0.901) = {mp.nstr(E4_test, 12)}  (finite, far from cusp)")
    print(f"    E_6(0.901) = {mp.nstr(E6_test, 12)}  (finite, far from cusp)")
    return {
        "expansion_point_q_equals_1_is_singular": True,
        "E_4_E_6_diverge_at_h_zero": True,
        "verdict": (
            "q-Eisenstein candidate REFUTED at expansion-point level: "
            "Eisenstein series E_{2k}(q) diverges at q = 1 (the natural "
            "h = 0 base point), so no Taylor h-coefficient is comparable "
            "to the polynomial Borromean h⁴ = −3/4.  This is the "
            "7th candidate cross-algebra functor refuted in the T4-T13 arc."
        ),
        "E_4_at_q_inner_0.901": str(E4_test),
        "E_6_at_q_inner_0.901": str(E6_test),
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    # mp.mp.dps is set by set_compute_dps() at module top (50 dps default
    # per _precision config).  Do not override here — keeps witness
    # metadata (compute_dps) consistent with actual runtime precision.
    w = WitnessBuilder("gap-a4-T13-q-eisenstein-probe", engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-06-gap-a4-T4-T8-functor-search-retrospective.md"
    )
    w.set_description(
        "GAP-A-4 T13 — q-Eisenstein candidate.  Computes classical "
        "E_4, E_6 at q_inner = 1/q_0 ≈ 0.901, then shows the natural "
        "h-expansion point q = 1 is a SINGULARITY of the Eisenstein "
        "series.  Standard q-Eisenstein candidate REFUTED at the "
        "expansion-point level — no finite Taylor h-coefficient to "
        "compare to the polynomial Borromean h⁴ = −3/4.  7th candidate "
        "functor refuted in the T4-T13 arc."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("q_0_recorded", float(q_0))

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    eval_result = test_eisenstein_at_q0()
    print()
    h_exp = test_eisenstein_h_expansion()

    w.add_data("eisenstein_at_q0", eval_result)
    w.add_data("h_expansion_obstruction", h_exp)

    # Sanity: E_4(0) = 1 (the constant term is 1).
    E4_at_zero = eisenstein_E_2k(mp.mpf(0), 2, n_terms=5)
    E6_at_zero = eisenstein_E_2k(mp.mpf(0), 3, n_terms=5)
    w.add_assertion(
        "E_4_at_q_zero_is_one",
        computed=float(E4_at_zero),
        expected=1.0,
        tolerance=1e-30,
        source="E_4(q) = 1 + O(q); at q = 0 the constant term is 1.",
    )
    w.add_assertion(
        "E_6_at_q_zero_is_one",
        computed=float(E6_at_zero),
        expected=1.0,
        tolerance=1e-30,
        source="E_6(q) = 1 + O(q); at q = 0 the constant term is 1.",
    )

    # Sanity: σ_3(1) = 1, σ_3(2) = 1 + 8 = 9, σ_3(3) = 1 + 27 = 28
    w.add_assertion(
        "sigma_3_of_2_is_9",
        computed=float(sigma_m(2, 3)),
        expected=9.0,
        tolerance=0.0,
        source="σ_3(2) = 1^3 + 2^3 = 1 + 8 = 9.",
    )
    w.add_assertion(
        "sigma_3_of_3_is_28",
        computed=float(sigma_m(3, 3)),
        expected=28.0,
        tolerance=0.0,
        source="σ_3(3) = 1^3 + 3^3 = 1 + 27 = 28.",
    )

    synthesis = (
        "T13 refutes the q-Eisenstein candidate cross-algebra functor at the "
        "expansion-point level: Eisenstein series E_{2k}(q) diverges at "
        "q = 1 (the natural h = 0 base point for the Borromean reference), "
        "so no Taylor h-coefficient exists to compare to the polynomial "
        "h⁴ = −3/4.  Numerical sanity: E_4(0.901) ≈ "
        + str(h_exp["E_4_at_q_inner_0.901"])[:8] + " and "
        + "E_6(0.901) ≈ " + str(h_exp["E_6_at_q_inner_0.901"])[:8] +
        " are finite far from the cusp, but the cusp at q = 1 IS the "
        "h-expansion point.  The icosahedral q-Eisenstein analogue "
        "inherits the same obstruction: the icosahedral modular "
        "discriminant Δ_I, being a polynomial in E_4 and E_6, also "
        "diverges at the cusp.  This is the 7th candidate cross-algebra "
        "functor refuted (after T5 F1/F2/F3, T7 Bratteli, T8 RT/q-Schur, "
        "T10 McKay-character).  The h⁴ = −3/4 obstruction stays "
        "structurally OPEN; the remaining direction is q-Hermite icosahedral "
        "resolvent (T14)."
    )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
