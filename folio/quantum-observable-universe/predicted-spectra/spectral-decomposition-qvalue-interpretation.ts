import { remark } from "../../schema/builders";

// Manifest restored 2026-08-23. The .md and .qa.json landed in the bulk import
// `52c68267f2` alongside every sibling in this family; only this member's .ts
// was omitted, so the block has been unregistered — and invisible to the
// rendered paper — ever since. Nine of that commit's 3,593 content .md files
// were missed the same way; this is one, not a deliberate exclusion.
//
// Kind and shape are not a judgement call: they are fixed by the six
// registered siblings, and by `rj-inner-product-interpretation` two entries
// above in the same section, which is the `-interpretation` convention here.
export default remark({
  label: "rem:spectral-decomposition-qvalue-interpretation",
  title:
    "Torus knots on $\\Sigma_4$ as a self-dual basis: why the $Q$-value decomposition is exact and terminates at degree $2$",
  interprets: "cor:spectral-decomposition-qvalue",
  tags: [
    "spectral-decomposition",
    "q-value",
    "torus-knots",
    "hecke-algebra",
    "beta-decay",
  ],
  uses: ["cor:spectral-decomposition-qvalue"],
  computation: {
    engine: "mpmath",
    script: "computations/spectral_decomposition_qvalue_d.py",
    witness: "computations/spectral-decomposition-qvalue-d.witness.json",
    status: "verified",
  },
});
