import QOU.MathlibExt.DisjointBlockTraceLaw

/-!
# `TowerSpan` reduced to one local rewriting rule

Bean `qou-301d`. Continuation of `QOU.MathlibExt.DisjointBlockTraceLaw`, which
derives the disjoint-block trace law from `TowerSpan` — the hypothesis that each
step of the level filtration is spanned by the previous stage together with
single sandwiches `v * g (M+1) * w`.

`TowerSpan` is a claim about **every element** of a filtration step, which is an
awkward thing either to prove or to check. This file replaces it with a claim
about **one element shape**:

    SandwichReduces B m  :  ∀ c ∈ B,  g m * c * g m  ∈  B + span (sandwich B m)

i.e. *a doubled generator with base material between it collapses back down*.
`towerSpan_of_sandwichReduces` shows the two are related in the useful direction:
the local rule implies the global decomposition.

## Why this is the right reduction

`DisjointBlockTraceLaw` identifies the obstruction to the unconditional argument
as a **repeated maximal-level generator** — a word `g M * x * g M` that no
rotation can peel. `SandwichReduces` is precisely the statement that such a word
rewrites, and nothing more. So the hypothesis has been moved from "the whole
filtration decomposes" to "the one blocking shape reduces", which is
* smaller — one element shape rather than a submodule containment,
* local — it mentions a single level `m`, not the tower, and
* **where the braid relation lives** — in the Iwahori-Hecke algebra this is the
  content of `g_i g_{i±1} g_i = g_{i±1} g_i g_{i±1}` together with the quadratic
  relation, which is what lets a doubled generator be pushed down.

## The proof

