import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:exterior-square-borromean",
  proofs: ["prf:exterior-square-borromean"],
  title: "45 = dim_q Λ²(V_natural^10) — Borromean strand-pair representation",
  lean: {
    ref: "qou:QOU.WedderburnMass.exterior_square_borromean",
    validation: "not_checked",
  },
  uses: [
    "rem:borromean-baryon-interpretation",
    "prop:spectral-sequence-collapse",
  ],
});
