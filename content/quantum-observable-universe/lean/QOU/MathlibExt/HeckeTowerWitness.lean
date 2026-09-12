/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.OcneanuTrace
import QOU.MathlibExt.HeckeRankTwoMarkov
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import Mathlib.Tactic.LinearCombination

/-!
# The infinite Hecke tower as a `MarkovTrace` — a non-constant filtration with `h ≠ 0`

Bean `qou-cins` (step S1 of the wiring plan `qou-0fmb`, epic `qou-08a2`).

`OcneanuTrace.MarkovTrace` bundles a *filtration* (`H`, `H_mono`, `g`, `ginv`)
with a *trace* (`tr`, `z`, `markov`). Every existing witness is degenerate in one
of the two ways that matter:

* `OcneanuTrace.unitMarkovTrace u` — the quadratic scalar `h = u - u⁻¹` is
  genuinely non-zero, but the carrier is `R` itself, every generator is the
  *same* element, and the filtration is **constant** (`H = ⊤`).
* `SymmetricGroupTowerWitness` — the filtration grows, but the generators are
  involutions, so `h = 0`: that is the `q = 1` specialisation, not a Hecke tower.

This file supplies a witness in the missing quadrant: the carrier is the
**presented** infinite Iwahori-Hecke algebra `H_∞`, the generators `σ₀, σ₁, …`
are distinct free generators, the filtration is the tower's own
`Algebra.adjoin` filtration, and `h` is a **free parameter** of the
construction, so `h ≠ 0` is available.

## The construction

`HeckeTower R h` is `FreeAlgebra R ℕ` quotiented (via `RingQuot`) by the three
defining relations of `H_n(q)` — with `h = q - q⁻¹`:

```
quad   σ_m * σ_m = h • σ_m + 1
braid  σ_{m+1} * σ_m * σ_{m+1} = σ_m * σ_{m+1} * σ_m
far    σ_m * σ_k = σ_k * σ_m                          (k + 1 < m)
```

Because they are *imposed*, the three relations hold **by construction**
(`twGen_quad`, `twGen_braid`, `twGen_far`) rather than being hypotheses to
discharge. The inverse generator is `σ_m - h·1`, forced by `quad`, so the
two-sided-inverse fields are proved, not assumed.

## The trace, and what it is NOT

The trace is obtained by collapsing every generator onto the single generator of
the rank-2 algebra `HeckeRankTwoMarkov.Hecke2 R h` and composing with its
Ocneanu trace. The Markov axioms then hold **exactly when `z` is a root of the
Hecke quadratic** `z² = h·z + 1` (`ocneanuTrace_markov_gen`) — the same
quadratic that `HeckeRankTwoMarkov.ocneanuTrace_mul_defect` identifies. For
`h = q - q⁻¹` the root is `z = q`.

🛑 **This trace is NOT the Ocneanu trace of `H_∞(q)`, and is not faithful.** It
factors through a rank-2 commutative quotient, so it cannot separate elements of
the tower. Constructing the faithful Markov trace on `H_∞(q)` is Jones' theorem
and remains open here (bean `qou-g8i1`, step S2). Nothing below claims otherwise:
`MarkovTrace` never requires faithfulness, and the theorems that consume a
`MarkovTrace`'s *filtration* (`TowerSpanReduction`, `DisjointBlockTraceLaw`) do
not touch the trace at all.

## What is proved about the filtration, and what is not

**Proved.** `twH_zero_lt_one` : `H 0 < H 1` whenever `R` is non-trivial. This is
the structural separation from `unitMarkovTrace`: the filtration is **not**
constant, and in particular not `⊤`. The proof is by the collapse map — if
`H 0 = H 1` then `σ₀` is a scalar, hence `σ` is a scalar in `Hecke2`, hence
`0 = 1` in `R`.

🛑 **NOT proved.** `H n < H (n+1)` for `n ≥ 1`. The collapse map sends every
generator to the same element, so it cannot separate `H 1` from `H 2`; a finer
separating quotient (rank 6, i.e. `H₃`) or the Iwahori-Hecke coset basis is
needed. The upper half of that basis theorem is already in the corpus
(`IwahoriHecke` `finrank_le_factorial`, bean `qou-uoal`); the lower bound is
open. Do not read `twH_mono` as strict growth at every level — it is `≤`.

