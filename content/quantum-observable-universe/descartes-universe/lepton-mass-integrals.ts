import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:brings-surface",
  label: "rem:lepton-mass-integrals",
  title: "Electron and muon mass from Seiberg--Witten integrals",
  tags: [
    "lepton",
    "electron",
    "muon",
    "mass",
    "seiberg-witten",
    "jet-bundle",
    "residue",
  ],
  uses: ["rem:generation-dependent-sw"],
});
