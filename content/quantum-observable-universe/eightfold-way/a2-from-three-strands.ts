import { proposition } from "../../schema/builders";

/**
 * The A₂ root system emerges from the Hecke relations of H₃(q).
 *
 * This is the foundational result of the eightfold-way chapter:
 * the braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ encodes the A₂ Cartan matrix,
 * and the six roots at 120° angles emerge from the Weyl group S₃ acting
 * on the weight space.
 *
 * DERIVATION SOURCE: Purely from QOU's categorical axioms. The A₂
 * structure is a theorem of B₃ representation theory, not an imported
 * physics result.
 */
export default proposition({
  label: "prop:a2-from-three-strands",
  title: "The $A_2$ root system from the Hecke algebra $H_3(q)$",
  md: "a2-from-three-strands.md",
  uses: [
    "def:braid-group",
    "def:hecke-algebra",
  ],
  lean: "qou:QOU.Eightfold.A2FromThreeStrands",
});
