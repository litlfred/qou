import { remark } from "../../schema/builders";

export default remark({
  label: "rem:swampland-distance-conjecture",
  title: "Swampland correspondence: the brane tower and the Distance Conjecture",
  interprets: "def:jet-horizon",
  uses: [
    "def:jet-horizon",
    "def:recursive-brane-tower",
    "def:direct-limit-algebra",
  ],
  tags: [
    "swampland",
    "distance-conjecture",
    "brane-tower",
    "jet-horizon",
    "external-program",
  ],
  cites: ["ooguri-vafa2007"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The horizon is Lean-formalised." },
  ],
});
