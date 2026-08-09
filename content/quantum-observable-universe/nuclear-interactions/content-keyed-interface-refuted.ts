import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:content-keyed-interface-refuted",
  title:
    "No interface keyed on nucleon content can work: the two $pn$ channels share content and differ in boundness",
  lean: {
    ref: "qou:QOU.QBeta.InterfaceScalar.content_keyed_interface_refuted",
    validation: "not_checked",
  },
  uses: ["prop:isospin-singlet-binds-more"],
  tags: [
    "refutation",
    "isospin",
    "nn-channel",
    "crossing-multiplicity",
    "deuteron",
  ],
});
