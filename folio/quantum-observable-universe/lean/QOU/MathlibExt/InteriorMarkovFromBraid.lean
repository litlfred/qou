/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.HeckeSandwichReduces

/-!
# The interior-bond Markov property, from the braid relations

Bean `qou-gr3t`. That bean states the blocker for the general-`A` bond
factorisation in these words:

> A hypothetical field `interior_markov : ∀ g, ∀ a ∈ H g, ∀ b ∈ upper g,
> tr(a*σ_g*b) = z*tr(a*b)` would be independent of the existing fields
> (`cmTower` satisfies all of them and violates it), so it may NOT be added as a
> field or axiom; **it is a THEOREM of the Hecke tower, to be proved from the
> Hecke relations**, not of the abstract tower.

and names the route:

> prove `InteriorMarkov` for a tower carrying the quadratic relation + braid
> relation + **word-spanning**, by the reduction `b ↦ (H_m + H_m σ_m H_m)` on the
> top letter `m` of `b` and induction on `m` — a multi-session build of the
> Ocneanu uniqueness argument on the word level.

**The third ingredient landed the day after that was written.** Word-spanning is
`TowerSpanReduction.step_of_sandwichReduces`, and `HeckeSandwichReduces`
discharges it from the same three relations (`BraidedTower`). With it the
reduction the bean describes is a short induction, not a multi-session build,
and this file carries it out.

## 🔁 This is a SECOND, independent proof — the canonical one is elsewhere

`QOU.Hecke.InteriorMarkovOfBraidedTower.interiorMarkov_of_braided` (#7265,
landed 2026-09-13) proves the same statement and is **the one to cite and to
build on**: it lands on the `MarkovTower` carrier, so
`MarkovInteriorBond.tr_bondWord_of_interiorMarkov` consumes it directly, which
is what `tr_bondWord_of_braided` there does.

The two proofs are genuinely different arguments, which is why this one is kept:

| | route |
|---|---|
| `InteriorMarkovOfBraidedTower` | `DisjointBlockMultiplicative → DisjointBlock → InteriorMarkov` — three applications of the block law |
| **here** | direct induction over the tower from `step_of_sandwichReduces` + `markov₂_of_markov`, **never mentioning the block law** |

Same hypothesis (`BraidedTower`), same conclusion. Do **not** export a second
`interiorMarkov_of_braided` from this file — the exported name is
`interiorMarkov_shiftedUpTo`, and the carrier is `OcneanuTrace.MarkovTrace`
rather than `MarkovTower`.

## The statement

`interiorMarkov_shiftedUpTo` : for a `BraidedTower`, every `g`, every `M`, every
`a ∈ H g` and every `b` in the stage `shiftedUpTo (g+1) M`,

    tr (a * g g * b) = z * tr (a * b).

`shiftedUpTo (g+1) M` is the part of the tail above `g` generated at levels
`≤ M`, and every element of `Hecke/MarkovInteriorBond.upper g` lies in some such
stage, so this is the interior-bond rule on the whole tail, stage by stage.

## The proof

Induction on `M`, exactly as in `sandwichReduces_all`, and for the same reason:
the *previous* stage's spanning decomposition already puts `b` in one-sandwich
form, so only two shapes arise.

* `M = 0`. The stage is `⊥` — the generator window `{m : g+1 ≤ m ≤ 0}` is empty
  for every `g` — so `b` is a scalar and the claim is the Markov axiom T3.
* `M+1`. `step_of_sandwichReduces` writes `b = u + Σ vᵢ · g (M+1) · wᵢ` with
  `u, vᵢ, wᵢ` in the previous stage. On `u` the inductive hypothesis applies
  directly. On a sandwich, **both sides peel the same generator with the same
  two-sided Markov step**:

      tr (a * g g * (v * g (M+1) * w))  =  z * tr (a * g g * (v * w))   [markov₂]
                                        =  z * z * tr (a * (v * w))     [IH]
      z * tr (a * (v * g (M+1) * w))    =  z * z * tr (a * (v * w))     [markov₂]

  and the two agree. The level bookkeeping is the only content: `a * g g * v`
  and `w` must both sit in `H (M+1)`, which needs `g ≤ M` — and when `g > M` the
  stage is `⊥` again, so that case never reaches the sandwich branch.

`markov₂` is free (`DisjointBlockTrace.markov₂_of_markov` derives it from
cyclicity and T3), so no hypothesis beyond `BraidedTower` enters.

## What this does and does not settle

