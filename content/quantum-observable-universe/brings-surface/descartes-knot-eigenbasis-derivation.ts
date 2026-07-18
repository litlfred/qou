import { remark } from "../../schema/builders";

export default remark({
  interprets: "cor:descartes-knot-eigenbasis",
  label: "rem:descartes-knot-eigenbasis-derivation",
  title: "Derivation of knot-eigenbasis completeness",
  tags: ["archimedean-universe", "knot-invariant", "hecke-algebra", "schur-weyl"],
  uses: [
    "cor:descartes-knot-eigenbasis",
    "cor:descartes-braid-structure",
    "thm:jones-markov-trace",
    "prop:knot-eigenbasis-complete",
  ],
});
