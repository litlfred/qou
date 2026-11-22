import Mathlib.Tactic
import QOU.MassTheory.OrbitCount

/-!
# The `q = 1` shadow of the atom word, and both of `ClassicalTraceFloor`'s counts

Bean `qou-tjys`. Probe: `computations/probes/atom_word_merge_count_probe.py`.
Successor to `qou-qro1` (`OrbitCount.lean`), which proved the general transposition
step; this file applies it to the specific word.

## What this closes

`ClassicalTraceFloor` states its step 2 as **two** hypotheses, both "verified for
`A = 2 … 20` directly from the words":

    hfree  : cFree = 2 * A
    hmerge : cFree = cAtom + (A - 1)

Both follow from **one** lemma here, `orbitDefect_freshProd`.

## Why the word has a permutation shadow at all

`atom_braid_word_3A` is **not a braid word**: every letter is the Hecke element
`c·σ_g + d·1`, and `2A+1` of them are *averaged*, so the object lies outside the
image of `ρ : B_n → H_n(q)` and carries no link. At `q = 1`, though, `h = q − q⁻¹`
is `0`, so **every** offset template `{0, −h, −h/2, −h(½−δ/4)}` vanishes at once and
each letter degenerates to the transposition `s_g`. The `q = 1` shadow is therefore
fixed by the `g`-index sequence alone.

## The shape, measured rather than assumed

The probe reports (`A = 2 … 20`, all `(Z,N)`, 228 pairs) that each nucleon block's
*net* shadow is a single transposition — `swap (3k) (3k+1)`, the same one for every
`k`, proton or neutron, its eleven letters collapsing to one — and that the whole
word's shadow is, in word order,

    swap 0 1,  then for k = 1 … A−1:   swap (3k−1) (3k),  swap (3k) (3k+1)

i.e. `2A − 1` transpositions. The free word drops the `swap (3k−1) (3k)` interfaces
and is the `A` disjoint blocks.

**The one property that matters is that each transposition's right endpoint is
*fresh*** — never an endpoint of any earlier letter. The right endpoints run
`1, 3, 4, 6, 7, 9, 10, …`, strictly increasing, so this is immediate. A fresh
endpoint is a **fixed point** of the partial product, and two distinct points one of
which is fixed cannot share a cycle — so `orbitDefect_swap_mul_of_not_sameCycle`
applies at every step with its hypothesis met rather than assumed.

## Scope

`Fresh`/`freshProd` and `orbitDefect_freshProd` are general: any list of
transpositions with fresh right endpoints. Nothing in them mentions nucleons, and
they are the reusable content. What is **not** in this file is a Lean definition of
`atom_braid_word_3A` itself — the shadow's index pattern is taken from the probe,
which is why the concrete corollaries below name it as their source. Formalising the
producer would be a separate and much larger undertaking.

-- Ref: [leitner2026] bean qou-tjys; computations/probes/atom_word_merge_count_probe.py
-/

namespace QOU.MassTheory

open Equiv Equiv.Perm Finset

/-- A point fixed by `σ` shares no cycle with anything but itself. This is what makes
a *fresh* endpoint hand `orbitDefect_swap_mul_of_not_sameCycle` its hypothesis.

Stated above the `variable` line: it needs neither `Fintype` nor `DecidableEq`. -/
theorem not_sameCycle_of_apply_eq {α : Type*} {σ : Perm α} {a b : α}
    (hb : σ b = b) (hab : a ≠ b) :
    ¬ σ.SameCycle a b := by
  rintro ⟨i, hi⟩
  refine hab ?_
  calc a = (σ ^ (-i)) ((σ ^ i) a) := by
            rw [← Perm.mul_apply, ← zpow_add, neg_add_cancel, zpow_zero]; rfl
    _ = (σ ^ (-i)) b := by rw [hi]
    _ = b := zpow_apply_eq_self_of_apply_eq_self hb (-i)

variable {α : Type*} [DecidableEq α]

/-- The product of a list of transpositions, the head applied **last** (leftmost).
So the list is read in *reverse* word order, and the tail is everything that came
*earlier* in the word. -/
def freshProd : List (α × α) → Perm α
  | [] => 1
  | (a, b) :: l => swap a b * freshProd l

@[simp] theorem freshProd_nil : freshProd ([] : List (α × α)) = 1 := rfl

