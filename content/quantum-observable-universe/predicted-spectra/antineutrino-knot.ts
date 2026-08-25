import { definition } from "../../schema/builders";

export default definition({
  label: "def:antineutrino-knot",
  title: "Antineutrino as mirror unknot $T_{1,0}^{\\sigma}$",
  tags: [
    "antineutrino",
    "unknot",
    "mirror",
    "antiparticle",
    "lepton",
    "fermion",
    "beta-decay",
  ],
  lean: { ref: "qou:QOU.Archimedean.Antineutrino",
    validation: "not_checked",
  },
  uses: [],
});
