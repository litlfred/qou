import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sw-period-thimble-equivalence",
  title:
    "Equivalence of categorical Markov–Frobenius pairing and SW thimble periods on $\\mathcal{E}_q$",
  chapter: "descartes-universe",
  cites: ["witten2011", "yekutieli2015"],
  uses: [
    "def:picard-lefschetz-thimble",
    "rem:lepton-mass-integrals",
    "prop:descartes-elliptic-curve",
    "prop:e-infinity-page-identifications",
    "prop:gb-spectral-sequence",
    "prop:categorical-mass-markov",
    "prop:baryon-product-from-alt",
    "prop:mobius-limit-from-thimble",
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
    ref: "qou:QOU.Descartes.swPeriodThimbleEquivalence",
    validation: "not_checked",
  },
  computation: {
    engine: "scipy",
    script: "folio-assistant/computations/sw_period_thimble_equivalence.py",
    witness:
      "folio-assistant/computations/sw-period-thimble-equivalence.witness.json",
    status: "not_run",
    requires: ["numpy", "scipy"],
  },
});
