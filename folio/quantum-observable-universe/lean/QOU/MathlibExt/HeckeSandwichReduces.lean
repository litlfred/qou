import QOU.MathlibExt.TowerSpanReduction

/-!
# The braid relations discharge `SandwichReduces` — and hence `TowerSpan`

Bean `qou-301d`. `DisjointBlockTraceLaw` derives the disjoint-block trace law
from `TowerSpan`; `TowerSpanReduction` replaces `TowerSpan` by the local
rewriting rule `SandwichReduces`. Both files close with the same 🛑: the local
rule is **not proved for any tower with a growing filtration**.

This file proves it, from the defining relations of a braid tower.

## What is assumed

`BraidedTower T` carries exactly three equations, all of them relations the
Iwahori-Hecke algebra `H_n(q)` satisfies by presentation:

* `quad`  — `g m * g m = h • g m + 1` for some `h : R` (in `H_n(q)`, `h = q - q⁻¹`);
* `far`   — `g m * g k = g k * g m` when `k + 1 < m` (distant generators commute);
* `braid` — `g (m+1) * g m * g (m+1) = g m * g (m+1) * g m`.

Nothing else: no basis, no dimension count, no faithful representation, no
Markov property. In particular the trace fields of `MarkovTrace` play no part in
anything proved here — this is a statement about the **filtration**, which is
what `TowerSpan` was always about.

## The argument

`sandwichReduces_all` is an induction on the level `M`. Writing `g₁ = g (M+1)`
and `g₂ = g (M+2)`, and using the previous level's decomposition
`c = u + Σ vᵢ g₁ wᵢ` with `u, vᵢ, wᵢ` at level `≤ M`:

* every element at level `≤ M` commutes with `g₂` (`far`, since `M + 1 < M + 2`);
* the base part collapses by the quadratic relation,
  `g₂ u g₂ = u g₂² = h • (u g₂) + u`;
* each sandwich part is turned over by the braid relation,
  `g₂ (v g₁ w) g₂ = v (g₂ g₁ g₂) w = v (g₁ g₂ g₁) w = (v g₁) g₂ (g₁ w)`,
  and `v g₁`, `g₁ w` are at level `≤ M + 1`.

The base case is the quadratic relation together with one application of `braid`
at `m = 0`; below the bottom of the shift window the stage is `⊥` and only the
quadratic relation is needed.

## What this does and does not settle

**Settled.** `TowerSpan` is no longer a hypothesis for any tower whose
generators satisfy the braid relations — `towerSpan_of_braided`. Composing with
`DisjointBlockTraceLaw.disjointBlock_of_towerSpan` gives
`disjointBlock_of_braided`: the disjoint-block trace law holds for every
`MarkovTrace` on a braided tower.

**🛑 NOT settled here — but see `MathlibExt.BraidedTowerInstances`, which
supplies the instances this file does not.** `BraidedTower` is a hypothesis on a
`MarkovTrace`, and **this file constructs no instance of it**.
The existing witnesses do not qualify, which is a fact about them worth stating
rather than leaving implicit:
`InvolutionTowerWitness` has commuting involutions, and
`braid_fails_for_commuting_involutions` below shows the braid relation there
would force `g m = g (m+1)`, so that witness satisfies `SandwichReduces` for a
reason that has nothing to do with this file's argument;
`DisjointBlockTraceLaw.towerSpan_unit` is degenerate for the reasons its own
docstring gives. So the honest status of the corpus claim is unchanged in one
respect — nothing here exhibits a Hecke tower in Lean — while the *hypothesis*
has moved from an unproved structure theorem to a list of defining relations.

What *is* supplied is a bracket on the class, in two halves that no single
witness combines:

* `braidedTower_unit` — an instance in which the quadratic scalar `h = u - u⁻¹`
  is genuinely non-zero (`unit_quad_scalar_ne_zero`), i.e. the relations are
  consistent with the Hecke case `h = q - q⁻¹`; its filtration is constant.
* the symmetric-group algebra tower (bean `qou-fq1i`) — a growing filtration and
  a non-multiplicative trace, but `h = 0`, and its `SandwichReduces` is proved by
  support arguments in the permutation model rather than by rewriting with the
  relations, so it does not reach `q ≠ 1`.

**UPDATED 2026-09-13 — the corpus now supplies a carrier, and this paragraph's
earlier form was wrong twice.** It read: *"A witness with both a growing
filtration and `h ≠ 0` is an Iwahori-Hecke tower, which Mathlib does not supply.
That, and only that, is what stands between this theorem and an unconditional
disjoint-block law for the production trace."*

