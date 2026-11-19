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
  authorNotes: [
    {
      kind: "status",
      body: "**Tabulation block.** Aggregates existing paper content under a\nsingle Goncharov-depth ledger. Adds two new structural observations:\n(1) the Jones-faithfulness $\\Rightarrow$ Vol-injectivity implication,\n(2) the $S_5$-equivariant 4-dim depth-3 period space at $\\zeta_5$ (orbit-sum trace verified in `computations/bring-trilog-zeta5-depth-3.witness.json`).\nNeither is a new theorem; both are open structural claims awaiting\na sharp formulation.",
    },
  ],
});
