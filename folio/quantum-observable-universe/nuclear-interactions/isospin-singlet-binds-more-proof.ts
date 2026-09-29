import { proof } from "../../schema/builders";

export default proof({
  label: "prf:isospin-singlet-binds-more",
  title: "Proof: the positive numerator, and the transport to binding energy",
  of: "prop:isospin-singlet-binds-more",
  lean: {
    ref: "qou:QOU.QBeta.InterfaceScalar.singlet_binds_more",
    validation: "not_checked",
  },
  uses: ["prop:isospin-singlet-binds-more"],
  tags: ["isospin", "nn-channel", "convention-d"],
});
