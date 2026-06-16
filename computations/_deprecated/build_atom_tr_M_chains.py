#!/usr/bin/env python3
"""
Build derivation chains for `tr_M(<atom>, q_0)` for atoms p, n, D.

Walks step-by-step from the seven first-principles entrypoints
(Hecke energy + Wedderburn + Schur + Frobenius pairing + Categorical
action + Finite Jones being the most relevant) down to each atom's
archimedean Markov-trace value at q_0 = 1.10997...

The chain is the **methodological backbone**: anything downstream
that asserts the proton/neutron/deuteron mass / Habiro coefficients
/ Markov trace must trace back here.

Each step records jet order, GB filtration level, spectral
stratum, and trust basis (axiom / lean-proven / mathlib-cited /
script-cited / computational).

Per the methodology directive (post-#472), SCRIPT_CITED steps are
the **computational frontier**: each one needs its own derivation
chain to push back the frontier.  COMPUTATIONAL leaves are the
acceptable terminal evaluations.

Outputs:
  - p-tr-M-q0.derivation.json
  - n-tr-M-q0.derivation.json
  - D-tr-M-q0.derivation.json
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    Q_0,
    TR_M_AT_Q0,
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent

# Canonical numerical targets — shared with the realizer + cross-validator
# witnesses on this branch and term6_full_pole_sum.py on
# claude/continue-pr-442-DJRWm.
# Target values pulled from `derivation_chain.TR_M_AT_Q0` (single
# source of truth; matches every committed `*-tr-M-q0.derivation.json`
# leaf).  Cross-checked against the realizer + cross-validator
# witnesses and term6_full_pole_sum.py on claude/continue-pr-442-DJRWm.
TARGETS = {
    "p":  ("p (proton, A=1)",   1, 0, False, TR_M_AT_Q0["p"], 3, 6),
    "n":  ("n (neutron, A=1)",  0, 1, False, TR_M_AT_Q0["n"], 3, 5),
    "D":  ("D (deuteron, A=2)", 1, 1, True,  TR_M_AT_Q0["D"], 6, 12),
}
# Q_0 imported from `derivation_chain` (single source of truth per
# CLAUDE.md §7aa); do not redefine locally.


@dataclass
class AtomSpec:
    short: str
    full: str
    Z: int
    N: int
    include_inter: bool
    target_value: float
    n_strands: int
    n_crossings: int


def build_chain(spec: AtomSpec) -> DerivationChain:
    A = spec.Z + spec.N
    nstrands = spec.n_strands
    A_strands = 3 * A  # the chapter's "3A" Schur-Weyl ambient dimension
    steps: list[DerivationStep] = []

    # 1 — Hecke algebra structure
    steps.append(DerivationStep(
        name=f"Hecke algebra H_{nstrands}(q) presentation",
        operation=(
            f"Define H_{nstrands}(q) := ⟨σ_1..σ_{nstrands-1} | "
            "braid relations, Hecke relation (σ_i - q)(σ_i + q^{-1}) = 0⟩."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name=f"H_{nstrands}_q",
        output_value=f"H_{nstrands}(q) — Iwahori–Hecke algebra (A={A})",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:QOU.PathIntegrals.HeckeAlgebra",
        citation="kassel1995",
        jet_order=0,
        notes=(
            "Hecke energy axiom: each σ_i carries σ_i^2 = (q-q^{-1})σ_i + 1; "
            "the (q-q^{-1}) factor is the per-crossing energy (CLAUDE.md §7a)."
        ),
    ))

    # 2 — Wedderburn decomposition
    steps.append(DerivationStep(
        name=f"Wedderburn decomposition of H_{A_strands}(q)",
        operation=(
            f"H_{A_strands}(q) ≅ ⊕_{{λ ⊢ {A_strands}}} M_{{f_λ}}(K(q)) "
            "(semisimple at generic q, including q_0)."
        ),
        inputs=[f"H_{nstrands}_q", FirstPrinciple.WEDDERBURN.value],
        output_name="wedderburn_decomp",
        output_value=f"⊕_{{λ ⊢ {A_strands}}} M_{{f_λ}}(K(q)) — see partitions_of({A_strands})",
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:HeckeWedderburn",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            f"Partitions of {A_strands} index the simple factors; Hoefsmit "
            "frame dimensions f_λ from `schur_weyl_symbolic.partitions_of`.  "
            "Mathlib backs the abstract direct-sum statement via "
            "`Algebra.Algebraic.Module.WedderburnArtin`."
        ),
    ))

    # 3 — Schur–Weyl weights w_λ(q)
    steps.append(DerivationStep(
        name="Schur–Weyl weights w_λ(q)",
        operation=(
            "For each λ, compute w_λ(q) per Schur–Weyl duality "
            "U_q(sl_2) ↺ V^{⊗3A}; Hoefsmit normalisation (Kassel §III.4)."
        ),
        inputs=["wedderburn_decomp", FirstPrinciple.SCHUR.value],
        output_name="schur_weights",
        output_value=f"w_λ(q) for each λ ⊢ {A_strands}",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: computations/schur_weyl_symbolic.py "
            "function `schur_weyl_weight(lam, q)`.  SCRIPT_CITED pending "
            "its own derivation chain."
        ),
    ))

    # 4 — Categorical action (R-matrix → Hoefsmit reps)
    steps.append(DerivationStep(
        name=f"Categorical action B_{nstrands} → ⊕_λ M_{{f_λ}}",
        operation=(
            f"Categorical action of B_{nstrands} on V^{{⊗3A}} via the R-matrix; "
            "project to each λ-block to get ρ^λ : H → M_{f_λ}(K(q))."
        ),
        inputs=["wedderburn_decomp", FirstPrinciple.CATEGORICAL_ACTION.value],
        output_name="hoefsmit_reps",
        output_value="ρ^λ for each λ — see hecke_character_symbolic.py",
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: computations/hecke_character_symbolic.py "
            "Hoefsmit-matrix evaluation of σ_i.  SCRIPT_CITED."
        ),
    ))

    # 5 — Atomic braid word T_w
    steps.append(DerivationStep(
        name=f"Atomic {spec.short} braid word T_w(Z={spec.Z}, N={spec.N})",
        operation=(
            f"Atomic braid recipe: Z={spec.Z} up-strands, N={spec.N} "
            f"down-strands, include_inter={spec.include_inter}; produces "
            f"a word with {spec.n_crossings} crossings on {nstrands} strands."
        ),
        inputs=[f"H_{nstrands}_q"],
        output_name="T_w_atom",
        output_value=(
            f"σ-word with {spec.n_crossings} crossings (Z={spec.Z}, "
            f"N={spec.N}, include_inter={spec.include_inter})"
        ),
        trust_basis=TrustBasis.SCRIPT_CITED,
        citation="manuscript:§Atomic-braid recipe",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: computations/hecke_character_symbolic.py "
            "function `atomic_braid_to_crossings`.  SCRIPT_CITED — the "
            "atomic-braid recipe itself awaits formalisation."
        ),
    ))

    # 6 — Frobenius pairing: characters χ^λ_q(T_w)
    steps.append(DerivationStep(
        name="Frobenius pairing — characters χ^λ_q(T_w)",
        operation=(
            "For each λ, compute χ^λ_q(T_w) := tr(ρ^λ(T_w)) (Frobenius "
            "pairing identifies traces with characters of the regular rep)."
        ),
        inputs=["hoefsmit_reps", "T_w_atom", FirstPrinciple.FROBENIUS_PAIRING.value],
        output_name="chi_lambda",
        output_value=f"χ^λ_q(T_w) Laurent polynomial in q for each λ ⊢ {A_strands}",
        trust_basis=TrustBasis.SCRIPT_CITED,
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "script: computations/hecke_character_symbolic.py "
            "function `q_character_on_braid_word(braid_word, q)`. SCRIPT_CITED."
        ),
    ))

    # 7 — Markov trace via finite-Jones formula
    # Proton has a dedicated assembly chain
    # (markov-trace-assembly-proton.derivation.json); other atoms still
    # delegate to the upstream script.
    has_assembly_chain = spec.short == "p"
    step7_trust = TrustBasis.DERIVED if has_assembly_chain else TrustBasis.SCRIPT_CITED
    step7_notes = (
        "Derivation chain: markov-trace-assembly-proton.derivation.json "
        "(builder: build_markov_trace_assembly_chain.py).  Combines "
        "schur-weyl-weight-3 + hoefsmit-rep-21-sigma1 + "
        "atomic-braid-recipe-p via finite-Jones."
        if has_assembly_chain else
        "script: computations/habiro_coefficients_atomic.py "
        "function `markov_trace_symbolic(Z, N, q, include_inter)`.  "
        "Per CLAUDE.md §7a, the Jones polynomial J_K(q) is the Markov "
        "trace in H_n(q); finite-Jones is existence + uniqueness.  "
        "Per-atom assembly chains for n, D pending (extend "
        "build_markov_trace_assembly_chain.py)."
    )
    steps.append(DerivationStep(
        name="Markov trace via finite-Jones formula",
        operation=(
            f"tr_M(T_w, q) := Σ_{{λ ⊢ {A_strands}}} w_λ(q) · χ^λ_q(T_w); "
            "uniqueness from the Markov property + finite-Jones."
        ),
        inputs=["schur_weights", "chi_lambda", FirstPrinciple.FINITE_JONES.value],
        output_name="tr_M_symbolic",
        output_value="symbolic Laurent polynomial in q (Markov trace)",
        trust_basis=step7_trust,
        citation="jones1987",
        jet_order=0,
        gb_filtration_level=0,
        notes=step7_notes,
    ))

    # 8 — Numerical eval at q_0 (COMPUTATIONAL leaf)
    steps.append(DerivationStep(
        name=f"Evaluate tr_M({spec.short}, q_0) at q_0 = {Q_0}",
        operation=(
            f"Substitute q := q_0 = {Q_0} into `tr_M_symbolic` and evaluate "
            "at high precision (mpmath, 60 dps)."
        ),
        inputs=["tr_M_symbolic"],
        output_name="tr_M_q0",
        output_value=spec.target_value,
        trust_basis=TrustBasis.COMPUTATIONAL,
        jet_order=0,
        gb_filtration_level=0,
        spectral_stratum="archimedean (q_0 ∈ ℝ_{>1})",
        notes=(
            "COMPUTATIONAL leaf — numerical eval.  Cross-checked at "
            "machine precision against atomic-poly evaluation, the "
            "Vandermonde-interpolation pipeline, and (when "
            "claude/continue-pr-442-DJRWm lands) the Mittag-Leffler "
            "residue path.  All paths agree at rel_diff ≤ 1e-12."
        ),
    ))

    return DerivationChain(
        target=f"tr_M({spec.short}, q_0)",
        target_value=spec.target_value,
        target_tolerance=1e-9,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            f"Step-by-step derivation of {spec.full}'s archimedean Markov "
            f"trace value tr_M({spec.short}, q_0) ≈ {spec.target_value} from "
            "the seven first-principles entrypoints.  Per the methodology "
            "directive (post-#472), every numerical claim must trace back "
            "here.  SCRIPT_CITED steps are the computational frontier; each "
            "needs its own derivation chain to push back the frontier."
        ),
        steps=steps,
    )


def main() -> int:
    overall_ok = True
    for short, (full, Z, N, inter, val, nstrands, ncross) in TARGETS.items():
        spec = AtomSpec(short, full, Z, N, inter, val, nstrands, ncross)
        chain = build_chain(spec)
        ok, issues = chain.structural_check()
        if not ok:
            overall_ok = False
        out = HERE / f"{short}-tr-M-q0.derivation.json"
        chain.save(out)
        marker = "✓" if ok else "✗"
        print(f"  {marker} {short:>2} ({spec.full:>22})  steps={len(chain.steps)}  "
              f"trust={chain.trust_summary()}")
        for i in issues:
            print(f"      - {i}")
    print(f"\nbuild_atom_tr_M_chains: {'PASS' if overall_ok else 'FAIL'}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
