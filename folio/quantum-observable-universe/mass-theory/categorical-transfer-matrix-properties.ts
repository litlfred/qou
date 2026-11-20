import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-transfer-matrix-properties",
  interprets: "def:categorical-transfer-matrix",
  title:
    "Configuration space, bi-filtration, and categorification of $\\mathcal{T}(\\mathfrak{H})$",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "equivalence-class", "braiding", "configuration-space",
    "interaction-filtration",
  ],
  uses: [
    "def:categorical-transfer-matrix",
    "def:hadron",
    "def:localized-hadron",
    "def:exceptional-divisor",
    "rem:knot-factorization",
    "def:vertex-operator",
    "rem:observation-braid",
    "prop:jet-prolongation",
    "rem:jet-planck-steps",
    "def:bundle-initial-conditions",
    "def:operational-entropy",
    "thm:markov-trace-product",
    "conj:crystal-graph-realization",
  ],
  cites: [
    "brundankleshchev2009",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Only the parenthetical example changed (it gave the up quark the knot $T_{2,3}$). Not checked here: whether any downstream use of the constituent-slot embedding $K_i \\hookrightarrow V^{\\otimes 2j_i}$ took $j_i$ from a trefoil quark; if so it needs re-scoping to the unknot strand." },
  ],
});
