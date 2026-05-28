import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-oper-hecke",
  lean: { ref: "qou:QOU.QGeometricLanglands.q_oper_hecke", validation: "not_checked" },
  title: "$q$-Opers are $q$-Hecke eigensheaves",
  uses: [
    "def:q-oper",
    "prop:q-geometric-langlands",
  ],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "oper", "hecke-algebra"],
});
