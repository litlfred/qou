import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qz-bicompletion-properties",
  interprets: "def:qz-bicompletion",
  title:
    "Cyclotomic apex, conjectural mass element, and open questions for the $(q,z)$-bicompletion",
  tags: [
    "habiro-ring",
    "bicompletion",
    "cyclotomic-completion",
    "brane-tower",
    "colored-jones",
    "open-construction",
  ],
  uses: [
    "def:qz-bicompletion",
    "def:habiro-ring",
    "def:z-habiro-ring",
    "conj:mass-endomorphism",
    "conj:brane-tower-z-habiro",
    "conj:quantum-dilogarithm-stratified",
    "def:motivic-substrate",
  ],
});
