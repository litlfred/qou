import { definition } from "../../schema/builders";

export default definition({
  label: "def:classical-limit-functor",
  title: "The classical limit functor $q \\to 1$",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.ClassicalLimitFunctor",
    validation: "not_checked",
  },
  uses: [
    "def:substrate-parameter-planck",
    "def:motivic-substrate",
    "def:adelic-substrate",
    "def:classical-limit-obstruction",
  ],
  tags: [
    "classical-limit",
    "functor",
    "q-to-1",
    "deformation",
    "symmetric-monoidal",
    "adelic-assembly",
    "realization-tower",
  ],
});
