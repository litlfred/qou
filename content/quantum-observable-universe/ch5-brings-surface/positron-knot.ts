import { definition } from "../../schema/builders";

export default definition({
  label: "def:positron-knot",
  title: "Positron",
  tags: ["positron", "antiparticle", "trefoil", "mirror", "lepton"],
  lean: {
    decl: "QOU.Descartes.Positron",
    validation: "not_checked",
  },
  uses: [
    "def:electron-knot",
    "def:down-quark",
    "rem:chirality-trefoil-electron-positron",
  ],
});
