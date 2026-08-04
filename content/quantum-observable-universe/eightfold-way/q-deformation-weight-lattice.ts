import { remark } from "../../schema/builders";

/**
 * What q-deformation does and does not do to the weight lattice.
 *
 * Key result from the dialog assessment: the root datum (Cartan matrix,
 * root angles, Weyl group) is an INPUT to the Drinfeld–Jimbo quantization
 * functor, so it is q-independent. What q deforms is the representation
 * category (R-matrices, braiding, quantum dimensions).
 *
 * ANTI-FITTING: This block corrects a specific error (the "two 2s"
 * conflation) and prevents future occurrences. The q-independence is
 * proved in Lean (WeylInvarianceQDeformation.lean).
 */
export default remark({
  label: "rem:q-deformation-weight-lattice",
  title: "The $q$-deformation and the invariance of the root datum",
  md: "q-deformation-weight-lattice.md",
  uses: [
    "prop:a2-from-three-strands",
    "def:hecke-algebra",
  ],
  lean: "qou:QOU.Eightfold.WeylInvarianceQDeformation",
});
