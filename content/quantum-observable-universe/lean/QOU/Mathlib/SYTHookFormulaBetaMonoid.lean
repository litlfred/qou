import QOU.Mathlib.SYTHookFormulaBeta

/-!
# QOU.Mathlib.SYTHookFormulaBetaMonoid — the per-row FRT identity in any commutative monoid

`SYTHookFormulaBeta` proves the divisor-free per-row Frame–Robinson–Thrall identity over `ℕ`:

`rowHookProd a t · betaGapProd a t = (a + |t|)!`.

Read the proof and the arithmetic turns out to be **incidental**.  Every step is a reindexing of the
*multiset of hook lengths* against the multiset `{1, …, a + |t|}`; the only genuinely numerical moves
are `omega` facts about the **arguments**, never about the values.  So the identity holds with `ℕ`
multiplication replaced by any commutative monoid and each factor `n` replaced by `f n`.

| | |
|---|---|
| `rowHookProdF f a t` | `∏_{j<a} f((a−j) + cnt t j)` — the row's hook lengths, pushed through `f` |
| `betaGapProdF f a t` | the β-gap product, pushed through `f` |
| `descFactF f n` | `f(n)·f(n−1)⋯f(1)`, the `f`-analogue of `n!` |
| `rowHookProdF_mul_betaGapProdF` | `rowHookProdF f a t · betaGapProdF f a t = descFactF f (a + |t|)` |

**Why this generality is the point.** At `f = id` over `(ℕ, ×)` it is the corpus statement
(`rowHookProdF_id`, proved below, so the generalisation is checked against its own special case
rather than merely asserted to contain it).  At `f n = 1 − Q^n` over a field it is the **q-analogue**
— the per-row half of the hook-length identity that general-`r` branching needs, relating
`∏_c (1 − Q^{h(c)})` to the shifted parts `β_i`.  See bean `qou-j7ln` and
`QOU.Mathlib.LagrangeCoeffSum.sum_eq_bracket_mul_of_qratio_scaling`, which is waiting on exactly
that.

## Base ring (§7c)

Generic `[CommMonoid M]`.  Nothing archimedean, no ordering, no ring — the arguments stay in `ℕ`.

LaTeX label: `lem:frt-per-row-monoid`
-/

namespace QOU.Mathlib.SYTBeta

variable {M : Type*} [CommMonoid M]

/-- `SYTHookFormulaBeta.list_range_map_prod` is `ℕ`-specific; this is the same bridge in any
commutative monoid. -/
theorem list_range_map_prod' (n : ℕ) (f : ℕ → M) :
    ((List.range n).map f).prod = ∏ j ∈ Finset.range n, f j := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.prod_append, ih, Finset.prod_range_succ]
    simp

/-- The row's hook lengths pushed through `f`: `∏_{j<a} f((a−j) + cnt t j)`. -/
def rowHookProdF (f : ℕ → M) (a : ℕ) (t : List ℕ) : M :=
  ∏ j ∈ Finset.range a, f ((a - j) + cnt t j)

/-- The β-gap product pushed through `f`. -/
def betaGapProdF (f : ℕ → M) : ℕ → List ℕ → M
  | _, [] => 1
  | a, c :: r => f (a + 1 - c) * betaGapProdF f (a + 1) r

/-- `f(n)·f(n−1)⋯f(1)` — the `f`-analogue of `n!`. -/
def descFactF (f : ℕ → M) (n : ℕ) : M := ∏ j ∈ Finset.range n, f (n - j)

@[simp] theorem betaGapProdF_nil (f : ℕ → M) (a : ℕ) : betaGapProdF f a [] = 1 := rfl

theorem betaGapProdF_cons (f : ℕ → M) (a c : ℕ) (r : List ℕ) :
    betaGapProdF f a (c :: r) = f (a + 1 - c) * betaGapProdF f (a + 1) r := rfl

theorem rowHookProdF_nil (f : ℕ → M) (a : ℕ) : rowHookProdF f a [] = descFactF f a := by
  simp [rowHookProdF, descFactF]

/-- **The inductive step, in any commutative monoid.**

`rowHookProdF f a (c :: r) · f(a + 1 − c) = rowHookProdF f (a+1) r`.

