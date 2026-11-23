import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jones-mobius-diagonal",
  title: "Proof of jones mobius diagonal",
  uses: ["lem:jones-mobius-diagonal"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): whose $N \\to \\infty$ logarithmic\ngrowth rate is the hyperbolic volume\n([Kashaev volume–density](#rem:kashaev-volume-density))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Surreal reading.** Under the surreal lift\n([Möbius renormalization](#rem:mobius-surreal-renormalization)) the regularized\ntwo-point $I_1$ and the contact term $I_2$ are both infinite surreals of\n$\\mathrm{ord}_\\omega = +1$ with the *same* leading coefficient; the shared\n$\\omega^{+1}$ divergence **is** this contact / self-energy, and $E_{\\mathrm{cat}}\n= \\mathrm{std}(I_1 - I_2)$ is the appreciable remainder. The lemma\nidentifies that shared divergence with $J_K(q)$." },
  ],
});
