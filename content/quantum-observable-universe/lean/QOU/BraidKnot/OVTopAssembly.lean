import QOU.BraidKnot.Specht
import QOU.BraidKnot.SpechtClassification
import QOU.BraidKnot.JucysMurphyOV
import QOU.BraidKnot.WedderburnSn
import QOU.BraidKnot.RegularRepBlockTrace
import QOU.BraidKnot.RegularRepTrace
import QOU.BraidKnot.SpechtFinrankWired
import QOU.BraidKnot.SnWedderburnPartitionBridge

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
**wiring each field to the brick that supplies it**.  The construction is de-abstracted: the six
projection-data fields no longer carry bare opaque `sorry`s — each is wired to the **named brick
theorem** it cites, via the glue lemma `snBlocks` (the OV-reindexing residual, itself now discharged
by `SnWedderburnPartitionBridge.snBridge` — no direct `sorry`) and per-field consumption of the
proved/stubbed bricks.

| field | source brick | status here |
|-------|--------------|-------------|
| `Idx` | brick 3 `SpechtClassification.PartitionIndex n` = `{μ : YoungDiagram // μ.card = n}` | **sorry-free** |
| `fintypeIdx` | brick 3 `instFintypePartitionIndex` | **sorry-free** |
| `d i` | brick 1/2 `numSYT i.diagram` (`dim Sᵘ = #SYT`) | **sorry-free** (the *definition*; `rank` carries the dim-identity) |
| `ω i` | brick 5 `((contentSqSum i.diagram : ℤ) : R)` (the JM eigenvalue `Σ_{c∈λ} c²`) | **sorry-free** (the *definition*; `decomp` carries the action-identity) |
| `p i`, `proj i` | the `λ`-isotypic projections (Wedderburn `∏ Matrix` blocks, brick `WedderburnSn`) re-indexed by partition (brick 3), via `snBlocks` | `sorryAx`-via-`snBlocks` → `snBridge` (Ref `SnWedderburnPartitionBridge.sn_rational_specht_split`) |
| `isProj i` | `LinearMap.IsProj` of the isotypic projection, via `snBlocks` | `sorryAx`-via-`snBlocks` → `snBridge` (Ref `SnWedderburnPartitionBridge.sn_rational_specht_split`) |
| `rank i` | brick 4 `SpechtFinrankWired.specht_finrank_eq_numSYT_wired` (`dim Sᵘ = #SYT`, sourced from the **proved** independence core `SpechtTriangularCore.standardPolytabloid_triangular'`) + `WedderburnSn.sn_block_finrank_sq` (`dim block = dim(λ)²`) | **no `sorryAx` from brick 4** — `specht_finrank_eq_numSYT_wired` is axiom-clean (`[propext, Classical.choice, Quot.sound]`, verified 2026-08-08); the earlier "sorry-path = spanning/straightening" attribution here was wrong. Residual `sorryAx` on this row is `snBlocks` block-size only |
| `decomp` | brick 5 `centralC2_acts_by_contentSqSum` + `centralC2_eq_sum_jucysMurphy_sq` (`C₂` acts by `ω_λ` on `Sᵘ`) | `sorryAx`-via-`JucysMurphy.centralC2_acts_by_contentSqSum`; the rfl bridge `centralC2_eq_sum_jucysMurphy_sq` is consumed sorry-free |
| `complete` | `WedderburnSn.sn_wedderburnArtin_algClosed` `Σ proj = id` + brick 3 `card_irreducibles_eq_card_partitions` | `sorryAx`-via-`snBlocks` → `snBridge` (Ref `SnWedderburnPartitionBridge.sn_rational_specht_split`) |

