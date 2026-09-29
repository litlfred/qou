import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:birthday-axioms-underdetermine",
  title:
    "The birthday axioms do not characterise Conway's birthday: a two-valued " +
    "function satisfies all six",
  tags: [
    "surreal",
    "hyperreal",
    "axiomatisation",
    "defect-report",
    "limit-transfer",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.HyperrealTransfer.flatBirthday_avg_le",
    validation: "leanok",
  },
  uses: ["prop:ideal-tetrahedron-relabelling-invariance"],
  cites: ["conway1976", "robinson1966"],
});
