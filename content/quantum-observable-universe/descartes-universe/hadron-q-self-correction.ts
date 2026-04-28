import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hadron-q-self-correction",
  title:
    "Effective substrate parameter: hadron self-deformation of $q$",
  tags: [
    "substrate-parameter",
    "self-energy",
    "effective-q",
    "hadron",
    "linking-number",
    "back-reaction",
  ],
  lean: { ref: "qou:QOU.Descartes.hadron_q_self_correction",
    validation: "not_checked",
  },
  uses: ["prop:hadron-half-life"],
});
