import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-oper-hecke",
  lean: { decl: "QOU.q_oper_hecke", validation: "not_checked" },
  title: "$q$-Opers are $q$-Hecke eigensheaves",
  uses: [
    "def:q-oper",
    "def:q-hecke-eigensheaf",
    "conj:q-geometric-langlands",
  ],
  proofs: ["prf:q-oper-hecke"],
  tags: ["geometric-langlands", "oper", "hecke-algebra"],
});
