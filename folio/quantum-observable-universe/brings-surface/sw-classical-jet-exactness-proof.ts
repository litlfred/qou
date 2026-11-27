import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sw-classical-jet-exactness",
  title: "Proof that the classical-jet prolongation is exact and period-free",
  uses: [
    "prop:sw-classical-jet-exactness",
    "prop:sw-period-residue-sum",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): with $I(m)$ the involution numbers (Lean `involutionNumber_pos`), and a vanishing period cannot equal a nonzero number. The Lean witness `QOU.Brings.classical_jet_period_zero` proves the coefficient-level core (`fresidue_fderiv`: the $t^{-1}$ coefficient of a termwise derivative vanishes, over a generic commutative ring) and composes it with the residue-sum hypothesis; `classical_jet_period_ne_lw` concludes the non-realisability." },
  ],
});
