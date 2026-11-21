import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Statement restated 2026-11-21. The previous proof derived positivity from non-degeneracy of the pairing (\"non-degeneracy forces ⟨f,f⟩ ≠ 0\"), which is false because non-degenerate forms have isotropic vectors; it also derived $S^2 = \\mathrm{id}$ from pivotality, which holds only for involutory Hopf algebras, and asserted ⟨f,f⟩ is a square. $S^2 = \\mathrm{id}$ and positive-definiteness of $h(f,g) = \\int_A \\mu(S(f) \\otimes g)$ are now hypotheses (round-trip audit pass 2, C13). The Lean `frobenius_dagger_positive_definite` (sorry-free since 2026-11-21; earlier it checked only the scalar case on $\\mathbb{C}^2$) works over an $R$-algebra with form and antipode: it proves the adjoint formula $h(xa, b) = h(a, S(x) b)$, uniqueness of the adjoint when $h$ is positive definite, that $S$ fixes the scalars, and $f^\\dagger f > 0$ for $f \\neq 0$. The self-adjointness hypothesis is not needed." },
  ],
  label: "prop:positive-definite-dagger",
  examples: ["ex:positive-dagger-su2"],
  title: "Frobenius dagger is positive-definite",
  lean: { ref: "qou:QOU.frobenius_dagger_positive_definite",
    validation: "not_checked",
  },
  uses: [
    "def:involutive-structure",
    "def:frobenius-pairing",
  ],
  proofs: ["prf:positive-definite-dagger"],
  tags: ["category-theory", "positive-definite", "frobenius"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/positive-definite-dagger-0.svg", blockIndex: 0, hash: "60707ebb7060" },
  ],
});
