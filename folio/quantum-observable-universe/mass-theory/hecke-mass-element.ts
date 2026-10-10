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
  lean: { ref: "qou:QOU.Torsion.HeckeMassElement",
    validation: "not_checked",
  },
  uses: [
    // The mass integrand this definition builds.
    "def:mass-identity",
    "rem:hecke-algebra-from-braiding",
    // Fixes tr_M : H_n(R, q) -> k in the setup sentence.
    "thm:jones-markov-trace",
  ],
});
