---
# qou-ko4g
title: 'Provable today: the SU(2) to SU(3) obstruction set, no new Mathlib needed'
status: completed
type: task
priority: normal
created_at: 2026-08-24T14:13:36Z
updated_at: 2026-08-24T14:37:43Z
---

Five statements behind `qou-8p1g` ("tetraplectic reaches SU(2), not SU(3)")
that need **no** Mathlib infrastructure. Each turns a prose judgement into a
checkable invariant.

- [x] **Reality obstruction.** A real matrix commutes with entrywise
  conjugation, so the rep it generates is self-conjugate. Under the *principal*
  embedding `SU(2) ↪ SU(3)` the **3** restricts to the adjoint of `su(2)`,
  which is real — hence `3 ≅ 3̄`. Colour needs `3 ≇ 3̄`. This is the decisive
  one: `qou-8p1g` argues "three Reeb fields is the *adjoint*, colour needs the
  *fundamental*" as a judgement; reality makes it mechanical.
- [x] **SU(2) is not normal in SU(3)**, by concrete witness:
  `h = diag(i, −i, 1)` in the top-left block, `g` the 3-cycle permutation
  matrix (det +1, orthogonal); `(g h g⁻¹)₂₂ = −i ≠ 1`, so it leaves the block.
  Consequence: there is **no** short exact sequence `1 → SU(2) → SU(3) → Q → 1`,
  so "lift SU(2) to SU(3)" cannot be posed as an extension problem at all.
- [x] **The order-120 trap.** `|Aut(Bring)| = |S₅| = 120 = |2I|` (binary
  icosahedral), but `Z(2I) = ℤ₂` and `Z(S₅) = 1`, so `2I ≇ S₅`. Any argument
  sliding from "Bring has order-120 symmetry" to "so `2I ⊂ SU(2)`" is invalid;
  the valid route is `A₅ ⊂ S₅`, which lifts to `2I`. Lean: the centre criterion
  plus `Z(S₅) = ⊥`; `2I` is not in Mathlib so its centre is narrative input,
  matching the `OctonionInvariantObstruction` house pattern.
- [x] **G₂ dimension arithmetic.** `dim SU(3) + dim SO(4) = 8 + 6 = 14 = dim G₂`.
  Trivial to prove, worth pinning: it is the statement that G₂'s two homogeneous
  spaces `G₂/SU(3) = S⁶` and `G₂/SO(4)` (quaternionic Wolf space, dim 8) are
  complementary. **The corpus has `S⁶ = G₂/SU(3)` but no mention of
  `G₂/SO(4)` anywhere** — so the tetraplectic SU(2) and colour SU(3) have never
  been put in the same frame, and G₂ is that frame.
- [x] **Abstract exact-triangle vanishing lemma.** If the correction term in a
  three-term exact sequence vanishes, the connecting map is an isomorphism.
  Pure homological algebra (`ShortComplex.Exact`); this is Seidel's bookkeeping
  **without** the Floer theory, and it is where filtration / jet-order / Gröbner
  degree bookkeeping would hang.

Sibling beans: `qou-fngs` (fix vacuous), `qou-8p1g` (the verdict these support).

## Summary of Changes — 2026-08-24

`QOU/StandardModel/ColourObstruction.lean`, seven results, all
`#print axioms`-clean (`propext` / `Classical.choice` / `Quot.sound` only, no
`sorry`, no custom axiom).

| result | what it settles |
|---|---|
| `real_rep_selfConjugate` | a real matrix commutes with conjugation ⇒ `3 ≅ 3̄`. The mechanical form of `qou-8p1g`'s "wrong 3": the failure is **reality**, not dimension. |
| `cyc3_orthogonal` | the conjugator is genuinely in `SU(3)` (real orthogonal, `det +1`) |
| `conj_leaves_block` | `(g h gᵀ)₂₂ = −i` for `h = diag(i,−i,1)` |
| `blockEmbed_not_normal` | so `SU(2)` is **not normal** in `SU(3)` — hence no `1 → SU(2) → SU(3) → Q → 1`, and the "lift" is not an extension problem |
| `center_perm5_eq_bot` | **`Z(S₅) = 1`, derived** |
| `not_mulEquiv_perm5_of_center` | no group with non-trivial centre is `≃* S₅` ⇒ `2I ≇ S₅` |
| `g2_dim_split` | `8 + 6 = 14`: `G₂/SU(3) = S⁶` and `G₂/SO(4)` are complementary |
| `twist_surj_of_correction_trivial` | vanishing correction ⇒ twist onto — Seidel's bookkeeping without Floer |

### `Z(S₅) = ⊥` was derived, not cited

Mathlib does not ship it — checked by name and by `exact?`, not assumed. I first
recorded it as narrative input and was told to spend the time; it took about
twenty lines. Standard argument: `σ` central with `σ a = b ≠ a`, pick
`c ∉ {a, b}` (`Fin 5` has room, via a `Finset` complement-cardinality step),
commute `σ` past the transposition `(b c)`, evaluate at `a`, get `c = b`.

This upgraded obstruction 3 from a **criterion with two narrative inputs** to a
theorem with **one**: `Z(2I) ≠ 1` still has to be asserted in prose, because the
binary icosahedral group is not in Mathlib and cannot be computed here.

### What is deliberately not claimed

- `real_rep_selfConjugate` is about a *real matrix*. That the principal
  `SU(2) ↪ SU(3)` lands in real matrices is standard representation theory,
  stated in the docstring, not formalised — Mathlib has no Lie-group structure
  theory to hang it on (`qou-pan0`).
- `InBlock` is a concrete predicate on `3 × 3` matrices, not
  `Matrix.specialUnitaryGroup`. The witness computation is what carries the
  content; wrapping it in the group type would add plumbing, not certainty.
- `twist_surj_of_correction_trivial` is homological algebra. It is **not** a
  Floer-theoretic statement and must not be cited as one (`qou-jbfx`).

    lean-direct-cone     exit 0
    run-validate         Valid — 26 issues, 0 errors
    mirror drift  @35    exit 0
    duplicate decls @57  exit 0
