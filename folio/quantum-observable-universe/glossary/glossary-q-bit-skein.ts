import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-q-bit-skein",
  title: "One $q$-bit $=$ one Skein operation",
  interprets: "rem:glossary-q-bit",
  tags: ["glossary", "q-bit", "skein-relation", "transfer-matrix", "crossing-resolution", "markov-trace"],
  uses: ["rem:glossary-q-bit", "def:categorical-transfer-matrix"],
  defines: ["q-bit-skein"],
});
