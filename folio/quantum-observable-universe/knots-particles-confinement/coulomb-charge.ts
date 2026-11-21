import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-29",
      body: "**Correction (2026-08-29, bean `qou-toul`).** This block previously assigned $\\tfrac{1}{2}(n_+ + n_-)$ to the symmetric channel and $Q = \\tfrac{1}{2}(n_+ - n_-)$ to the antisymmetric one — the two multiplicities exchanged. That decomposition does not reconstruct $\\mathfrak{E}_{\\mathrm{cross}}$: it exceeds it by $2 n_- q^{-1}$, agreeing only on positive braids. It also stated the $\\tanh(\\ln q)$ ratio unconditionally, where it holds only at $n_- = 0$, and read the trichotomy $Q \\lessgtr 0$ as attractive-versus-repulsive Coulomb, which the corrected assignment does not support. [The channel decomposition](#prop:crossing-energy-decomposition) carried the correct multiplicities throughout; this block and its Lean sibling were the outliers.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): By [the channel decomposition](#prop:crossing-energy-decomposition), the crossing energy" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [an open problem](#conj:sm-hypercharge-invariant)" },
  ],
  label: "def:coulomb-charge",
  title: "Coulomb charge of a knot composite",
  tags: ["coulomb", "charge", "crossing", "asymmetry", "skein"],
  lean: { ref: "qou:QOU.Braiding.CoulombCharge",
    validation: "not_checked",
  },
  uses: [
    "def:crossing-energy",
  ],
});
