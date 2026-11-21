import { conjecture } from "../../schema/builders";

/**
 * Shell closure is detectable from NF term count in the quotient atom model.
 */
export default conjecture({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (witness [`chebyshev-pairing-engine.witness.json`](../../../computations/chebyshev-pairing-engine.witness.json))." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:shell-closure-nf-term-count",
  title: "Shell closure from NF term count",
  lean: { ref: "qou:QOU.Molecular.ShellClosureNFTermCount",
    validation: "not_checked",
  },
  uses: ["def:electron-shell-braid-capacity"],
  cites: ["iwahori1964", "jones1987"],
  tags: [
    "tier:E",
    "normal-form",
    "quotient-ideal",
    "hecke-algebra",
    "shell-closure",
  ],
});