The genuinely hard, irreducibly-OV content (which Mathlib does not provide at the pinned `f897ebcf`)
is exactly the explicit isotypic-projection family **re-indexed by partitions** — i.e. the rational,
OV-labelled Wedderburn split of `R[S_n]` over a char-0 field, matching the blocks against
`SpechtClassification.PartitionIndex n` with each block's `R`-dimension the squared SYT count.  That
residual is **de-abstracted in `SnWedderburnPartitionBridge`**: the passage from a `∏ Matrix` algebra
split to the projection bundle (`snBlocks`-shaped `snBridge`) is sorry-free linear algebra there, and
the irreducible gap is isolated in that file's **single** named core
`SnWedderburnPartitionBridge.sn_rational_specht_split` (the `ℚ`-rationality + partition labelling).
So `snBlocks` here carries no `sorry` of its own.  Two further fields then *consume their named bricks
load-bearingly* on top of `snBlocks`:
`rank` rewrites with the brick-4 **wired** finrank
`SpechtFinrankWired.specht_finrank_eq_numSYT_wired`, and `decomp` aligns the central element with
the rfl-proved `JucysMurphy.centralC2_eq_sum_jucysMurphy_sq` and cites the eigenvalue punchline
`JucysMurphy.centralC2_acts_by_contentSqSum`.

### `rank` re-route (brick-4 finrank → proved independence)

