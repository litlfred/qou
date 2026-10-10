import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:neutron-prediction-comparison",
  title:
    "Comparison of predicted and observed stable neutron numbers for $p \\leq 103$",
  tags: [
    "stability-cubic",
    "neutron-number",
    "codata",
    "comparison",
    "beta-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.stable_neutron_max_error",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-10",
      body:
        "**$c = 0.01497$ is not reproduced by any chain the corpus states, and the republish is HELD pending the author (bean `qou-opjb`).** The display and the $n_{\\mathrm{pred}}$ inversion are now consistent with `prop:beta-stability`, whose $a_C$ no longer double-counts $(q-q^{-1})$ — neither edit moves a number. What remains is the numeral. Measured in `decimal` at 50 digits (no float64), proton pin, $m_e$ from the corpus CODATA table: the coefficient assignments $\\lambda_C = (q-q^{-1})[6]_q m_e$ and $a_{\\mathrm{asym}} = 3[2]_q[7]_q m_e$ give $c = 0.01451583$ (**-3.03 %** from the published value), the SEMF ratio $0.714/(2\\cdot 23.69)$ gives $0.01506965$ (**+0.67 %**), and the superseded chain $a_C = (q-q^{-1})\\lambda_C$ gave $0.00303468$ (**-79.73 %**). So neither candidate provenance reproduces 0.01497 and the margin does not discriminate: the derived $a_{\\mathrm{asym}} = 23.50663$ MeV is itself within 0.77 % of the empirical SEMF $a_A = 23.69$ MeV. **Epistemic tier, which is the reason this is held:** the two coefficients are `noncomputable def`s in `lean/QOU/Interactions/QIntegerMassFormula.lean` carrying `-- Ref: [manuscript] Ch 11 \u00a78`, NOT theorems. Its only two theorems about them (`asym_volume_relation`, `exchange_coulomb_relation`) are discharged by `unfold; ring` / `unfold; field_simp`, i.e. true by definition — notation, not content, by AGENTS.md Strict Lean Discipline item 8. Nothing derives the assignments $[6]_q$ or $3[2]_q[7]_q$. So replacing 0.01497 with 0.01451583 would swap an untraced numeral for a definitionally-asserted one; that is an improvement but is not a derivation, and republishing it moves the reported $\\overline{|\\Delta n|}$. Awaiting the author's word.",
    },
  ],
});
