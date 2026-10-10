import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:fermion-boson-decomposition",
  label: "rem:archimedean-leptons",
  title: "Electrons, muons and the Reeb decomposition",
  tags: ["archimedean-universe", "leptons", "reeb-decomposition"],
  uses: [
    "ex:reeb-decomposition",
    "def:fermion-boson-decomposition",
  ],
});
