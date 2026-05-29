import { remark } from "../../schema/builders";

export default remark({
  label: "rem:electron-shells-hopf",
  interprets: "prop:torus-hopf-stability",
  title:
    "Electron shells as closed sub-Hopf links of the trefoil chain",
  lean: {
    ref: "qou:QOU.ElectronShellsHopf.ElectronShellsHopf",
    validation: "not_checked",
  },
  tags: [
    "electron",
    "shell",
    "hopf-link",
    "sub-link",
    "photon",
    "orbital",
    "trefoil",
    "absorption",
  ],
  uses: [
    "prop:torus-hopf-stability",
  ],
});
