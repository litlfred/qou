import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:homological-shell-condensation",
  label: "rem:homological-shell-condensation-interpretation",
  title:
    "Condensation terminology, conditional categorical-neutrality, and supporting evidence",
  tags: [
    "magic-numbers",
    "shell-closure",
    "spectral-sequence",
    "brane-tower",
    "homological-condensation",
  ],
  foreshadows: ["prop:categorical-neutrality-saturated-shells"],
  uses: [
    "conj:homological-shell-condensation",
    "prop:categorical-neutrality-saturated-shells",
    "prop:graded-trace-residue-split",
  ],
  cites: ["yekutieli2010"],
});
