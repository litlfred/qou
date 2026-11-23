import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:substrate-gm-torsion",
  title:
    "The substrate parameter as a $\\mathbb{G}_m$-section: torsion, specialisation, and the $q = 1$ boundary",
  uses: ["prop:ns-obstruction-tower"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [NS obstruction class](#prop:ns-obstruction-tower) (link retargeted to the defining block of the obstruction classes)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [Kummer specialisation](#prop:ns-kummer-specialisation); " },
  ],
  tags: [
    "multiplicative-group",
    "torsion",
    "specialisation",
    "projective",
    "not-root-of-unity",
  ],
});
