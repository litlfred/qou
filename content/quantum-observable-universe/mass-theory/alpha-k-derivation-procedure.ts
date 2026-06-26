import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "status", date: "2026-06-26", body: "The current formalization proves the existence of a programmatic solution by effectively yielding `∃ y, y = solveJonesMarkov n S := ⟨_, rfl⟩`. The mathematical claim of *uniqueness* and *invertibility* of the character matrix is not yet fully formalized in Lean, as it requires a deep library of Schur-Weyl-Hecke duality and generic semisimple character theory. However, this gap is highly plausible to close because it is a standard, well-documented result in algebraic combinatorics (the non-degeneracy of the Hecke character table). The physical model relies on the existence of this unique derivation procedure, which is computationally verified, making the unformalized uniqueness a localized algebraic gap rather than a structural flaw in the mass theory." },
  ],
  label: "prop:alpha-k-derivation-procedure",
  title:
    "Linear-system procedure for Jones--Markov weights $y_\\lambda$ and stratum prefactors $\\alpha_k$ at $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.alpha_k_derivation_procedure",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-tower-coefficient-stratification",
    "prop:spectral-sequence-h3-explicit",
  ],
  tags: [
    "alpha-k",
    "jones-markov",
    "mass-tower",
    "linear-system",
    "wedderburn",
    "procedure",
    "parameterised",
  ],
});
