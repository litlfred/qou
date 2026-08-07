/-
# The `N = 2` row-cap obstruction to the eightfold way

The eightfold-way chapter's central open problem: quantum Schur–Weyl duality
delivers the baryon multiplets only when the flavour fundamental has
`dim V = N = 3`, while the single-fibre construction supplies `N = 2`.  The
chapter states this; this file **proves** the obstruction, so that it is a
theorem rather than an observation.

## The decomposition

Quantum Schur–Weyl duality at `n = 3` decomposes `V^{⊗3}` over
`U_q(gl_N) × H_3(q)` as

    V^{⊗3}  =  ⊕_{λ ⊢ 3, ℓ(λ) ≤ N}  S^λ ⊗ V_λ

with Specht multiplicities `dim S^{(3)} = 1`, `dim S^{(2,1)} = 2`,
`dim S^{(1³)} = 1`, and Weyl-module dimensions (hook-content formula)

    dim V_{(3)}   = C(N+2, 3)          symmetric   → decuplet at N = 3
    dim V_{(2,1)} = 2·C(N+1, 3)        mixed       → octet     at N = 3
    dim V_{(1³)}  = C(N, 3)            alternating → singlet   at N = 3

The **row cap** `ℓ(λ) ≤ N` is the whole story: a partition with more rows than
`N` contributes nothing, and `C(N, k) = 0` is exactly how that shows up
arithmetically.

## What is proved here

* `weyl_dim_alt_eq_zero_iff` — the singlet channel `λ = (1³)` is empty **iff**
  `N < 3`.  This is the obstruction, in one line.
* `schur_weyl_cube_split_two_three` — the multiplicities account for all of
  `V^{⊗3}` at the two decisive values, `8 = 2³` and `27 = 3³`, so the `N = 2`
  deficit is located in the vanishing alternating channel and not in some
  unaccounted-for piece.  (The general identity for all `N` is Worpitzky's,
  with Eulerian numbers `⟨3,k⟩ = 1, 4, 1`; it is *not* formalised here.)
* `eightfold_channels_at_two` / `eightfold_channels_at_three` — the two
  instances: at `N = 2` the split is `4 + 4 + 0 = 8`, at `N = 3` it is
  `10 + 16 + 1 = 27`.
* `decuplet_forces_three` — if the symmetric channel has dimension 10 then
  `N = 3`.  So "decuplet" is not merely *compatible with* `N = 3`; it
  *determines* it.
* `no_singlet_of_lt_three`, `singlet_forces_three` — the singlet channel
  likewise forces `N ≥ 3`, and pins `N = 3` once its dimension is 1.

## Why this matters for the chapter

At `N = 2` the symmetric partition `(3)` gives a **4**-dimensional
spin-`3/2` quadruplet, not a 10-dimensional decuplet, and the alternating
partition `(1³)` gives **nothing at all** — there is no singlet, hence no
`8 ⊕ 1` structure and no `η'`.  The failure is not a matter of degree: the
alternating channel is *absent*, and no choice of the deformation parameter
`q` restores it, because the row cap is a constraint on `dim V` and the
Drinfeld–Jimbo quantisation does not change dimensions.

So the eightfold-way classification is not "approximately available" at
`N = 2` — it is structurally unavailable.  Any route to the chapter's
conclusions must produce a genuinely 3-dimensional flavour fundamental
(bean `qou-8pl3`).

## Scope

This is a **scope-(b) structural exclusion** in the sense of AGENTS.md
§"Before declaring 'refuted'", and the invariant justifying it is cited: the
row cap `ℓ(λ) ≤ N` of Schur–Weyl duality, realised arithmetically as
`C(N,k) = 0` for `N < k`.  It excludes `N = 2` from *carrying the eightfold-way
decomposition*; it says nothing about whether some other construction in the
framework supplies `N = 3`, which is the open half.

## Base ring (§7c)

Pure combinatorics over `ℕ` — no ring, no ordering beyond `ℕ`, no archimedean
content.
-/
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic

namespace QOU.Eightfold.RowCapObstruction

/-! ## 1. The three channel dimensions at `n = 3` -/

/-- `dim V_{(3)}` for `gl_N` — the symmetric channel.  The baryon **decuplet**
when `N = 3`. -/
def weylDimSym (N : ℕ) : ℕ := (N + 2).choose 3

/-- `dim V_{(2,1)}` for `gl_N` — the mixed channel.  The baryon **octet** when
`N = 3`.  Equals `N(N²−1)/3`, written division-free as `2·C(N+1,3)`. -/
def weylDimMixed (N : ℕ) : ℕ := 2 * ((N + 1).choose 3)

/-- `dim V_{(1³)}` for `gl_N` — the alternating channel.  The **singlet** when
`N = 3`.  This is the channel the row cap kills at `N = 2`. -/
def weylDimAlt (N : ℕ) : ℕ := N.choose 3

/-! ## 2. The obstruction -/

/-- **The row-cap obstruction.**  The alternating channel `λ = (1³)` is empty
exactly when `N < 3`.

