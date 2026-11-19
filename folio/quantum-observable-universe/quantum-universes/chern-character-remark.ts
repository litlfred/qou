import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chern-character-remark",
  title: "The block presentation of the Chern character and the factorisation of the quantum dimension",
  interprets: "def:chern-character",
  uses: ["def:chern-character", "def:rigid-monoidal-category", "rem:grothendieck-group-of-a-qou-remark"],
  tags: ["chern-character", "hochschild-homology", "grothendieck-group", "quantum-dimension", "trace"],
  cites: ["bghl-2017"],
});
