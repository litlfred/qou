import { example } from "../../schema/builders";

export default example({
  label: "ex:double-magic-Ca40-diagram",
  title:
    "Double magic ${}^{40}\\mathrm{Ca}$ — twin self-conjugate blocks, gapless interlock",
  interprets: "conj:diagrammatic-double-magic-lr-fusion",
  uses: [
    "conj:categorical-neutrality-saturated-shells",
    "conj:diagrammatic-double-magic-lr-fusion",
    "conj:homological-shell-condensation",
  ],
  tags: [
    "young-diagram",
    "magic-numbers",
    "calcium-40",
    "double-magic",
    "lr-fusion",
    "illustration",
  ],
});
