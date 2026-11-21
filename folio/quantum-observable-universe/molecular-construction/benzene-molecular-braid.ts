import { definition } from "../../schema/builders";

/**
 * Benzene molecular braid: C₆H₆ with delocalized π electrons.
 */
export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Step 5 originally linked \"threading link\" to the emergence proposition: 5. *Add $\\pi$ electrons: 6 electrons form a [threading link](#prop:benzene-threading-emergence) $T(2, 6)$ around the ring.*" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): *The threading link of step 5 emerges from the LP dual as the optimal configuration for the remaining 6 electrons, rather than being postulated.*" },
  ],
  label: "def:benzene-molecular-braid",
  title: "Benzene $C_6H_6$ as a molecular braid",
  lean: { ref: "qou:QOU.Molecular.BenzeneBraid",
    validation: "not_checked",
  },
  uses: ["def:ch4-molecular-braid"],
  tags: [
    "benzene",
    "C6H6",
    "aromatic",
    "delocalization",
    "threading-link",
    "molecular-braid",
  ],
});
