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

The two carriers were built independently, for different reasons. The table
below once said that *between them they cover the two ways a witness can be
degenerate*; the last column shows why that is **not** so — see the correction
under "What the Hecke instance buys".

| carrier | `h` | filtration | trace |
|---|---|---|---|
| `unitMarkovTrace u` (`HeckeSandwichReduces.braidedTower_unit`) | `u - u⁻¹`, can be `≠ 0` | **constant** (`H = ⊤`) | identity |
| `SymmetricGroupTowerWitness.symTrace` | `0` | grows at every level | not a homomorphism |
| `HeckeTowerWitness.heckeTowerMarkovTrace h z` | **free parameter** | `H 0 < H 1` | 🛑 **IS a homomorphism** — `towerTrace_mul` below |

## What the Hecke instance buys

`braidedTower_heckeTower` is the one the caveat named: the presented infinite
Iwahori-Hecke algebra `H_∞`, with `h` a free parameter of the construction, so
`h ≠ 0` — the Hecke case `h = q - q⁻¹` — is available. That is a real gain **for
the filtration**, and `towerSpan_heckeTower` is the first `TowerSpan` witness
with both a provably growing filtration (`twH_zero_lt_one`) and `h ≠ 0`.

🛑 **CORRECTED 2026-09-13 — it buys nothing for the TRACE, and this is measured,
not suspected.** This paragraph continued: *"Composing it with
`disjointBlock_of_braided` gives `disjointBlock_heckeTower`: the disjoint-block
trace law on a Hecke tower at `h ≠ 0`, which is the configuration every prior
witness missed."* The composition is valid and `disjointBlock_heckeTower` is
true; what is wrong is reading it as exercising the disjoint-block content.

`ocneanuTrace_mul_of_markov` below proves that the rank-2 Ocneanu trace is
multiplicative on **every** pair exactly when `z * z = h * z + 1` — and that
equation is precisely the hypothesis `heckeTowerMarkovTrace` requires in order to
be a `MarkovTrace` at all. Since `towerTrace = ocneanuTrace ∘ collapse` with
`collapse` an algebra hom, `towerTrace_mul` makes the whole trace an algebra
**homomorphism**, and `heckeTower_tr_mul_unconditional` states the trace law for
arbitrary `a, b` with no level hypothesis whatsoever. So
`disjointBlock_heckeTower` holds for reasons that have nothing to do with
disjoint blocks.

The table's third column said "not faithful". That is true and it is a different
property: faithfulness is about separating elements, multiplicativity is about
the law under test. Only the second answers whether the witness exercises
`DisjointBlockMultiplicative`.

**Consequence: no witness has all three properties** — growing filtration,
`h ≠ 0`, and a non-multiplicative trace. `SymmetricGroupTowerWitness` has the
first and third at `h = 0`; this one has the first and second. The *trace*
content at `q ≠ 1` remains unexercised by any inhabited witness.

🛑 **What that gap IS, corrected 2026-09-13 — it is NOT "Jones' theorem is
open".** This read *"which is Jones' theorem on `H_∞(q)` and stays open (bean
`qou-g8i1`)"*, and both halves are wrong. `qou-g8i1` is `completed` and is
titled *"Prove the (z+d) bond rule"* — a different result; the pointer comes
from a scoping in `qou-0fmb` that `qou-0fmb` itself retracted on 2026-09-12.
And the Ocneanu trace's **existence and uniqueness are PROVED on `main`**,
sorry-free: `SchurWeyl/MarkovTraceInstance.ocneanuMarkovTrace :
MarkovTraceFamily ℝ q q⁻¹ (q³/(q²+1))` and
`SchurWeyl/MarkovTraceUnique.markovTrace_unique`.

The real gap is that those live in a **different abstraction**:
`HeckeCoset.MarkovTraceFamily` is level-indexed with one trace per level, one
Markov parameter and no `ginv`, while `OcneanuTrace.MarkovTrace` is a single
algebra with a filtration, one trace, `ginv`, and both `z` and `zinv`. Nothing
bridges them. The live carrier is bean **`qou-ejde`** (the colimit route), whose
step 1 `SchurWeyl/HeckeProductInjective.heckeProduct_injective` landed on
2026-09-13.

Note also that **"faithful on `H_∞(q)`" is the wrong target at convention D** —
the weight vanishes for `ℓ(λ) ≥ 3` (`QBeta/WenzlWeightVanishing.
conventionD_weight_eq_zero_iff_rowLens`), so the radical is nonzero and the
attainable statement is faithfulness on `H_∞(q)/rad`. That over-claim is bean
`qou-phlk`, already adjudicated.

