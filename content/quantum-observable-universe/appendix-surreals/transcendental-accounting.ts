import { remark } from "../../schema/builders";

export default remark({
  label: "rem:transcendental-accounting",
  title:
    "Transcendental-accounting ledger: every period in the paper, indexed by Goncharov depth",
  interprets: "rem:algebraic-core-survives",
  uses: [
    "rem:algebraic-core-survives",
    "conj:gb-depth-period-correspondence",
    "rem:figure-8-archimedean-illustration",
    "conj:bring-figure-eight-depth-2-witness",
    "conj:bring-trilog-depth-3-witness",
    "rem:chirality-period-pairing",
    "prop:explicit-central-idempotent",
    "rem:bring-embeddable-knots",
    "rem:knot-exhaustiveness",
    "prop:quantum-dilogarithm-stratified",
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
