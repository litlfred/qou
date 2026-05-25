import { definition } from "../../schema/builders";

export default definition({
  label: "def:positron-knot",
  title: "Positron",
  tags: ["positron", "antiparticle", "trefoil", "mirror", "lepton"],
  lean: { ref: "qou:QOU.Archimedean.Positron",
    validation: "not_checked",
  },
  uses: ["rem:chirality-trefoil-electron-positron"],
});