* **"Mathlib does not supply"** was true and beside the point — the corpus
  supplies one. `MathlibExt.HeckeTowerWitness` (bean `qou-cins`) presents `H_∞`
  as `FreeAlgebra R ℕ` quotiented by exactly these three relations, with `h` a
  free parameter, and `BraidedTowerInstances.braidedTower_heckeTower`
  instantiates this class on it. Even against Mathlib the line overstated:
  `SchurWeyl.finrank_le_factorial` (bean `qou-uoal`, `completed`) is the `≤ n!`
  upper half of the coset-basis theorem the strict-growth question needs.
* **"That, and only that"** was wrong about what remains. Two things do, and the
  instance repairs neither: `HeckeTowerWitness`'s trace is **not faithful** (it
  factors through a rank-2 quotient), and its filtration is proved to grow only
  at the bottom (`twH_zero_lt_one`: `H 0 < H 1`).

  🛑 **Corrected 2026-09-13**, because the first version of this line said
  *"Jones' existence theorem for the Ocneanu trace of `H_∞(q)` is still open —
  bean `qou-g8i1`"*, and that is wrong twice. Jones' theorem is **proved in this
  corpus with uniqueness**, sorry-free on `main`
  (`SchurWeyl.MarkovTraceInstance`, `SchurWeyl.MarkovTraceUnique`); the gap is
  that it is stated in `HeckeCoset.MarkovTraceFamily` and **nothing bridges it
  to `OcneanuTrace.MarkovTrace`**. And `qou-g8i1` is the `(z+d)` bond rule, and
  is `completed`. See `BraidedTowerInstances` for the full correction and the
  live beans (`qou-0fmb`, `qou-p8yg`, `qou-ejde`).

So `BraidedTower` is inhabited in the quadrant that matters, and the distance to
"an unconditional disjoint-block law for the production trace" is a faithful
trace, not a carrier.

**Nothing here derives the bond product.** That reading of the atom word remains
measured, per `DisjointBlockTraceLaw`'s own statement of scope.

-- Ref: [leitner2026] bean qou-301d; Kassel-Turaev, *Braid Groups*, ch. 4;
--      Geck-Pfeiffer, *Characters of Finite Coxeter Groups and Iwahori-Hecke
--      Algebras*, §4.4 (the tower decomposition `H_{n+1} = H_n + H_n g_n H_n`).
-/

namespace QOU.MathlibExt.HeckeSandwichReduces

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
open QOU.MathlibExt.TowerSpanReduction

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- **The braid-tower relations.** Three equations on the generator family of a
`MarkovTrace`, each of them a defining relation of the Iwahori-Hecke algebra.
None of them mentions the trace. -/
class BraidedTower : Prop where
  /-- The quadratic relation. In `H_n(q)` the scalar is `h = q - q⁻¹`. -/
  quad : ∀ m : ℕ, ∃ h : R, T.g m * T.g m = h • T.g m + 1
  /-- Distant generators commute. -/
  far : ∀ m k : ℕ, k + 1 < m → T.g m * T.g k = T.g k * T.g m
  /-- The braid relation on adjacent generators. -/
  braid : ∀ m : ℕ, T.g (m + 1) * T.g m * T.g (m + 1) = T.g m * T.g (m + 1) * T.g m

/-! ## The relations propagate to `ginv` and to whole stages -/

/-- The inverse generator inherits distant commutation, because the quadratic
relation makes it affine in `g`. -/
theorem ginv_far [hbt : BraidedTower T] (m k : ℕ) (hk : k + 1 < m) :
    T.g m * T.ginv k = T.ginv k * T.g m := by
  obtain ⟨c, hc⟩ := hbt.quad k
  rw [T.gen_inv_eq_of_quadratic k c hc, mul_sub, sub_mul, hbt.far m k hk,
    mul_smul_comm, smul_mul_assoc, mul_one, one_mul]

/-- Everything in a stage capped at level `M` commutes with a generator at any
level `> M + 1`. -/
theorem shiftedUpTo_commute [hbt : BraidedTower T] (n M j : ℕ) (hj : M + 1 < j) {c : A}
    (hc : c ∈ shiftedUpTo T n M) : T.g j * c = c * T.g j := by
  unfold shiftedUpTo at hc
  induction hc using Algebra.adjoin_induction with
  | mem x hx =>
      obtain ⟨m, _, hmM, rfl | rfl⟩ := hx
      · exact hbt.far j m (by omega)
      · exact ginv_far T j m (by omega)
  | algebraMap r => exact (Algebra.commutes r _).symm
  | add x y _ _ ihx ihy => rw [mul_add, add_mul, ihx, ihy]
  | mul x y _ _ ihx ihy => rw [← mul_assoc, ihx, mul_assoc, ihy, ← mul_assoc]