`P B m` is the candidate submodule `B + span (sandwich B m)`. The work is showing
it is closed under multiplication, which needs exactly one non-trivial case:

    (v * g * w) * (v' * g * w')  =  v * (g * (w * v') * g) * w'

whose middle factor is `SandwichReduces` applied to `w * v' ∈ B`. Everything else
is `mul_base_left` / `mul_base_right`. With multiplication closure, `P` becomes a
subalgebra via `Submodule.toSubalgebra` and `Algebra.adjoin_le` finishes.

## 🛑 What is NOT established

**`SandwichReduces` is not proved for any tower with a growing filtration.** This
file moves the hypothesis; it does not discharge it. Per AGENTS.md
§"Axiomatization is NOT a Proof", a reduction between two unproved statements is
progress in *shape* only, and the honest summary of `qou-301d` remains: the
disjoint-block law, and hence the bond-product reading of the atom word, is
**measured, not derived**.

The inhabitation caveat from `DisjointBlockTraceLaw.towerSpan_unit` carries over
unchanged — the only witness has a constant filtration, and
`towerSpan_of_constant` shows such a witness satisfies `TowerSpan` for reasons
that have nothing to do with any of this.

-- Ref: [leitner2026] bean qou-301d; Kassel–Turaev, *Braid Groups*, ch. 4.
-/

namespace QOU.MathlibExt.TowerSpanReduction

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- The base together with single sandwiches, as a submodule. -/
def P (B : Subalgebra R A) (m : ℕ) : Submodule R A :=
  Subalgebra.toSubmodule B ⊔ Submodule.span R (sandwich T B m)

theorem base_le_P (B : Subalgebra R A) (m : ℕ) {x : A} (hx : x ∈ B) : x ∈ P T B m :=
  Submodule.mem_sup_left (by simpa using hx)

theorem gen_mem_P (B : Subalgebra R A) (m : ℕ) : T.g m ∈ P T B m := by
  refine Submodule.mem_sup_right (Submodule.subset_span ?_)
  exact ⟨1, B.one_mem, 1, B.one_mem, by simp⟩

/-- Left multiplication by a base element preserves `P`. -/
theorem mul_base_left (B : Subalgebra R A) (m : ℕ) (c : A) (hc : c ∈ B)
    {x : A} (hx : x ∈ P T B m) : c * x ∈ P T B m := by
  rw [P, Submodule.mem_sup] at hx ⊢
  obtain ⟨u, hu, s, hs, rfl⟩ := hx
  refine ⟨c * u, by simpa using B.mul_mem hc (by simpa using hu), c * s, ?_,
    (mul_add c u s).symm⟩
  induction hs using Submodule.span_induction with
  | mem x hx =>
      obtain ⟨v, hv, w, hw, rfl⟩ := hx
      exact Submodule.subset_span ⟨c * v, B.mul_mem hc hv, w, hw, by simp only [mul_assoc]⟩
  | zero => simp
  | add x y _ _ ihx ihy => rw [mul_add]; exact Submodule.add_mem _ ihx ihy
  | smul r x _ ihx => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ ihx

/-- Right multiplication by a base element preserves `P`. -/
theorem mul_base_right (B : Subalgebra R A) (m : ℕ) (c : A) (hc : c ∈ B)
    {x : A} (hx : x ∈ P T B m) : x * c ∈ P T B m := by
  rw [P, Submodule.mem_sup] at hx ⊢
  obtain ⟨u, hu, s, hs, rfl⟩ := hx
  refine ⟨u * c, by simpa using B.mul_mem (by simpa using hu) hc, s * c, ?_,
    (add_mul u s c).symm⟩
  induction hs using Submodule.span_induction with
  | mem x hx =>
      obtain ⟨v, hv, w, hw, rfl⟩ := hx
      exact Submodule.subset_span ⟨v, hv, w * c, B.mul_mem hw hc, by simp only [mul_assoc]⟩
  | zero => simp
  | add x y _ _ ihx ihy => rw [add_mul]; exact Submodule.add_mem _ ihx ihy
  | smul r x _ ihx => rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ ihx

/-- **The reduction hypothesis.** A doubled generator with base material between
it collapses back into `P`. This is the one blocking shape identified in
`DisjointBlockTraceLaw`, and in the Hecke case it is where the braid relation
does its work. -/
def SandwichReduces (B : Subalgebra R A) (m : ℕ) : Prop :=
  ∀ c ∈ B, T.g m * c * T.g m ∈ P T B m

theorem gen_mul_span (B : Subalgebra R A) (m : ℕ) (hred : SandwichReduces T B m)
    (v w : A) (hv : v ∈ B) (hw : w ∈ B)
    {y : A} (hy : y ∈ Submodule.span R (sandwich T B m)) :
    (v * T.g m * w) * y ∈ P T B m := by
  induction hy using Submodule.span_induction with
  | mem b hb =>
      obtain ⟨v', hv', w', hw', rfl⟩ := hb
      have key : T.g m * (w * v') * T.g m ∈ P T B m := hred _ (B.mul_mem hw hv')
      have e : (v * T.g m * w) * (v' * T.g m * w')
          = v * (T.g m * (w * v') * T.g m) * w' := by simp only [mul_assoc]
      rw [e]
      exact mul_base_right T B m w' hw' (mul_base_left T B m v hv key)
  | zero => simp
  | add x y _ _ ihx ihy => rw [mul_add]; exact Submodule.add_mem _ ihx ihy
  | smul r x _ ihx => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ ihx

theorem span_mul_span (B : Subalgebra R A) (m : ℕ) (hred : SandwichReduces T B m)
    {x y : A} (hx : x ∈ Submodule.span R (sandwich T B m))
    (hy : y ∈ Submodule.span R (sandwich T B m)) : x * y ∈ P T B m := by
  induction hx using Submodule.span_induction with
  | mem a ha =>
      obtain ⟨v, hv, w, hw, rfl⟩ := ha
      exact gen_mul_span T B m hred v w hv hw hy
  | zero => simp
  | add x y _ _ ihx ihy => rw [add_mul]; exact Submodule.add_mem _ ihx ihy
  | smul r x _ ihx => rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ ihx

/-- `P` is closed under multiplication once sandwiches reduce. -/
theorem P_mul_mem (B : Subalgebra R A) (m : ℕ) (hred : SandwichReduces T B m)
    {x y : A} (hx : x ∈ P T B m) (hy : y ∈ P T B m) : x * y ∈ P T B m := by
  rw [P, Submodule.mem_sup] at hx hy
  obtain ⟨u, hu, s, hs, rfl⟩ := hx
  obtain ⟨u', hu', s', hs', rfl⟩ := hy
  have hu2 : u ∈ B := by simpa using hu
  have hu2' : u' ∈ B := by simpa using hu'
  have e : (u + s) * (u' + s') = u * u' + (u * s' + (s * u' + s * s')) := by
    rw [add_mul, mul_add, mul_add]; abel
  rw [e]
  refine Submodule.add_mem _ (base_le_P T B m (B.mul_mem hu2 hu2')) ?_
  refine Submodule.add_mem _ (mul_base_left T B m u hu2 (Submodule.mem_sup_right hs')) ?_
  exact Submodule.add_mem _ (mul_base_right T B m u' hu2' (Submodule.mem_sup_right hs))
    (span_mul_span T B m hred hs hs')

/-- **One filtration step decomposes, from the single local rewriting rule.**

The global decomposition at level `M` is implied by the local fact that
`g (M+1) * c * g (M+1)` reduces, for `c` in the previous stage. -/
theorem step_of_sandwichReduces (n M : ℕ)
    (hquad : ∀ m : ℕ, ∃ h : R, T.g m * T.g m = h • T.g m + 1)
    (hred : SandwichReduces T (shiftedUpTo T n M) (M + 1)) :
    Subalgebra.toSubmodule (shiftedUpTo T n (M + 1)) ≤
      Subalgebra.toSubmodule (shiftedUpTo T n M) ⊔
        Submodule.span R (sandwich T (shiftedUpTo T n M) (M + 1)) := by
    set B := shiftedUpTo T n M with hB
    have hone : (1 : A) ∈ P T B (M + 1) := base_le_P T B (M + 1) B.one_mem
    let S : Subalgebra R A :=
      Submodule.toSubalgebra (P T B (M + 1)) hone
        (fun _ _ hx hy => P_mul_mem T B (M + 1) hred hx hy)
    have hsub : shiftedUpTo T n (M + 1) ≤ S := by
      refine Algebra.adjoin_le ?_
      rintro x ⟨m, hnm, hmM, rfl | rfl⟩
      · rcases Nat.lt_or_ge m (M + 1) with hlt | hge
        · exact base_le_P T B (M + 1)
            (Algebra.subset_adjoin ⟨m, hnm, by omega, Or.inl rfl⟩)
        · obtain rfl : m = M + 1 := by omega
          exact gen_mem_P T B (M + 1)
      · rcases Nat.lt_or_ge m (M + 1) with hlt | hge
        · exact base_le_P T B (M + 1)
            (Algebra.subset_adjoin ⟨m, hnm, by omega, Or.inr rfl⟩)
        · obtain rfl : m = M + 1 := by omega
          obtain ⟨h, hq⟩ := hquad (M + 1)
          rw [T.gen_inv_eq_of_quadratic (M + 1) h hq]
          exact Submodule.sub_mem _ (gen_mem_P T B (M + 1))
            (Submodule.smul_mem _ _ hone)
    intro x hx
    exact hsub (by simpa using hx)

/-- **`TowerSpan` follows from the single local rewriting rule**, at every level
at once. Pure repackaging of `step_of_sandwichReduces`. -/
theorem towerSpan_of_sandwichReduces
    (hquad : ∀ m : ℕ, ∃ h : R, T.g m * T.g m = h • T.g m + 1)
    (hred : ∀ n M : ℕ, SandwichReduces T (shiftedUpTo T n M) (M + 1)) :
    TowerSpan T where
  step := fun n M => step_of_sandwichReduces T n M hquad (hred n M)

/-- **The end-to-end statement.** The disjoint-block law follows from the local
rewriting rule alone (plus the quadratic relation), by composing this file's
reduction with `DisjointBlockTraceLaw.disjointBlock_of_towerSpan`.

🛑 Still conditional: `SandwichReduces` is not proved for any tower with a
growing filtration. -/
theorem disjointBlock_of_sandwichReduces
    (hquad : ∀ m : ℕ, ∃ h : R, T.g m * T.g m = h • T.g m + 1)
    (hred : ∀ n M : ℕ, SandwichReduces T (shiftedUpTo T n M) (M + 1)) :
    DisjointBlockMultiplicative T :=
  letI : TowerSpan T := towerSpan_of_sandwichReduces T hquad hred
  disjointBlock_of_towerSpan T hquad

end QOU.MathlibExt.TowerSpanReduction
