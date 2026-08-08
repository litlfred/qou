import { definition } from "../../schema/builders";

/**
 * Atomic valence v(Z) = min(Z_val, 2·n_val² − Z_val) and the lone pair as the
 * Φ₁-cheaper-bound-than-shared electron pair. Split out of
 * def:electron-shell-braid-capacity (the second definiendum).
 */
export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). The valence count is a generic combinatorial quantity." },
  ],
  label: "def:atomic-valence-open-sites",
  title: "Valence and lone pairs as open bonding sites",
  lean: {
    ref: "qou:QOU.Molecular.atomicValence",
    validation: "not_checked",
  },
  uses: ["def:electron-shell-braid-capacity"],
  tags: [
    "valence",
    "lone-pair",
    "open-sites",
    "covalent-bond",
  ],
});
