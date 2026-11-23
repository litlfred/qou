import { proposition } from "../../schema/builders";

/**
 * The traceless symmetric square of the adjoint of the gauge SU(2) is the
 * single spin-2 summand V₂. The Lean declaration lives in the QOU library
 * (`QOU.Eightfold.Sym2AdjointSpinTwo`) because it reuses
 * `QOU.Eightfold.Sym2GateParity` and `QOU.SpinLabels`. The Clebsch–Gordan
 * decomposition is cited; the Lean checks the bookkeeping on the index model
 * `Sym2GateParity.sym2Indices`, which encodes that decomposition as a
 * definition.
 */
export default proposition({
  label: "prop:sym2-adjoint-traceless-spin-two",
  title:
    "The traceless part of $\\mathrm{Sym}^2(V_1)$ is the spin-$2$ object $V_2$",
  lean: {
    ref: "qou:QOU.Eightfold.Sym2AdjointSpinTwo.adjoint_sym2_traceless_is_spin_two",
  },
  uses: [
    "thm:su2-emergence",
    "prop:spin-labels",
    "ex:spin-labels-su2",
    "thm:ew-triplet-charge-spin-from-involution",
  ],
  cites: ["fulton-harris1991"],
  tags: ["spin", "gauge-group", "symmetric-square", "clebsch-gordan"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Encoding of the label.** The electroweak spin label $2s$ of [the charge–spin theorem](#thm:ew-triplet-charge-spin-from-involution) is defined from a two-valued sector, singlet or doublet, so it takes only the values $0$ and $2$. It is proved that this label never takes the value $4$, and that any map from doubled spin to a two-valued sector gives the same value to two of the spins $0, 1, 2$. The obstruction therefore comes from having two values, not from the particular values chosen. A graded spin label $2s \\in \\mathbb{N}$, in the $2j$ convention of the spin labels, is also defined. Its projection to the sector recovers the sector of every electroweak carrier, and the value $2s = 4$ lies outside the image of the two-valued encoding. The graded label and the label of this proposition share the $2j$ convention; no proved statement connects them." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Scope of the formalisation.** The Lean declaration `QOU.Eightfold.Sym2AdjointSpinTwo.adjoint_sym2_traceless_is_spin_two` does not prove the Clebsch–Gordan decomposition. That decomposition enters as the definition `Sym2GateParity.sym2Indices`, the set of $k \\le 2j$ with $k \\equiv 2j \\pmod 2$. On this index model the Lean proves four facts: | The Lean sibling of that theorem proves that it never takes the value $4$ (`spinDouble_ne_four`), and that any map from doubled spin to a two-valued sector gives the same value to two of the spins $0, 1, 2$ (`bool_sector_not_injective_on_spins`). | The same file defines `GradedSpin`, a label $2s \\in \\mathbb{N}$ in the $2j$ convention of the spin labels. Its projection to the sector recovers the sector of every electroweak carrier (`GradedSpin.toSector_spinDouble`), and the value $2s = 4$ lies outside the image of the two-valued encoding (`GradedSpin.spinTwo_not_ofSector`). `GradedSpin` and the label of this proposition share the $2j$ convention; no Lean statement connects them." },
  ],
});
