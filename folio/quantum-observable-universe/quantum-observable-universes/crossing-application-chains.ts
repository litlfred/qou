import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:crossing-application-chains",
  title: "Closed chains of crossing applications on words and on states",
  lean: {
    ref: "qou:QOU.Chronology.not_closedChainAt_tick",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: ["prop:braiding-induced-ordering"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): For example, for $H_n(q)$ at generic $q$ neither condition is established here." },
  ],
  tags: [
    "arrow-of-time",
    "well-ordering",
    "braid-group",
    "writhe",
    "symmetric-braiding",
    "closed-chains",
  ],
});
