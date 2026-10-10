import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-09-04", body: "Two Lean carriers. The primary definition (categorical action difference) is `QOU.Archimedean.QqValue.value` in the sibling `q-value-transition.lean`, which `lean.ref` names. The mass-difference form is carried separately by `QOU.Archimedean.QValueTransition` (library file `lean/QOU/Archimedean/QValueTransition.lean`), whose `q_mass_difference` proves the expansion $Q = m_n - m_p - m_e + (B(Z{+}1,N{-}1) - B(Z,N))$. Before 2026-09-04 the `.md` labelled the mass-difference form \"primary\" while the title and the sibling Lean defined the action difference, and `lean.ref` named the library structure; the mismatch is bean `qou-181p`." },
  ],
  label: "def:Q-value-transition",
  title:
    "$\\mathcal{Q}_q$-Value as Categorical Action Difference",
  tags: [
    "q-value",
    "transition-energy",
    "beta-decay",
    "crossing-change",
    "recoil",
    "kinetic-energy",
    "skein",
  ],
  lean: { ref: "qou:QOU.Archimedean.QqValue.value",
    validation: "not_checked",
  },
  defines: ["q-value"],
  uses: [
    "def:categorical-action",
    "conj:q-integer-mass-formula",
  ],
});
