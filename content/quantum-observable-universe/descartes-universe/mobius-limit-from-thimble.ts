import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mobius-limit-from-thimble",
  title:
    "The integration limit $a(q) = (4-q)/(4q+3)$ is determined by the color-tube cubic's Galois data",
  chapter: "descartes-universe",
  cites: ["witten2011", "pham1965", "arnold-gusein-zade-varchenko1988"],
  uses: [
    "def:picard-lefschetz-thimble",
    "prop:mobius-golden-fixed-points",
    "rem:baryon-integration-limit",
  ],
  defines: [],
  tags: [
    "picard-lefschetz",
    "thimble",
    "steepest-descent",
    "integration-limit",
    "mobius-transformation",
    "color-tube",
    "archimedean",
  ],
  lean: {
    ref: "qou:QOU.Descartes.mobiusLimitFromThimble",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/mobius_limit_from_thimble.py",
    witness: "folio-assistant/computations/mobius-limit-from-thimble.witness.json",
    status: "not_run",
    requires: ["sympy", "mpmath"],
  },
});
