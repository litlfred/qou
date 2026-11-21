import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Statement restated 2026-11-21. The previous proof derived positivity from non-degeneracy of the pairing (\"non-degeneracy forces ⟨f,f⟩ ≠ 0\"), which is false because non-degenerate forms have isotropic vectors; it also derived $S^2 = \\mathrm{id}$ from pivotality, which holds only for involutory Hopf algebras, and asserted ⟨f,f⟩ is a square. $S^2 = \\mathrm{id}$ and positive-definiteness of $h(f,g) = \\int_A \\mu(S(f) \\otimes g)$ are now hypotheses (round-trip audit pass 2, C13). Restated again 2026-11-21 after QA: the dagger is now stated on morphisms $\\mathbf{1} \\to A$ and on left multiplications $L_x$, not on arbitrary $f \\colon \\mathbf{1} \\to X$; the pairing self-adjointness hypothesis on $S$ was dropped because nothing uses it. The Lean `frobenius_dagger_positive_definite` (sorry-free) proves items 1 to 3: the adjoint of $L_x$ is $L_{S(x)}$ and is unique, involution (from $S^2 = \\mathrm{id}$), contravariance (from $S(xy) = S(y)S(x)$), and that the dagger is $S$ and the identity on scalars. Item 4 is `frobeniusDagger_pos`, which is the positivity hypothesis read through $f^\\dagger f = h(f,f)$, and the .md says so." },
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
