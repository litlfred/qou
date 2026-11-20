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
  ],
});
