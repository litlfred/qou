import { remark } from "../../schema/builders";

export default remark({
  label: "rem:sign-sequence-of-braid-invariant",
  title:
    "The sign-sequence functor as a transfinite refinement of the crossing number",
  interprets: "def:sign-sequence-of-braid",
  tags: [
    "surreal-numbers",
    "braid-group",
    "hecke-algebra",
    "sign-sequence",
    "knot-invariant",
  ],
  uses: [
    "def:sign-sequence-of-braid",
    "prop:hoefsmit-seminormal-form",
    "def:birthday-grading",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): It refines the Jones polynomial ([Jones polynomial birthday refinement](#conj:jones-birthday)) and places knot complexity on a transfinite scale." },
  ],
});
