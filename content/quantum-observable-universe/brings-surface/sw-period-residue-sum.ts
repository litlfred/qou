import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sw-period-residue-sum",
  lean: {
    ref: "qou:QOU.Brings.sw_period_eq_residue_sum",
    validation: "not_checked",
  },
  title: "The Seiberg–Witten period is an algebraic residue sum",
  uses: [
    "prop:mi-sw-abelianisation",
    "rem:brings-smoothness",
  ],
  proofs: ["prf:sw-period-residue-sum"],
});