The `rank` field formerly rewrote with the **opaque brick-2 stub**
`Specht.specht_finrank_eq_numSYT` (a bare `sorry : finrank Sᵘ = numSYT μ`).  It now rewrites with
`SpechtFinrankWired.specht_finrank_eq_numSYT_wired`, which rebuilds the same `dim Sᵘ = #SYT` identity
from the standard polytabloid basis but **sources linear independence from the proved triangular
core** `SpechtTriangularCore.standardPolytabloid_triangular'` (sorry-free — its dominance core
`SpechtDominanceCore.dominance_relation_exists` is discharged on the pinned oleans) instead of the
independence stub.  Consequently the `rank` sorry-path no longer contains the independence stub
`SpechtStandardBasis.standardPolytabloid_triangular` **nor** the opaque brick-2 finrank stub; its
**only** remaining `sorry` is the spanning / straightening stub
`SpechtStandardBasis.standardPolytabloid_straightening` (via `standardPolytabloid_span`).  The basis-
building + `finrank` machinery itself is sorry-free (demonstrated: a `Basis.mk` whose independence and
spanning are *both* supplied as hypotheses depends only on `[propext, Classical.choice, Quot.sound]`),
so the spanning stub is genuinely the sole residual.

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
-- genuinely requires.  The unused-section-variable linter flags it (and `R`) in some lemmas; we keep
-- it (it documents the real requirement, and is needed by `snBlocks`' OV-reindexing residual) and
-- disable the linter for the file rather than drop the typeclass.
set_option linter.unusedSectionVars false

namespace QOU.BraidKnot.OVTopAssembly

open QOU.BraidKnot

variable {R : Type} [Field R] [CharZero R]

/-! ## The OV-reindexing residual + `C₂` decomposition — from `SnWedderburnPartitionBridge`

The keystone's `SnWedderburnSpectralData` needs a partition-indexed isotypic projection family of
`R[S_n]` that is simultaneously the `snBlocks` bundle (projections, ranks `(dim Sᵘⁱ)²`, completeness)
**and** block-diagonalises the central Jucys–Murphy element `mulLeft C₂` with eigenvalues
`contentSqSum λ_i`.  These two halves are **inseparable**: `mulLeft C₂` is block-diagonal only in the
*isotypic* frame, which is strictly stronger than the size-aligned frame of `snBridge` (distinct
partitions can share `dim Sᵘ`, so a size-aligned split need not be isotypic-aligned; see
`SnWedderburnPartitionBridge` §5).  Both are therefore supplied together by the single aligned core
`SnWedderburnPartitionBridge.snBlocks_c2_aligned`.

**History / correction.** Earlier revisions split this into a `snBlocks` (delegating to the
size-aligned `snBridge`) plus a separate `c2_eigen_on_blocks` that took the projection family as a
*free* argument.  That free-`proj` `decomp` statement is **false**, machine-proved as
`SnWedderburnPartitionBridge.freeProjClaim_false` (instantiate `proj ≡ 0` ⇒ `mulLeft C₂ = 0` ⇒
`C₂ = 0`, contradicting `C₂(1) = binom(n,2) ≠ 0`) — because `mulLeft C₂` is block-diagonal only for the
*specific isotypic* projections, not an arbitrary `snBlocks`/`snBridge` family.  The over-general
`c2_eigen_on_blocks` is removed in favour of the aligned core. -/

/-! ## The capstone construction -/

/-- **TOP of the OV tower — the Wedderburn / Jucys–Murphy block spectral decomposition exists.**

We construct the keystone's `SnWedderburnSpectralData R n` by wiring each field to its brick:

* `Idx := SpechtClassification.PartitionIndex n` (brick 3) — sorry-free, with its `Fintype`.
* `d i := numSYT i.diagram` (bricks 1/2, `dim Sᵘ = #SYT`) — sorry-free *definition*.
* `ω i := ((contentSqSum i.diagram : ℤ) : R)` (brick 5, the JM content-square eigenvalue) —
  sorry-free *definition*.
* `p` / `proj` / `isProj` / `complete` / `decomp` are all drawn from the single aligned core
  `SnWedderburnPartitionBridge.snBlocks_c2_aligned` (the isotypic projection family **and** the `C₂`
  block-decomposition, produced together; Ref `sn_rational_specht_split` strengthened to isotypic
  alignment + `JucysMurphy.centralC2_acts_by_contentSqSum`).
* `rank i` additionally consumes the brick-4 **wired** finrank
  `SpechtFinrankWired.specht_finrank_eq_numSYT_wired` load-bearingly (a `rw` turning the aligned core's
  block-size `(dim Sᵘⁱ)²` into the field's `(numSYT λ_i)²`).  This wired finrank sources independence
  from the **proved** core `SpechtTriangularCore.standardPolytabloid_triangular'`, so the `rank`
  sorry-path is the **spanning / straightening stub only** — not the independence stub and not the
  opaque brick-2 finrank stub `Specht.specht_finrank_eq_numSYT`. -/
noncomputable def snSpectralData (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit R] :
    RegularRepBlockTrace.SnWedderburnSpectralData R n :=
  -- Destructure the single aligned core once and wire every projection-data field to it.
  let pf := (SnWedderburnPartitionBridge.snBlocks_c2_aligned (R := R) n).choose_spec.choose_spec
  { -- sorry-free: the index type is the partitions of `n` (brick 3).
    Idx := SpechtClassification.PartitionIndex n
    -- sorry-free: brick 3 supplies the `Fintype` instance.
    fintypeIdx := SpechtClassification.instFintypePartitionIndex n
    -- sorry-free: `d i = dim Sᵘⁱ = #SYT(λ_i)` (bricks 1/2).  The dim-identity is carried by `rank`.
    d := fun i => numSYT i.diagram
    -- sorry-free: `ω i = Σ_{c∈λ_i} c(c)²`, the JM eigenvalue (brick 5), cast `ℤ → R`.  The
    -- action-identity is carried by `decomp`.
    ω := fun i => ((JucysMurphy.contentSqSum i.diagram : ℤ) : R)
    -- The `λ_i`-isotypic block / its projection, from the single aligned core.
    p := (SnWedderburnPartitionBridge.snBlocks_c2_aligned (R := R) n).choose
    proj := (SnWedderburnPartitionBridge.snBlocks_c2_aligned (R := R) n).choose_spec.choose
    -- `proj i` is the projection onto `p i` (1st conjunct of the aligned core).
    isProj := pf.1
    -- `dim_R (p i) = (dim Sᵘⁱ)² = numSYT(λ_i)²`: the aligned core gives the block size `(dim Sᵘⁱ)²`
    -- (2nd conjunct), and the brick-4 **wired** finrank rewrites `dim Sᵘⁱ → numSYT λ_i`.  Its
    -- sorry-path is the spanning/straightening stub only.
    rank := fun i => by
      rw [pf.2.1 i, SpechtFinrankWired.specht_finrank_eq_numSYT_wired (k := R) i.diagram]
    -- **Block spectral decomposition** `mulLeft C₂ = Σ_i ω_i · proj_i` — the 4th conjunct of the
    -- aligned core (replaces the over-general, false `c2_eigen_on_blocks`).
    decomp := pf.2.2.2
    -- The blocks exhaust `R[S_n]`: `Σ_i proj_i = id` (3rd conjunct of the aligned core).
    complete := pf.2.2.1 }

/-- **The Wedderburn / JM block spectral decomposition of `R[S_n]` is inhabited** — the capstone
existence statement that discharges the side-2 hypothesis of Identity (B).  Constructed by
`snSpectralData`, whose `Idx` / `d` / `ω` fields are sorry-free and whose projection data is wired
to the bricks (see the per-field map in `snSpectralData`). -/
theorem sn_spectralData_exists (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit R] :
    Nonempty (RegularRepBlockTrace.SnWedderburnSpectralData R n) :=
  ⟨snSpectralData n⟩

/-! ## Identity (B), general `n` — the payoff -/

/-- **Identity (B), general `n` (modulo the tower's stubs).**  Feeding the assembled spectral datum
`(sn_spectralData_exists n).some` into the keystone's §3b-cond conditional theorem
`RegularRepBlockTrace.identityB_conditional` yields the Identity-(B) trace equation

`Σ_i ω_i · dim(λ_i)² = n! · binom(n,2)`

for **all `n`** — where `ω_i` is the Jucys–Murphy content-square eigenvalue and `dim(λ_i)` the SYT
dimension of block `i`.  This is the unconditional general-`n` Identity (B).

**Corrected 2026-08-23.** The sentence that stood here said "the only residual inputs are the
bricks' own honest `sorry`s (the isotypic-projection identification, the OV eigenvalue theorem, the
standard-basis dimension theorem's spanning core)". Measured, there are none left:
`#print axioms` on `identityB_general`, on `sum_numSYT_sq_eq_factorial` and on `snSpectralData`
reports `[propext, Classical.choice, Quot.sound]`. The class hypothesis `SnIsotypicSpechtSplit` is
also no longer an open premise — it is inhabited by `SnIsotypicSpechtSplitInstance`.

(The statement is stated exactly as the keystone's `identityB_conditional` concludes, against the
assembled `W := (sn_spectralData_exists n).some`.) -/
theorem identityB_general (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit R] :
    ∑ i : (sn_spectralData_exists (R := R) n).some.Idx,
        (sn_spectralData_exists (R := R) n).some.ω i
          * ((sn_spectralData_exists (R := R) n).some.d i : R) ^ 2
      = (n.factorial : R) * (n.choose 2 : R) :=
  RegularRepBlockTrace.identityB_conditional (sn_spectralData_exists (R := R) n).some

/-- **RSK sum-of-squares in SYT-count form — unconditional (modulo the assembled OV bricks).**
`∑_{λ ⊢ n} (#SYT λ)² = n!`, over the partition index `PartitionIndex n` with `#SYT = numSYT`.

Specialises the conditional `RegularRepBlockTrace.sumSq_dim_eq` to the assembled datum
`snSpectralData (R := ℚ) n` — whose `d = numSYT ∘ diagram` — over the characteristic-zero field `ℚ`,
then transports the resulting `ℚ`-identity back to `ℕ` (`exact_mod_cast`). This is the **dimension
side** the `Δ_λ`-gate / Identity-I note flagged as needing HLF/RSK: it now holds outright, the only
residual inputs being the assembled tower's own cited bricks (no new axiom). It is the SYT-count half
of the Burnside identity `Σ_λ (f^λ)² = n!` (`DeltaLambdaSignRule.burnside`); wiring it there
additionally needs `dimIrrep = numSYT` (the hook-length formula `numSYT_mul_hookProduct` + the
custom-`Partition` ↔ `YoungDiagram` hookProduct bridge) and the `List (Partition n)` ↔
`PartitionIndex n` reindexing. -/
theorem sum_numSYT_sq_eq_factorial (n : ℕ) [SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ] :
    ∑ i : SpechtClassification.PartitionIndex n, numSYT i.diagram ^ 2 = n.factorial := by
  have h := RegularRepBlockTrace.sumSq_dim_eq (snSpectralData (R := ℚ) n)
  have key : ((∑ i : SpechtClassification.PartitionIndex n, numSYT i.diagram ^ 2 : ℕ) : ℚ)
      = ((n.factorial : ℕ) : ℚ) := by
    push_cast
    exact h
  exact_mod_cast key

end QOU.BraidKnot.OVTopAssembly
