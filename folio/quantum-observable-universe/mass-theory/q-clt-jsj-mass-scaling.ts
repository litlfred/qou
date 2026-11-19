import { remark } from "../../schema/builders";

// Manifest restored 2026-08-23. The .md and .qa.json landed in the bulk import
// `52c68267f2` (3,593 content .md / 3,650 .ts) without a manifest; nine files
// were missed that way, and this is one. The block has been unregistered, and
// so absent from the rendered paper, ever since.
//
// The .md's own front-matter titled it "Remark: …", and its subject is exactly
// `conj:jsj-decomposition-linearity` ("JSJ additivity of nucleon braids") — the
// leading mass term being linear in (Z, N) because hyperbolic volume is
// additive under torus gluing. A `remark` may interpret a conjecture freely
// (AGENTS.md §3b); it makes no logical claim of its own.
//
// The YAML front-matter and H1 the .md carried were stripped: 0 of 400 sampled
// registered blocks have front-matter and 0 of 60 registered remarks open with
// an H1 — the title belongs here, and `render-latex.ts` does not strip either,
// so both would have rendered literally.
export default remark({
  label: "rem:q-clt-jsj-mass-scaling",
  title: "q-CLT / JSJ volume scaling for heavy isotopes",
  interprets: "conj:jsj-decomposition-linearity",
  tags: [
    "q-clt",
    "jsj",
    "mass-scaling",
    "heavy-isotopes",
    "binding",
  ],
  uses: ["conj:jsj-decomposition-linearity"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: m-qclt-approx.witness.json.",
    },
  ],
});
