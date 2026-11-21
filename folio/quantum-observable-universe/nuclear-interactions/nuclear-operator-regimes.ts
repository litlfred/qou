import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-operator-regimes",
  title:
    "Three operator regimes for nuclear binding",
  tags: [
    "nuclear-binding",
    "operator-selection",
    "magic-numbers",
    "torus-knot",
    "hopf-link",
    "shell-closure",
    "regime-transition",
  ],
  lean: { ref: "qou:QOU.Interactions.nuclearOperatorRegimes",
    validation: "not_checked",
  },
  uses: [
    "prop:demand-stability",
  ],
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Regime I used to read: the demand minimiser is the torus knot T_{2,n_s}, n_s the shell size, with Φ = T_{2,5} = (σ₀σ₁)²σ₀. The word (σ₀σ₁)²σ₀ ∈ B₃ closes to the T(2,4) torus link, not the cinquefoil T(2,5) (docs/audits/2026-11-21-electron-word-gs-interactions.md §7), so the T_{2,5} label was wrong and the general rule “T_{2,n_s}, n_s = shell size” rested on it. The rule is withdrawn from the statement, which now names only the observed operator at the one recorded Regime-I step. It is not re-stated as T_{2,4} with n_s = 4: that n would match the first-shell nucleon count, but one step cannot establish a rule indexed by shell size, and choosing the reading because it matches would be selection against the target. The evidence for the whole transition table is the witness nuclear-binding-lp.witness.json, which is not in the tree (no file of that name under computations/ on 2026-11-21); the regimes are recorded, not re-measured. Separately: L₊ = σ₀σ₁ and L₋ = σ₁σ₀ are called Hopf links in Regime II, but each closes in B₃ to a single component (the unknot); that naming is corpus-wide and was not changed here. Both points await the owner." },
  ],
});
