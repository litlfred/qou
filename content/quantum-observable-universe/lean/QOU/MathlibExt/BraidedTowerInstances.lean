import QOU.MathlibExt.HeckeSandwichReduces
import QOU.MathlibExt.HeckeTowerWitness
import QOU.MathlibExt.SymmetricGroupTowerWitness

/-!
# `BraidedTower` instances — the class is inhabited, in both quadrants

Bean `qou-301d`. `HeckeSandwichReduces` proves `SandwichReduces`, hence
`TowerSpan`, hence the disjoint-block trace law, from three equations
(`quad` / `far` / `braid`) and nothing else. It closed with the caveat that it
**constructed no instance** of that class, so the theorem was general but
unwitnessed. This file removes that caveat.

The two carriers were built independently, for different reasons, and between
them they cover the two ways a witness can be degenerate:

| carrier | `h` | filtration | trace |
|---|---|---|---|
| `unitMarkovTrace u` (`HeckeSandwichReduces.braidedTower_unit`) | `u - u⁻¹`, can be `≠ 0` | **constant** (`H = ⊤`) | identity |
| `SymmetricGroupTowerWitness.symTrace` | `0` | grows at every level | not a homomorphism |
| `HeckeTowerWitness.heckeTowerMarkovTrace h z` | **free parameter** | `H 0 < H 1` | not faithful |

## What the Hecke instance buys

`braidedTower_heckeTower` is the one the caveat named: the presented infinite
Iwahori-Hecke algebra `H_∞`, with `h` a free parameter of the construction, so
`h ≠ 0` — the Hecke case `h = q - q⁻¹` — is available. Composing it with
`disjointBlock_of_braided` gives `disjointBlock_heckeTower`: **the
disjoint-block trace law on a Hecke tower at `h ≠ 0`**, which is the
configuration every prior witness missed.

It is a three-line instantiation because `HeckeTowerWitness` imposes exactly
these three relations by `RingQuot`, so `twGen_quad` / `twGen_far` /
`twGen_braid` *are* the class fields. That is a statement about how well the
two halves fit, not about how much either one proves.

## What the symmetric-group instance buys

`braidedTower_sym` gives `SymmetricGroupTowerWitness.sandwichReduces_sym` a
**second, independent derivation**. That file proves `SandwichReduces` in the
permutation model, by support and point-pushing arguments through the double
coset `S_{k+1} = S_k ∪ S_k s_k S_k`; `sandwichReduces_all` reproves it by
rewriting with the relations, never mentioning a permutation. Two routes to the
same conclusion in the same model is a check on both.

The group-level inputs are the two classical facts about adjacent
transpositions, proved here from `Equiv.swap_apply_apply` alone: distant swaps
commute (`s_far`), and `s (m+1) s m s (m+1) = s m s (m+1) s m` because **both
sides are `swap m (m+2)`** (`s_braid`).

## 🛑 What is still NOT settled

Two limits, both inherited from the carriers and neither repaired here.

* **The Hecke trace is not faithful.** `HeckeTowerWitness`'s trace collapses
  every generator onto the single generator of the rank-2 algebra and composes
  with its Ocneanu trace, so `disjointBlock_heckeTower` is a statement about a
  coarse functional, **not** about the Ocneanu trace of `H_∞(q)`. Constructing
  that trace is Jones' existence theorem and remains open (bean `qou-g8i1`).
  This does not weaken `sandwichReduces_all` itself, which uses no trace field —
  it bounds what the *composition* delivers.
* **Strict growth is proved only at the bottom.** `twH_zero_lt_one` gives
  `H 0 < H 1`; `H n < H (n+1)` for `n ≥ 1` does not follow from the collapse
  map, which sends every generator to the same element. The symmetric-group
  instance does grow at every level (`t_not_mem_shiftedUpTo`) but has `h = 0`.
  **No single carrier yet has both `h ≠ 0` and growth at every level.**

**Nothing here derives the bond product.** That reading of the atom word
remains measured, per `DisjointBlockTraceLaw`'s own statement of scope.

-- Ref: [manuscript] beans qou-301d / qou-cins / qou-fq1i / qou-g8i1;
--      Jones, *Hecke algebra representations of braid groups and link
--      polynomials*, Ann. of Math. 126 (1987).
-/

namespace QOU.MathlibExt.BraidedTowerInstances

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
open QOU.MathlibExt.TowerSpanReduction QOU.MathlibExt.HeckeSandwichReduces

/-! ## The presented Hecke tower — `h` is a free parameter -/

section Hecke

open QOU.MathlibExt.HeckeTowerWitness

variable {R : Type*} [CommRing R]

