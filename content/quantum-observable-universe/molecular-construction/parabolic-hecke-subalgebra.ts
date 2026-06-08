import { definition } from "../../schema/builders";

export default definition({
  label: "def:parabolic-hecke-subalgebra",
  title: "Parabolic Hecke subalgebra $H_\\lambda(q) \\hookrightarrow H_N(q)$",
  lean: {
    ref: "qou:QOU.Molecular.ParabolicHecke",
    validation: "not_checked",
  },
  uses: ["def:molecular-strand-partition", "rem:hecke-algebra-from-braiding"],
  tags: [
    "parabolic-subalgebra",
    "young-subgroup",
    "hecke-algebra",
    "molecular",
    "wedderburn",
  ],
});
