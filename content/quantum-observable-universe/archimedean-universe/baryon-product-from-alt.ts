import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:baryon-product-from-alt",
  title:
    "The baryon integrand $\\prod_k dc_k/dz$ is the $\\mathrm{Alt}^3$-isotype of the color-tube Jacobian",
  chapter: "descartes-universe",
  cites: ["fulton1991", "macdonald1995"],
  uses: [
    "rem:color-tube-cubic",
    "prop:atom-knot-mass-derivation",
    "thm:frobenius-codim-universal",
  ],
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
    ref: "qou:QOU.Descartes.baryonProductFromAlt",
    validation: "not_checked",
  },
  computation: {
    engine: "scipy",
    script: "folio-assistant/computations/baryon_product_from_alt.py",
    witness: "folio-assistant/computations/baryon-product-from-alt.witness.json",
    status: "not_run",
    requires: ["numpy", "scipy"],
  },
});
