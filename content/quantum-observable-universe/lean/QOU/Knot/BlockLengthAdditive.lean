/-
# Coxeter length is additive across an order-separated block split

`BodyOrderExpansion.gf_pow` shows a generating function over a product index
set factorises as `G_1(x)^A` -- the bookkeeping half of the block
factorisation. Applying it to the atomic braid needs the *content* half: that
the filtration grade on `H_{3A}` really is additive across the nucleon blocks,
so that the index set is a product in the first place.

That is this file. For permutations acting on complementary, order-separated
parts of `Fin m`,

    ℓ(u · v) = ℓ(u) + ℓ(v).

## Order-separation is not decoration

Disjoint support alone is **not** enough. On `Fin 4`, `u = swap 0 2` and
`v = swap 1 3` have disjoint supports, and `ℓ(u) = 3`, so no additivity
statement of that shape can hold. What makes the blocks add is that every point
`u` moves lies strictly below every point `v` moves — which is exactly the
nucleon layout, block `i` occupying strands `3i, 3i+1, 3i+2`.

## The mechanism

Three kinds of pair, and the mixed kind is where the content sits:

* both below `k` — `v` fixes them, so the pair inverts under `u·v` exactly when
  it inverts under `u`;
* both at or above `k` — `u` fixes them, likewise for `v`;
* **straddling** — `u·v` sends the lower point below `k` and the upper point to
  at least `k`, so a straddling pair can never invert. This is what
  order-separation buys, and it is why interleaved supports fail.

So the inversion set of the product is the *disjoint* union of the two
inversion sets, and the count adds.

-- Ref: [bjorner-brenti2005] https://doi.org/10.1007/3-540-27596-7
-/
import QOU.Knot.JetGradePromotion
import QOU.Knot.JetGradeLengthShift

namespace QOU.Knot.BlockLengthAdditive

open QOU.Knot.JetGradePromotion

variable {m k : ℕ}

/-- `u` moves only points strictly below `k`. -/
def LowerOnly (k : ℕ) (u : Equiv.Perm (Fin m)) : Prop :=
  ∀ x : Fin m, k ≤ x.val → u x = x

/-- `v` moves only points at or above `k`. -/
def UpperOnly (k : ℕ) (v : Equiv.Perm (Fin m)) : Prop :=
  ∀ x : Fin m, x.val < k → v x = x

