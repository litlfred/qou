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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which we precompute once via `build_nucleon_nf`." },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body: "The earlier statement here, \"Gram indefiniteness ($\\det G < 0$)\", quoted the convention-C determinant $-0.18920521914403668$ on the bilinear pairing and is withdrawn on both counts (2026-08-09).",
    },
  ],
});
