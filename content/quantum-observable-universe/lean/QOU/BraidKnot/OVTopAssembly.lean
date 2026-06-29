import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.JucysMurphy
import QOU.BraidKnot.WedderburnSn
import QOU.BraidKnot.RegularRepBlockTrace
import QOU.BraidKnot.RegularRepTrace

/-!
# QOU.BraidKnot.OVTopAssembly — the TOP / capstone of the Okounkov–Vershik tower

This file is the **keystone of the keystone**: it assembles bricks 2 / 3 / 5 together with the
Wedderburn–Artin decomposition of `R[S_n]` into a single
`RegularRepBlockTrace.SnWedderburnSpectralData R n`, and thereby discharges the **side-2 hypothesis**
of Identity (B).  The §3b-cond conditional theorem
`RegularRepBlockTrace.identityB_conditional` — *if* a Wedderburn / Jucys–Murphy block spectral
decomposition exists, *then* `Σ_λ ω_λ·dim(λ)² = n!·binom(n,2)` — becomes, via this assembly,
the **unconditional** general-`n` Identity (B) (modulo the bricks' own honest stubs).

## What this capstone does

`sn_spectralData_exists n : Nonempty (SnWedderburnSpectralData R n)` constructs the structure,
**wiring each field to the brick that supplies it**:

| field | source brick | status here |
|-------|--------------|-------------|
| `Idx` | brick 3 `SpechtClassification.PartitionIndex n` = `{μ : YoungDiagram // μ.card = n}` | **sorry-free** |
| `fintypeIdx` | brick 3 `instFintypePartitionIndex` | **sorry-free** |
| `d i` | brick 1/2 `numSYT i.diagram` (`dim Sᵘ = #SYT`) | **sorry-free** (the *definition*; `rank` carries the dim-identity) |
| `ω i` | brick 5 `((contentSqSum i.diagram : ℤ) : R)` (the JM eigenvalue `Σ_{c∈λ} c²`) | **sorry-free** (the *definition*; `decomp` carries the action-identity) |
| `p i`, `proj i` | the `λ`-isotypic projections (Wedderburn `∏ Matrix` blocks, brick `WedderburnSn`) re-indexed by partition (brick 3) | `sorry` — *constructed* projection family is the OV identification not yet exposed as a `PartitionIndex`-indexed datum |
| `isProj i` | `LinearMap.IsProj` of the isotypic projection | `sorry` (`-- Ref:` `WedderburnSn.sn_wedderburnArtin_algClosed`) |
| `rank i` | brick 2 `specht_finrank_eq_numSYT` + `WedderburnSn.sn_block_finrank_sq` (`dim block = dim(λ)²`) | `sorry` (`-- Ref:` `Specht.specht_finrank_eq_numSYT`) |
| `decomp` | brick 5 `centralC2_acts_by_contentSqSum` + `centralC2_eq_sum_jucysMurphy_sq` (`C₂` acts by `ω_λ` on `Sᵘ`) | `sorry` (`-- Ref:` `JucysMurphy.centralC2_acts_by_contentSqSum`) |
| `complete` | `WedderburnSn.sn_wedderburnArtin_algClosed` `Σ proj = id` + brick 3 `card_irreducibles_eq_card_partitions` | `sorry` (`-- Ref:` `WedderburnSn.sn_wedderburnArtin_algClosed`) |

The genuinely hard, irreducibly-OV content (which Mathlib does not provide at the pinned `f897ebcf`)
is exactly the explicit isotypic-projection family **re-indexed by partitions** — i.e. matching the
abstract Wedderburn block count `N` of `WedderburnSn.sn_wedderburnArtin_algClosed` against
`SpechtClassification.PartitionIndex n` and identifying each block's size with `numSYT` and its `C₂`
eigenvalue with `contentSqSum`.  Every such field is honestly `sorry`-stubbed with a `-- Ref:` to the
precise brick theorem that discharges it.  The *value* of this capstone is that **the types line up
end-to-end**: each brick output has exactly the shape the keystone field demands, and the wiring map
above documents which stub feeds which field.

`identityB_general n` is the payoff: it feeds `(sn_spectralData_exists n).some` into
`RegularRepBlockTrace.identityB_conditional`, yielding the Identity-(B) trace equation
`Σ_i ω_i · dim(λ_i)² = n!·binom(n,2)` for **all `n`** — modulo the tower's stubs.

## Base ring (§7c)

`variable {R : Type} [Field R] [CharZero R]`.  This is *algebraic*: `Field` is what the structure and
the Wedderburn decomposition need; `CharZero` is what the brick-3 classification needs.  No `ℝ`, no
`Real.*`, no ordering on `R`, no archimedean tactics — the eigenvalues / contents are integers cast
into the field.

This module carries honest `sorry` targets, so — like bricks 1–5 — it is intentionally **not** wired
into the `QOU.BraidKnot` umbrella (that would taint the umbrella's sorry-free CI surface).  Verified
standalone via `lean`-direct against the pinned v4.24.0 oleans.

## References
- [vershik-kerov1977] Vershik–Okounkov, "A new approach to the representation theory of the symmetric
  groups II" (JM elements; the GZ algebra; eigenvalues = cell contents).
- [sagan2001] Sagan, *The Symmetric Group*, §2.3–2.5 (Specht modules, the standard basis, the
  classification of irreducibles).
- [james1984representation] James, *The Representation Theory of the Symmetric Groups* (Specht
  modules; pairwise non-isomorphism; irreducibility in char 0).
-/

open scoped BigOperators

-- `CharZero R` is part of the capstone's signature contract: it is the typeclass the brick-3
-- classification (`SpechtClassification`, which underwrites the `p` / `proj` / `complete` fields)
-- genuinely requires.  Because those fields are currently `sorry`-stubbed, Lean's
-- unused-section-variable linter flags `CharZero` as unused in `sn_spectralData_exists`; we keep it
-- (it documents the real requirement and is needed once the stubs are discharged) and disable the
-- linter for the file rather than drop the typeclass.
set_option linter.unusedSectionVars false

namespace QOU.BraidKnot.OVTopAssembly

open QOU.BraidKnot

variable {R : Type} [Field R] [CharZero R]

/-! ## The capstone construction -/

/-- **TOP of the OV tower — the Wedderburn / Jucys–Murphy block spectral decomposition exists.**

We construct the keystone's `SnWedderburnSpectralData R n` by wiring each field to its brick:

* `Idx := SpechtClassification.PartitionIndex n` (brick 3) — sorry-free, with its `Fintype`.
* `d i := numSYT i.diagram` (bricks 1/2, `dim Sᵘ = #SYT`) — sorry-free *definition*.
* `ω i := ((contentSqSum i.diagram : ℤ) : R)` (brick 5, the JM content-square eigenvalue) —
  sorry-free *definition*.
* the projection data `p` / `proj` / `isProj` / `rank` / `decomp` / `complete` are the explicit
  `λ`-isotypic decomposition of `mulLeft C₂`.  Each is honestly `sorry`-stubbed with a `-- Ref:` to
  the brick theorem that discharges it; the **irreducible OV content** is the re-indexing of the
  abstract Wedderburn blocks (`WedderburnSn.sn_wedderburnArtin_algClosed`) by partitions
  (`SpechtClassification.card_irreducibles_eq_card_partitions`), which Mathlib does not provide at
  this pin. -/
noncomputable def snSpectralData (n : ℕ) :
    RegularRepBlockTrace.SnWedderburnSpectralData R n where
  -- sorry-free: the index type is the partitions of `n` (brick 3).
  Idx := SpechtClassification.PartitionIndex n
  -- sorry-free: brick 3 supplies the `Fintype` instance.
  fintypeIdx := SpechtClassification.instFintypePartitionIndex n
  -- sorry-free: `d i = dim Sᵘⁱ = #SYT(λ_i)` (bricks 1/2).  The dim-identity is carried by `rank`.
  d := fun i => numSYT i.diagram
  -- sorry-free: `ω i = Σ_{c∈λ_i} c(c)²`, the JM eigenvalue (brick 5), cast `ℤ → R`.  The
  -- action-identity is carried by `decomp`.
  ω := fun i => ((JucysMurphy.contentSqSum i.diagram : ℤ) : R)
  -- The `λ_i`-isotypic block of the regular representation.  This *is* the OV identification
  -- (which Wedderburn block of `R[S_n]` is the partition `λ_i`) — not exposed by the bricks as a
  -- `PartitionIndex`-indexed datum, hence stubbed.
  -- Ref: [sagan2001] via SpechtClassification.card_irreducibles_eq_card_partitions
  --   (#{Wedderburn blocks} = #{partitions}) + WedderburnSn.sn_wedderburnArtin_algClosed
  --   (the `∏ Matrix` block structure whose blocks are these isotypic components).
  p := fun _ => sorry
  -- The projection onto the `λ_i`-isotypic block.  Same OV identification as `p`.
  -- Ref: [sagan2001] via SpechtClassification.card_irreducibles_eq_card_partitions
  --   + WedderburnSn.sn_wedderburnArtin_algClosed (the block idempotents of the matrix decomposition).
  proj := fun _ => sorry
  -- Each `proj i` is the projection onto `p i`.
  -- Ref: [james1984representation] via WedderburnSn.sn_wedderburnArtin_algClosed
  --   (the central block idempotents of `∏ Matrix(𝔫ᵢ)` are projections onto the isotypic blocks).
  isProj := fun _ => sorry
  -- `dim_R (p i) = dim(λ_i)² = numSYT(λ_i)²`.  Feeds: brick 2 `specht_finrank_eq_numSYT`
  -- (`dim Sᵘ = #SYT`) and `WedderburnSn.sn_block_finrank_sq` (`dim block = 𝔫ᵢ²`, with `𝔫ᵢ` the
  -- irreducible dimension); identifying `𝔫ᵢ = numSYT(λ_i)` is the OV labelling.
  -- Ref: [sagan2001] via Specht.specht_finrank_eq_numSYT + WedderburnSn.sn_block_finrank_sq.
  rank := fun _ => sorry
  -- **Block spectral decomposition** `mulLeft C₂ = Σ_i ω_i · proj_i`.  This is the punchline of
  -- brick 5: `C₂ = Σ_k X_k²` acts on the `λ_i`-block by the scalar `contentSqSum λ_i`, and the
  -- keystone's `C₂` (`RegularRepTrace.centralC2`) is brick 5's `centralC2` by `rfl`
  -- (`JucysMurphy.centralC2_eq_sum_jucysMurphy_sq`).
  -- Ref: [vershik-kerov1977] via JucysMurphy.centralC2_acts_by_contentSqSum
  --   (C₂ acts by Σ_{c∈λ} c² on Sᵘ) + JucysMurphy.centralC2_eq_sum_jucysMurphy_sq
  --   (brick-5 C₂ = keystone C₂).
  decomp := sorry
  -- The blocks exhaust `R[S_n]`: `Σ_i proj_i = id`.  Completeness of the Wedderburn decomposition.
  -- Ref: [sagan2001] via WedderburnSn.sn_wedderburnArtin_algClosed
  --   (`R[S_n] ≃ ∏ᵢ Matrix(𝔫ᵢ)`, so the block idempotents sum to `1`) + brick 3
  --   card_irreducibles_eq_card_partitions (the blocks are indexed by all partitions).
  complete := sorry

/-- **The Wedderburn / JM block spectral decomposition of `R[S_n]` is inhabited** — the capstone
existence statement that discharges the side-2 hypothesis of Identity (B).  Constructed by
`snSpectralData`, whose `Idx` / `d` / `ω` fields are sorry-free and whose projection data is wired
to the bricks (see the per-field `-- Ref:` map in `snSpectralData`). -/
theorem sn_spectralData_exists (n : ℕ) :
    Nonempty (RegularRepBlockTrace.SnWedderburnSpectralData R n) :=
  ⟨snSpectralData n⟩

/-! ## Identity (B), general `n` — the payoff -/

/-- **Identity (B), general `n` (modulo the tower's stubs).**  Feeding the assembled spectral datum
`(sn_spectralData_exists n).some` into the keystone's §3b-cond conditional theorem
`RegularRepBlockTrace.identityB_conditional` yields the Identity-(B) trace equation

`Σ_i ω_i · dim(λ_i)² = n! · binom(n,2)`

for **all `n`** — where `ω_i` is the Jucys–Murphy content-square eigenvalue and `dim(λ_i)` the SYT
dimension of block `i`.  This is the unconditional general-`n` Identity (B): the only residual inputs
are the bricks' own honest `sorry`s (the isotypic-projection identification, the OV eigenvalue
theorem, the standard-basis dimension theorem), all wired in `snSpectralData`.

(The statement is stated exactly as the keystone's `identityB_conditional` concludes, against the
assembled `W := (sn_spectralData_exists n).some`.) -/
theorem identityB_general (n : ℕ) :
    ∑ i : (sn_spectralData_exists (R := R) n).some.Idx,
        (sn_spectralData_exists (R := R) n).some.ω i
          * ((sn_spectralData_exists (R := R) n).some.d i : R) ^ 2
      = (n.factorial : R) * (n.choose 2 : R) :=
  RegularRepBlockTrace.identityB_conditional (sn_spectralData_exists (R := R) n).some

end QOU.BraidKnot.OVTopAssembly
