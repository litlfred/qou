import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-quantum-volume",
  title: "Algebraic quantum volume $\\mathrm{Vol}_q(K)$",
  lean: {
    ref: "qou:QOU.BraidKnot.AlgebraicQuantumVolume",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** The Lean " +
        "`AlgebraicQuantumVolume` carries `tracedVolume : Fin numCrossings → ℝ` " +
        "and `totalVolume : ℝ` even though the traced volumes themselves lie in " +
        "$\\mathbb{Z}[q^{1/2}, q^{-1/2}]$. The `ℝ` is forced by the ordering " +
        "hypothesis `tracedVolume_pos : ∀ i, 0 < tracedVolume i` — positivity " +
        "for $q > 1$ is an archimedean statement with no generic-`CommRing` " +
        "counterpart. The structure is therefore the *evaluated* volume at a " +
        "real substrate value, not the Laurent-polynomial object; the algebraic " +
        "content named in the docstring lives upstream.",
    },
  ],
  // The definition itself is purely algebraic
  // (Z[q^{±1}]-Laurent-polynomial construction). The previous
  // listing of `conj:shared-denominator-cusp-holonomy` in `uses[]`
  // was the wrong propagation direction — the conjecture
  // *interprets* the denominator structure of this definition, not
  // the other way round. See `docs/audits/conjecture-cones.md`
  // "Methodology" footnote (case (2) cleanup).
});
