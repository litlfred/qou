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
  lean: {
    decl: "QOU.Descartes.hadron_q_self_correction",
    validation: "not_checked",
  },
  uses: [
    "def:substrate-parameter",
    "def:hadron",
    "def:skein-binding-lagrangian",
    "def:stable-nucleus",
    "prop:local-substrate-q",
    "prop:hadron-half-life",
  ],
});
