import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:aether-line-bundle",
  label: "rem:aether-line-bundle-remark",
  renamedFrom: ["rem:substrate-line-bundle-remark"],
  title: "Archimedean fibring, $\\mathbb{P}^1$-compactification and base change of the aether bundle",
  uses: ["def:aether-line-bundle", "def:aether-parameter"],
});