-- Ref: [manuscript] beans qou-cins / qou-0fmb / qou-301d; Jones, *Hecke algebra
--      representations of braid groups and link polynomials*, Ann. of Math. 126
--      (1987), §5 (the Ocneanu trace); Geck-Pfeiffer, *Characters of Finite
--      Coxeter Groups and Iwahori-Hecke Algebras*, §4.4.
-/

namespace QOU.MathlibExt.HeckeTowerWitness

open QOU.MathlibExt.OcneanuTrace
open QOU.MathlibExt.HeckeRankTwoMarkov
open QOU.MathlibExt.HeckeRankTwoMarkov.Hecke2

variable {R : Type*} [CommRing R]

/-! ## The presented tower -/

/-- The `m`-th free generator of the free `R`-algebra on `ℕ`. -/
def fgen (R : Type*) [CommRing R] (m : ℕ) : FreeAlgebra R ℕ := FreeAlgebra.ι R m

/-- **The defining relations of the infinite Iwahori-Hecke tower.** With
`h = q - q⁻¹`, these are exactly the relations of `H_n(q)` for every `n`. -/
inductive HeckeRel (h : R) : FreeAlgebra R ℕ → FreeAlgebra R ℕ → Prop
  /-- The Hecke quadratic relation. -/
  | quad (m : ℕ) : HeckeRel h (fgen R m * fgen R m) (h • fgen R m + 1)
  /-- The braid relation on adjacent generators. -/
  | braid (m : ℕ) :
      HeckeRel h (fgen R (m + 1) * fgen R m * fgen R (m + 1))
        (fgen R m * fgen R (m + 1) * fgen R m)
  /-- Distant generators commute. -/
  | far (m k : ℕ) (hk : k + 1 < m) :
      HeckeRel h (fgen R m * fgen R k) (fgen R k * fgen R m)

/-- **The infinite Hecke tower** `H_∞`, presented by generators and relations. -/
abbrev HeckeTower (R : Type*) [CommRing R] (h : R) := RingQuot (HeckeRel h)

/-- The Hecke generator `σ_m` in the tower. -/
def twGen (h : R) (m : ℕ) : HeckeTower R h :=
  RingQuot.mkAlgHom R (HeckeRel h) (fgen R m)

/-- The inverse generator `σ_m⁻¹ = σ_m - h·1`, forced by the quadratic relation. -/
def twGenInv (h : R) (m : ℕ) : HeckeTower R h := twGen h m - h • 1

/-- The tower's own filtration: `H n` is generated by the first `n` generators. -/
def twH (h : R) (n : ℕ) : Subalgebra R (HeckeTower R h) :=
  Algebra.adjoin R (twGen h '' {m | m < n})

/-! ## The three relations hold by construction -/

/-- **The Hecke quadratic relation** in the tower. -/
theorem twGen_quad (h : R) (m : ℕ) :
    twGen h m * twGen h m = h • twGen h m + 1 := by
  have hrel := RingQuot.mkAlgHom_rel (S := R) (HeckeRel.quad (h := h) m)
  simpa [twGen] using hrel

/-- **The braid relation** in the tower. -/
theorem twGen_braid (h : R) (m : ℕ) :
    twGen h (m + 1) * twGen h m * twGen h (m + 1)
      = twGen h m * twGen h (m + 1) * twGen h m := by
  have hrel := RingQuot.mkAlgHom_rel (S := R) (HeckeRel.braid (h := h) m)
  simpa [twGen] using hrel

/-- **Distant generators commute** in the tower. -/
theorem twGen_far (h : R) (m k : ℕ) (hk : k + 1 < m) :
    twGen h m * twGen h k = twGen h k * twGen h m := by
  have hrel := RingQuot.mkAlgHom_rel (S := R) (HeckeRel.far (h := h) m k hk)
  simpa [twGen] using hrel

/-! ## The filtration data -/

theorem twGenInv_mul (h : R) (m : ℕ) : twGenInv h m * twGen h m = 1 := by
  rw [twGenInv, sub_mul, smul_mul_assoc, one_mul, twGen_quad]
  abel

theorem mul_twGenInv (h : R) (m : ℕ) : twGen h m * twGenInv h m = 1 := by
  rw [twGenInv, mul_sub, mul_smul_comm, mul_one, twGen_quad]
  abel

