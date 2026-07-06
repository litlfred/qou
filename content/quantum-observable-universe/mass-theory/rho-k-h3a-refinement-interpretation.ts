import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:rho-k-h3a-refinement",
  label: "rem:rho-k-h3a-refinement-interpretation",
  title: "Block-local binding correction $\\Delta_\\lambda$ as categorical shell structure",
  uses: [
    "prop:rho-k-h3a-refinement",
    "conj:hoefsmit-scattering-pipeline",
  ],
});
