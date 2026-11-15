import Mathlib.Logic.Relation
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith

/-!
# Chain reaction after a bond: termination and the light cone

Issue #7895, PR #7896 (round 6).  A bond changes the joint selection problem of
the particles it joins.  Re-selection then runs as a cascade of improving moves.
Two generic facts, independent of the Hecke algebra:

* `exists_stable_of_potential`, `no_infinite_cascade`: if every move strictly
  lowers a natural-number potential, every cascade stops, after at most
  `E s` moves, at a stable state (no improving move leaves it).  Any strict
  order on a FINITE state space (such as lexicographic (violation, crossing
  cost) on bounded powers) is of this kind, by ranking the states.
* `light_cone`: if one synchronous round updates each particle from its
  bond-graph neighbours only, then after `t` rounds a change at a set `D` can
  only have reached particles within `t` bond steps of `D`.

Whether the joint selection rule IS local is not claimed here; that is the
probe's question (`computations/probes/chain_reaction_cascade_probe.py`).
-/

namespace QOU.Optimization.ChainReaction

section Termination

variable {S : Type*}

/-- A state is stable when no improving move leaves it. -/
def Stable (step : S → S → Prop) (s : S) : Prop := ∀ t, ¬ step s t

/-- Every state reaches a stable state by improving moves, if every move
strictly lowers a natural-number potential. -/
theorem exists_stable_of_potential (step : S → S → Prop) (E : S → ℕ)
    (hE : ∀ s t, step s t → E t < E s) (s : S) :
    ∃ t, Relation.ReflTransGen step s t ∧ Stable step t := by
  suffices H : ∀ n, ∀ s, E s = n →
      ∃ t, Relation.ReflTransGen step s t ∧ Stable step t from H _ s rfl
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro s hs
    by_cases hst : Stable step s
    · exact ⟨s, Relation.ReflTransGen.refl, hst⟩
    · simp only [Stable, not_forall, not_not] at hst
      obtain ⟨u, hu⟩ := hst
      have hlt : E u < n := by rw [← hs]; exact hE s u hu
      obtain ⟨t, hut, ht⟩ := ih (E u) hlt u rfl
      exact ⟨t, Relation.ReflTransGen.head hu hut, ht⟩

/-- Along any cascade, after `k` moves the potential has dropped by at least `k`. -/
theorem potential_drop (step : S → S → Prop) (E : S → ℕ)
    (hE : ∀ s t, step s t → E t < E s) (f : ℕ → S)
    (hf : ∀ k, step (f k) (f (k + 1))) (k : ℕ) : E (f k) + k ≤ E (f 0) := by
  induction k with
  | zero => simp
  | succ k ih => have := hE _ _ (hf k); omega

/-- No cascade of improving moves is infinite. -/
theorem no_infinite_cascade (step : S → S → Prop) (E : S → ℕ)
    (hE : ∀ s t, step s t → E t < E s) (f : ℕ → S)
    (hf : ∀ k, step (f k) (f (k + 1))) : False := by
  have := potential_drop step E hE f hf (E (f 0) + 1)
  omega

/-- A product of a start state: a stable state reachable from it by improving
moves.  Two distinct products of the same start are two outcomes of the same
reactants along different pathways (the cascade's isomers). -/
def IsProduct (step : S → S → Prop) (s t : S) : Prop :=
  Relation.ReflTransGen step s t ∧ Stable step t

/-- Every start state has at least one product. -/
theorem exists_product (step : S → S → Prop) (E : S → ℕ)
    (hE : ∀ s t, step s t → E t < E s) (s : S) : ∃ t, IsProduct step s t :=
  exists_stable_of_potential step E hE s

/-- A stable start state is its own only product: nothing moves. -/
theorem isProduct_of_stable {step : S → S → Prop} {s t : S} (hs : Stable step s)
    (h : IsProduct step s t) : t = s := by
  rcases h.1.cases_head with h' | ⟨u, hu, _⟩
  · exact h'.symm
  · exact absurd hu (hs u)

end Termination

section LightCone

variable {ι α : Type*}

/-- `Reach adj D t i`: particle `i` is joined to the set `D` by a path of
exactly `t` steps of `adj` (with `adj` reflexive this is "within `t` steps"). -/
def Reach (adj : ι → ι → Prop) (D : ι → Prop) : ℕ → ι → Prop
  | 0, i => D i
  | t + 1, i => ∃ j, adj i j ∧ Reach adj D t j

/-- The light cone.  If the synchronous update `F` reads, at particle `i`,
only the particles `adj`-joined to `i`, and two configurations differ only on
`D`, then after `t` rounds they still agree at every particle not reached from
`D` in `t` steps. -/
theorem light_cone (adj : ι → ι → Prop) (F : (ι → α) → (ι → α))
    (hloc : ∀ x y i, (∀ j, adj i j → x j = y j) → F x i = F y i)
    (D : ι → Prop) (x y : ι → α) (hxy : ∀ i, ¬ D i → x i = y i) :
    ∀ t i, ¬ Reach adj D t i → F^[t] x i = F^[t] y i := by
  intro t
  induction t with
  | zero => intro i hi; exact hxy i hi
  | succ t ih =>
    intro i hi
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
    apply hloc
    intro j hj
    apply ih
    intro hjt
    exact hi ⟨j, hj, hjt⟩

end LightCone

end QOU.Optimization.ChainReaction
