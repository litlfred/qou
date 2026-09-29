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
});
