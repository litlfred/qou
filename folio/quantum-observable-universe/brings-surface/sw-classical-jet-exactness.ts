import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sw-classical-jet-exactness",
  lean: {
    ref: "qou:QOU.Brings.classical_jet_period_zero",
  },
  title: "The classical-jet prolongation of $\\lambda_{\\mathrm{SW}}$ is exact for $n \\ge 1$",
  uses: [
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
  ],
  proofs: ["prf:sw-classical-jet-exactness"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nThe load-bearing invariant is proved on the formal-residue model over a generic commutative ring: a local Laurent expansion is its coefficient function, the residue is the coefficient of $t^{-1}$, and a termwise derivative has vanishing $t^{-1}$ coefficient (`fresidue_fderiv`). The theorem `classical_jet_period_zero` composes this with the residue-sum shape of [The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum) (taken as an explicit hypothesis, as in the sibling `sw_period_eq_residue_sum`), and `classical_jet_period_ne_lw` concludes against the nonzero classical binding period $I(m)/m$ (involution numbers). The statement is also checked exactly at $z = \\infty$ from the sheet expansions, for jets $n = 1\\ldots4$." },
  ],
});
