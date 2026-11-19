import { definition } from "../../schema/builders";

export default definition({
  label: "def:interaction-sector-taxonomy",
  title: "Interaction-sector taxonomy",
  lean: { ref: "qou:QOU.Interactions.SectorTaxonomy.Sector" },
  uses: [
    "conj:binding-qbeta-complex-volume",
    "def:fusion-process",
  ],
  tags: [
    "interaction",
    "taxonomy",
    "strong",
    "electromagnetic",
    "weak",
    "bar-involution",
    "sector",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/h2_gg_electron/h2_gg_electron_probe.py",
    witness: [
      "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
      "computations/qbeta/qbeta-tanh-em-match-is-formal.witness.json",
    ],
    status: "verified",
  },
});