Same reindexing as the `ℕ` proof: the prefix `j < c` matches the `(a+1)`-row factor at `j`, the tail
`c ≤ j < a` matches it at `j+1`, and the β-gap `f(a + 1 − c)` supplies the missing middle factor at
`j = c`.  Every `omega` below is about the `ℕ` **argument** of `f`, never about a value in `M` — which
is exactly why the arithmetic of the original proof was incidental. -/
theorem rowHookProdF_cons_mul (f : ℕ → M) (a c : ℕ) (r : List ℕ) (hca : c ≤ a)
    (hr : ∀ p ∈ r, p ≤ c) :
    rowHookProdF f a (c :: r) * f (a + 1 - c) = rowHookProdF f (a + 1) r := by
  have hcnt0 : ∀ j, c ≤ j → cnt r j = 0 := fun j hj =>
    cnt_eq_zero_of_le r j (fun p hp => le_trans (hr p hp) hj)
  have hLfac : ∀ j, ((a - j) + cnt (c :: r) j)
      = (a - j) + (if j < c then 1 else 0) + cnt r j := by
    intro j; rw [cnt_cons]; ring
  unfold rowHookProdF
  simp_rw [hLfac]
  have hsplit : Finset.range a = Finset.range c ∪ Finset.Ico c a := by
    rw [Finset.range_eq_Ico, Finset.Ico_union_Ico_eq_Ico (Nat.zero_le c) hca]
  have hdisj : Disjoint (Finset.range c) (Finset.Ico c a) := by
    rw [Finset.range_eq_Ico]; exact Finset.Ico_disjoint_Ico_consecutive 0 c a
  rw [hsplit, Finset.prod_union hdisj]
  have hpre : ∏ j ∈ Finset.range c, f ((a - j) + (if j < c then 1 else 0) + cnt r j)
      = ∏ j ∈ Finset.range c, f ((a + 1 - j) + cnt r j) := by
    refine Finset.prod_congr rfl fun j hj => ?_
    rw [Finset.mem_range] at hj
    simp only [hj, if_true]
    congr 1
    omega
  have htail : ∏ j ∈ Finset.Ico c a, f ((a - j) + (if j < c then 1 else 0) + cnt r j)
      = ∏ j ∈ Finset.Ico c a, f ((a + 1 - (j + 1)) + cnt r (j + 1)) := by
    refine Finset.prod_congr rfl fun j hj => ?_
    rw [Finset.mem_Ico] at hj
    have hnj : ¬ j < c := by omega
    have e1 : cnt r j = 0 := hcnt0 j hj.1
    have e2 : cnt r (j + 1) = 0 := hcnt0 (j + 1) (by omega)
    simp only [hnj, if_false, e1, e2, Nat.add_zero]
    congr 1
    omega
  rw [hpre, htail]
  have hreindex : ∏ j ∈ Finset.Ico c a, f ((a + 1 - (j + 1)) + cnt r (j + 1))
      = ∏ j ∈ Finset.Ico (c + 1) (a + 1), f ((a + 1 - j) + cnt r j) := by
    rw [Finset.prod_Ico_eq_prod_range, Finset.prod_Ico_eq_prod_range]
    refine Finset.prod_congr (by congr 1; omega) fun j _ => ?_
    rw [show c + j + 1 = c + 1 + j from by omega]
  rw [hreindex]
  have hgc : f ((a + 1 - c) + cnt r c) = f (a + 1 - c) := by
    rw [hcnt0 c (le_refl c), Nat.add_zero]
  have hsplit2 : ∏ j ∈ Finset.range (a + 1), f ((a + 1 - j) + cnt r j)
      = (∏ j ∈ Finset.range (c + 1), f ((a + 1 - j) + cnt r j))
        * ∏ j ∈ Finset.Ico (c + 1) (a + 1), f ((a + 1 - j) + cnt r j) := by
    have hu : Finset.range (a + 1) = Finset.range (c + 1) ∪ Finset.Ico (c + 1) (a + 1) := by
      ext x
      simp only [Finset.mem_range, Finset.mem_union, Finset.mem_Ico]
      omega
    have hdj : Disjoint (Finset.range (c + 1)) (Finset.Ico (c + 1) (a + 1)) := by
      rw [Finset.range_eq_Ico]
      exact Finset.Ico_disjoint_Ico_consecutive 0 (c + 1) (a + 1)
    rw [hu, Finset.prod_union hdj]
  rw [hsplit2, Finset.prod_range_succ, hgc]
  exact mul_right_comm _ _ _

/-- **The per-row Frame–Robinson–Thrall identity, in any commutative monoid.**

For a weakly-decreasing tail `t` with every part `≤ a`,

`rowHookProdF f a t · betaGapProdF f a t = descFactF f (a + |t|)`.

At `f = id` over `(ℕ, ×)` this is `SYTBeta.rowHookProd_mul_betaGapProd`; at `f n = 1 − Q^n` over a
field it is the q-analogue. -/
theorem rowHookProdF_mul_betaGapProdF (f : ℕ → M) (a : ℕ) (t : List ℕ)
    (ht : List.Sorted (· ≥ ·) t) (hta : ∀ p ∈ t, p ≤ a) :
    rowHookProdF f a t * betaGapProdF f a t = descFactF f (a + t.length) := by
  induction t generalizing a with
  | nil => simp [rowHookProdF_nil]
  | cons c r ih =>
    obtain ⟨hcr, hr⟩ := List.sorted_cons.mp ht
    have hca : c ≤ a := hta c (List.mem_cons_self ..)
    have hrc : ∀ p ∈ r, p ≤ c := fun p hp => hcr p hp
    have hra : ∀ p ∈ r, p ≤ a + 1 := fun p hp => le_trans (hrc p hp) (by omega)
    rw [betaGapProdF_cons, ← mul_assoc, rowHookProdF_cons_mul f a c r hca hrc,
      ih (a + 1) hr hra, List.length_cons,
      show a + 1 + r.length = a + (r.length + 1) from by omega]

