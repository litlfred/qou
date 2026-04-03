import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:electron-shells-hopf",
  title:
    "Electron shells as closed sub-Hopf links of the trefoil chain",
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
