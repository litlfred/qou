import { definition } from "../../schema/builders";

export default definition({
  label: "def:hecke-mass-element",
  title: "Hecke mass element",
  tags: [
    "hecke-algebra",
    "mass",
    "frobenius-hopf",
    "fibre-functor",
    "schur-weyl",
  ],
  lean: { ref: "qou:QOU.Braiding.HeckeMassElement",
    validation: "not_checked",
  },
  uses: ["rem:hecke-algebra-from-braiding"],
});
