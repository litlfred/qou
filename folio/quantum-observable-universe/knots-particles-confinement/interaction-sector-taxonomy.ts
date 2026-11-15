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
});
