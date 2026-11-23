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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): *Processes* are not sectors: a [fusion process](#def:fusion-process) is a strand-balanced rearrangement inside the strong sector, while β-decay moves proton number on the subject side and is thereby routed to the weak sector. The bar-even and bar-odd channels are intertwined by the bar involution itself — the rotation between the two channel recurrences of [the binding–$Q_\\beta$ complex volume conjecture](#conj:binding-qbeta-complex-volume) — so the taxonomy's parity column is a statement about where each sector's observable lives, not a wall between algebras." },
  ],
});
