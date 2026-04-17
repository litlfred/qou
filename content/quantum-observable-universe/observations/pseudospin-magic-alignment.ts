import { remark } from "../../schema/builders";

export default remark({
  label: "rem:pseudospin-magic-alignment",
  title:
    "Alignment with Ding et al.\\ (2026): pseudospin symmetry from the resolution scale",
  interprets: "prop:magic-numbers-from-q",
  lean: {
    decl: "QOU.Observations.PseudospinMagicAlignment",
    validation: "not_checked",
  },
  uses: [
    "prop:magic-numbers-from-q",
    "prop:nuclear-shell-intruder",
    "prop:orbital-fourier-decomposition",
    "def:borromean-baryon",
  ],
  tags: [
    "magic-numbers",
    "pseudospin",
    "spin-orbit",
    "srg",
    "resolution-scale",
    "external-comparison",
  ],
  cites: ["ding2026"],
});
