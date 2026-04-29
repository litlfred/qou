import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-gb-pl-correspondence",
  title:
    "GB filtration $\\equiv$ jet order $\\equiv$ PL degree (under the archimedean fibre functor)",
  chapter: "descartes-universe",
  cites: ["yekutieli2015"],
  uses: [
    "def:picard-lefschetz-thimble",
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
    ref: "qou:QOU.Descartes.jetGBPLCorrespondence",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "folio-assistant/computations/jet_gb_pl_correspondence.py",
    witness: "folio-assistant/computations/jet-gb-pl-correspondence.witness.json",
    status: "not_run",
    requires: ["numpy"],
  },
});
