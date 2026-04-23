import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:jones-birthday",
  title:
    "Birthday refinement of the Jones polynomial",
  tags: [
    "surreal-numbers",
    "jones-polynomial",
    "birthday",
    "knot-invariant",
    "refinement",
    "open-problem",
  ],
  uses: [
    "prop:hoefsmit-is-surreal-construction",
    "def:sign-sequence-of-braid",
    "def:birthday-grading",
  ],
  cites: ["gonshor1986"],
});
