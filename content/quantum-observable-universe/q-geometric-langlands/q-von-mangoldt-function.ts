import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-von-mangoldt-function",
  title: "The $q$-von Mangoldt function",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.QVonMangoldtFunction",
    validation: "not_checked",
  },
  uses: ["def:brings-coordinate-ring", "def:substrate-parameter-planck"],
  defines: ["q-von-mangoldt-function"],
  tags: [
    "von-mangoldt",
    "q-deformation",
    "arithmetic-function",
    "prime-counting",
  ],
});
