import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:f4-wedderburn-sdp-shadow-price",
  title:
    "Shadow-price identification of active Wedderburn blocks: the dual support equals the irrep support of $T_\\beta$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.f4_wedderburn_sdp_shadow_price",
    validation: "not_checked",
  },
  uses: [
    "prop:hecke-markov-transition",
    "prop:hoefsmit-seminormal-form",
    "prop:f4-tensor-composer-lr",
  ],
  cites: ["stanley1999"],
  tags: [
    "f4",
    "wedderburn",
    "shadow-price",
    "lp-duality",
    "schrijver",
    "discovery",
    "entangled-braid",
  ],
});
