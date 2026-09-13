import { definition } from "../../schema/builders";

/**
 * Atomic braid definition: electrons in the nuclear braid.
 */
export default definition({
  label: "def:atomic-braid",
  title: "Atomic braid $H_{A+Z}(q)$",
  lean: { ref: "qou:QOU.AtomicBraid.NeutralAtom",
    validation: "not_checked",
  },
  uses: ["def:derived-atom"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-12",
      body:
        "**Owner ruling: $\\mathcal{A}$ is the $A+Z$ object.** This corpus " +
        "carried two braids both called \"the atomic braid\" and both written " +
        "$\\mathcal{A}$ — the one defined here, and the production $3A$ word " +
        "$\\mathcal{B}_K$. The ruling makes the definition here canonical for " +
        "the symbol and is a **scoping** decision: no call site moves, because " +
        "the $3A$ object already has its own register entry. Decided on the " +
        "recorded $\\Phi_3$ column of the $Z=1$–$20$ mass table, which this " +
        "definition's strand content reproduces on 19 of 19 rows " +
        "parameter-free — with Table 1's own crossing values — while the " +
        "nucleon-only, $3A$ and $3A+Z$ contents each reproduce 0. A third " +
        "count $3A+Z$ remains live and unresolved in " +
        "`mass-endomorphism/atomic-mass-gb-nf.md`, which cites this block " +
        "while using a count this block contradicts; the ruling does not " +
        "settle it. Bean `qou-jgg0`.",
      see: "docs/audits/2026-09-12-phi3-column-discriminates-the-strand-count.md",
    },
  ],
});
