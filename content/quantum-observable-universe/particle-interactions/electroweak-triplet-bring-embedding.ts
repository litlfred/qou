import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:electroweak-triplet-bring-embedding",
  title:
    "The even-twist triplet $T(2,4), T(2,6), T(2,8)$ co-embeds in Bring's genus-$4$ fiber",
  lean: {
    ref: "qou:QOU.Archimedean.electroweak_triplet_bring_embedding",
    validation: "not_checked",
  },
  uses: [
    "def:brings-surface",
    "prop:torus-embeddable-complete",
    "thm:hoefsmit-ew-cell-content",
  ],
  tags: [
    "electroweak",
    "torus-link",
    "seifert-genus",
    "bring-embedding",
    "provable",
  ],
});
