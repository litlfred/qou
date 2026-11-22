import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:binding-manybody-eq-jet-filtration",
  title:
    "Binding many-body series equals the jet-order filtration: $B(K)=\\sum_n m_e\\,a_D^{(n)}$",
  lean: {
    ref: "qou:QOU.Mass.BindingManyBodyJetFiltration",
    validation: "validated",
  },
  uses: [
    "conj:bond-order-eq-jet-degree",
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
    "prop:magic-A-binding-formula",
  ],
  tags: [
    "binding",
    "many-body",
    "jet-order-filtration",
    "seiberg-witten",
    "q-difference",
    "step-9b",
    "open-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): That finiteness is unattainable in the scalar form. The $q$-Borel-normalized\ncarrier is the rank-$2$ module $\\mathcal{K}$ of\n[The q-difference kernel R is the jet-prolongation symbol, carried by the binding q-lift module](#conj:qdifference-kernel-prolongation-symbol),\nwhich is **irreducible** — its Newton slope $\\tfrac12$ is not an integer, while\nevery rank-1 $q$-difference module has integer slope — so no scalar\n$R(q,x)\\in K(x)$ acts on it at all, at any depth. The kernel that closes this\nconjecture must be a $2\\times2$ **matrix**, and a rank-$2$ recursion needs two\nbase cases, so the $n=3$ term is required as an independent input rather than\nproduced by the recursion. This is consistent with, and independent of, the\none-free-parameter count recorded above." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): [`binding_n3_forcing_probe.py`](../../../computations/binding_n3_forcing_probe.py);\n\ngeometry-dependent: at the canonical *derived* $r_0 = \\hbar c/m_\\pi$ of\n`coulomb_energy.py` the correction\n\n$(q-1)^2\\Phi_3$ deviation, formalized in\n[`QOU.Mass.BindingEigenfunctionTwoTier`](../lean/QOU/Mass/BindingEigenfunctionTwoTier.lean))\n\n$B_2 \\neq 0$ the map $\\{r_k\\} \\leftrightarrow \\{B_n\\}$ is a **bijection**\n([`QOU.Mass.BindingScalarKernelParityExclusion.kernel_coeff_existsUnique`](../lean/QOU/Mass/BindingScalarKernelParityExclusion.lean))." },
  ],
});
