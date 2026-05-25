import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-quantum-volume",
  title: "Algebraic quantum volume $\\mathrm{Vol}_q(K)$",
  lean: {
    ref: "qou:QOU.BraidKnot.AlgebraicQuantumVolume",
    validation: "not_checked",
  },
  // The definition itself is purely algebraic
  // (Z[q^{±1}]-Laurent-polynomial construction). The previous
  // listing of `conj:shared-denominator-cusp-holonomy` in `uses[]`
  // was the wrong propagation direction — the conjecture
  // *interprets* the denominator structure of this definition, not
  // the other way round. See `docs/audits/conjecture-cones.md`
  // "Methodology" footnote (case (2) cleanup).
  uses: [
    "thm:wedderburn-mass-formula",
    "def:q-pochhammer-partial-product",
  ],
});
