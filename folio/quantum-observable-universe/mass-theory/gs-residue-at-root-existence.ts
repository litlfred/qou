import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-residue-at-root-existence",
  title:
    "Existence of the cyclotomic residue at each filtration level",
  lean: {
    ref: "qou:QOU.BraidKnot.ResidueAtRoot",
    validation: "not_checked",
  },
  uses: [
    "conj:gs-graded-markov-trace-existence",
    "def:habiro-ring",
  ],
  computation: {
    engine: "sympy",
    script: "computations/term6_full_pole_sum.py",
    witness: [
      "computations/term6-full-pole-sum.witness.json",
      "computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "residue",
    "cyclotomic",
    "quantum-dilogarithm",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [Cyclotomic residues of $\\Phi_q \\cdot \\mathrm{tr}_{M, \\ell}$ — algebraic definition](#prop:residue-at-root) is stated conditionally on it." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean encoding.** The conjecture is axiomatised as the class `QOU.BraidKnot.ResidueAtRoot` (fields: the target ring family `target : ℕ → Type` and the cyclotomic projection `project : (n : ℕ) → R →+* target n`); an instance supplies the Habiro-completion projection whose existence is the conjectural content, and [Cyclotomic residues of $\\Phi_q \\cdot \\mathrm{tr}_{M, \\ell}$ — algebraic definition](#prop:residue-at-root) is stated conditionally on it per the conditional-class convention. The archimedean per-level residue values enter downstream as the class field `residue : Fin levelBound → ℝ` of `GBResidueSpectralSum`. A fully constructive definition requires Mathlib infrastructure for meromorphic functions and the Habiro completion as a topological ring.\n\nA Lean proof awaits the meromorphic-function infrastructure. Instances supply the value directly." },
  ],
});
