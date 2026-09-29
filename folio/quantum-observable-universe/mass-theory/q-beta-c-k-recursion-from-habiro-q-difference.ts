import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  title:
    "$c_k$ precision-ladder recursion induced by the fibre-level Habiro $q$-difference equation — depth-$d$ linear recursion on $c_k$ from the $q$-shift kernel $R(q,\\xi)$ acting on $F(\\xi)$",
  lean: {
    ref: "qou:QOU.QBeta.CKRecursion.CKRecursion",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-over-e0-classical-vanishing",
    "prop:t-beta-markov-frobenius-collapse",
    "prop:alpha-em-habiro-bar-involution",
    "rem:markov-trace-inductive-limit",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004", "koelink1994"],
  computation: {
    engine: "sympy",
    script:
      "computations/qbeta/qbeta_c_k_recursion_scaffold.py",
    witness:
      "computations/qbeta/qbeta-c-k-recursion-scaffold.witness.json",
    status: "experimental",
  },
  tags: [
    "q-beta",
    "habiro",
    "precision-ladder",
    "recursion",
    "q-difference",
    "scaffolding",
    "categorical-derivation",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Scaffolding.** The Lean structure + applyRecursion method form a\nworking recursion engine; the compute scaffold demonstrates two toy\nkernels (depth-1 geometric, depth-2 underdetermined-from-seeds-alone).\nThe categorical $F(q)$ construction remains the open keystone for the\n$1\\,\\mathrm{ppQ}$ target.",
    },
  ],
});