@[simp] theorem freshProd_cons (a b : α) (l : List (α × α)) :
    freshProd ((a, b) :: l) = swap a b * freshProd l := rfl

/-- A point that is no endpoint of any pair in the list is fixed by the product. -/
theorem freshProd_apply_eq_self :
    ∀ {l : List (α × α)} {x : α}, (∀ p ∈ l, x ≠ p.1 ∧ x ≠ p.2) → freshProd l x = x
  | [], _, _ => rfl
  | (a, b) :: l, x, h => by
      obtain ⟨hxa, hxb⟩ := h (a, b) (List.mem_cons_self ..)
      rw [freshProd_cons, Perm.mul_apply,
        freshProd_apply_eq_self (fun p hp => h p (List.mem_cons_of_mem _ hp)),
        swap_apply_of_ne_of_ne hxa hxb]

/-- **Fresh chain.** Each pair's right endpoint is distinct from its own left endpoint
and from every endpoint appearing later in the list — which, by the reversed reading
of `freshProd`, means every endpoint appearing *earlier in the word*. -/
inductive Fresh : List (α × α) → Prop
  | nil : Fresh []
  | cons {a b : α} {l : List (α × α)} (hne : a ≠ b)
      (hfresh : ∀ p ∈ l, b ≠ p.1 ∧ b ≠ p.2) (hl : Fresh l) : Fresh ((a, b) :: l)

variable [Fintype α]

/-- **The one lemma both counts come from.** A fresh chain of `k` transpositions has
orbit defect exactly `k`: every letter merges, none splits.

Each step is `orbitDefect_swap_mul_of_not_sameCycle` (proved in `OrbitCount`), whose
`¬ SameCycle` hypothesis is supplied by freshness via `not_sameCycle_of_apply_eq` —
the fresh endpoint is still a fixed point of everything applied before it. -/
theorem orbitDefect_freshProd :
    ∀ {l : List (α × α)}, Fresh l → orbitDefect (freshProd l) = l.length
  | [], _ => by simp [orbitDefect_one]
  | (a, b) :: l, h => by
      cases h with
      | cons hne hfresh hl =>
          have hfix : freshProd l b = b := freshProd_apply_eq_self hfresh
          have hnc : ¬ (freshProd l).SameCycle a b :=
            not_sameCycle_of_apply_eq hfix hne
          rw [freshProd_cons, orbitDefect_swap_mul_of_not_sameCycle hne hnc,
            orbitDefect_freshProd hl]
          simp

/-- A fresh chain cannot be longer than the ground set: each letter consumes a point
that no earlier letter touched. (Recorded rather than assumed — it is what makes the
`ℕ` subtraction in `orbitCount_freshProd` honest, so it should be a consequence of
freshness, not a side hypothesis on it.) -/
theorem Fresh.length_le {l : List (α × α)} (h : Fresh l) :
    l.length ≤ Fintype.card α := by
  rw [← orbitDefect_freshProd h]
  exact orbitDefect_le_card _

/-- The orbit count of a fresh chain: every letter costs exactly one orbit.

No length bound is needed as a hypothesis — `orbitCount` is *defined* by this
subtraction, and `Fresh.length_le` shows it never truncates anyway. -/
theorem orbitCount_freshProd {l : List (α × α)} (h : Fresh l) :
    orbitCount (freshProd l) = Fintype.card α - l.length := by
  rw [orbitCount, orbitDefect_freshProd h]

/-! ### The concrete shadow, and both of `ClassicalTraceFloor`'s counts

The index patterns below are **taken from the probe**, which measures them on the
live producer; Lean does not know what `atom_braid_word_3A` returns. So what these
give is *"if the shadow is this list, then the counts are `2A` and `A+1`"* — the same
epistemic shape as `ClassicalTraceFloor`'s own hypotheses, but with **the counting
now proved instead of computed**. That is the strengthening: two numerical
hypotheses (`hfree`, `hmerge`) are replaced by one *structural* one about the word's
letters, which is far more directly checkable against the producer.

Indices are handled in `ℕ` and transported through an injection, so no `Fin`
arithmetic appears.
-/

/-- The free word's shadow as index pairs, in **reverse** word order: block `k` is
the transposition `(3k, 3k+1)`, and the blocks are pairwise disjoint.