The corpus already held `HeckeRankTwoMarkov.ocneanuTrace_mul_defect`, whose
defect is literally `h * z + 1 - z * z`. What it had not recorded is that the
`MarkovTrace` hypothesis **kills** that defect.

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
  coarse functional, **not** about the Ocneanu trace of `H_∞(q)`. This does not
  weaken `sandwichReduces_all` itself, which uses no trace field — it bounds
  what the *composition* delivers.

  🛑 **The gap is a BRIDGE, not Jones' theorem — corrected 2026-09-13.** The
  first version of this paragraph said *"constructing that trace is Jones'
  existence theorem and remains open (bean `qou-g8i1`)"*. **Both halves are
  wrong.** Jones' theorem is *proved in this corpus, with uniqueness*, both
  sorry-free on `main`: `SchurWeyl.MarkovTraceInstance` builds `wtrace` with the
  trace property, normalisation, Markov stabilisation **and** tower
  compatibility (`wtrace_incl`) at `z = q³/(q²+1)`, plus `eq_wtrace_of_markov`;
  `SchurWeyl.MarkovTraceUnique.markovTrace_unique` gives uniqueness. What is
  missing is that all of it lives in `HeckeCoset.MarkovTraceFamily`, a
  **different** Markov-trace abstraction, and nothing bridges it to
  `OcneanuTrace.MarkovTrace` — which is the structure this file's theorems
  consume. And `qou-g8i1` is not that item at all: it is the `(z+d)` bond rule,
  and it is `completed`. The live carrier is `qou-0fmb`'s re-scope of
  2026-09-12, which names `qou-ejde` (`heckeIncl` injective) as the keystone
  that discharges it.
* **Strict growth is proved only at the bottom.** `twH_zero_lt_one` gives
  `H 0 < H 1`; `H n < H (n+1)` for `n ≥ 1` does not follow from the collapse
  map, which sends every generator to the same element. The symmetric-group
  instance does grow at every level (`t_not_mem_shiftedUpTo`) but has `h = 0`.
  **No single carrier yet has both `h ≠ 0` and growth at every level.**

  The bean is **`qou-p8yg`**, not `qou-uoal` (corrected 2026-09-13: `qou-uoal`
  is `completed`, and it is the `≤ n!` *upper* half). `qou-p8yg` records that
  `H 1 < H 2` is a **wiring job rather than a build** — the rank-6 separator
  already exists sorry-free (`SchurWeyl.HeckeDim3Dim.finrank_hecke3`,
  `sixBasis`, `HeckeDim3.braid3`) — while general `n` needs the `(n+1)!`
  lower bound. It also records the *negative* that closes the cheap route:
  `scalar_tail_forces_central` excludes the whole tail-to-scalars family.

**Nothing here derives the bond product.** That reading of the atom word
remains measured, per `DisjointBlockTraceLaw`'s own statement of scope.

-- Ref: [leitner2026] beans qou-301d / qou-cins / qou-fq1i / qou-0fmb /
--      qou-p8yg / qou-ejde;
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

/-! ## Measuring the Hecke instance's trace, rather than assuming it

The three theorems the correction above rests on. They are about
`HeckeTowerWitness`'s trace only; nothing here touches `BraidedTower`,
`sandwichReduces_all`, or any conclusion drawn from them. -/

section TraceIsMultiplicative

open QOU.MathlibExt.HeckeRankTwoMarkov QOU.MathlibExt.HeckeRankTwoMarkov.Hecke2
open QOU.MathlibExt.HeckeTowerWitness

variable {R : Type*} [CommRing R]

/-- **The Markov hypothesis makes the rank-2 Ocneanu trace multiplicative.**

`HeckeRankTwoMarkov.ocneanuTrace_mul_defect` computes the defect on `σ · σ` as
`h * z + 1 - z * z`; this shows the defect vanishes on *every* pair precisely
under `z * z = h * z + 1`, which is the Markov condition. -/
theorem ocneanuTrace_mul_of_markov {h : R} (z : R) (hz : z * z = h * z + 1)
    (x y : Hecke2 R h) :
    ocneanuTrace z (x * y) = ocneanuTrace z x * ocneanuTrace z y := by
  simp only [ocneanuTrace_apply, mul_const, mul_gen]
  linear_combination (-(x.gen * y.gen)) * hz

/-- **Hence the presented tower's trace is an algebra homomorphism**, since
`collapse` is one and `towerTrace = ocneanuTrace ∘ collapse`. -/
theorem towerTrace_mul (h z : R) (hz : z * z = h * z + 1) (x y : HeckeTower R h) :
    towerTrace h z (x * y) = towerTrace h z x * towerTrace h z y := by
  simp only [towerTrace_apply, map_mul]
  exact ocneanuTrace_mul_of_markov z hz _ _

/-- The same fact in the form that makes the degeneracy unmissable: for this
witness the trace law holds for **arbitrary** `a` and `b`, with no hypothesis
about levels, so `disjointBlock_heckeTower` is an instance of it and carries no
disjoint-block information. -/
theorem heckeTower_tr_mul_unconditional (h z : R) (hz : z * z = h * z + 1)
    (a b : HeckeTower R h) :
    (heckeTowerMarkovTrace h z hz).tr (a * b)
      = (heckeTowerMarkovTrace h z hz).tr a * (heckeTowerMarkovTrace h z hz).tr b :=
  towerTrace_mul h z hz a b

end TraceIsMultiplicative

end QOU.MathlibExt.BraidedTowerInstances
