import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:descartes",
  label: "rem:descartes-calabi-yau",
  title: "The Descartes condition on examples",
  tags: ["descartes-universe", "calabi-yau", "ale", "affine"],
  uses: [
    "ex:calabi-yau",
    "ex:ale",
  ],
});