**Settles:** the interior-bond rule is a *theorem* for any `MarkovTrace`
satisfying the three Iwahori-Hecke relations, which is what `qou-gr3t` asked for
and what its counter-model showed cannot be had from the tower axioms alone.
`cmTower` is not a counterexample here because it fails `quad`: its generators
are polynomial variables and `X_m * X_m ≠ h • X_m + 1` in `R[X₀, X₁, X₂]`.

**The bridge to `Hecke/MarkovInteriorBond` is DEFINITIONAL — measured by #7265,
not by this file.** An earlier version of this docstring said the two carriers
"have to be related first, and whether that is a definitional bridge or real
work is not measured here". It is definitional:
`InteriorMarkovOfBraidedTower.toTower S hfar : MarkovTower R A` is built
field-by-field from an `OcneanuTrace.MarkovTrace` (`σ := S.g`, `tr := S.tr`,
`z := S.z`, `H := S.H`, `markov := S.markov`, `tr_comm := S.tr_mul_comm`,
`far_comm := hfar`), and `toTowerB S` supplies `hfar` from `BraidedTower.far`.
So `InteriorMarkov (toTowerB S)` unfolds to exactly the quantifier form proved
here with `S.g` for `T.σ`, and `tr_bondWord_of_interiorMarkov` consumes it
directly. `qou-gr3t`'s conditional is therefore **discharged** — by #7265, with
this file as an independent confirmation.

🛑 **Does not settle the bond product for the production word.** The
factorisation `tr(atom)/tr(free) = ∏ (z + dᵢ)` is measured (`qou-qqm4`, orders
≤ 5, `A ≤ 5`), and the production word is monotone, for which
`MonotoneWordTraceFactorizes.tr_stabWord_eq_prod_tr` already gives the
free-word half unconditionally. Nothing here computes a binding coefficient.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] bean qou-gr3t; bean qou-301d.
-/

namespace QOU.MathlibExt.InteriorMarkovFromBraid

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
open QOU.MathlibExt.TowerSpanReduction QOU.MathlibExt.HeckeSandwichReduces

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- A stage whose generator window is empty is `⊥`. -/
theorem shiftedUpTo_eq_bot (n M : ℕ) (hM : M < n) : shiftedUpTo T n M = ⊥ := by
  have hset : {x : A | ∃ m, n ≤ m ∧ m ≤ M ∧ (x = T.g m ∨ x = T.ginv m)} = ∅ := by
    ext x
    simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
    rintro ⟨m, hnm, hmM, _⟩
    omega
  rw [shiftedUpTo, hset, Algebra.adjoin_empty]

/-- The interior-bond rule on a stage that is `⊥`: `b` is a scalar, and the
claim is the Markov axiom. -/
theorem interior_of_mem_bot (g : ℕ) {a : A} (ha : a ∈ T.H g)
    {b : A} (hb : b ∈ (⊥ : Subalgebra R A)) :
    T.tr (a * T.g g * b) = T.z * T.tr (a * b) := by
  obtain ⟨r, rfl⟩ := Algebra.mem_bot.1 hb
  have e₁ : a * T.g g * algebraMap R A r = r • (a * T.g g) := by
    rw [Algebra.smul_def, ← Algebra.commutes r (a * T.g g)]
  have e₂ : a * algebraMap R A r = r • a := by
    rw [Algebra.smul_def, ← Algebra.commutes r a]
  rw [e₁, e₂, map_smul, map_smul, T.markov g a ha]
  simp only [smul_eq_mul]
  ring

/-- The sandwich half of the induction step, as a standalone lemma so that the
`span_induction` runs in a context mentioning nothing but `s`.

