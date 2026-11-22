import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gravitational-constant-properties",
  interprets: "def:gravitational-constant",
  title: "Variational origin and Hausdorff-dimension prediction of $G_q$",
  tags: [
    "gravitational-constant",
    "information-theory",
    "jacobson",
    "entropy-area",
    "emergent-gravity",
  ],
  uses: [
    "def:gravitational-constant",
    "def:information-speed-of-light",
    "def:operational-entropy",
    "rem:gr-substrate-geometry",
    "rem:jet-planck-steps",
    "prop:descent-eigenspaces",
    "rem:julia-hausdorff-dimension-prediction",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The associated Julia-set\nHausdorff-dimension prediction is recorded separately\n([Hausdorff-dimension prediction](#rem:julia-hausdorff-dimension-prediction))." },
  ],
  foreshadows: ["rem:julia-hausdorff-dimension-prediction"],
  cites: [
    "jacobson1995",
    "bekenstein1981",
  ],
});
