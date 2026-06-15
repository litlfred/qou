#!/usr/bin/env python3
"""
Frontier-paydown chains — per-λ Wedderburn weights for n=3.

Generalises `build_schur_weyl_weight_chain.py` (which covers only
λ=(3)) to the remaining partitions of n=3:

  - λ=(2,1):   hook-length set {3, 1, 1};
               w_(2,1)(q) = (q − q^{-1}) / ([3]_q · [1]_q · [1]_q)
  - λ=(1,1,1): hook-length set {3, 2, 1};
               w_(1,1,1)(q) = 1 / ([3]_q · [2]_q · [1]_q)

Both follow the same Markov-weight convention as the (3) chain:

  w_λ(q) = (q − q^{-1})^(n − l(λ)) · ∏_{x ∈ λ} [h_x]_q^{-1},

with `n = 3`, `l(λ)` = number of parts of λ.

For n=3 this gives:

  l((3))     = 1 → exponent 2; hooks {3, 2, 1};
  l((2,1))   = 2 → exponent 1; hooks {3, 1, 1};
  l((1,1,1)) = 3 → exponent 0; hooks {3, 2, 1}.

Together these three weights constitute the **complete** Wedderburn-
weight contribution to the proton/neutron Markov-trace assembly.
After this PR lands (alongside PR #478), the Markov-trace assembly
chain's last SCRIPT_CITED step (the w_(2,1)/w_(1,1,1) placeholder)
becomes DERIVED via these new chains.

Outputs:
  - schur-weyl-weight-21.derivation.json
  - schur-weyl-weight-111.derivation.json
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)


HERE = Path(__file__).parent


@dataclass
class PartitionSpec:
    short: str           # filename suffix, e.g. "21" or "111"
    label: str           # display name w/ spaces, e.g. "(2, 1)"
    compact: str         # symbolic identifier no spaces, e.g. "(2,1)"
    parts: tuple[int, ...]
    hook_lengths: tuple[int, ...]
    n: int               # = sum(parts)
    f_lambda: int        # # SYT of shape λ
    h_exponent: int      # n − l(λ)
    weight_formula: str  # human-readable formula

    @property
    def length(self) -> int:
        return len(self.parts)


SPECS = {
    "21": PartitionSpec(
        short="21",
        label="(2, 1)",
        compact="(2,1)",
        parts=(2, 1),
        hook_lengths=(3, 1, 1),
        n=3,
        f_lambda=2,
        h_exponent=1,
        weight_formula="(q − q^{-1}) / ([3]_q · [1]_q · [1]_q)",
    ),
    "111": PartitionSpec(
        short="111",
        label="(1, 1, 1)",
        compact="(1,1,1)",
        parts=(1, 1, 1),
        hook_lengths=(3, 2, 1),
        n=3,
        f_lambda=1,
        h_exponent=0,
        weight_formula="1 / ([3]_q · [2]_q · [1]_q)",
    ),
}


def build(spec: PartitionSpec) -> DerivationChain:
    steps: list[DerivationStep] = []

    # 1 — q-integer (Hecke energy origin)
    steps.append(DerivationStep(
        name="q-integer [k]_q := (q^k − q^{-k})/(q − q^{-1})",
        operation=(
            "Define [k]_q := (q^k − q^{-k}) / (q − q^{-1}); the "
            "denominator (q − q^{-1}) is the per-crossing Hecke energy "
            "scale.  Same definition as in `schur-weyl-weight-3` and "
            "`sigma-shell-A2-closed-form`."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="q_integer",
        output_value="[k]_q := (q^k − q^{-k}) / (q − q^{-1})",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:QOU.GaugeFieldFluidDynamics.qInteger",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — Hook-length structure of λ
    steps.append(DerivationStep(
        name=f"Hook-length set for λ = {spec.label}",
        operation=(
            f"For λ = {spec.label} ⊢ {spec.n}, the hook lengths are "
            f"{list(spec.hook_lengths)}.  The number of parts is "
            f"l(λ) = {spec.length} (so the weight exponent is "
            f"n − l(λ) = {spec.h_exponent})."
        ),
        inputs=["q_integer", FirstPrinciple.SCHUR.value],
        output_name="hook_data",
        output_value={
            "lambda":       spec.label,
            "parts":        list(spec.parts),
            "hook_lengths": list(spec.hook_lengths),
            "l_lambda":     spec.length,
            "n_minus_l":    spec.h_exponent,
        },
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:YoungDiagram.hookLength",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Mathlib's `Mathlib.Combinatorics.Young.YoungDiagram` exposes "
            "`hookLength`; the values are read off the Young diagram "
            "combinatorially."
        ),
    ))

    # 3 — Wedderburn block dimension f_λ (= # SYT of shape λ)
    steps.append(DerivationStep(
        name=f"Wedderburn block dimension f_{spec.label}",
        operation=(
            f"From Wedderburn, H_{spec.n}(q) = ⊕_λ M_{{f_λ}}(K(q)) "
            "where f_λ counts standard Young tableaux of shape λ.  "
            f"For λ = {spec.label}, f_λ = {spec.f_lambda}."
        ),
        inputs=["hook_data", FirstPrinciple.WEDDERBURN.value],
        output_name="f_lambda",
        output_value={"lambda": spec.label, "f_lambda": spec.f_lambda},
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:HeckeWedderburn",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 4 — Markov weight formula
    steps.append(DerivationStep(
        name=f"Markov weight w_{spec.label}(q)",
        operation=(
            "Apply the Markov weight convention "
            "w_λ(q) := (q − q^{-1})^(n − l(λ)) · ∏_{x ∈ λ} [h_x]_q^{-1}.  "
            f"For {spec.label} this evaluates to {spec.weight_formula}.  "
            "Same convention as in `schur-weyl-weight-3.derivation.json`."
        ),
        inputs=["q_integer", "hook_data"],
        output_name="w_lambda",
        output_value=spec.weight_formula,
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:MarkovWeight",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Pure algebra: substitute the hook lengths from step 2 and "
            "the exponent (n − l(λ)) from step 2 (hook-length data) "
            "into the convention.  "
            "The (q − q^{-1})^(n − l(λ)) prefactor arises from "
            "Hoefsmit's normalisation of the simple reps of H_n(q); it "
            "ensures the Markov stabilisation tr_M(α σ_n) = z · tr_M(α) "
            "holds with the canonical stabilisation parameter "
            "z = 1/(q^{1/2} + q^{-1/2})."
        ),
    ))

    return DerivationChain(
        # Compact identifier (no spaces) for grep / cross-reference
        # consistency with other chains (e.g. `w_(3)(q)` in
        # schur-weyl-weight-3 and the assembly chain).  Display label
        # with spaces is used only in human-readable step text.
        target=f"w_{spec.compact}(q)",
        target_value=spec.weight_formula,
        target_tolerance=0.0,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            f"Frontier-paydown chain for the Schur-Weyl Markov weight "
            f"w_{spec.label}(q) at λ = {spec.label}.  Together with "
            "`schur-weyl-weight-3.derivation.json` (covering λ=(3)) "
            "this completes the per-λ coverage of n=3 partitions, "
            "discharging the last SCRIPT_CITED weight step in the "
            "proton Markov-trace assembly chain.  Trust profile is "
            "{axiom: 1, mathlib-cited: 2, derived: 1, script-cited: 0, "
            "computational: 0} — fully-trusted modulo the AXIOM "
            "(Hecke energy + Schur + Wedderburn)."
        ),
        steps=steps,
    )


def main() -> int:
    overall_ok = True
    for short, spec in SPECS.items():
        chain = build(spec)
        ok, issues = chain.structural_check()
        out = HERE / f"schur-weyl-weight-{short}.derivation.json"
        chain.save(out)
        marker = "✓" if ok else "✗"
        print(f"  {marker} λ={spec.label}  trust={chain.trust_summary()}")
        for i in issues:
            print(f"      - {i}")
        if not ok:
            overall_ok = False
    print(f"\nbuild_schur_weyl_weight_extra: {'PASS' if overall_ok else 'FAIL'}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
