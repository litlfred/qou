import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gram-matrix-h3-symbolic",
  label: "rem:gram-matrix-h3-symbolic-eval-role",
  title:
    "Numerical evaluation and role of the symbolic $H_3(q)$ Gram matrix",
  tags: [
    "gram-matrix",
    "hoefsmit",
    "h3",
    "symbolic",
    "frobenius",
  ],
  uses: ["prop:gram-matrix-h3-symbolic"],
  authorNotes: [
    {
      kind: "note",
      body: "Historical note migrated from prose: prior to 2026-10-10 this block quoted Convention-C figures (det ~ -0.189, lambda ~ -0.855).",
    },
  ],
  computation: {
    engine: "numpy",
    script: "computations/gram-matrix-dual.py",
    witness: "computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
