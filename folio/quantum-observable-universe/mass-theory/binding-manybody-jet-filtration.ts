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
    "lem:bond-order-eq-jet-degree",
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): [`binding_n3_forcing_probe.py`](../../../computations/binding_n3_forcing_probe.py);\n\ngeometry-dependent: at the canonical *derived* $r_0 = \\hbar c/m_\\pi$ of\n`coulomb_energy.py` the correction\n\n$(q-1)^2\\Phi_3$ deviation, formalized in\n[`QOU.Mass.BindingEigenfunctionTwoTier`](../lean/QOU/Mass/BindingEigenfunctionTwoTier.lean))\n\n$B_2 \\neq 0$ the map $\\{r_k\\} \\leftrightarrow \\{B_n\\}$ is a **bijection**\n([`QOU.Mass.BindingScalarKernelParityExclusion.kernel_coeff_existsUnique`](../lean/QOU/Mass/BindingScalarKernelParityExclusion.lean))." },
  ],
});