/-! ## The two pieces of the inductive step -/

/-- The base part of a decomposed element collapses by the quadratic relation
alone: `g₂ u g₂ = u g₂² = h • (u g₂) + u`. -/
theorem base_conj [hbt : BraidedTower T] (n M : ℕ) {u : A} (hu : u ∈ shiftedUpTo T n M) :
    T.g (M + 2) * u * T.g (M + 2) ∈ P T (shiftedUpTo T n (M + 1)) (M + 2) := by
  obtain ⟨h, hq⟩ := hbt.quad (M + 2)
  have hcomm := shiftedUpTo_commute T n M (M + 2) (by omega) hu
  have hu' : u ∈ shiftedUpTo T n (M + 1) := shiftedUpTo_mono T n (by omega) hu
  have e : T.g (M + 2) * u * T.g (M + 2) = u * (T.g (M + 2) * T.g (M + 2)) := by
    rw [hcomm]; simp only [mul_assoc]
  rw [e, hq, mul_add, mul_one, mul_smul_comm]
  refine Submodule.add_mem _ (Submodule.smul_mem _ _ ?_) (base_le_P T _ _ hu')
  refine Submodule.mem_sup_right (Submodule.subset_span ?_)
  exact ⟨u, hu', 1, (shiftedUpTo T n (M + 1)).one_mem, by rw [mul_one]⟩

/-- The sandwich part is turned over by the braid relation:
`g₂ (v g₁ w) g₂ = v (g₁ g₂ g₁) w = (v g₁) g₂ (g₁ w)`, and both outer factors have
risen one level. -/
theorem sandwich_conj [hbt : BraidedTower T] (n M : ℕ) (hn : n ≤ M + 1) {s : A}
    (hs : s ∈ Submodule.span R (sandwich T (shiftedUpTo T n M) (M + 1))) :
    T.g (M + 2) * s * T.g (M + 2) ∈ P T (shiftedUpTo T n (M + 1)) (M + 2) := by
  have hg1 : T.g (M + 1) ∈ shiftedUpTo T n (M + 1) :=
    Algebra.subset_adjoin ⟨M + 1, hn, le_refl _, Or.inl rfl⟩
  induction hs using Submodule.span_induction with
  | mem x hx =>
      obtain ⟨v, hv, w, hw, rfl⟩ := hx
      have hcv := shiftedUpTo_commute T n M (M + 2) (by omega) hv
      have hcw := shiftedUpTo_commute T n M (M + 2) (by omega) hw
      have hbr : T.g (M + 2) * T.g (M + 1) * T.g (M + 2)
          = T.g (M + 1) * T.g (M + 2) * T.g (M + 1) := hbt.braid (M + 1)
      have e : T.g (M + 2) * (v * T.g (M + 1) * w) * T.g (M + 2)
          = v * (T.g (M + 2) * T.g (M + 1) * T.g (M + 2)) * w := by
        have h1 : T.g (M + 2) * (v * T.g (M + 1) * w) * T.g (M + 2)
            = T.g (M + 2) * v * T.g (M + 1) * (w * T.g (M + 2)) := by
          simp only [mul_assoc]
        rw [h1, hcv, ← hcw]; simp only [mul_assoc]
      rw [e, hbr]
      refine Submodule.mem_sup_right (Submodule.subset_span ?_)
      refine ⟨v * T.g (M + 1), (shiftedUpTo T n (M + 1)).mul_mem
          (shiftedUpTo_mono T n (by omega) hv) hg1,
        T.g (M + 1) * w, (shiftedUpTo T n (M + 1)).mul_mem hg1
          (shiftedUpTo_mono T n (by omega) hw), ?_⟩
      simp only [mul_assoc]
  | zero => simp
  | add x y _ _ ihx ihy => rw [mul_add, add_mul]; exact Submodule.add_mem _ ihx ihy
  | smul r x _ ihx => rw [mul_smul_comm, smul_mul_assoc]; exact Submodule.smul_mem _ _ ihx

/-! ## The induction -/

/-- Below the bottom of the shift window the stage is trivial, and the quadratic
relation alone reduces the sandwich. -/
theorem sandwichReduces_of_le_bot [hbt : BraidedTower T] (m : ℕ) (B : Subalgebra R A)
    (hB : B ≤ ⊥) : SandwichReduces T B m := by
  intro c hc
  obtain ⟨r, rfl⟩ := Algebra.mem_bot.1 (hB hc)
  obtain ⟨h, hq⟩ := hbt.quad m
  have e : T.g m * algebraMap R A r * T.g m = r • (T.g m * T.g m) := by
    rw [← Algebra.commutes r (T.g m), Algebra.smul_def]
    simp only [mul_assoc]
  rw [e, hq]
  exact Submodule.smul_mem _ _
    (Submodule.add_mem _ (Submodule.smul_mem _ _ (gen_mem_P T B m))
      (base_le_P T B m B.one_mem))

/-- The bottom stage of the full shift window sits inside the subalgebra
generated by `g 0`, because the quadratic relation makes `ginv 0` affine in
`g 0`. -/
theorem shiftedUpTo_zero_le [hbt : BraidedTower T] :
    shiftedUpTo T 0 0 ≤ Algebra.adjoin R ({T.g 0} : Set A) := by
  refine Algebra.adjoin_le ?_
  rintro x ⟨m, _, hm0, rfl | rfl⟩
  · obtain rfl : m = 0 := Nat.le_zero.1 hm0
    exact Algebra.subset_adjoin rfl
  · obtain rfl : m = 0 := Nat.le_zero.1 hm0
    obtain ⟨h, hq⟩ := hbt.quad 0
    rw [T.gen_inv_eq_of_quadratic 0 h hq]
    exact Subalgebra.sub_mem _ (Algebra.subset_adjoin rfl)
      (Subalgebra.smul_mem _ (Subalgebra.one_mem _) h)

/-- The base case: at the bottom of the full shift window the stage is affine in
`g 0`, so one quadratic and one braid application suffice. -/
theorem sandwichReduces_zero [hbt : BraidedTower T] :
    SandwichReduces T (shiftedUpTo T 0 0) 1 := by
  intro c hc
  obtain ⟨h₀, hq₀⟩ := hbt.quad 0
  obtain ⟨h₁, hq₁⟩ := hbt.quad 1
  obtain ⟨u, v, rfl⟩ := adjoin_gen_affine T 0 h₀ hq₀ c (shiftedUpTo_zero_le T hc)
  have hg0 : T.g 0 ∈ shiftedUpTo T 0 0 :=
    Algebra.subset_adjoin ⟨0, le_refl _, le_refl _, Or.inl rfl⟩
  have hbr : T.g 1 * T.g 0 * T.g 1 = T.g 0 * T.g 1 * T.g 0 := hbt.braid 0
  have e : T.g 1 * (u • (1 : A) + v • T.g 0) * T.g 1
      = u • (T.g 1 * T.g 1) + v • (T.g 1 * T.g 0 * T.g 1) := by
    simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, mul_one]
  rw [e, hbr, hq₁, smul_add, smul_smul]
  refine Submodule.add_mem _ (Submodule.add_mem _
    (Submodule.smul_mem _ _ (gen_mem_P T _ 1))
    (base_le_P T _ _ (Subalgebra.smul_mem _ (Subalgebra.one_mem _) u)))
    (Submodule.smul_mem _ _ (Submodule.mem_sup_right (Submodule.subset_span
      ⟨T.g 0, hg0, T.g 0, hg0, rfl⟩)))

