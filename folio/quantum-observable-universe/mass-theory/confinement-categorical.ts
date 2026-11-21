import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Honest sorry restored 2026-11-21 (owner ruling on the PR #8819 follow-up).** The field `confinement_ident` is deleted and the theorem body is now `sorry`, so `#print axioms` reports `sorryAx` and the block reads as stated-not-proved. The statement is unchanged. Earlier disclosure follows. The `lean.ref` theorem `confinement_categorical` was a self-assuming projection (AGENTS.md §3b-cond item 5): its body is `ctx.confinement_ident`, a field of `ConfinementCategoricalContext` that states the theorem's three-clause conclusion verbatim (survival on E_∞^{0,0}, factorisation of the integral through the centre projector, centrality of observables). The Lean therefore derives nothing; `#print axioms` shows no `sorryAx`, so a status audit reads it as proved. The inputs the proof needs, semisimple Hochschild vanishing HH^k(A) = 0 for k ≥ 1 and the Wedderburn decomposition of A, are not formalised. The projection was removed on 2026-08-08 (bean qou-mtc9, option 1: honest `sorry`) and has since returned as the field `confinement_ident`; the Lean file's own docstring records this. Bean qou-mtc9.",
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
