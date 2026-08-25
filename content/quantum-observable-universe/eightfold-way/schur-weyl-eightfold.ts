import { proposition } from "../../schema/builders";

/**
 * Schur–Weyl duality: eightfold-way multiplets as H₃(q) partners.
 *
 * The 10/8/1 dimensions (decuplet/octet/singlet) are the SU(N=3)
 * irrep dimensions that appear as Schur–Weyl partners of H₃(q)
 * in V^⊗3. The Hecke block dimensions (1,2,1) are the
 * multiplicities: 3³ = 10·1 + 8·2 + 1·1 = 27.
 *
 * CRITICAL: This derivation requires N=3 (why V is 3-dimensional).
 * In QOU's single-fibre tower, V is 2-dimensional (Descartes
 * condition χ = -6), so N=3 cannot come from one fibre. The N=3
 * must arise from a multi-fibre/groupoid structure — this is the
 * open problem (T3b).
 */
export default proposition({
  label: "prop:schur-weyl-eightfold",
  title: "Eightfold-way multiplets via quantum Schur--Weyl duality",
  // Immediate neighbours only. rem:hecke-algebra-from-braiding was also
  // listed here, but prop:a2-from-three-strands already uses it, so the
  // direct edge was transitively redundant (uses-editorial-hygiene warn).
  uses: [
    "prop:a2-from-three-strands",
  ],
  // Lean backs the OBSTRUCTION half of this block, not the affirmative half.
  // RowCapObstruction proves sorry-free that the alternating channel (1³)
  // vanishes iff N < 3, that the decuplet dimension forces N = 3, and the
  // channel arithmetic at N = 2 (8 = 4+4+0) and N = 3 (27 = 10+16+1).
  // What it does NOT formalise is quantum Schur-Weyl duality itself, nor any
  // construction supplying N = 3 -- that remains the chapter's principal open
  // problem (bean qou-8pl3).
  // The ref now names a DECLARATION, not the module. `weyl_dim_alt_eq_zero_iff`
  // is the row-cap obstruction the module is named for: the alternating
  // channel (1³) has dimension zero iff N < 3.
  lean: { ref: "qou:QOU.Eightfold.RowCapObstruction.weyl_dim_alt_eq_zero_iff" },
});
