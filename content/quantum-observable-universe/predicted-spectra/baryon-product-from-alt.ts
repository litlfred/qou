import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:baryon-product-from-alt",
  title:
    "The baryon integrand $\\prod_k dc_k/dz$ is the $\\mathrm{Alt}^3$-isotype of the color-tube Jacobian",
  chapter: "archimedean-universe",
  cites: ["fulton1997", "macdonald1995"],
  uses: ["prop:atom-knot-mass-derivation"],
  defines: [],
  tags: [
    "schur-weyl",
    "alternating-representation",
    "wedderburn",
    "frobenius-pairing",
    "color-tube",
    "vandermonde",
    "baryon",
    "categorical",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.baryonProductFromAlt",
    validation: "not_checked",
  },
});
