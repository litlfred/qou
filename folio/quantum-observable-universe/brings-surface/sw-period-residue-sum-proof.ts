import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sw-period-residue-sum",
  title: "Proof that the Seiberg–Witten period is an algebraic residue sum",
  uses: [
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the keystone requires. The Lean records this as a derived consequence rather than a claim: [`QOU.Brings.period_eq_zero_of_total_residue_vanishes`](#prop:sw-period-residue-sum) and its contrapositive `total_residue_ne_zero_of_period_ne_zero`, which is what forces $E$ to be a *proper* subset. The companion witness [`QOU.Brings.sw_period_eq_residue_sum`](#prop:sw-period-residue-sum) carries the residue-sum shape as an explicit hypothesis; it does not derive it." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): A second, independent route reaches the same vanishing under the classical-jet\nrule: [The classical-jet prolongation of $\\lambda_{\\mathrm{SW}}$ is exact for $n \\ge 1$](#prop:sw-classical-jet-exactness) shows\n$\\lambda_{\\mathrm{SW}}^{(n)} = d\\bigl(X^{(n-1)}\\bigr)$ is exact, so each residue\nvanishes on its own. That argument is stronger where it applies and is scoped to\nthe classical-jet reading; the one here assumes only that the *total* vanishes,\nand is a property of the ambient surface rather than of the jet rule." },
  ],
});
