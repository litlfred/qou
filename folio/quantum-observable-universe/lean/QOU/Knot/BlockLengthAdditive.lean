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

/-! ## A blocks, not two

`length_mul` is the two-block statement and carries the content. The atomic
braid has `A` nucleon blocks, so the composition law needs the `A`-fold form.
I previously declined this as "index plumbing that adds no insight" — the
insight claim was right, the declining was not: two is not `A`, and
`gf_pow`'s `A`-fold factorisation has nothing to stand on without it. -/

/-- The identity has no inversions. -/
theorem length_one : length (1 : Equiv.Perm (Fin m)) = 0 := by
  rw [length, Finset.card_eq_zero]
  ext p
  simp only [invSet, Finset.mem_filter, Finset.mem_univ, true_and,
    Finset.notMem_empty, iff_false, not_and, Equiv.Perm.one_apply, not_lt]
  exact fun h => le_of_lt h

/-- Lower-only is closed under multiplication. -/
theorem lowerOnly_mul {u v : Equiv.Perm (Fin m)} (hu : LowerOnly k u)
    (hv : LowerOnly k v) : LowerOnly k (u * v) := by
  intro x hx
  rw [Equiv.Perm.mul_apply, hv x hx, hu x hx]

/-- Lower-only at a threshold is lower-only at any larger one. -/
theorem lowerOnly_mono {u : Equiv.Perm (Fin m)} {k k' : ℕ} (h : LowerOnly k u)
    (hk : k ≤ k') : LowerOnly k' u :=
  fun x hx => h x (le_trans hk hx)

/-- The identity is lower-only at every threshold. -/
theorem lowerOnly_one : LowerOnly k (1 : Equiv.Perm (Fin m)) := fun _ _ => rfl

/-- The product of the first `n` blocks, in order. -/
def blockProd (w : ℕ → Equiv.Perm (Fin m)) : ℕ → Equiv.Perm (Fin m)
  | 0 => 1
  | (n + 1) => blockProd w n * w n

/-- The first `n` blocks together move nothing at or above the `n`-th split. -/
theorem lowerOnly_blockProd {b : ℕ → ℕ} (hb : Monotone b)
    {w : ℕ → Equiv.Perm (Fin m)} (hlow : ∀ i, LowerOnly (b (i + 1)) (w i)) :
    ∀ n, LowerOnly (b n) (blockProd w n)
  | 0 => lowerOnly_one
  | (n + 1) => by
      exact lowerOnly_mul
        (lowerOnly_mono (lowerOnly_blockProd hb hlow n) (hb (Nat.le_succ n)))
        (hlow n)

/-- **Length is additive across `A` order-separated blocks.** Block `i` occupies
`[b i, b (i+1))`; the Coxeter length of the whole is the sum of the blocks'.

This is what `BodyOrderExpansion.gf_pow` needs in order to apply to the atomic
braid: it makes the filtration's index set an honest `A`-fold product, not a
two-fold one. -/
theorem length_blockProd {b : ℕ → ℕ} (hb : Monotone b)
    {w : ℕ → Equiv.Perm (Fin m)} (hlow : ∀ i, LowerOnly (b (i + 1)) (w i))
    (hup : ∀ i, UpperOnly (b i) (w i)) :
    ∀ A, length (blockProd w A) = ∑ i ∈ Finset.range A, length (w i)
  | 0 => by simp [blockProd, length_one]
  | (n + 1) => by
      rw [blockProd, length_mul (lowerOnly_blockProd hb hlow n) (hup n),
        length_blockProd hb hlow hup n, Finset.sum_range_succ]

/-! ## The hypotheses are exactly "each block acts inside its own block"

`length_blockProd` takes `hlow` and `hup` separately, which leaves open whether
anything satisfies both at once. It does, and the condition is the natural one:
a permutation supported in the half-open interval `[a, b)` is lower-only at `b`
and upper-only at `a` simultaneously.

Stating this matters for the same reason the Hecke-relation instantiation did.
A theorem whose hypotheses no interesting family satisfies proves nothing about
the object it names, and the two-sided form is what a nucleon block actually
is: block `i` moves strands `3i, 3i+1, 3i+2` and nothing else. -/

/-- `w` moves only points in the half-open interval `[a, b)`. -/
def SupportedIn (a b : ℕ) (w : Equiv.Perm (Fin m)) : Prop :=
  ∀ x : Fin m, x.val < a ∨ b ≤ x.val → w x = x

theorem lowerOnly_of_supportedIn {a b : ℕ} {w : Equiv.Perm (Fin m)}
    (h : SupportedIn a b w) : LowerOnly b w :=
  fun x hx => h x (Or.inr hx)

theorem upperOnly_of_supportedIn {a b : ℕ} {w : Equiv.Perm (Fin m)}
    (h : SupportedIn a b w) : UpperOnly a w :=
  fun x hx => h x (Or.inl hx)

/-- **Length is additive over any family of block-supported permutations.**
This is `length_blockProd` with its two hypotheses replaced by the single
condition that each `w i` acts inside its own block — the form a nucleon
decomposition actually supplies. -/
theorem length_blockProd_of_supportedIn {b : ℕ → ℕ} (hb : Monotone b)
    {w : ℕ → Equiv.Perm (Fin m)} (hs : ∀ i, SupportedIn (b i) (b (i + 1)) (w i)) :
    ∀ A, length (blockProd w A) = ∑ i ∈ Finset.range A, length (w i) :=
  length_blockProd hb (fun i => lowerOnly_of_supportedIn (hs i))
    (fun i => upperOnly_of_supportedIn (hs i))

/-- The condition is satisfiable non-trivially: a permutation fixing everything
outside `[a, b)` is block-supported there, and the identity is the degenerate
case rather than the only one. -/
theorem supportedIn_one {a b : ℕ} : SupportedIn a b (1 : Equiv.Perm (Fin m)) :=
  fun _ _ => rfl

/-- For two permutations supported in separated intervals `[a₁, b₁)` and `[a₂, b₂)`
with `b₁ ≤ a₂`, the length of their product is the sum of their lengths. -/
theorem length_mul_of_supportedIn {a₁ b₁ a₂ b₂ : ℕ} {u v : Equiv.Perm (Fin m)}
    (hu : SupportedIn a₁ b₁ u) (hv : SupportedIn a₂ b₂ v) (hsep : b₁ ≤ a₂) :
    length (u * v) = length u + length v := by
  have hu_low : LowerOnly a₂ u :=
    lowerOnly_mono (lowerOnly_of_supportedIn hu) hsep
  have hv_up : UpperOnly a₂ v :=
    upperOnly_of_supportedIn hv
  exact length_mul hu_low hv_up

end QOU.Knot.BlockLengthAdditive