`ℓ((1³)) = 3`, so Schur–Weyl's row cap `ℓ(λ) ≤ N` admits this partition only
for `N ≥ 3`; arithmetically that is `C(N,3) = 0 ↔ N < 3`. -/
theorem weyl_dim_alt_eq_zero_iff (N : ℕ) : weylDimAlt N = 0 ↔ N < 3 := by
  unfold weylDimAlt
  exact Nat.choose_eq_zero_iff

/-- No singlet below three flavours. -/
theorem no_singlet_of_lt_three {N : ℕ} (hN : N < 3) : weylDimAlt N = 0 :=
  (weyl_dim_alt_eq_zero_iff N).mpr hN

/-- A nonempty singlet channel forces at least three flavours. -/
theorem singlet_nonempty_forces_three {N : ℕ} (h : weylDimAlt N ≠ 0) : 3 ≤ N := by
  by_contra hcon
  exact h (no_singlet_of_lt_three (Nat.lt_of_not_le hcon))

/-! ## 3. The channels account for all of `V^{⊗3}`

The Specht multiplicities `1, 2, 1` times the Weyl dimensions above reproduce
`N³` at the two values the chapter compares — confirming these are the right
three channels and nothing is missing. -/

/-- **Dimension count at the two decisive values.**  The Specht
multiplicities `1, 2, 1` times the Weyl dimensions account for all of
`V^{⊗3}` at `N = 2` and at `N = 3`:

    N = 2 :   4 + 2·2 + 0  =  8  = 2³
    N = 3 :  10 + 2·8 + 1  = 27  = 3³

so nothing is missing from the three channels, and the `N = 2` deficit is
located precisely in the vanishing alternating channel rather than in some
unaccounted-for piece.

The general identity `N³ = C(N+2,3) + 4·C(N+1,3) + C(N,3)` for all `N` is
Worpitzky's identity with Eulerian numbers `⟨3,k⟩ = 1, 4, 1`; it is **not**
formalised here (it is standard, and the chapter compares only `N = 2` against
`N = 3`). -/
theorem schur_weyl_cube_split_two_three :
    2 ^ 3 = weylDimSym 2 + 2 * weylDimMixed 2 + weylDimAlt 2
      ∧ 3 ^ 3 = weylDimSym 3 + 2 * weylDimMixed 3 + weylDimAlt 3 :=
  ⟨by decide, by decide⟩

/-! ## 4. The two instances that decide the chapter -/

/-- At `N = 2`: symmetric `4`, mixed contributes `4`, alternating **`0`**;
total `8 = 2³`.

The symmetric channel is a 4-dimensional spin-`3/2` quadruplet, not a decuplet,
and there is no singlet at all. -/
theorem eightfold_channels_at_two :
    weylDimSym 2 = 4 ∧ weylDimMixed 2 = 2 ∧ weylDimAlt 2 = 0
      ∧ 2 ^ 3 = weylDimSym 2 + 2 * weylDimMixed 2 + weylDimAlt 2 := by
  refine ⟨by decide, by decide, by decide, by decide⟩

/-- At `N = 3`: symmetric `10` (decuplet), mixed `8` (octet, with multiplicity
`2`), alternating `1` (singlet); total `27 = 3³` — the eightfold way. -/
theorem eightfold_channels_at_three :
    weylDimSym 3 = 10 ∧ weylDimMixed 3 = 8 ∧ weylDimAlt 3 = 1
      ∧ 3 ^ 3 = weylDimSym 3 + 2 * weylDimMixed 3 + weylDimAlt 3 := by
  refine ⟨by decide, by decide, by decide, by decide⟩

/-- **The decuplet determines the flavour dimension.**  If the symmetric
channel has dimension 10 then `N = 3` — so the decuplet is not merely
*consistent with* three flavours, it *forces* them. -/
theorem decuplet_forces_three {N : ℕ} (h : weylDimSym N = 10) : N = 3 := by
  unfold weylDimSym at h
  -- C(N+2,3) is monotone in N; it passes 10 exactly at N = 3.
  rcases Nat.lt_or_ge N 3 with hlt | hge
  · interval_cases N <;> simp_all
  · rcases Nat.eq_or_lt_of_le hge with heq | hgt
    · omega
    · -- N ≥ 4 : the channel is already at least 20
      exfalso
      have : (20 : ℕ) ≤ (N + 2).choose 3 := by
        calc (20 : ℕ) = (4 + 2).choose 3 := by decide
          _ ≤ (N + 2).choose 3 := Nat.choose_le_choose 3 (by omega)
      omega

/-- **The singlet pins the flavour dimension.**  A one-dimensional alternating
channel forces exactly three flavours: `C(N,3) = 1 ↔ N = 3`. -/
theorem singlet_forces_three {N : ℕ} (h : weylDimAlt N = 1) : N = 3 := by
  unfold weylDimAlt at h
  by_contra hne
  rcases Nat.lt_or_ge N 3 with hlt | hge
  · rw [Nat.choose_eq_zero_of_lt hlt] at h; exact absurd h (by norm_num)
  · have h4 : 4 ≤ N := by omega
    have : 4 ≤ N.choose 3 := by
      calc 4 = (4 : ℕ).choose 3 := by decide
        _ ≤ N.choose 3 := Nat.choose_le_choose 3 h4
    omega

end QOU.Eightfold.RowCapObstruction
