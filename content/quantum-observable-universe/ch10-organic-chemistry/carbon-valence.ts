import { remark } from "../../schema/builders";

export default remark({
  label: "rem:carbon-valence",
  title: "Carbon's four open linking sites",
  tags: [
    "carbon",
    "valence",
    "electron-shell",
    "hopf-link",
    "half-filled",
    "tetravalent",
  ],
  uses: [
    "conj:electron-shells-hopf",
    "def:covalent-bond-types",
    "def:stable-nucleus",
  ],
});
