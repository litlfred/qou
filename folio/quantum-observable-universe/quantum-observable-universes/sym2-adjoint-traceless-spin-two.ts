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
});
