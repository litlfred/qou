import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:pl-jsj-mass-integration-equivalence",
  title:
    "PL/JSJ mass-integration equivalence: Markov trace = SW thimble integral over JSJ-bounded thimbles",
  lean: {
    ref: "qou:QOU.PicardLefschetz.pl_jsj_mass_integration",
    validation: "not_checked",
  },
  uses: [
    "conj:denominator-zeros-as-sw-critical-points",
    "conj:phi-q-tower-jsj-bridge",
    "prop:sw-period-thimble-equivalence",
    "prop:mi-sw-abelianisation",
    "lem:mi-sw-abelianisation-cartan",
    "def:q-pochhammer-partial-product",
    "rem:kashaev-as-archimedean-realization",
  ],
  cites: [
    "kashaev1997",
    "neumann-zagier1985",
    "thurston1978",
    "witten2011",
    "yekutieli2015",
    "zagier1986",
  ],
  tags: [
    "picard-lefschetz",
    "seiberg-witten",
    "jsj",
    "mass",
    "kashaev",
    "synthesis",
    "open-problem",
  ],
});
