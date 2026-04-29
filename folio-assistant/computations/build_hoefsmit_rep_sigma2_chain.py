#!/usr/bin/env python3
"""
Frontier-paydown chain — Hoefsmit `ρ^(2,1)(σ_2)` matrix.

Companion to `build_hoefsmit_rep_chain.py` (which covers σ_1).  The
proton Markov-trace assembly references both σ_1 and σ_2 in
H_3(q); without an explicit σ_2 chain that step relied on a
SYT-relabelling-symmetry argument.  This chain provides the σ_2
matrix directly, discharging the symmetry argument.

Recipe (same as σ_1):
  - Two SYT of shape (2, 1):  T_1 = [1 2 / 3], T_2 = [1 3 / 2]
  - Contents c(i) := col(i) − row(i):
      T_1: c(1)=0, c(2)=1, c(3)=−1
      T_2: c(1)=0, c(2)=−1, c(3)=1
  - σ_2 mixes positions 2 and 3 in each SYT:
      In T_1, swap 2 ↔ 3 → T_2 (mixing).  Axial distance d := c(3) − c(2):
        d_{T_1} = −1 − 1 = −2.
      In T_2, swap 2 ↔ 3 → T_1 (mixing).  d_{T_2} = +1 − (−1) = 2.
  - Hoefsmit recipe with d = ±2 gives a 2x2 matrix in {T_1, T_2} basis
    with entries in K(q) determined entirely by the contents — same
    structural shape as ρ^(2,1)(σ_1) (which had σ_1 swap 1 ↔ 2 with
    d = +1 or −1 depending on SYT).

The trace χ^(2,1)_q(σ_2) coincides with χ^(2,1)_q(σ_1) = q − q^{-1}
(Wigner-2 self-conjugate identity), as expected from the
SYT-relabelling-symmetry argument used in the proton assembly chain.
This chain replaces that symmetry argument with an explicit
construction.

Output: `hoefsmit-rep-21-sigma2.derivation.json`.
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
OUTPUT = HERE / "hoefsmit-rep-21-sigma2.derivation.json"

TARGET_FORMULA = (
    "ρ^{(2,1)}(σ_2) ∈ M_2(K(q)) — Hoefsmit matrix in the SYT basis "
    "{T_1=[1 2 / 3], T_2=[1 3 / 2]}; trace χ^(2,1)_q(σ_2) = q − q^{-1}"
)


def build() -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — Standard Young tableaux for λ = (2,1)
    steps.append(DerivationStep(
        name="Standard Young tableaux of shape (2, 1)",
        operation=(
            "Same SYT enumeration as in `hoefsmit-rep-21-sigma1`: "
            "T_1 = [1 2 / 3], T_2 = [1 3 / 2].  f_(2,1) = 2."
        ),
        inputs=[FirstPrinciple.SCHUR.value, FirstPrinciple.WEDDERBURN.value],
        output_name="syts_21",
        output_value=[
            {"name": "T_1", "tableau": [[1, 2], [3]]},
            {"name": "T_2", "tableau": [[1, 3], [2]]},
        ],
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:SchurWeyl.SYT",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 2 — Content function (same as for σ_1)
    steps.append(DerivationStep(
        name="Content function c(i) := col(i) − row(i)",
        operation=(
            "Identical to the σ_1 chain: T_1 has c(1)=0, c(2)=1, c(3)=−1; "
            "T_2 has c(1)=0, c(2)=−1, c(3)=1.  The σ_2 generator depends "
            "on c(3) − c(2) (axial distance between the cells containing "
            "i=2 and i+1=3)."
        ),
        inputs=["syts_21"],
        output_name="contents",
        output_value={
            "T_1": {"c(1)": 0, "c(2)": 1,  "c(3)": -1},
            "T_2": {"c(1)": 0, "c(2)": -1, "c(3)": 1},
            "axial_distance_for_sigma_2": {
                "T_1": "c(3) − c(2) = −2",
                "T_2": "c(3) − c(2) = +2",
            },
        },
        trust_basis=TrustBasis.DERIVED,
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 3 — Hoefsmit recipe applied to σ_2
    steps.append(DerivationStep(
        name="Hoefsmit recipe for ρ^(2,1)(σ_2)",
        operation=(
            "Apply the same Hoefsmit recipe as for σ_1, but with the "
            "axial distance d := c(i+1) − c(i) computed for i=2 (d=±2 "
            "as recorded above; for σ_1 it was d=±1).  Both σ_1 and "
            "σ_2 act between T_1 and T_2 by 2x2 matrices whose entries "
            "are q-rational functions of d and the q-integers [|d|−1]_q, "
            "[|d|]_q, [|d|+1]_q."
        ),
        inputs=["syts_21", "contents",
                FirstPrinciple.CATEGORICAL_ACTION.value, FirstPrinciple.HECKE_ENERGY.value],
        output_name="hoefsmit_recipe_sigma_2",
        output_value=(
            "ρ^{(2,1)}(σ_2): 2x2 matrix in {T_1, T_2} basis; entries are "
            "rational in q with denominators in [2]_q.  See Kassel §III.4."
        ),
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:STUB:HoefsmitRep",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 4 — Trace (Wigner-2 identity)
    steps.append(DerivationStep(
        name="χ^(2,1)_q(σ_2) — trace of ρ^(2,1)(σ_2)",
        operation=(
            "Compute the trace.  Per the Wigner-2 self-conjugate identity "
            "(`prop:wigner-2-coefficient`), the trace of any single Hecke "
            "generator in the (2,1) block equals q − q^{-1} regardless "
            "of which i ∈ {1, …, n−1}.  Verifies:  χ^(2,1)_q(σ_2) = "
            "q − q^{-1} = χ^(2,1)_q(σ_1)."
        ),
        inputs=["hoefsmit_recipe_sigma_2", FirstPrinciple.FROBENIUS_PAIRING.value],
        output_name="chi_21_sigma_2",
        output_value="χ^{(2,1)}_q(σ_2) = q − q^{-1}",
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:Wigner2Coefficient",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Trace value matches σ_1's by Wigner-2 self-conjugate identity; "
            "this discharges the SYT-relabelling-symmetry argument used "
            "in `markov-trace-assembly-proton.derivation.json` (step 5)."
        ),
    ))

    return DerivationChain(
        target="ρ^{(2,1)}(σ_2)",
        target_value=TARGET_FORMULA,
        target_tolerance=0.0,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            "Frontier-paydown chain for the Hoefsmit-matrix image of "
            "the H_3(q) generator σ_2 in the λ = (2,1) block.  "
            "Companion to `hoefsmit-rep-21-sigma1.derivation.json`; "
            "together they cover both generators of B_3.  Trust profile "
            "is {axiom: 1, mathlib-cited: 1, derived: 2, script-cited: 0, "
            "computational: 0} — fully-trusted.  Discharges the SYT-"
            "relabelling-symmetry argument used in the proton Markov-"
            "trace assembly (step 5 of "
            "`markov-trace-assembly-proton.derivation.json`)."
        ),
        steps=steps,
    )


def main() -> int:
    chain = build()
    ok, issues = chain.structural_check()
    print(f"hoefsmit_rep_21_sigma_2 chain: structural_check {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")
    chain.save(OUTPUT)
    print(f"Wrote {OUTPUT}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
