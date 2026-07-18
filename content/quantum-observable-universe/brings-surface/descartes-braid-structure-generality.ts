import { remark } from "../../schema/builders";

export default remark({
  interprets: "cor:descartes-braid-structure",
  label: "rem:descartes-braid-structure-generality",
  title: "Base-ring generality and the $\\mathfrak{p}$-adic realisation",
  tags: ["archimedean-universe", "braid-group", "dic3"],
  uses: [
    "cor:descartes-braid-structure",
    "ex:p-adic-realisation",
  ],
});
