import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hecke-baer-star-generic",
  label: "rem:hecke-baer-star-generic-interpretation",
  title:
    "Co-location with the volume conjecture and significance for the depth correspondence's period witnesses",
  tags: [
    "baer-star",
    "hecke-algebra",
    "volume-conjecture",
    "period-classes",
    "wall-crossing",
  ],
  uses: [
    "prop:hecke-baer-star-generic",
    "conj:kashaev-volume-conjecture",
    "rem:vc-as-depth-2-instance",
    "conj:gb-depth-period-correspondence",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Kashaev volume conjecture](#conj:kashaev-volume-conjecture))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): See [Volume Conjecture as the depth-2 instance of GS $\\leftrightarrow$ period correspondence](#rem:vc-as-depth-2-instance) for the depth-$2$ reading." },
  ],
});
