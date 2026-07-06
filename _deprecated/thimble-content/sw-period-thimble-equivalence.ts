import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sw-period-thimble-equivalence",
  title:
    "Equivalence of categorical Markov–Frobenius pairing and SW thimble periods on $\\mathcal{E}_q$",
  chapter: "archimedean-universe",
  cites: ["witten2011", "yekutieli2015", "grothendieck1966", "hartshorne1966", "pham1965"],
  uses: [
    "rem:picard-lefschetz-thimble",
    "rem:lepton-mass-integrals",
    "prop:descartes-elliptic-curve",
    "prop:e-infinity-page-identifications",
    "prop:gb-spectral-sequence",
    "prop:categorical-mass-markov",
    "prop:baryon-product-from-alt",
    "conj:mobius-limit-from-thimble",
    "rem:yekutieli-stokes",
  ],
  defines: [],
  tags: [
    "picard-lefschetz",
    "seiberg-witten",
    "thimble",
    "spectral-sequence",
    "frobenius-pairing",
    "non-abelian-stokes",
    "schur-weyl",
    "archimedean",
    "equivalence",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.swPeriodThimbleEquivalence",
    validation: "not_checked",
  },
  computation: {
    engine: "scipy",
    script: "computations/sw_period_thimble_equivalence.py",
    witness:
      "computations/sw-period-thimble-equivalence.witness.json",
    status: "not_run",
    requires: ["numpy", "scipy"],
  },
});
