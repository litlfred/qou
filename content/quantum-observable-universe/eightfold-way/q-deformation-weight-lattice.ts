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
 * conflation) and prevents future occurrences. The q-independence of the
 * root datum under Drinfeld–Jimbo is STANDARD (Lusztig/Kashiwara), cited
 * and not formalised here; WeylInvarianceQDeformation.lean machine-checks
 * only the arithmetic of the separation.
 */
export default remark({
  label: "rem:q-deformation-weight-lattice",
  title: "The $q$-deformation and the invariance of the root datum",
  interprets: "prop:a2-from-three-strands",
  uses: [
    "prop:a2-from-three-strands",
    "rem:hecke-algebra-from-braiding",
  ],
  // The ref now names a DECLARATION, not the module.
  // `cartan_fixed_while_qSerre_moves` is the conjunction the file's own
  // docstring calls "the file's actual claim" — the Cartan datum constant in
  // q, the Serre coefficient demonstrably not (witnessed at q = 2) — which is
  // exactly this block's "two 2s" separation. It does NOT formalise
  // q-independence of the root datum under Drinfeld–Jimbo; that is standard
  // (Lusztig/Kashiwara) and cited, per the refined-framing note below.
  lean: {
    ref: "qou:QOU.Eightfold.WeylInvarianceQDeformation.cartan_fixed_while_qSerre_moves",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-08",
      body:
        "The machine-checked list previously included " +
        "`cartanMatrix_A2_q_independent`, cited as proving that the Cartan " +
        "datum is q-independent. That declaration asserted only " +
        "`cartanMatrix_A2 = cartanMatrix_A2 := rfl`, with its `R, q₁, q₂` " +
        "binders unused, so it said nothing about q; and its file did not " +
        "compile (two `No goals to be solved` errors). Both were repaired " +
        "on PR #4727 — the file is now `lean`-direct exit 0, sorry-free, " +
        "and the contentful half of the separation (`qSerre_not_constant`, " +
        "witnessed at q = 2) was added. The mathematics is unchanged: " +
        "q-independence of the root datum is a standard Drinfeld–Jimbo " +
        "result, correctly cited, and only the evidence line was wrong. " +
        "See docs/audits/2026-08-08-weyl-invariance-file-repair.md.",
      see: "docs/audits/2026-08-08-weyl-invariance-file-repair.md",
    },
  ],
});
