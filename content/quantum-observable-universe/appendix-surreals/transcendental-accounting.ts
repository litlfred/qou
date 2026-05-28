import { remark } from "../../schema/builders";

export default remark({
  label: "rem:transcendental-accounting",
  title:
    "Transcendental-accounting ledger: every period in the paper, indexed by Goncharov depth",
  interprets: "rem:algebraic-core-survives",
  uses: [
    "rem:chirality-period-pairing",
    "rem:bring-embeddable-knots",
    "prop:vol-through-tau",
  ],
  cites: [
    "kontsevich1995",
    "zagier1986",
    "bloch2000",
    "suslin1991",
    "thurston1978",
    "neumann-zagier1985",
    "kashaev1997",
  ],
  tags: [
    "transcendental-accounting",
    "goncharov-period-filtration",
    "wall-crossing",
    "post-archimedean",
    "q-rational-structure",
    "S5-galois-orbit",
    "ledger",
  ],
});
