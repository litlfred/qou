import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:one-loop-prefactor-provenance",
  title:
    "The 1-loop prefactor law splits: the exponent $-1/2$ is normalisation-invariant and measured, and on the link side the constant $k$ is derived from van der Veen rather than calibrated",
  chapter: "mass-theory",
  lean: {
    ref: "qou:QOU.OneLoopPrefactorInvariance.k_const_iff_exponent_neg_half",
    validation: "checked",
  },
  uses: ["conj:b1-hyperbolic-rows-theorem"],
  cites: [
    "dimofte-gukov-lenells-zagier-2009",
    "gukov-murakami-2008",
    "vanderveen2008",
    "dimofte-garoufalidis-2013",
    "garoufalidis-yoon-2024",
  ],
  tags: [
    "one-loop",
    "prefactor",
    "adjoint-torsion",
    "volume-conjecture",
    "whitehead-link",
    "borromean-rings",
    "normalisation-convention",
    "c-sigma",
    "van-der-veen",
    "dglz",
  ],
});
