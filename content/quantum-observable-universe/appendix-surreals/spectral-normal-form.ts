import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:spectral-normal-form",
  title:
    "Spectral gap closure and singularity formation as $q \\to 1$ read from normal-form exponents",
  tags: [
    "surreal-numbers",
    "spectral-gap",
    "conway-normal-form",
    "leading-exponent",
    "singularity",
    "q-deformation",
    "open-problem",
  ],
  uses: [
    "rem:conway-normal-form",
    "rem:big-o-surreal",
    "def:standard-part-functor",
    "conj:classical-limit-stpart",
  ],
  cites: [
    "conway1976",
    "berarducci-mantova2018",
  ],
});