theorem twGen_mem (h : R) (n : ℕ) : twGen h n ∈ twH h (n + 1) :=
  Algebra.subset_adjoin ⟨n, Nat.lt_succ_self n, rfl⟩

theorem twGenInv_mem (h : R) (n : ℕ) : twGenInv h n ∈ twH h (n + 1) :=
  Subalgebra.sub_mem _ (twGen_mem h n)
    (Subalgebra.smul_mem _ (Subalgebra.one_mem _) h)

/-- The filtration is increasing. **This is `≤`, not strict** — see the module
docstring. -/
theorem twH_mono (h : R) : Monotone (twH h) := fun _ _ hab =>
  Algebra.adjoin_mono (Set.image_mono fun _ hm => lt_of_lt_of_le hm hab)

/-! ## The collapse map onto the rank-2 algebra -/

/-- Every generator of the tower is sent to the single generator of `H₂`. This is
an algebra map precisely because `Hecke2` satisfies all three relations: `quad`
is `sigma_sq`, and `braid` / `far` are trivial for a single element. -/
def collapse (h : R) : HeckeTower R h →ₐ[R] Hecke2 R h :=
  RingQuot.liftAlgHom R
    ⟨FreeAlgebra.lift R fun _ => (sigma : Hecke2 R h), by
      intro x y hxy
      induction hxy with
      | quad m => simp [fgen, sigma_sq]
      | braid m => simp [fgen]
      | far m k hk => simp [fgen]⟩

@[simp] theorem collapse_twGen (h : R) (m : ℕ) :
    collapse h (twGen h m) = (sigma : Hecke2 R h) := by
  simp [collapse, twGen, fgen]

@[simp] theorem collapse_twGenInv (h : R) (m : ℕ) :
    collapse h (twGenInv h m) = (sigmaInv : Hecke2 R h) := by
  rw [twGenInv, map_sub, collapse_twGen, map_smul, map_one]
  -- `Hecke2` carries `@[simp]` projections for `+` and `-ᵢ` but none for `-`,
  -- so `(x - y).const` does not reduce until the subtraction is unfolded.
  ext <;> simp [sigma, sigmaInv, sub_eq_add_neg]

/-! ## The Markov axioms on `H₂`, for a general element

`HeckeRankTwoMarkov.ocneanuTrace_markov` covers only the scalar bottom `c·1` of
the two-step tower. The tower below needs stabilisation against *every* element,
which costs exactly one hypothesis: `z` must be a root of the Hecke quadratic. -/

/-- **(T3) for a general element.** Stabilisation holds for all of `H₂` iff `z`
is a root of `X² - h·X - 1` — the same quadratic as `ocneanuTrace_mul_defect`. -/
theorem ocneanuTrace_markov_gen (h z : R) (hz : z * z = h * z + 1)
    (x : Hecke2 R h) :
    ocneanuTrace z (x * sigma) = z * ocneanuTrace z x := by
  simp only [ocneanuTrace_apply, mul_const, mul_gen, sigma_const, sigma_gen]
  linear_combination (-x.gen) * hz