Measured: each nucleon's eleven letters collapse to exactly this one transposition,
the same for every `k`, proton or neutron. -/
def freeIdx : ℕ → List (ℕ × ℕ)
  | 0 => []
  | A + 1 => (3 * A, 3 * A + 1) :: freeIdx A

/-- The atom word's shadow as index pairs, in **reverse** word order. In *word* order
it is `swap 0 1`, then for `k = 1 … A−1` the interface `swap (3k−1) (3k)` followed by
the block `swap (3k) (3k+1)`. -/
def atomIdx : ℕ → List (ℕ × ℕ)
  | 0 => []
  | 1 => [(0, 1)]
  | A + 2 => (3 * A + 3, 3 * A + 4) :: (3 * A + 2, 3 * A + 3) :: atomIdx (A + 1)

/-! **Transcription anchors.** `freeIdx`/`atomIdx` are my transcription of a pattern
the probe *measured* on the live producer, so a transcription slip would give true
theorems about the wrong word. These pin the transcription to the measured sequences
(in word order, i.e. reversed) and fail the build if either definition drifts. -/

example : (atomIdx 4).reverse = [(0, 1), (2, 3), (3, 4), (5, 6), (6, 7), (8, 9), (9, 10)] := rfl
example : (atomIdx 2).reverse = [(0, 1), (2, 3), (3, 4)] := rfl
example : (atomIdx 1).reverse = [(0, 1)] := rfl
example : (freeIdx 4).reverse = [(0, 1), (3, 4), (6, 7), (9, 10)] := rfl

@[simp] theorem freeIdx_length : ∀ A, (freeIdx A).length = A
  | 0 => rfl
  | A + 1 => by simp [freeIdx, freeIdx_length A]

/-- `2A − 1` letters: `A` blocks and `A − 1` interfaces. -/
@[simp] theorem atomIdx_length : ∀ A, (atomIdx (A + 1)).length = 2 * A + 1
  | 0 => rfl
  | A + 1 => by
      simp only [atomIdx, List.length_cons, atomIdx_length A]
      omega

/-- Every index used by `freeIdx A` is below `3A` — the bound that makes the next
letter's endpoint fresh. -/
theorem freeIdx_lt : ∀ {A : ℕ} {p : ℕ × ℕ}, p ∈ freeIdx A → p.1 < 3 * A ∧ p.2 < 3 * A
  | 0, _, h => by simp [freeIdx] at h
  | A + 1, p, h => by
      rcases List.mem_cons.mp h with rfl | h
      · exact ⟨by omega, by omega⟩
      · have := freeIdx_lt h; omega

theorem atomIdx_lt : ∀ {A : ℕ} {p : ℕ × ℕ}, p ∈ atomIdx A → p.1 < 3 * A ∧ p.2 < 3 * A
  | 0, _, h => by simp [atomIdx] at h
  | 1, p, h => by
      rw [atomIdx, List.mem_singleton] at h; subst h; exact ⟨by omega, by omega⟩
  | A + 2, p, h => by
      rw [atomIdx, List.mem_cons, List.mem_cons] at h
      rcases h with rfl | rfl | h
      · exact ⟨by omega, by omega⟩
      · exact ⟨by omega, by omega⟩
      · have := atomIdx_lt h; omega

variable (x : ℕ → α)

/-- Transport an index list to transpositions of `α`. -/
def toPairs (l : List (ℕ × ℕ)) : List (α × α) := l.map (fun p => (x p.1, x p.2))

omit [DecidableEq α] [Fintype α] in
@[simp] theorem toPairs_length (l : List (ℕ × ℕ)) : (toPairs x l).length = l.length := by
  simp [toPairs]

