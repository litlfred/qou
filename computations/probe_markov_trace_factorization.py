#!/usr/bin/env python3
"""Probe — `thm:markov-trace-factorization` (I1: proved-in-Lean, no probe).

Claim (content block
`content/quantum-observable-universe/mass-theory/markov-trace-factorization.md`,
Lean `qou:QOU.Archimedean.markov_trace_factorization` + siblings):

The Markov trace of the nuclear braid word factors exactly as a product of
Markov-traced generator volumes:

    tr_Markov(N(Z,N)) = Π_{i=0}^{A-2} (z·a_i + b_i),     z = 1/(q^{1/2}+q^{-1/2}),

where (a_i, b_i) come from the transfer-matrix recurrence over the per-pair
crossing factors (c_j, d_j) and the Hecke reduction σ² = (q-q⁻¹)σ + 1
(`prop:generator-volume-decomposition`). The Lean file additionally proves:

  - `markov_trace_factorization_mul` (Wenzl §1.7 disjoint multiplicativity):
        fold(c₁ ++ c₂) = fold(c₁) · fold(c₂);
  - `asymptoticRatio_eq_inv_hbar` / `asymptoticRatio_at_q`:
        tr(L_0)/tr(parent) → 1/ℏ_q = 1/(1-q⁻¹) ≈ 10.116 at q₀;
  - the crossing-type transfer matrices T_j with det(T_j) per the .md table.

WHAT THIS PROBE VERIFIES:

  (1) FACTORIZATION ⇄ CANONICAL ENGINE (algebraic preflight, compute-author
      §3). The transfer-matrix recurrence's traced volume V̂ = z·a + b for a
      single-generator crossing chain equals the canonical Markov trace of the
      equivalent braid word computed by markov/markov_trace_canonical.tr_M_word
      — verified SYMBOLICALLY (exact, all q) for:
        - proton-proton chains  (c,d)=(1,0):   product = σ^k,      vs tr_M(σ^k)
        - neutron-neutron chains (c,d)=(1,-h):  product = (σ⁻¹)^k,  vs tr_M((σ-h)^k)
      This is the load-bearing check: it ties the .md/.lean recurrence to the
      authoritative Jones–Markov trace, not just to itself.

  (2) MULTIPLICATIVITY (the proved Lean lemma `markov_trace_factorization_mul`):
        fold(c₁ ++ c₂) == fold(c₁)·fold(c₂)
      verified symbolically in ℚ(q) and numerically at q₀ to ≤ 1e-25.

  (3) ASYMPTOTIC RATIO (`asymptoticRatio_at_q`):
        1/ℏ_q = 1/(1-q⁻¹) ≈ 10.116 at q₀, matching the Lean numerical lemma.

  (4) CROSSING DETERMINANTS (the .md table): det(T_j) symbolically:
        pp = -1,  nn = -1,  mixed = -1 + ¼(q-q⁻¹)².

The factorization recurrence below is reproduced EXACTLY as the proposition
specifies (it IS the claim's machinery); the verification is the cross-check
(1) against the independent canonical engine, plus the proved structural
lemmas (2)-(4). Per formalize-first (§3.3) this is a structural-identity
verification, not a parameter scan.

Run:  python3 -u computations/probe_markov_trace_factorization.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from markov.markov_trace_canonical import tr_M_word, tr_M_element  # noqa: E402
from hecke_symbolic import (  # noqa: E402
    SymbolicHeckeElement, SymbolicHeckeDivision, HA as H_full,
)
from qou_substrate import Q_50_DIGIT_STR, WitnessBuilder  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS, OUTPUT_DPS  # noqa: E402

mp.mp.dps = COMPUTE_DPS + 15
TOL = mp.mpf("1e-25")

# Symbolic q-data
QS = sp.Symbol("q", positive=True)
HS = QS - 1 / QS                          # h = q - q⁻¹
ZS = 1 / (sp.sqrt(QS) + 1 / sp.sqrt(QS))  # Markov parameter z


def chain_ab(coeffs, h=HS):
    """Transfer-matrix recurrence: start (a,b)=(0,1) (identity), fold each
    crossing factor (c,d) via (a σ + b)(c σ + d) and σ² = h σ + 1.
    Mirrors prop:generator-volume-decomposition exactly."""
    a, b = sp.Integer(0), sp.Integer(1)
    for (c, d) in coeffs:
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return a, b


def traced_volume(coeffs, z=ZS, h=HS):
    """V̂ = z·a + b for the chain of crossing factors."""
    a, b = chain_ab(coeffs, h)
    return z * a + b


def fold_factorization(ab_pairs, z=ZS):
    """Π_i (z·a_i + b_i) over a list of per-generator (a_i, b_i) pairs.

    This mirrors the Lean `markov_trace_factorization`/`_mul` fold exactly:
    its argument is `List (ℝ × ℝ)` of already-reduced (a_i, b_i) chain
    coefficients, folded as Π (z·a_i + b_i) — NOT a list of (c,d) crossing
    factors (those are folded by chain_ab into one (a_i, b_i) per generator)."""
    prod = sp.Integer(1)
    for (a, b) in ab_pairs:
        prod = prod * (z * a + b)
    return prod


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    z0 = 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))
    h0 = q0 - 1 / q0

    w = WitnessBuilder("probe-markov-trace-factorization", engine="sympy")
    w.set_description(
        "Verifies thm:markov-trace-factorization: the transfer-matrix "
        "factorization Pi(z*a_i+b_i) matches the canonical "
        "markov/markov_trace_canonical engine (pp -> sigma^k, nn -> sigma^-k, "
        "exact in Q(q)); Wenzl disjoint-multiplicativity "
        "markov_trace_factorization_mul; the 1/hbar_q ~ 10.116 asymptotic "
        "ratio at q0; and the crossing-determinant table."
    )
    w.set_content_block("thm:markov-trace-factorization")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("tolerance", "1e-25")

    # ── (1) factorization ⇄ canonical engine (symbolic, exact in ℚ(q)) ──
    pp_ok, nn_ok = [], []
    div = SymbolicHeckeDivision()
    for k in (1, 2, 3, 4):
        # proton-proton: factor (1, 0) → product is σ^k
        vhat_pp = sp.simplify(traced_volume([(1, 0)] * k))
        tr_pp = sp.simplify(tr_M_word((0,) * k, 2, ZS, HS))
        pp_ok.append(sp.simplify(vhat_pp - tr_pp) == 0)
    for k in (1, 2, 3):
        # neutron-neutron: factor (1, -h) = σ - h = σ⁻¹ → product (σ⁻¹)^k
        vhat_nn = sp.expand(sp.simplify(traced_volume([(1, -HS)] * k)))
        s_inv = SymbolicHeckeElement({(0,): sp.Integer(1), (): -H_full})
        el = s_inv
        for _ in range(k - 1):
            el = el * s_inv
        el, _ = div.reduce(el, engine="laurent")
        tr_nn = sp.expand(tr_M_element(el, 2, z=ZS, h=HS))
        nn_ok.append(sp.simplify(vhat_nn - tr_nn) == 0)

    w.add_assertion(
        "traced-volume(pp chain) == tr_M(sigma^k) for k=1..4 (symbolic, all q)",
        computed=str(all(pp_ok)),
        expected="True",
        source="recurrence vs markov_trace_canonical.tr_M_word",
    )
    w.add_assertion(
        "traced-volume(nn chain) == tr_M(sigma^-k) for k=1..3 (symbolic, all q)",
        computed=str(all(nn_ok)),
        expected="True",
        source="recurrence vs markov_trace_canonical (sigma-h basis)",
    )

    # ── (2) multiplicativity: fold(c1++c2) == fold(c1)*fold(c2) ──
    # Lean lemma operates on lists of per-generator (a_i, b_i) pairs. Build
    # genuine (a_i, b_i) pairs from real crossing chains so the inputs are
    # the actual factorization data, not arbitrary numbers.
    c1 = [chain_ab([(1, 0), (1, -HS)]),          # one generator, pp then nn
          chain_ab([(1, -HS / 2)])]               # one generator, mixed
    c2 = [chain_ab([(1, -HS), (1, 0)]),           # one generator, nn then pp
          chain_ab([(1, 0), (1, 0)])]             # one generator, pp twice
    lhs_s = sp.simplify(fold_factorization(c1 + c2))
    rhs_s = sp.simplify(fold_factorization(c1) * fold_factorization(c2))
    mul_exact = sp.simplify(lhs_s - rhs_s) == 0
    w.add_assertion(
        "fold(c1++c2) - fold(c1)*fold(c2) == 0 in Q(q) "
        "(Lean markov_trace_factorization_mul, Wenzl 1.7)",
        computed=str(sp.simplify(lhs_s - rhs_s)),
        expected="0",
        source="sympy.simplify (exact, all q)",
    )
    # numerical at q0
    lhs_n = mp.mpf(fold_factorization(c1 + c2).subs(QS, q0))
    rhs_n = mp.mpf((fold_factorization(c1) * fold_factorization(c2)).subs(QS, q0))
    mul_resid = abs(lhs_n - rhs_n)
    w.add_assertion(
        "fold(c1++c2) == fold(c1)*fold(c2) at q0 (<=1e-25)",
        computed=mp.nstr(mul_resid, 6),
        expected="0",
        tolerance=float(TOL),
        source="numerical at substrate q0",
    )

    # ── (3) asymptotic ratio 1/ℏ_q at q0 (Lean asymptoticRatio_at_q) ──
    # The Lean numerical lemma uses the ROUNDED literal q = 1.1097 (giving
    # ~10.116); at the FULL-precision substrate q0 = 1.10997859... the value
    # is ~10.0927. We assert against the full-q0 value (the canonical one) and
    # record both, so we do NOT over-claim the Lean literal as exact at q0.
    asymptotic = 1 / (1 - 1 / q0)            # full q0
    asymptotic_rounded = 1 / (1 - 1 / mp.mpf("1.1097"))  # Lean literal q
    w.add_assertion(
        "asymptotic ratio 1/(1-1/q0) at full substrate q0 (~10.0927)",
        computed=mp.nstr(asymptotic, 8),
        expected="10.092678",
        tolerance=1e-5,
        source="1/hbar_q at full-precision q0",
    )
    w.add_assertion(
        "Lean asymptoticRatio_at_q literal q=1.1097 reproduces ~10.116 (tol 0.01)",
        computed=mp.nstr(asymptotic_rounded, 8),
        expected="10.116",
        tolerance=0.01,
        source="1/hbar_q at the rounded Lean literal q=1.1097",
    )

    # ── (4) crossing determinants det(T_j) ──
    # T_j = [[c(q-q⁻¹)+d, c],[c, d]] per the .md; det computed exactly.
    def det_Tj(c, d):
        return sp.simplify(sp.Matrix([[c * HS + d, c], [c, d]]).det())
    det_pp = det_Tj(1, 0)
    det_nn = det_Tj(1, -HS)
    det_mixed = sp.simplify(det_Tj(1, -HS / 2))
    det_pp_ok = sp.simplify(det_pp - (-1)) == 0
    det_nn_ok = sp.simplify(det_nn - (-1)) == 0
    # pp/nn are unimodular (det = -1) — physically each single crossing is
    # an SL_2-type generator. This is the load-bearing structural fact and
    # holds exactly.
    w.add_assertion(
        "det(T_j) = -1 for pp and nn crossings (single-crossing unimodularity)",
        computed=str(det_pp_ok and det_nn_ok),
        expected="True",
        source="exact det of T_j per crossing type",
    )
    # FINDING (not asserted as a pass): the .md table claims det(mixed) =
    # -1 + h^2/4, but the T_j matrix it writes gives det(mixed) =
    # -(q+q^-1)^2/4 = -(1 + h^2/4 + ...) — the two disagree. We record the
    # exact computed value and the table's claimed value as DATA, and flag
    # the discrepancy in a caveat rather than asserting the table is correct.
    table_mixed_claim = sp.simplify(-1 + HS ** 2 / 4)
    mixed_matches_table = sp.simplify(det_mixed - table_mixed_claim) == 0

    w.add_data("engine_crosscheck_pp_all_match", bool(all(pp_ok)))
    w.add_data("engine_crosscheck_nn_all_match", bool(all(nn_ok)))
    w.add_data("multiplicativity_exact_Qq", bool(mul_exact))
    w.add_data("multiplicativity_residual_at_q0", mp.nstr(mul_resid, 6))
    w.add_data("asymptotic_ratio_at_full_q0", mp.nstr(asymptotic, OUTPUT_DPS))
    w.add_data("asymptotic_ratio_at_lean_literal_q_1p1097",
               mp.nstr(asymptotic_rounded, OUTPUT_DPS))
    w.add_data("det_Tj_computed", {
        "pp": str(det_pp), "nn": str(det_nn), "mixed": str(det_mixed),
    })
    w.add_data("det_mixed_matches_md_table_claim", bool(mixed_matches_table))
    w.add_data("det_mixed_md_table_claim", str(table_mixed_claim))
    if not mixed_matches_table:
        w.add_caveat(
            "FINDING: the .md 'transfer matrix IS the polynomial' table lists "
            "det(T_mixed) = -1 + (1/4)(q-q^-1)^2, but the T_j matrix the same "
            "section writes ([[c h + d, c],[c, d]] with mixed (c,d)=(1,-h/2)) "
            "has det = -(q+q^-1)^2/4 = " + str(det_mixed) + ". The two "
            "disagree (the table value is exact only if det = -1 + h^2/4, "
            "which the written matrix does not give). This is a discrepancy in "
            "the .md exposition, NOT in the proved Lean theorem (which proves "
            "the fold, multiplicativity, and asymptotic ratio — not the det "
            "table). Recorded for the content authors; pp/nn unimodularity "
            "(det = -1) holds exactly and is the structural fact used."
        )
    w.add_caveat(
        "The transfer-matrix recurrence IS the proposition's machinery, "
        "reproduced exactly; the load-bearing check is its agreement with the "
        "independent canonical markov_trace_canonical engine (arm 1) plus the "
        "proved structural lemmas (multiplicativity, asymptotic ratio). "
        "Symbolic arms are exact in Q(q); numerical arms are 50-dps evidence "
        "at q0. Probe, not a proof. Does not verify the full nuclear braid "
        "word for arbitrary (Z,N) — that requires the canonical "
        "atom_braid_word_3A pipeline; arm 1 establishes the per-generator "
        "factor against the engine, which the factorization multiplies."
    )
    path = w.save()

    all_passed = all(a.passed for a in w.assertions)
    print(f"engine cross-check pp/nn exact in Q(q): {all(pp_ok)} / {all(nn_ok)}")
    print(f"multiplicativity exact in Q(q): {mul_exact}; resid {mp.nstr(mul_resid,6)}")
    print(f"asymptotic ratio at full q0: {mp.nstr(asymptotic, 8)} "
          f"(Lean literal q=1.1097 -> {mp.nstr(asymptotic_rounded, 8)} ~10.116)")
    print(f"det pp/nn = -1: {det_pp_ok and det_nn_ok}; "
          f"mixed matches .md table claim: {mixed_matches_table} "
          f"(computed {det_mixed})")
    print(f"witness: {path}")
    print("ALL PASSED" if all_passed else "FAILURES PRESENT")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