/-- **(T3') for a general element**, with `zinv = z - h`. -/
theorem ocneanuTrace_markovInv_gen (h z : R) (hz : z * z = h * z + 1)
    (x : Hecke2 R h) :
    ocneanuTrace z (x * sigmaInv) = (z - h) * ocneanuTrace z x := by
  simp only [ocneanuTrace_apply, mul_const, mul_gen, sigmaInv_const, sigmaInv_gen]
  linear_combination (-x.gen) * hz

/-! ## The `MarkovTrace` instance -/

/-- The tower trace: collapse to `H₂`, then take the rank-2 Ocneanu trace.
🛑 Not faithful — see the module docstring. -/
def towerTrace (h z : R) : HeckeTower R h →ₗ[R] R :=
  (ocneanuTrace (h := h) z).comp (collapse h).toLinearMap

@[simp] theorem towerTrace_apply (h z : R) (x : HeckeTower R h) :
    towerTrace h z x = ocneanuTrace z (collapse h x) := rfl

/-- **A `MarkovTrace` on the presented infinite Hecke tower**, for any `h` and any
root `z` of the Hecke quadratic. With `h = q - q⁻¹` the root is `z = q`.

The filtration is the tower's own `Algebra.adjoin` filtration and `h` is free, so
this inhabits the quadrant no previous witness reached: non-constant filtration
(`twH_zero_lt_one`) **and** `h ≠ 0` available. -/
def heckeTowerMarkovTrace (h z : R) (hz : z * z = h * z + 1) :
    MarkovTrace R (HeckeTower R h) where
  H := twH h
  H_mono := twH_mono h
  g := twGen h
  g_mem := twGen_mem h
  ginv := twGenInv h
  ginv_mem := twGenInv_mem h
  ginv_mul := twGenInv_mul h
  mul_ginv := mul_twGenInv h
  tr := towerTrace h z
  tr_mul_comm := fun a b => by
    simp only [towerTrace_apply, map_mul]
    exact ocneanuTrace_mul_comm z _ _
  tr_one := by simp
  z := z
  zinv := z - h
  markov := fun _ a _ => by
    simp only [towerTrace_apply, map_mul, collapse_twGen]
    exact ocneanuTrace_markov_gen h z hz _
  markov_inv := fun _ a _ => by
    simp only [towerTrace_apply, map_mul, collapse_twGenInv]
    exact ocneanuTrace_markovInv_gen h z hz _

@[simp] theorem heckeTowerMarkovTrace_g (h z : R) (hz : z * z = h * z + 1) (m : ℕ) :
    (heckeTowerMarkovTrace h z hz).g m = twGen h m := rfl

@[simp] theorem heckeTowerMarkovTrace_H (h z : R) (hz : z * z = h * z + 1) (n : ℕ) :
    (heckeTowerMarkovTrace h z hz).H n = twH h n := rfl

/-! ## Non-degeneracy

Two things separate this witness from `unitMarkovTrace`: the filtration is not
constant, and the carrier is not a one-dimensional algebra. -/

theorem algebraMap_gen (h r : R) : (algebraMap R (Hecke2 R h) r).gen = 0 := rfl

/-- The bottom of the filtration is the scalars. -/
theorem twH_zero (h : R) : twH h 0 = ⊥ := by
  have : {m : ℕ | m < 0} = (∅ : Set ℕ) := by
    ext m; simp
  rw [twH, this, Set.image_empty, Algebra.adjoin_empty]

/-- **The filtration is not constant.** `H 0 ⊊ H 1`, so this witness is not the
degenerate `H = ⊤` tower. -/
theorem twH_zero_lt_one [Nontrivial R] (h : R) : twH h 0 < twH h 1 := by
  refine lt_of_le_of_ne (twH_mono h (by omega)) ?_
  intro heq
  have hmem : twGen h 0 ∈ twH h 0 := heq ▸ twGen_mem h 0
  rw [twH_zero] at hmem
  obtain ⟨r, hr⟩ := Algebra.mem_bot.1 hmem
  have hcol : (algebraMap R (Hecke2 R h) r) = (sigma : Hecke2 R h) := by
    have := congrArg (collapse h) hr
    simpa using this
  have : (0 : R) = 1 := by
    have := congrArg Hecke2.gen hcol
    rwa [algebraMap_gen, sigma_gen] at this
  exact zero_ne_one this

/-- The tower is non-trivial: `0 ≠ 1`. -/
theorem heckeTower_nontrivial [Nontrivial R] (h : R) :
    Nontrivial (HeckeTower R h) := by
  refine ⟨⟨0, 1, fun he => ?_⟩⟩
  have hc : (collapse h) 0 = (collapse h) 1 := by rw [he]
  rw [map_zero, map_one] at hc
  have : (0 : R) = 1 := congrArg Hecke2.const hc
  exact zero_ne_one this

/-- **The quadratic scalar is genuinely free.** Unlike the symmetric-group tower
(where the generators are involutions and `h = 0` is forced), `h` here is a
parameter: for every `h` there is a tower whose generators satisfy `σ² = h·σ + 1`.
Together with `twH_zero_lt_one` this is the missing quadrant. -/
theorem exists_tower_with_nonzero_h (h : R) (hne : h ≠ 0) :
    ∃ T : ℕ → HeckeTower R h, (∀ m, T m * T m = h • T m + 1) ∧ h ≠ 0 :=
  ⟨twGen h, twGen_quad h, hne⟩

end QOU.MathlibExt.HeckeTowerWitness
