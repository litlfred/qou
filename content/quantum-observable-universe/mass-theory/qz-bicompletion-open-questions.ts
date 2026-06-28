import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:qz-bicompletion",
  label: "rem:qz-bicompletion-open-questions",
  title:
    "Open questions for the $(q,z)$-bicompletion mass element",
  tags: [
    "bicompletion",
    "open-construction",
    "volume-conjecture",
    "non-archimedean",
    "p-adic",
  ],
  uses: [
    "def:qz-bicompletion",
    "rem:qz-bicompletion-properties",
    "prop:quantum-dilogarithm-stratified",
    "def:motivic-substrate",
  ],
});