/-! ## The theorem -/

/-- **`SandwichReduces` holds at every level of a braided tower.**

Induction on `M`. Below the bottom of the shift window the stage is `⊥`; at the
bottom of the full window it is affine in `g 0`; above, the previous level's
decomposition (`step_of_sandwichReduces` applied to the induction hypothesis)
splits the element into a base part and sandwiches, and `base_conj` /
`sandwich_conj` handle them. -/
theorem sandwichReduces_all [hbt : BraidedTower T] (n M : ℕ) :
    SandwichReduces T (shiftedUpTo T n M) (M + 1) := by
  induction M with
  | zero =>
      rcases Nat.eq_zero_or_pos n with rfl | hn
      · exact sandwichReduces_zero T
      · exact sandwichReduces_of_le_bot T 1 _ (by
          refine Algebra.adjoin_le ?_
          rintro x ⟨m, hnm, hm0, _⟩
          omega)
  | succ M ih =>
      rcases Nat.lt_or_ge (M + 1) n with hlt | hge
      · exact sandwichReduces_of_le_bot T (M + 2) _ (by
          refine Algebra.adjoin_le ?_
          rintro x ⟨m, hnm, hmM, _⟩
          omega)
      · intro c hc
        have hc' := step_of_sandwichReduces T n M hbt.quad ih (by simpa using hc)
        rw [Submodule.mem_sup] at hc'
        obtain ⟨u, hu, s, hs, rfl⟩ := hc'
        rw [mul_add, add_mul]
        exact Submodule.add_mem _ (base_conj T n M (by simpa using hu))
          (sandwich_conj T n M hge hs)

