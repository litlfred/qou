import { definition } from "../../schema/builders";

export default definition({
  label: "def:z-habiro-ring",
  title: "$z$-Habiro ring $\\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z$",
  lean: { ref: "qou:QOU.HabiroRing.ZHabiroElement",
    validation: "not_checked",
  },
  uses: ["cor:habiro-expansion-atomic"],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "quantum-dilogarithm",
    "brane-tower",
    "regularization",
    "open-construction",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "status",
      body: "**Caveat.** The analytic dilogarithm $\\Phi_q(z)$ itself is **not** an\nelement of $\\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z$ — it is the inverse\nof an element whose image in every cyclotomic quotient is zero (the\nlimit of $P_n$ has zero image at every level). The same phenomenon\nholds in the $q$-Habiro picture: $1/(q;q)_\\infty$ is not in\n$\\widehat{\\mathbb{Z}[q]}$, but partial sums of cyclotomic expansions\nof quantum invariants are.\n\nWhat is conjectured to live in $\\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z$\nis the **brane-tower element** — a single element collecting the\nfinite-rank brane-tower partial sums $\\Phi_q^{(N)}(\\beta) = \\sum_{i=1}^{N} \\Phi_q(z_i)$\nacross all $N$ as a Cauchy sequence in the $z$-cyclotomic topology.\nSee [brane tower in $z$-Habiro](#conj:brane-tower-z-habiro) for the\nprecise statement.",
    },
  ],
});
