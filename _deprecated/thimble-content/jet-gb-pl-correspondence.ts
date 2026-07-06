import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-gb-pl-correspondence",
  title:
    "GB filtration $\\equiv$ jet order $\\equiv$ PL degree (under the archimedean fibre functor)",
  chapter: "archimedean-universe",
  cites: ["yekutieli2015"],
  uses: [
    "rem:picard-lefschetz-thimble",
    "prop:gb-spectral-sequence",
    "prop:e-infinity-page-identifications",
    "cor:jet-prolongation-C",
    "prop:sw-period-thimble-equivalence",
  ],
  defines: [],
  tags: [
    "picard-lefschetz",
    "jet-bundle",
    "spectral-sequence",
    "grobner-shirshov",
    "fibre-functor",
    "archimedean",
    "correspondence",
    "keystone",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.jetGBPLCorrespondence",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "computations/jet_gb_pl_correspondence.py",
    witness: "computations/jet-gb-pl-correspondence.witness.json",
    status: "not_run",
    requires: ["numpy"],
  },
});
