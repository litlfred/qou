import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Proved sorry-free 2026-11-21 (PR #8888, owner choice \"Prove all three fully\").** `confinement_categorical` is now a real theorem about `A = H_{n+1}(q)` over a field `K` (`q ≠ 0`, not a root of unity, every block size `f^λ` nonzero in `K`). For any trace `τ` it proves: (1) the centre projector `π_Z`, defined through the Wedderburn isomorphism `AnyChar.heckeWedderburnF`, lands in the centre; (2) `τ ∘ π_Z = τ`, and `τ(x) = Σ_λ τ(e_λ)·tr(ρ_λ x)/f^λ`; (3) every central element is fixed by `π_Z`. `#print axioms`: propext, Classical.choice, Quot.sound. **Not formalised:** the reading of survival as collapse of the GB-filtration spectral sequence (`E_∞^{0,0} = Z(A)` via `HH^k(A) = 0`, `k ≥ 1`); Hochschild cohomology is not in Mathlib. The old context class `ConfinementCategoricalContext`, whose data was unconstrained and whose theorem was a `sorry`, is deleted. History: the class once carried the conclusion as a field (`confinement_ident`), a self-assuming projection; removed 2026-08-08, returned, removed again 2026-11-21. Bean qou-mtc9.",
    },
  ],
  label: "prop:confinement-categorical",
  title: "Confinement = spectral-sequence collapse (only Wedderburn-central observables survive)",
  lean: {
    ref: "qou:QOU.WedderburnMass.confinement_categorical",
    validation: "not_checked",
  },
  uses: [],
  computation: {
    engine: "python",
    script: "computations/atomic_chirality_residue.py",
    witness: "computations/atomic-chirality-residue.witness.json",
    status: "verified",
    requires: ["mpmath", "numpy"],
  },
});
