import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-oper-hecke",
  lean: { ref: "qou:QOU.q_oper_hecke", validation: "not_checked" },
  title: "$q$-Opers are $q$-Hecke eigensheaves",
  uses: [
    "def:q-oper",
    "conj:q-geometric-langlands",
  ],
  cites: ["frenkel2007"],
  tags: ["geometric-langlands", "oper", "hecke-algebra"],
});