/-- **`TowerSpan` holds on any braided tower** — the hypothesis of
`DisjointBlockTraceLaw` is discharged. -/
theorem towerSpan_of_braided [hbt : BraidedTower T] : TowerSpan T :=
  towerSpan_of_sandwichReduces T hbt.quad (fun n M => sandwichReduces_all T n M)

/-- **The disjoint-block trace law on any braided tower**, unconditionally in the
tower structure: only the three defining relations are assumed. -/
theorem disjointBlock_of_braided [hbt : BraidedTower T] : DisjointBlockMultiplicative T :=
  letI : TowerSpan T := towerSpan_of_braided T
  disjointBlock_of_towerSpan T hbt.quad

/-! ## The hypothesis is not free

`InvolutionTowerWitness` satisfies `quad` and `far` (its generators commute) but
**not** `braid`: for commuting involutions the braid relation collapses to
`g m = g (m+1)`.  Stated here for a generic tower so that no reader mistakes that
witness for an instance of `BraidedTower`. -/

/-- If two adjacent generators commute and both square to `1`, the braid relation
forces them equal. So a commuting-involution tower is braided only if it is
constant — which is exactly why `InvolutionTowerWitness` is not an instance. -/
theorem braid_forces_eq_of_commuting_involutions (m : ℕ)
    (hcomm : T.g (m + 1) * T.g m = T.g m * T.g (m + 1))
    (hi : T.g m * T.g m = 1) (hi' : T.g (m + 1) * T.g (m + 1) = 1)
    (hbraid : T.g (m + 1) * T.g m * T.g (m + 1) = T.g m * T.g (m + 1) * T.g m) :
    T.g m = T.g (m + 1) := by
  have hl : T.g (m + 1) * T.g m * T.g (m + 1) = T.g m := by
    rw [hcomm, mul_assoc, hi', mul_one]
  have hr : T.g m * T.g (m + 1) * T.g m = T.g (m + 1) := by
    rw [← hcomm, mul_assoc, hi, mul_one]
  rw [hl, hr] at hbraid
  exact hbraid

/-! ### An instance, with the quadratic scalar genuinely non-zero

`OcneanuTrace.unitMarkovTrace u` — the one-point tower on `R` with every
generator equal to a fixed unit `u` — satisfies all three relations, with
`h = u - u⁻¹`. Its filtration is constant (`H = ⊤`), so it witnesses the
*relations* and not the *tower*; but it does establish that `BraidedTower` does
not secretly force `h = 0`, which is the one thing a reader might suspect after
`braid_forces_eq_of_commuting_involutions`. -/

instance braidedTower_unit {R₀ : Type*} [CommRing R₀] (u : R₀ˣ) :
    BraidedTower (OcneanuTrace.unitMarkovTrace u) where
  quad _ := ⟨(u : R₀) - ((u⁻¹ : R₀ˣ) : R₀), by
    show (u : R₀) * (u : R₀) = ((u : R₀) - ((u⁻¹ : R₀ˣ) : R₀)) • (u : R₀) + 1
    rw [smul_eq_mul, sub_mul, u.inv_mul, sub_add_cancel]⟩
  far _ _ _ := mul_comm _ _
  braid _ := rfl

/-- In that instance the quadratic scalar is `u - u⁻¹`, and it is non-zero as
soon as `u² ≠ 1` — so the three relations are consistent with `h ≠ 0`, which is
the Hecke case `h = q - q⁻¹`. -/
theorem unit_quad_scalar_ne_zero {R₀ : Type*} [CommRing R₀] (u : R₀ˣ)
    (hu : (u : R₀) * (u : R₀) ≠ 1) : (u : R₀) - ((u⁻¹ : R₀ˣ) : R₀) ≠ 0 := by
  intro h
  apply hu
  have h' : (u : R₀) = ((u⁻¹ : R₀ˣ) : R₀) := sub_eq_zero.1 h
  calc (u : R₀) * (u : R₀) = ((u⁻¹ : R₀ˣ) : R₀) * (u : R₀) := by rw [← h']
    _ = 1 := u.inv_mul

end QOU.MathlibExt.HeckeSandwichReduces
