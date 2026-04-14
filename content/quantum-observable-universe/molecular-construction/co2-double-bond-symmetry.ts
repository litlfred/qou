import { remark } from "../../schema/builders";

/**
 * CO₂ double bond symmetry: VSEPR from the LP dual.
 */
export default remark({
  label: "rem:co2-double-bond-symmetry",
  title: "VSEPR molecular geometry from $\\Phi_1$ minimisation",
  interprets: "prop:co2-lp-dual-binding",
  uses: ["def:co2-molecular-braid"],
  tags: ["CO2", "VSEPR", "geometry", "symmetry", "LP-dual"],
});
