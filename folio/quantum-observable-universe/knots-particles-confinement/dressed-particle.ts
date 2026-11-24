import { definition } from "../../schema/builders";

export default definition({
  label: "def:dressed-particle",
  title: "Dressed particle via shell-attachment morphism",
  lean: { ref: "qou:QOU.BraidsAndKnots.DressedParticle",
    validation: "not_checked",
  },
  tags: [
    "morphism",
    "dressing",
    "shell",
    "confinement-category",
    "atom",
    "noble-gas",
  ],
});
