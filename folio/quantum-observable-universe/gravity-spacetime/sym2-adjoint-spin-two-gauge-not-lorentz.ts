import { remark } from "../../schema/builders";

/**
 * Graviton candidate 2: V₂ = Sym²(V₁) ⊖ V₀ for the adjoint of the gauge SU(2).
 *
 * The Lean sibling content lives in the QOU library
 * (`QOU.Eightfold.Sym2AdjointSpinTwo`) because it reuses
 * `QOU.Eightfold.Sym2GateParity` and `QOU.SpinLabels`, which a content
 * sibling cannot import together with other siblings. The companion no-go
 * (`spinDouble` cannot represent spin 2) is appended to the sibling of
 * thm:ew-triplet-charge-spin-from-involution, where `spinDouble` lives.
 *
 * KEY CAVEAT, the reason this is a remark and not a proposition about
 * gravity: the spin is for the gauge group Aut⊗(τ) ≅ SU(2), not for a
 * rotation or Lorentz group of spacetime.
 */
export default remark({
  label: "rem:sym2-adjoint-spin-two-gauge-not-lorentz",
  title:
    "The spin-$2$ summand of $\\mathrm{Sym}^2(V_1)$ is gauge spin, not spacetime spin",
  interprets: "prop:spin-labels",
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
  tags: ["spin", "gauge-group", "graviton", "symmetric-square", "scope"],
});
