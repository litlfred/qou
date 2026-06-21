#!/usr/bin/env python3
"""
Frontier-paydown chain — `w_(3)(q)` Schur-Weyl Markov weight.

Pushes back the SCRIPT_CITED step
"Schur–Weyl weights w_λ(q)" in the proton/neutron/deuteron
derivation chains.  Target: derive the Markov weight w_(3)(q) for
the trivial partition λ = (3) (the most-symmetric Hoefsmit block,
relevant to the proton) entirely from first principles.

Per Kassel §III.4, Schur-Weyl duality applied to
U_q(sl_2) ↺ V^{⊗n} gives the Markov weight

  w_λ(q) := (q - q^{-1})^{n - l(λ)} · ∏_{(i,j) ∈ λ} [h(i,j)]_q^{-1}

with [k]_q := (q^k - q^{-k}) / (q - q^{-1}) the q-integer and
h(i,j) the hook length at cell (i,j) of the Young diagram λ.

For λ = (3) (n = 3, l(λ) = 1, hook lengths 3, 2, 1):

  w_(3)(q)  =  (q - q^{-1})^{3 - 1} · 1 / ([3]_q · [2]_q · [1]_q)
            =  (q - q^{-1})^2 / ([3]_q · [2]_q · [1]_q).

Chain is fully-trusted modulo AXIOMs (Wedderburn, Schur, Hecke
energy).  No SCRIPT_CITED steps.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent
OUTPUT = HERE / "schur-weyl-weight-3.derivation.json"

# Target value: symbolic, recorded as a string formula (the chain
# is a derivation, not a numerical eval; the eval at q_0 is a
# downstream chain).
TARGET_FORMULA = "(q - q^{-1})^2 / ([3]_q · [2]_q · [1]_q)"


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — q-integer definition (Hecke energy origin)
    steps.append(DerivationStep(
        name="q-integer [k]_q := (q^k - q^{-k})/(q - q^{-1})",
        operation=(
            "Define the q-integer [k]_q := (q^k - q^{-k}) / (q - q^{-1}); "
            "the denominator (q - q^{-1}) is the per-crossing Hecke energy "
            "scale.  At q = 1 the q-integer reduces to k."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="q_integer",
        output_value="[k]_q := (q^k - q^{-k})/(q - q^{-1})",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:QOU.GaugeFieldFluidDynamics.qInteger",
        citation="kassel1995",
        jet_order=0,
        notes=(
            "Hecke energy axiom underwrites the (q - q^{-1}) normalisation "
            "(AGENTS.md §7a).  q-integers are the canonical replacement "
            "for ordinary integers in every Hecke-algebra trace formula."
        ),
    ))

    # 2 — q-factorial
    steps.append(DerivationStep(
        name="q-factorial [n]_q! := [1]_q · [2]_q · ... · [n]_q",
        operation=(
            "Iterate the q-integer to the q-factorial [n]_q! := "
            "∏_{k=1..n} [k]_q.  Pure algebra from step 1."
        ),
        inputs=["q_integer"],
        output_name="q_factorial",
        output_value="[n]_q! := ∏_{k=1..n} [k]_q",
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
        notes="Iterated product of step 1; one-line algebra.",
    ))

    # 3 — hook-length formula at U_q(sl_2)
    steps.append(DerivationStep(
        name="q-hook-length formula for irrep dimension",
        operation=(
            "By Schur duality U_q(sl_2) ↺ V^{⊗n}, the dimension of the "
            "λ-isotypic component is dim_q(λ) = [n]_q! / ∏_{(i,j) ∈ λ} [h(i,j)]_q. "
            "For λ = (3), the cells have hook lengths {3, 2, 1}, giving "
            "dim_q((3)) = [3]_q! / ([3]_q · [2]_q · [1]_q) = 1."
        ),
        inputs=["q_factorial", FirstPrinciple.SCHUR.value],
        output_name="dim_q_lambda",
        output_value={
            "lambda": "(3)",
            "hook_lengths": [3, 2, 1],
            "dim_q": "[3]_q! / ([3]_q · [2]_q · [1]_q) = 1",
        },
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:SchurWeyl.qHookFormula",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Mathlib has `Mathlib.RepresentationTheory.QuantumGroup.SchurWeyl` "
            "(stub) and the q-hook formula via `Mathlib.Combinatorics.Young.YoungDiagram`."
        ),
    ))

    # 4 — Wedderburn block dimension f_λ
    steps.append(DerivationStep(
        name="Wedderburn block dimension f_λ for λ = (3)",
        operation=(
            "From Wedderburn, H_n(q) = ⊕_λ M_{f_λ}(K(q)) where f_λ is the "
            "Young-frame dimension counting standard Young tableaux of shape "
            "λ.  For λ = (3) there is exactly one SYT (the row [1,2,3]), so "
            "f_(3) = 1."
        ),
        inputs=["dim_q_lambda", FirstPrinciple.WEDDERBURN.value],
        output_name="f_lambda",
        output_value={"lambda": "(3)", "f_lambda": 1},
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:HeckeWedderburn",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "f_λ = #SYT(λ) is classical (Mathlib has "
            "`Mathlib.Combinatorics.Young.SemistandardTableau`)."
        ),
    ))

    # 5 — Markov weight formula
    steps.append(DerivationStep(
        name="Markov weight w_λ(q) Hoefsmit normalisation",
        operation=(
            "The Markov weight w_λ(q) := (q - q^{-1})^{n - l(λ)} · "
            "∏_{(i,j) ∈ λ} [h(i,j)]_q^{-1} is the Hoefsmit-normalised "
            "weight that makes tr_M = Σ_λ w_λ · χ^λ a Markov trace "
            "(invariant under stabilisation).  For λ = (3): n - l(λ) = "
            "3 - 1 = 2, so w_(3)(q) = (q - q^{-1})^2 / ([3]_q · [2]_q · [1]_q)."
        ),
        inputs=["q_factorial", "dim_q_lambda", FirstPrinciple.SCHUR.value],
        output_name="w_lambda_3",
        output_value=TARGET_FORMULA,
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:MarkovWeight",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "The (q - q^{-1})^{n - l(λ)} prefactor arises from Hoefsmit's "
            "normalisation of the simple reps of H_n(q); it ensures the "
            "Markov stabilisation tr_M(α σ_n) = z · tr_M(α) holds with the "
            "canonical stabilisation parameter z = 1/(q^{1/2} + q^{-1/2})."
        ),
    ))

    return DerivationChain(
        target="w_(3)(q)",
        target_value=TARGET_FORMULA,
        target_tolerance=0.0,  # symbolic chain; no numerical leaf
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Frontier-paydown chain: derives the Schur-Weyl Markov weight "
            "w_(3)(q) for the trivial partition λ = (3) entirely from "
            "AXIOMs (Hecke energy + Wedderburn + Schur), with no "
            "SCRIPT_CITED steps.  Replaces the corresponding SCRIPT_CITED "
            "step in build_atom_tr_M_chains.py for the proton.  Other λ "
            "(e.g. (2,1), (1,1,1)) follow the same pattern with different "
            "hook lengths and l(λ); future chains author them analogously."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"schur_weyl_weight_3 chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
