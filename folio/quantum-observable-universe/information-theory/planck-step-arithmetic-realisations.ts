import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:planck-time",
  label: "rem:planck-step-arithmetic-realisations",
  title: "Finite-field and $p$-adic Planck dynamics",
  tags: [
    "planck-time",
    "finite-field",
    "p-adic",
    "witt-vector",
    "algebraic-dynamics",
    "information-theory",
  ],
  uses: [
    "rem:discrete-planck-step",
    "rem:witt-lift-qou",
  ],
});
