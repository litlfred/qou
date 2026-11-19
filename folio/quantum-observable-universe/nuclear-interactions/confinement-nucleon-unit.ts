import { remark } from "../../schema/builders";

export default remark({
  label: "rem:confinement-nucleon-unit",
  title:
    "Nucleon-as-unit justification from LP confinement proof",
  tags: [
    "confinement",
    "nucleon",
    "transfer-matrix",
    "lp-duality",
    "frobenius",
    "borromean",
  ],
  uses: ["prop:confinement-topological"],
  interprets: "prop:confinement-lp",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body: "The earlier statement here, \"Gram indefiniteness ($\\det G < 0$)\", quoted the convention-C determinant $-0.18920521914403668$ on the bilinear pairing and is withdrawn on both counts (2026-08-09).",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_c3_barodd_knot_operator_gram_probe.py",
    witness: "computations/qbeta/qbeta-c3-barodd-knot-operator-gram.witness.json",
    status: "verified",
  },
});
