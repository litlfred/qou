import { proposition } from "../../schema/builders";

/**
 * Proposition: Categorical Recovery of Möbius Energy.
 *
 * Shows that the classical Möbius energy E(γ) is recovered as the
 * leading-order term of the categorical mass m(γ) in the q → 1 limit.
 */
export default proposition({
  label: "prop:categorical-mobius-energy",
  title: "Categorical recovery of Möbius energy",
  tags: [
    "knot-theory",
    "mobius-energy",
    "categorical-action",
    "frobenius-hopf",
    "su2",
  ],
  uses: [],
  lean: {
    decl: "QOU.PathIntegrals.CategoricalMobiusEnergy",
    file: "QOU/PathIntegrals/MobiusEnergy.lean",
    validation: "not_checked",
  },
  status: "not_started",
  hasProof: true,
});
