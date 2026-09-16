import { remark } from "../../schema/builders";

export default remark({
  label: "rem:yekutieli-setting-explicit",
  title: "Yekutieli's hypotheses made explicit: which the axioms supply, and which they do not",
  interprets: "prop:yekutieli-lifting",
  uses: [
    "prop:yekutieli-lifting",
    "def:yekutieli-lifting-condition",
    "def:quantum-characteristic-classes",
    "def:spatial-realization-functor",
    "def:hochschild-homology",
  ],
  foreshadows: ["rem:hkr-theorem"],
  cites: ["yekutieli2010", "kontsevich-2003", "hkr-1962", "hartshorne-1977"],
  tags: ["yekutieli", "gerbes", "deformation-quantization", "maurer-cartan", "formal-parameter", "smoothness", "hypotheses"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Part of the 2026-09-15 explicit-layer selection (owner option B), recording §10 of the analysis doc `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md`. The table is a hypothesis ledger, not a proof: it names, for each of Yekutieli's standing assumptions, what the corpus has in its place and which reading closes the gap. The two rows that change wording in a definition (smoothness of the base; the formal parameter) are recorded here and left for the owner; nothing in the proposition is altered.",
    },
  ],
});
