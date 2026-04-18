import { remark } from "../../schema/builders";

/**
 * Bent ∠HOH ≈ 104.5° geometry of H₂O emerges from the LP dual's
 * preference for placing the two O-lone-pair trefoils and the two
 * O–H bonding channels into an approximately tetrahedral strand
 * arrangement around O, with lone-pair–bond repulsion slightly
 * compressing the bond angle below the ideal 109.5°.
 */
export default remark({
  interprets: "prop:h2o-lp-dual-binding",
  label: "rem:h2o-bent-geometry",
  title: "Bent $\\angle \\mathrm{HOH} \\approx 104.5^\\circ$ from lone-pair trefoils",
  uses: [
    "def:h2o-molecular-braid",
    "prop:h2o-lp-dual-binding",
    "def:ch4-molecular-braid",
  ],
  tags: [
    "H2O",
    "water",
    "bond-angle",
    "bent",
    "lone-pair",
    "VSEPR",
    "tetrahedral",
    "prediction",
  ],
});
