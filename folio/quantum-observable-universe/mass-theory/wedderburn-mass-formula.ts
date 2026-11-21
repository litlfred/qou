import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:wedderburn-mass-formula",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Moved out of the prose by the voice-leak drain (qou-d4kh, W14b, 2026-11-21): Lean names for the facts stated in the prose: `extremal_exhausts_iff_n_le_three` (extremal blocks exhaust the partition lattice iff n ≤ 3), `non_extremal_irreps_at_n_eq_four`, `adjacentChain_twice_lt_allPairs_twice`, and `QOU.Mass.WedderburnMassFormulaCoefficients.beta3_of_beta2` (2β₃ + β₂ + 6 = 0)." },
  ],
  title: "Three-invariant atomic mass formula",
  lean: { ref: "qou:QOU.WedderburnMass.atomicMass",
    validation: "not_checked",
  },
});
