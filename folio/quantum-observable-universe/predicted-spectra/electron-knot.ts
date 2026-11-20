import { definition } from "../../schema/builders";

export default definition({
  label: "def:electron-knot",
  title: "Electron",
  tags: ["electron", "lepton", "trefoil", "fermion"],
  lean: { ref: "qou:QOU.Archimedean.Electron",
    validation: "not_checked",
  },
  uses: ["def:up-quark", "rem:knot-particle-dictionary"],
});
