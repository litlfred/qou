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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): All of this is proved over any field in the library module `QOU.Interactions.EmCouplingBarParity`." },
  ],
});
