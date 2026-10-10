# I1 probe author-queue (2026-05-19)

Items where the probe could not be authored solo and need a
specific call from the author.  Each entry includes: the
`.ts` file path, the corollary/proposition claim, the specific
ambiguity, and 2–3 options for resolution.

## Deferred items

### `cor:descartes-braid-structure`

- **File**: `folio/quantum-observable-universe/descartes-universe/descartes-braid-structure.ts`
- **Claim**: image of ρ_3 : B_3 → Aut(V^⊗3) in SU(2) is the binary dihedral group `Dic_3` of order 12.
- **Ambiguity**: at generic `q` (including `q_0 ≈ 1.110`), the braid image is typically infinite. A finite Dic_3 image requires `q` at a specific root of unity. The `def:descartes-condition` block doesn't pin down which.
- **Options**:
  1. **Specify q-value**: clarify the Descartes condition's q-value in the .md (e.g., `q = e^(πi/6)` for Dic_3 to have order 12).
  2. **Re-frame claim**: corollary should say "subject to the Descartes specialisation `q = ζ_{12}`" or similar explicit hypothesis.
  3. **Defer to existing computational evidence**: if a Rust/SnapPy probe has already verified order-12 elsewhere, point me at the witness and I'll wire it.

