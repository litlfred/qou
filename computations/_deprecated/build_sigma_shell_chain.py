#!/usr/bin/env python3
"""
Frontier-paydown chain — σ_shell (Term 7) at A=2 closed form.

Per `conj:shell-correction-term-seven`
(content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.md):

  Term 7 = m_e · Σ_{λ ⊢ 3A, height(λ) = 6} C_λ(q) · S_λ(Z, N, A)

The paper specialises this to A = 2 (the smallest A where height-6
partitions of 3A exist).  The unique height-6 partition of 6 is the
**staircase** λ = (3, 2, 1), and Wigner-2 (`prop:wigner-2-coefficient`)
gives the closed form

  C_{(3,2,1)}(q) = ([2]_q · [4]_q · [6]_q · h) / (2 · [3]_q^3 · [5]_q),

with `h = q − q^{-1}` the per-crossing Hecke energy.  The outer
empirical scale α_5 ≈ −4.2 × 10^5 MeV (fit residual on A=1..4)
remains COMPUTATIONAL pending its own derivation chain.

This chain certifies the **closed-form** part of the σ_shell
derivation: every step from Hecke energy + Schur to the explicit
ratio of q-integers is AXIOM / MATHLIB_CITED / DERIVED.  The outer
α_5 normalisation enters as a single COMPUTATIONAL leaf.

Output: `sigma-shell-A2-closed-form.derivation.json`.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    Q_0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = HERE / "sigma-shell-A2-closed-form.derivation.json"


def _q_int(q: mp.mpf, k: int) -> mp.mpf:
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def _c_321_at(q: mp.mpf) -> mp.mpf:
    """Closed-form C_{(3,2,1)}(q) = [2][4][6] · h / (2 · [3]^3 · [5]) at q."""
    h = q - q ** (-1)
    num = _q_int(q, 2) * _q_int(q, 4) * _q_int(q, 6) * h
    den = 2 * _q_int(q, 3) ** 3 * _q_int(q, 5)
    return num / den


# Numerical anchor at q = q_0 — the leaf of this chain is the
# C_{(3,2,1)}(q_0) value to 30 dps; downstream consumers use it
# directly in the Term-7 assembly.  Keep as mp.mpf to preserve
# precision (float() would truncate to ~16 dp, contradicting the
# 30-dp contract).  Serialize via mp.nstr at the point of use.
mp.mp.dps = 60
Q0_MP = mp.mpf(repr(Q_0))
C_321_AT_Q0_MP = _c_321_at(Q0_MP)
# Float view retained for downstream consumers that explicitly
# want f64 (e.g. logging); mp.mpf is the canonical value.
C_321_AT_Q0 = float(C_321_AT_Q0_MP)


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Hecke energy axiom: per-crossing energy (q − q^{-1})
    steps.append(DerivationStep(
        name="Hecke energy h = q − q^{-1}",
        operation=(
            "Hecke energy axiom: each braid generator σ_i carries "
            "the relation σ_i² = (q − q^{-1}) σ_i + 1; the prefactor "
            "h := q − q^{-1} is the per-crossing energy scale "
            "(AGENTS.md §7a)."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="h_hecke",
        output_value="h := q − q^{-1}",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:HeckeEnergy",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — q-integer definition (reuses the schur-weyl-weight-3 chain's
    #     foundation; replicate it locally so this chain is self-
    #     contained)
    steps.append(DerivationStep(
        name="q-integer [k]_q := (q^k − q^{-k})/(q − q^{-1})",
        operation=(
            "Define [k]_q via Hecke energy h: [k]_q = (q^k − q^{-k}) / h.  "
            "At q → 1 reduces to k.  Same definition as in the "
            "schur-weyl-weight-3 chain."
        ),
        inputs=["h_hecke"],
        output_name="q_integer",
        output_value="[k]_q := (q^k − q^{-k})/h",
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:QOU.GaugeFieldFluidDynamics.qInteger",
        citation="kassel1995",
        jet_order=0,
    ))

    # 3 — Wedderburn decomposition of H_6(q) with height filter
    steps.append(DerivationStep(
        name="Wedderburn decomposition of H_6(q) — height-6 sector",
        operation=(
            "H_6(q) ≅ ⊕_{λ ⊢ 6} M_{f_λ}(K(q)).  Height filter "
            "height(λ) = 6 picks out the unique staircase partition "
            "(3, 2, 1) of 6 (the only partition of 6 with all rows of "
            "distinct length and maximal height)."
        ),
        inputs=["q_integer", FirstPrinciple.WEDDERBURN.value],
        output_name="staircase_321_isolated",
        output_value={"lambda": "(3, 2, 1)", "f_lambda": 16},
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:HeckeWedderburn",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 4 — Wedderburn weight w_{(3,2,1)}(q)
    steps.append(DerivationStep(
        name="Wedderburn weight w_{(3,2,1)}(q)",
        operation=(
            "By Schur–Weyl duality the Markov-Wedderburn weight of "
            "λ = (3, 2, 1) ⊢ 6 is w_λ(q) = dim_q(λ)² / [6]_q!, "
            "where dim_q is the q-deformed Young-frame dimension.  "
            "Hook lengths for the staircase are {5,3,1; 3,1; 1}; "
            "dim_q((3,2,1)) = [6]_q! / ([5]_q [3]_q^2 [1]_q^3) = "
            "[6]_q! / ([5]_q [3]_q^2)."
        ),
        inputs=["staircase_321_isolated", FirstPrinciple.SCHUR.value],
        output_name="w_321",
        output_value="w_{(3,2,1)}(q) = ([6]_q!)² / ([5]_q² · [3]_q⁴ · [6]_q!) = [6]_q! / ([5]_q² · [3]_q⁴)",
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:MarkovWeight.staircase",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 5 — Wigner-2 trace identity τ_{(3,2,1)} = h/2
    steps.append(DerivationStep(
        name="Wigner-2 trace identity τ_{(3,2,1)} = h/2",
        operation=(
            "Per `prop:wigner-2-coefficient` (the Wigner-2 closed form), "
            "self-conjugate partitions admit the trace-per-dimension "
            "identity τ_λ(σ_g) = h/2 for the canonical generator σ_g.  "
            "(3, 2, 1) is the smallest self-conjugate staircase, so "
            "τ_{(3,2,1)} = h/2."
        ),
        inputs=["staircase_321_isolated", "h_hecke", FirstPrinciple.FROBENIUS_PAIRING.value],
        output_name="tau_321",
        output_value="τ_{(3,2,1)}(σ_g) = h / 2",
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:Wigner2Coefficient",
        citation="manuscript:§Wigner-2",
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 6 — Closed-form C_{(3,2,1)}(q)
    steps.append(DerivationStep(
        name="Closed form C_{(3,2,1)}(q) — staircase shadow price",
        operation=(
            "C_λ(q) := w_λ(q) · τ_λ(σ_g) is the BW shadow-price "
            "coefficient (`prop:bw-coefficient-shadow-price`).  "
            "Substitute w_{(3,2,1)} and τ_{(3,2,1)} = h/2; collect "
            "q-integer factors:\n"
            "  C_{(3,2,1)}(q) = [2]_q · [4]_q · [6]_q · h / "
            "(2 · [3]_q³ · [5]_q).\n"
            "(The combinatorial reduction from [6]_q! / ([5]_q² · "
            "[3]_q⁴) · h/2 to the stated form uses [k]_q recurrences "
            "and simplification.)"
        ),
        inputs=["w_321", "tau_321"],
        output_name="C_321_symbolic",
        output_value=(
            "C_{(3,2,1)}(q) = [2]_q · [4]_q · [6]_q · h / "
            "(2 · [3]_q³ · [5]_q)"
        ),
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:ShadowPriceStaircase",
        citation="manuscript:§Term-7-A2",
        jet_order=0,
        gb_filtration_level=5,
    ))

    # 7 — Numerical evaluation at q_0
    steps.append(DerivationStep(
        name=f"Evaluate C_{{(3,2,1)}}(q_0) at q_0 = {Q_0:.10f}",
        operation=(
            "Substitute q := q_0 ≈ 1.110 into the closed form; "
            "evaluate at 60 dps mpmath.  Result agrees with the "
            "paper's quoted ≈ 0.0375."
        ),
        inputs=["C_321_symbolic"],
        output_name="C_321_at_q0",
        # Serialize at 30+ dp via mp.nstr to preserve precision; the
        # raw mp.mpf can't go through JSON, but the string form keeps
        # all digits for downstream consumers that want >16 dp.
        output_value=mp.nstr(C_321_AT_Q0_MP, 30, strip_zeros=False),
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=5,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "COMPUTATIONAL leaf — bare arithmetic.  Reproduces the "
            "paper's `≈ 0.0375` quote in shell-correction-term-seven.md.  "
            "The OUTER α_5 normalisation (≈ −4.2 × 10^5 MeV per the "
            "diagnostic fit) is NOT yet derived; it remains a separate "
            "computational debt tracked under "
            "`higher-a-shell-diagnostic.witness.json`."
        ),
    ))

    return DerivationChain(
        target="C_{(3,2,1)}(q_0)",
        # 30-dp string preserves the full mp.mpf precision under JSON
        # serialization (float would truncate to ~16 dp).
        target_value=mp.nstr(C_321_AT_Q0_MP, 30, strip_zeros=False),
        target_tolerance=1e-12,
        content_block="conj:shell-correction-term-seven",
        description=(
            "Frontier-paydown chain for the σ_shell (Term 7) "
            "closed-form coefficient at A = 2: derives "
            "C_{(3,2,1)}(q) from Hecke energy + Schur–Weyl + Wigner-2 "
            "with NO SCRIPT_CITED steps — fully trusted modulo "
            "AXIOMs and the still-conjectural classifications "
            "(MarkovWeight.staircase, Wigner2Coefficient, "
            "ShadowPriceStaircase) marked qou:STUB:.  The OUTER "
            "α_5 empirical fit (−4.2 × 10^5 MeV) is the remaining "
            "frontier debt for σ_shell at A ≥ 4."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"σ_shell A=2 chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    print(f"target_value:  {chain.target_value}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
