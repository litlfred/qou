import { definition } from "../../schema/builders";

export default definition({
  label: "def:antineutrino-knot",
  title: "Antineutrino as mirror unknot $\\overline{T_{1,0}}$",
  tags: [
    "antineutrino",
    "unknot",
    "mirror",
    "antiparticle",
    "lepton",
    "fermion",
    "beta-decay",
  ],
  lean: {
    decl: "QOU.Descartes.Antineutrino",
    validation: "not_checked",
  },
  uses: ["prop:parity-violation-skein"],
});