/-- A lower-only permutation keeps the lower part lower — by injectivity, since
it already fixes everything upper. -/
theorem lower_maps_lower {u : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    {x : Fin m} (hx : x.val < k) : (u x).val < k := by
  by_contra h
  push_neg at h
  have h1 : u (u x) = u x := hu (u x) h
  have h2 : u x = x := u.injective h1
  rw [h2] at h
  omega

/-- An upper-only permutation keeps the upper part upper. -/
theorem upper_maps_upper {v : Equiv.Perm (Fin m)} (hv : UpperOnly k v)
    {x : Fin m} (hx : k ≤ x.val) : k ≤ (v x).val := by
  by_contra h
  push_neg at h
  have h1 : v (v x) = v x := hv (v x) h
  have h2 : v x = x := v.injective h1
  rw [h2] at h
  omega

/-- Every inversion of a lower-only permutation has both coordinates below `k`. -/
theorem invSet_lower {u : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    {p : Fin m × Fin m} (hp : p ∈ invSet u) : p.1.val < k ∧ p.2.val < k := by
  rw [JetGradeLengthShift.mem_invSet] at hp
  obtain ⟨hlt, hinv⟩ := hp
  rw [Fin.lt_def] at hlt hinv
  by_cases hb : p.2.val < k
  · exact ⟨by omega, hb⟩
  · push_neg at hb
    rw [hu p.2 hb] at hinv
    by_cases ha : p.1.val < k
    · have hmap := lower_maps_lower hu ha
      omega
    · push_neg at ha
      rw [hu p.1 ha] at hinv
      omega

/-- Every inversion of an upper-only permutation has both coordinates at or
above `k`. -/
theorem invSet_upper {v : Equiv.Perm (Fin m)} (hv : UpperOnly k v)
    {p : Fin m × Fin m} (hp : p ∈ invSet v) : k ≤ p.1.val ∧ k ≤ p.2.val := by
  rw [JetGradeLengthShift.mem_invSet] at hp
  obtain ⟨hlt, hinv⟩ := hp
  rw [Fin.lt_def] at hlt hinv
  by_cases ha : k ≤ p.1.val
  · exact ⟨ha, by omega⟩
  · push_neg at ha
    rw [hv p.1 ha] at hinv
    by_cases hb : k ≤ p.2.val
    · have hmap := upper_maps_upper hv hb
      omega
    · push_neg at hb
      rw [hv p.2 hb] at hinv
      omega

/-- Below the split, the product acts as `u` — `v` fixes that part. -/
theorem mul_apply_lower {u v : Equiv.Perm (Fin m)} (hv : UpperOnly k v)
    {x : Fin m} (hx : x.val < k) : (u * v) x = u x := by
  rw [Equiv.Perm.mul_apply, hv x hx]

/-- At or above the split, the product acts as `v` — `u` fixes where `v` lands. -/
theorem mul_apply_upper {u v : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    (hv : UpperOnly k v) {x : Fin m} (hx : k ≤ x.val) : (u * v) x = v x := by
  rw [Equiv.Perm.mul_apply, hu (v x) (upper_maps_upper hv hx)]

/-- **The inversion sets add.** Every inversion of the product is an inversion
of exactly one factor, and a straddling pair is never an inversion at all. -/
theorem invSet_mul {u v : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    (hv : UpperOnly k v) : invSet (u * v) = invSet u ∪ invSet v := by
  ext p
  obtain ⟨a, b⟩ := p
  simp only [Finset.mem_union, JetGradeLengthShift.mem_invSet]
  by_cases ha : a.val < k
  · by_cases hb : b.val < k
    · rw [mul_apply_lower hv ha, mul_apply_lower hv hb]
      have e1 : v a = a := hv a ha
      have e2 : v b = b := hv b hb
      rw [e1, e2]
      simp only [Fin.lt_def]
      omega
    · push_neg at hb
      rw [mul_apply_lower hv ha, mul_apply_upper hu hv hb]
      have e1 : v a = a := hv a ha
      have e2 : u b = b := hu b hb
      have f1 : (u a).val < k := lower_maps_lower hu ha
      have f2 : k ≤ (v b).val := upper_maps_upper hv hb
      rw [e1, e2]
      simp only [Fin.lt_def]
      omega
  · push_neg at ha
    by_cases hb : k ≤ b.val
    · rw [mul_apply_upper hu hv ha, mul_apply_upper hu hv hb]
      have e1 : u a = a := hu a ha
      have e2 : u b = b := hu b hb
      rw [e1, e2]
      simp only [Fin.lt_def]
      omega
    · push_neg at hb
      simp only [Fin.lt_def]
      omega

/-- The two inversion sets are disjoint: one lives strictly below the split,
the other at or above it. -/
theorem invSet_disjoint {u v : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    (hv : UpperOnly k v) : Disjoint (invSet u) (invSet v) := by
  rw [Finset.disjoint_left]
  intro p hpu hpv
  have h1 := invSet_lower hu hpu
  have h2 := invSet_upper hv hpv
  omega

/-- **Coxeter length is additive across an order-separated block split.**

This is the content half of the block factorisation: it is what makes the
index set of the filtration a product, and hence what lets
`BodyOrderExpansion.gf_pow` apply to the atomic braid rather than to an
abstract product. -/
theorem length_mul {u v : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    (hv : UpperOnly k v) : length (u * v) = length u + length v := by
  rw [length, length, length, invSet_mul hu hv,
    Finset.card_union_of_disjoint (invSet_disjoint hu hv)]

end QOU.Knot.BlockLengthAdditive