/-! ## The content side

The hook side above is the *denominator* of the level-`r` principal specialisation.  Its *numerator*
`∏_c f(r + content c)` splits row by row into a contiguous block `f(b), f(b+1), …, f(b+m−1)`, and
such a block is a ratio of two `descFactF`s.  This section proves that, division-free. -/

theorem descFactF_succ (f : ℕ → M) (n : ℕ) : descFactF f (n + 1) = f (n + 1) * descFactF f n := by
  unfold descFactF
  rw [Finset.prod_range_succ']
  simp only [Nat.sub_zero, mul_comm]
  congr 1
  refine Finset.prod_congr rfl fun k _ => ?_
  congr 1
  omega

/-- **A contiguous block of `f`-factors is a ratio of `descFactF`s**, division-free:

`f(b)·f(b+1)⋯f(b+m−1) · descFactF f (b−1) = descFactF f (b+m−1)`.

Row `i` of the level-`r` numerator is exactly such a block: its cells have content `j − i` for
`j < μ_i`, so its factors are `f(r − i + j)`, a block starting at `b = r − i` of length `m = μ_i`.
The top index `b + m − 1 = μ_i + r − 1 − i` **is** the β-number `β_i`, which is why the
`∏_i descFactF f β_i` produced here cancels against the one the hook side produces. -/
theorem prod_block_mul_descFactF (f : ℕ → M) (b m : ℕ) (hb : 1 ≤ b) :
    (∏ j ∈ Finset.range m, f (b + j)) * descFactF f (b - 1) = descFactF f (b + m - 1) := by
  induction m with
  | zero => simp
  | succ k ih =>
    have hbk : b + (k + 1) - 1 = (b + k - 1) + 1 := by omega
    have harg : (b + k - 1) + 1 = b + k := by omega
    rw [Finset.prod_range_succ, mul_right_comm, ih, hbk, descFactF_succ, harg]
    exact mul_comm _ _

/-- The content side at `f n = 1 − Qⁿ`: row `i`'s numerator block, cleared of division. -/
theorem prod_block_one_sub_pow {R : Type*} [CommRing R] (Q : R) (b m : ℕ) (hb : 1 ≤ b) :
    (∏ j ∈ Finset.range m, (1 - Q ^ (b + j))) * descFactF (fun n => 1 - Q ^ n) (b - 1)
      = descFactF (fun n => 1 - Q ^ n) (b + m - 1) :=
  prod_block_mul_descFactF (fun n => 1 - Q ^ n) b m hb

/-! ## Conservativity: at `f = id` over `(ℕ, ×)` this is the corpus statement -/

theorem rowHookProdF_id (a : ℕ) (t : List ℕ) : rowHookProdF (M := ℕ) id a t = rowHookProd a t := by
  rw [rowHookProd_eq_finset]
  rfl

theorem descFactF_id (n : ℕ) : descFactF (M := ℕ) id n = Nat.factorial n := by
  have h := rowHookProdF_nil (M := ℕ) id n
  rw [rowHookProdF_id] at h
  rw [← h, rowHookProd_nil]

theorem betaGapProdF_id (a : ℕ) (t : List ℕ) :
    betaGapProdF (M := ℕ) id a t = betaGapProd a t := by
  induction t generalizing a with
  | nil => rfl
  | cons c r ih => rw [betaGapProdF_cons, betaGapProd_cons, ih]; rfl

/-! ## The q-analogue, spelled out

The instance `f n = 1 − Qⁿ`, which is what general-`r` branching needs. -/

/-- **The per-row hook identity, q-analogue.**

`∏_{j<a} (1 − Q^{h(j)}) · ∏ (β-gaps as `1 − Q^{gap}`) = ∏_{k=1}^{a+|t|} (1 − Q^k)`,

where `h(j) = (a − j) + cnt t j` runs over the hook lengths of the row.  This is
`rowHookProdF_mul_betaGapProdF` at `f n = 1 − Qⁿ`; it needs no separate proof because the original
argument never touched the values, only the exponents.

This is the per-row half of the hook-length input that
`QOU.Mathlib.LagrangeCoeffSum.sum_eq_bracket_mul_of_qratio_scaling` is waiting on.  What remains is
to assemble the rows (`SYTHookFormulaBetaProd.prodHooks_eq_prod_rowHookProd`, likewise arithmetic-free
in shape) and to recognise the assembled β-gap product as the Vandermonde denominator. -/
theorem rowHookProdF_one_sub_pow {R : Type*} [CommRing R] (Q : R) (a : ℕ) (t : List ℕ)
    (ht : List.Sorted (· ≥ ·) t) (hta : ∀ p ∈ t, p ≤ a) :
    (∏ j ∈ Finset.range a, (1 - Q ^ ((a - j) + cnt t j)))
        * betaGapProdF (fun n => 1 - Q ^ n) a t
      = ∏ j ∈ Finset.range (a + t.length), (1 - Q ^ ((a + t.length) - j)) :=
  rowHookProdF_mul_betaGapProdF (fun n => 1 - Q ^ n) a t ht hta

end QOU.Mathlib.SYTBeta
