import { conjecture } from "../../schema/builders";

/**
 * Shell closure is detectable from NF term count in the quotient atom model.
 */
export default conjecture({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. Chebyshev pairing identity numerically checked to 10^-40 in computations/chebyshev-pairing-engine.witness.json." },
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