Both sides peel `g (M+1)` with the same two-sided Markov step, so they agree as
soon as the inductive hypothesis handles the shortened word `v * w`. -/
theorem interior_span_step [BraidedTower T] (g M : ℕ) (hge : g ≤ M)
    {a : A} (ha : a ∈ T.H g)
    (ih : ∀ b ∈ shiftedUpTo T (g + 1) M, T.tr (a * T.g g * b) = T.z * T.tr (a * b))
    {s : A} (hs : s ∈ Submodule.span R (sandwich T (shiftedUpTo T (g + 1) M) (M + 1))) :
    T.tr (a * T.g g * s) = T.z * T.tr (a * s) := by
  induction hs using Submodule.span_induction with
  | mem x hx =>
      obtain ⟨v, hv, w, hw, rfl⟩ := hx
      have haM : a ∈ T.H (M + 1) := T.H_mono (by omega) ha
      have hgM : T.g g ∈ T.H (M + 1) := T.H_mono (by omega) (T.g_mem g)
      have hvM : v ∈ T.H (M + 1) := shiftedUpTo_le T (g + 1) M hv
      have hwM : w ∈ T.H (M + 1) := shiftedUpTo_le T (g + 1) M hw
      have hav : a * v ∈ T.H (M + 1) := (T.H (M + 1)).mul_mem haM hvM
      have hagv : a * T.g g * v ∈ T.H (M + 1) :=
        (T.H (M + 1)).mul_mem ((T.H (M + 1)).mul_mem haM hgM) hvM
      have e₁ : a * T.g g * (v * T.g (M + 1) * w)
          = (a * T.g g * v) * T.g (M + 1) * w := by simp only [mul_assoc]
      have e₂ : a * (v * T.g (M + 1) * w)
          = (a * v) * T.g (M + 1) * w := by simp only [mul_assoc]
      rw [e₁, e₂, markov₂_of_markov T (M + 1) _ hagv w hwM,
        markov₂_of_markov T (M + 1) _ hav w hwM,
        show a * T.g g * v * w = a * T.g g * (v * w) by simp only [mul_assoc],
        show a * v * w = a * (v * w) by simp only [mul_assoc],
        ih (v * w) ((shiftedUpTo T (g + 1) M).mul_mem hv hw)]
  | zero => simp
  | add x y _ _ ihx ihy =>
      rw [mul_add, mul_add, map_add, map_add, ihx, ihy]; ring
  | smul r x _ ihx =>
      rw [mul_smul_comm, mul_smul_comm, map_smul, map_smul, ihx]
      simp only [smul_eq_mul]; ring

/-- **The interior-bond Markov property, stage by stage, from the braid
relations.**

For every `g` and `M`, every `a ∈ H g` and every `b` in the stage
`shiftedUpTo (g+1) M` of the tail above `g`:

    tr (a * g g * b) = z * tr (a * b).

This is `qou-gr3t`'s `InteriorMarkov` — the property its counter-model shows is
*independent of the tower axioms* — derived from `BraidedTower` alone. -/
theorem interiorMarkov_shiftedUpTo [hbt : BraidedTower T] (g : ℕ) :
    ∀ M : ℕ, ∀ a ∈ T.H g, ∀ b ∈ shiftedUpTo T (g + 1) M,
      T.tr (a * T.g g * b) = T.z * T.tr (a * b) := by
  intro M
  induction M with
  | zero =>
      intro a ha b hb
      exact interior_of_mem_bot T g ha
        (by rw [shiftedUpTo_eq_bot T (g + 1) 0 (Nat.succ_pos g)] at hb; exact hb)
  | succ M ih =>
      intro a ha b hb
      rcases Nat.lt_or_ge M g with hlt | hge
      · rcases Nat.lt_or_ge (M + 1) (g + 1) with hlt' | hge'
        · exact interior_of_mem_bot T g ha
            (by rw [shiftedUpTo_eq_bot T (g + 1) (M + 1) hlt'] at hb; exact hb)
        · omega
      · have hspan := step_of_sandwichReduces T (g + 1) M
          (fun m => hbt.quad m) (sandwichReduces_all T (g + 1) M)
        have hb' : b ∈ Subalgebra.toSubmodule (shiftedUpTo T (g + 1) M) ⊔
            Submodule.span R (sandwich T (shiftedUpTo T (g + 1) M) (M + 1)) :=
          hspan (by simpa using hb)
        rw [Submodule.mem_sup] at hb'
        obtain ⟨u, hu, s, hs, rfl⟩ := hb'
        have hu' : u ∈ shiftedUpTo T (g + 1) M := by simpa using hu
        have hbase : T.tr (a * T.g g * u) = T.z * T.tr (a * u) := ih a ha u hu'
        have hsand : T.tr (a * T.g g * s) = T.z * T.tr (a * s) :=
          interior_span_step T g M hge ha (fun c hc => ih a ha c hc) hs
        rw [mul_add, mul_add, map_add, map_add, hbase, hsand]
        ring

/-- The same statement with the membership hypotheses as arguments rather than
bounded quantifiers, for convenience at call sites.

Deliberately **not** named `interiorMarkov_of_braided`: that name belongs to
`QOU.Hecke.InteriorMarkovOfBraidedTower`, on the `MarkovTower` carrier, and two
declarations sharing it across carriers is the overload defect this corpus has
already paid for once with `markovZ`. -/
theorem interiorMarkov_apply [BraidedTower T] (g M : ℕ)
    {a : A} (ha : a ∈ T.H g) {b : A} (hb : b ∈ shiftedUpTo T (g + 1) M) :
    T.tr (a * T.g g * b) = T.z * T.tr (a * b) :=
  interiorMarkov_shiftedUpTo T g M a ha b hb

end QOU.MathlibExt.InteriorMarkovFromBraid
