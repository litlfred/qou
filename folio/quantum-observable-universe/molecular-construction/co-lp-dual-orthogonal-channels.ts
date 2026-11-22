import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:co-lp-dual-binding",
  label: "rem:co-lp-dual-orthogonal-channels",
  title: "Orthogonal-channel derivation of the $CO$ bond order",
  uses: ["prop:h2-lp-dual-binding"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([carbon valence](#rem:carbon-valence))" },
  ],
  tags: ["CO", "LP-dual", "orthogonal-channels", "bond-order"],
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/co_bond_order_active_set.py",
    witness: ["computations/co-bond-order-active-set.witness.json"],
  },
});
