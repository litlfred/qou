import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:covalent-bond-types",
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
  uses: ["def:covalent-bond-types"],
});