omit [DecidableEq α] [Fintype α] in
/-- **The free word's shadow is a fresh chain.** Each block's right endpoint `3k+1`
exceeds every index used by the earlier blocks. -/
theorem fresh_freeIdx {A : ℕ} (hx : ∀ i j, i < 3 * A → j < 3 * A → x i = x j → i = j) :
    Fresh (toPairs x (freeIdx A)) := by
  induction A with
  | zero => exact Fresh.nil
  | succ A ih =>
      have hx' : ∀ i j, i < 3 * A → j < 3 * A → x i = x j → i = j :=
        fun i j hi hj h => hx i j (by omega) (by omega) h
      refine Fresh.cons ?_ ?_ (ih hx')
      · exact fun h => absurd (hx _ _ (by omega) (by omega) h) (by omega)
      · rintro ⟨u, v⟩ hp
        obtain ⟨⟨i, j⟩, hmem, heq⟩ := List.mem_map.mp hp
        obtain ⟨hi, hj⟩ := freeIdx_lt hmem
        cases heq
        exact ⟨fun h => absurd (hx _ _ (by omega) (by omega) h) (by omega),
               fun h => absurd (hx _ _ (by omega) (by omega) h) (by omega)⟩

omit [DecidableEq α] [Fintype α] in
/-- **The atom word's shadow is a fresh chain.** The right endpoints run
`1, 3, 4, 6, 7, 9, 10, …`, strictly increasing, so each is fresh — which is exactly
why every interface *merges* rather than splits. -/
theorem fresh_atomIdx {A : ℕ} (hx : ∀ i j, i < 3 * A → j < 3 * A → x i = x j → i = j) :
    Fresh (toPairs x (atomIdx A)) := by
  induction A using atomIdx.induct with
  | case1 => exact Fresh.nil
  | case2 =>
      refine Fresh.cons (fun h => absurd (hx 0 1 (by omega) (by omega) h) (by omega))
        (by simp) Fresh.nil
  | case3 A ih =>
      have hx' : ∀ i j, i < 3 * (A + 1) → j < 3 * (A + 1) → x i = x j → i = j :=
        fun i j hi hj h => hx i j (by omega) (by omega) h
      have hne : ∀ u v : ℕ, u < 3 * (A + 2) → v < 3 * (A + 2) → u ≠ v → x u ≠ x v :=
        fun u v hu hv huv h => huv (hx u v hu hv h)
      have htail : ∀ (b : ℕ), b < 3 * (A + 2) →
          (∀ i, i < 3 * (A + 1) → b ≠ i) →
          ∀ p ∈ toPairs x (atomIdx (A + 1)), x b ≠ p.1 ∧ x b ≠ p.2 := by
        rintro b hb hbi ⟨u, v⟩ hp
        obtain ⟨⟨i, j⟩, hmem, heq⟩ := List.mem_map.mp hp
        obtain ⟨hi, hj⟩ := atomIdx_lt hmem
        cases heq
        exact ⟨hne _ _ hb (by omega) (hbi i hi), hne _ _ hb (by omega) (hbi j hj)⟩
      refine Fresh.cons (hne _ _ (by omega) (by omega) (by omega)) ?_
        (Fresh.cons (hne _ _ (by omega) (by omega) (by omega)) ?_ (ih hx'))
      · intro p hp
        rcases List.mem_cons.mp hp with rfl | hp
        · exact ⟨hne _ _ (by omega) (by omega) (by omega),
                 hne _ _ (by omega) (by omega) (by omega)⟩
        · exact htail (3 * A + 4) (by omega) (fun i hi => by omega) _ hp
      · exact htail (3 * A + 3) (by omega) (fun i hi => by omega)

/-- **`hfree`, PROVED from the shadow.** The free word leaves `2A` orbits on `3A`
strands: `A` disjoint blocks, each costing one. -/
theorem orbitCount_freeShadow {A : ℕ} (hcard : Fintype.card α = 3 * A)
    (hx : ∀ i j, i < 3 * A → j < 3 * A → x i = x j → i = j) :
    orbitCount (freshProd (toPairs x (freeIdx A))) = 2 * A := by
  rw [orbitCount_freshProd (fresh_freeIdx x hx), hcard, toPairs_length, freeIdx_length]
  omega

/-- **`hmerge`, PROVED from the shadow.** The atom word leaves `A + 1` orbits: the
`A − 1` interfaces each merge exactly one pair, so `2A − (A−1) = A + 1`.

This is `ClassicalTraceFloor`'s second stated hypothesis, no longer a tabulated
count. -/
theorem orbitCount_atomShadow {A : ℕ} (hcard : Fintype.card α = 3 * (A + 1))
    (hx : ∀ i j, i < 3 * (A + 1) → j < 3 * (A + 1) → x i = x j → i = j) :
    orbitCount (freshProd (toPairs x (atomIdx (A + 1)))) = A + 2 := by
  rw [orbitCount_freshProd (fresh_atomIdx x hx), hcard, toPairs_length, atomIdx_length]
  omega

end QOU.MassTheory
