import { example } from "../../schema/builders";

export default example({
  interprets: "def:recursive-brane-tower",
  label: "ex:brane-tower-levels",
  title: "Archimedean realisation of the brane tower",
  tags: ["archimedean", "brane-tower"],
  uses: [
    "def:recursive-brane-tower",
    "cor:jet-prolongation-C",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , determining the connection $A_2$ via [jet prolongation ($\\mathbb{C}$)](#cor:jet-prolongation-C)." },
  ],
});
