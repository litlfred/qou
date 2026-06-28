import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:categorical-neutrality-saturated-shells",
  label: "rem:categorical-neutrality-saturated-shells-interpretation",
  title:
    "Self-conjugate support, the dropped locality assumption, and operator-level vs character-sum reading",
  tags: [
    "magic-numbers",
    "shell-closure",
    "full-twist",
    "global-section",
    "categorical-neutrality",
  ],
  uses: [
    "prop:categorical-neutrality-saturated-shells",
    "prop:hoefsmit-seminormal-form",
    "rem:phi-n-global-section",
    "prop:atom-knot-mass-derivation",
  ],
  cites: ["geckpfeiffer2000", "mathas1999"],
});
