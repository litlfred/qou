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
    { kind: "caveat", date: "2026-11-21", body: "Re-measured: docs/audits/2026-11-21-nuclear-regime-shell-rule.md, witness computations/nuclear-regime-shell-rule.witness.json (mpmath 80/120 dps, convention D, proton q₀). The criteria were fixed before the run. The original producer (nuclear-binding-lp.py, off main since 6333715860) printed the transition table to stdout only, so its witness never recorded it. Re-run with the original nucleons, candidates and orders, it reproduces (σ₀σ₁)²σ₀ → L₊ → L₊ → L₋ → C_pn. Only the first step is decided by the demand criterion. The other four are Markov-trace tie-breaks among 4–9 candidates whose demand is exactly zero. Across 65 steps (orders ppnn, ppnnpn, p²⁰, n²⁰, (pn)¹⁰), 57 are such tie-breaks. With σ₀ⁿσ₁ (closure T(2,n), n ≤ 12) added to the candidates, the step p→pp selects σ₀³σ₁, not (σ₀σ₁)²σ₀ (which has demand 0.0046 > 0). The rule “T(2,n_s), n_s = shell size” passes 3 of 65 steps and never passes past the first shell. This is a scope-(a) negative for this model. No shell rule is restated. In this model B₃ is also selected, by tie-break, on the p²⁰ and (pn)¹⁰ orders from A = 5 on. Lean: QOU.Interactions.NuclearRegimeShellRule states the rule as a class with no instance and proves its falsifiers." },
  ],
});
