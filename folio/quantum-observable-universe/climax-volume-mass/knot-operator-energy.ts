import { definition } from "../../schema/builders";

export default definition({
  label: "def:knot-operator-energy",
  title: "Knot operator energy (LP-dual shadow price)",
  lean: { ref: "qou:QOU.BraidKnot.KnotOperatorEnergy",
    validation: "not_checked",
  },
  uses: ["def:stable-atom", "prop:operator-selection-lp"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Interpretation of the subtrahend $1/[k]_q!$.** In [the operator-selection LP](#prop:operator-selection-lp), the net-constraint dual multiplier is identically zero at every $n$ and $q$ because the normal-form basis contains the identity and the first Frobenius row coincides with the objective vector. The subtrahend $1/[k]_q!$ in the displayed formula is therefore the minimum normalized weight $\\min_{\\lambda \\vdash k} w_\\lambda(q)/d_\\lambda(q)$ across partitions of $k$ (attained on the one-dimensional representations $(k)$ and $(1^k)$), rather than a nonzero dual multiplier of the normalisation constraint." },
  ],
  cites: [],
  tags: [
    "knot-operator",
    "shadow-price",
    "lp-dual",
    "energy-functional",
  ],
});
