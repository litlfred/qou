import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ew-triplet-far-commuting-minimal",
  title:
    "Far-commuting minimality: three even-twist torus-link generators fit minimally in $B_6$ at $(1,3,5)$, enumerating $\\{T(2,4),T(2,6),T(2,8)\\}$",
  lean: {
    ref: "qou:QOU.ParticleInteractions.electroweak_triplet_far_commuting_minimal",
    validation: "not_checked",
  },
  uses: [
    "prop:electroweak-triplet-bring-embedding",
    "thm:hoefsmit-ew-cell-content",
  ],
  tags: [
    "electroweak",
    "torus-link",
    "far-commutativity",
    "braid-group",
    "seifert-genus",
    "provable",
  ],
});
