import { definition } from "../../schema/builders";

export default definition({
  label: "def:dressed-particle",
  title: "Dressed particle via shell-attachment morphism",
  lean: { ref: "qou:QOU.BraidKnot.DressedParticle",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "def:electron-shell",
    "def:confinement-category",
    "prop:confinement-sdp",
    "prop:confinement-phase-stratification",
  ],
  tags: [
    "morphism",
    "dressing",
    "shell",
    "confinement-category",
    "atom",
    "noble-gas",
  ],
});
