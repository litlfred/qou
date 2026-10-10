import { definition } from "../../schema/builders";

export default definition({
  label: "def:sign-sequence-of-braid",
  lean: {
    ref: "qou:QOU.AppendixSurreals.signSequenceOfBraid",
    validation: "not_checked",
  },
  title:
    "Sign-sequence functor $B_n \\to \\mathbf{No}$ via Hecke eigenspaces",
  tags: [
    "surreal-numbers",
    "braid-group",
    "hecke-algebra",
    "sign-sequence",
    "gonshor",
    "functor",
  ],
  uses: [
    "prop:hoefsmit-seminormal-form",
    "def:birthday-grading",
  ],
  cites: ["gonshor1986", "conway1976"],
});
