import { definition } from "../../schema/builders";

export default definition({
  label: "def:classical-limit-functor",
  title: "The classical limit functor $q \\to 1$",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.ClassicalLimitFunctor",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate", "def:substrate-parameter-planck"],
  tags: [
    "classical-limit",
    "functor",
    "q-to-1",
    "deformation",
    "symmetric-monoidal",
  ],
});