/-- **The presented infinite Hecke tower is a `BraidedTower`.** The three class
fields are the three relations `RingQuot` imposes, verbatim. -/
instance braidedTower_heckeTower (h z : R) (hz : z * z = h * z + 1) :
    BraidedTower (heckeTowerMarkovTrace h z hz) where
  quad m := ⟨h, twGen_quad h m⟩
  far m k hk := twGen_far h m k hk
  braid m := twGen_braid h m

/-- **`TowerSpan` on the presented Hecke tower**, at any `h` — including the
Hecke case `h = q - q⁻¹ ≠ 0`. -/
theorem towerSpan_heckeTower (h z : R) (hz : z * z = h * z + 1) :
    TowerSpan (heckeTowerMarkovTrace h z hz) :=
  towerSpan_of_braided _

/-- **The disjoint-block trace law on a Hecke tower with `h` unconstrained.**

🛑 The trace here is the collapse-and-Ocneanu functional of `HeckeTowerWitness`,
which is not faithful; this is not a statement about the Ocneanu trace of
`H_∞(q)`. See the file docstring. -/
theorem disjointBlock_heckeTower (h z : R) (hz : z * z = h * z + 1) :
    DisjointBlockMultiplicative (heckeTowerMarkovTrace h z hz) :=
  disjointBlock_of_braided _

end Hecke

/-! ## The symmetric-group tower — a second route to `sandwichReduces_sym` -/

section Sym

open QOU.MathlibExt.SymmetricGroupTowerWitness
open Equiv

/-- Distant adjacent transpositions commute. Conjugating `swap m (m+1)` by
`s k` fixes both endpoints when `k + 1 < m`, so the conjugation is trivial. -/
theorem s_far (m k : ℕ) (hk : k + 1 < m) : s m * s k = s k * s m := by
  have h1 : s k m = m := s_apply_of_ne k m (by omega) (by omega)
  have h2 : s k (m + 1) = m + 1 := s_apply_of_ne k (m + 1) (by omega) (by omega)
  have hc := Equiv.swap_apply_apply (s k) m (m + 1)
  rw [h1, h2] at hc
  have hc' : s m = s k * s m * (s k)⁻¹ := hc
  calc s m * s k = (s k * s m * (s k)⁻¹) * s k := by rw [← hc']
    _ = s k * s m := by rw [mul_assoc, inv_mul_cancel, mul_one]

/-- **The braid relation for adjacent transpositions**: both sides are
`swap m (m+2)`. Each is a conjugation of one swap by the other, computed with
`Equiv.swap_apply_apply` and the involution `(s j)⁻¹ = s j`. -/
theorem s_braid (m : ℕ) :
    s (m + 1) * s m * s (m + 1) = s m * s (m + 1) * s m := by
  have hL : s (m + 1) * s m * s (m + 1) = Equiv.swap m (m + 2) := by
    have h1 : s (m + 1) m = m := s_apply_of_ne (m + 1) m (by omega) (by omega)
    have h2 : s (m + 1) (m + 1) = m + 2 := s_apply_left (m + 1)
    have hc := Equiv.swap_apply_apply (s (m + 1)) m (m + 1)
    rw [h1, h2] at hc
    rw [hc, s_inv]
    rfl
  have hR : s m * s (m + 1) * s m = Equiv.swap m (m + 2) := by
    have h1 : s m (m + 1) = m := s_apply_right m
    have h2 : s m (m + 2) = m + 2 := s_apply_of_ne m (m + 2) (by omega) (by omega)
    have hc := Equiv.swap_apply_apply (s m) (m + 1) (m + 2)
    rw [h1, h2] at hc
    rw [hc, s_inv]
    rfl
  rw [hL, hR]

variable (R : Type*) [CommRing R]

/-- **The symmetric-group algebra tower is a `BraidedTower`**, with `h = 0`. -/
instance braidedTower_sym : BraidedTower (symTrace R) where
  quad m := ⟨0, quad_sym R m⟩
  far m k hk := by
    show t R m * t R k = t R k * t R m
    rw [t, t, ← map_mul, ← map_mul, s_far m k hk]
  braid m := by
    show t R (m + 1) * t R m * t R (m + 1) = t R m * t R (m + 1) * t R m
    rw [t, t, ← map_mul, ← map_mul, ← map_mul, ← map_mul, s_braid m]

/-- **`SandwichReduces` on the symmetric-group tower, derived from the
relations** rather than from the permutation model.

`SymmetricGroupTowerWitness.sandwichReduces_sym` is the same statement proved by
support arguments through the double coset. Two independent routes to one
conclusion. -/
theorem sandwichReduces_sym_via_relations (n M : ℕ) :
    SandwichReduces (symTrace R) (shiftedUpTo (symTrace R) n M) (M + 1) :=
  sandwichReduces_all _ n M

end Sym

end QOU.MathlibExt.BraidedTowerInstances
