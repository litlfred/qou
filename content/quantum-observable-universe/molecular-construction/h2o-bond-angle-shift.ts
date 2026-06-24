import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:h2o-bond-angle-shift",
  proofs: ["prf:h2o-bond-angle-shift"],
  title: "Bent angle as a quadratic-well shift",
  lean: {
    ref: "qou:QOU.Molecular.bond_angle_shift",
    validation: "not_checked",
  },
  uses: ["def:h2o-molecular-braid"],
  tags: ["water", "H2O", "bond-angle", "quadratic", "harmonic", "lone-pair"],
});
