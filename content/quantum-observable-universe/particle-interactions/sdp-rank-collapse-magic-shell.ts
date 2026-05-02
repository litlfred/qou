import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:sdp-rank-collapse-magic-shell",
  title:
    "Proposition 5. Nuclear-confinement SDP rank-1 collapse selects the magic ladder (q-independent)",
  lean: {
    ref: "qou:QOU.Interactions.SDPRankCollapse.MagicShellRankConjecture",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-sdp",
    "prop:operator-selection-lp",
    "prop:bw-coefficient-shadow-price",
    "conj:categorical-neutrality-saturated-shells",
    "conj:homological-shell-condensation",
    "conj:diagrammatic-double-magic-lr-fusion",
    "prop:hoefsmit-seminormal-form",
  ],
  cites: [
    "mathas1999",
    "kassel1995",
    "hoefsmit1974",
  ],
  tags: [
    "sdp",
    "rank-collapse",
    "shadow-price",
    "magic-numbers",
    "q-independent",
    "lr-fusion",
    "open-problem",
    "axiom-class",
  ],
});
