import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:exterior-square-borromean",
  title: "$45 = \\dim_q \\Lambda^2(V_{\\mathrm{nat}}^{10})$ — Borromean strand-pair representation",
  lean: {
    ref: "qou:QOU.WedderburnMass.exterior_square_borromean",
    validation: "not_checked",
  },
  uses: [
    "rem:borromean-baryon-interpretation",
    "prop:spectral-sequence-collapse",
  ],
});
