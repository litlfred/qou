import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Data.Finset.Prod

/-!
# QOU.MathlibExt.SignProdComm — the signature of the coordinate swap on `ι × ι`

Bean `qou-kwoa`.  `QOU.Hecke.TwBasis.twGram_det_eq_sq_mul_prod` states the Gram determinant
of the `T_w` basis as a square times `∏_λ sign(prodComm) · d_λ^(d_λ²)`, leaving the sign as
the abstract `Equiv.Perm.sign (Equiv.prodComm ι ι)`.  This evaluates it:

    sign (prodComm ι ι) = (-1) ^ (d * (d - 1) / 2),    d = card ι

so the per-block sign of that determinant is explicit rather than a black box.

## The argument, and the step that is easy to miss

`prodComm` is an involution, so its cycle type is a multiset of `2`s.
`Equiv.Perm.sign_of_cycleType` gives `sign = (-1) ^ (cycleType.sum + card cycleType)`, and for
an involution with support of size `s` that is `(-1) ^ (s + s / 2)`.  The support here is the
**off-diagonal** — `prodComm` fixes exactly the pairs `(a, a)` — so `s = d² - d = d(d-1)`.

That `s` is **even**, being a product of consecutive integers, is doing real work: it is what
kills the first summand and collapses `(-1)^(s + s/2)` to `(-1)^(s/2)`.  Without it the
formula does not simplify to the half-count alone.

## A Lean note worth keeping

Writing `(Equiv.prodComm ι ι : Equiv.Perm (ι × ι)).support` does **not** work: the ascription
is unfolded before dot-notation is resolved, so Lean looks for `Equiv.support` and fails.
Hence the named `prodSwap` below — its declared type has head constant `Equiv.Perm`, so
`.support`, `.cycleType` and `.sign` resolve.  `prodSwap_eq` transfers the result back.

## Cross-check against measurement

`computations/hecke/tw_gram_square_class_crosscheck.py` uses exactly this formula to predict
the sign of `det(twGram)`, and it matches the determinants `tw_gram_determinant_probe.py`
measured at `n = 1, 2, 3`: block dimensions `(1,1)`, `(1,2,1)` and `(1,3,2,3,1)` give `+1`,
`-1`, `-1` against measured `+`, `-`, `-`.  The Lean here and that measurement are
independent.
-/

namespace QOU.MathlibExt

open Equiv Finset

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **The coordinate swap on `ι × ι`, as a permutation.**

Definitionally `Equiv.prodComm ι ι`; the point of the wrapper is that its declared type has
head constant `Equiv.Perm`, so `Equiv.Perm` dot-notation resolves against it. -/
def prodSwap (ι : Type*) : Equiv.Perm (ι × ι) := Equiv.prodComm ι ι

omit [Fintype ι] [DecidableEq ι] in
@[simp] theorem prodSwap_apply (p : ι × ι) : prodSwap ι p = (p.2, p.1) := rfl

omit [Fintype ι] [DecidableEq ι] in
/-- **Swapping coordinates twice is the identity.** -/
theorem prodSwap_sq : (prodSwap ι) ^ 2 = 1 := by
  rw [pow_two]
  exact Equiv.ext fun p => rfl

/-- **The coordinate swap moves exactly the off-diagonal.**

Its fixed points are the pairs `(a, a)`, so the support is `univ.offDiag`. -/
theorem support_prodSwap : (prodSwap ι).support = Finset.univ.offDiag := by
  ext p
  obtain ⟨a, b⟩ := p
  simp only [Equiv.Perm.mem_support, prodSwap_apply, Finset.mem_offDiag, Finset.mem_univ,
    true_and, ne_eq, Prod.mk.injEq, not_and]
  constructor
  · intro h hab
    exact h (hab.symm) hab
  · intro h hba _
    exact h hba.symm

/-- **`d² - d` moved points.** -/
theorem card_support_prodSwap :
    #(prodSwap ι).support = Fintype.card ι * Fintype.card ι - Fintype.card ι := by
  rw [support_prodSwap, Finset.offDiag_card, Finset.card_univ]

/-- **Every cycle of the coordinate swap has length exactly 2.**

Upper bound from the involution, lower bound because a cycle has length at least 2. -/
theorem mem_cycleType_prodSwap {n : ℕ} (hn : n ∈ (prodSwap ι).cycleType) : n = 2 :=
  le_antisymm
    (Nat.le_of_dvd zero_lt_two
      ((Equiv.Perm.dvd_of_mem_cycleType hn).trans
        (orderOf_dvd_of_pow_eq_one (prodSwap_sq (ι := ι)))))
    (Equiv.Perm.two_le_of_mem_cycleType hn)

/-- **Half as many cycles as moved points.** -/
theorem card_cycleType_prodSwap :
    2 * Multiset.card (prodSwap ι).cycleType = #(prodSwap ι).support := by
  rw [← Equiv.Perm.sum_cycleType,
    Multiset.eq_replicate_card.mpr fun n hn => mem_cycleType_prodSwap hn,
    Multiset.sum_replicate, Multiset.card_replicate, smul_eq_mul, mul_comm]

/-- **The signature of the coordinate swap on `ι × ι` is `(-1)^(d(d-1)/2)`.** -/
theorem sign_prodSwap :
    Equiv.Perm.sign (prodSwap ι)
      = (-1) ^ (Fintype.card ι * (Fintype.card ι - 1) / 2) := by
  have hsupp : #(prodSwap ι).support = Fintype.card ι * (Fintype.card ι - 1) := by
    rw [card_support_prodSwap, Nat.mul_sub_one]
  have hsum : (prodSwap ι).cycleType.sum = Fintype.card ι * (Fintype.card ι - 1) := by
    rw [Equiv.Perm.sum_cycleType, hsupp]
  have hcard : 2 * Multiset.card (prodSwap ι).cycleType
      = Fintype.card ι * (Fintype.card ι - 1) := by
    rw [card_cycleType_prodSwap, hsupp]
  obtain ⟨k, hk⟩ : 2 ∣ Fintype.card ι * (Fintype.card ι - 1) := ⟨_, hcard.symm⟩
  have hck : Multiset.card (prodSwap ι).cycleType = k := by omega
  rw [Equiv.Perm.sign_of_cycleType, hsum, hck, hk, Nat.mul_div_cancel_left k zero_lt_two,
    show 2 * k + k = k + 2 * k from by ring, pow_add, pow_mul]
  simp

/-- **The same statement for `Equiv.prodComm`**, which is what
`twGram_det_eq_sq_mul_prod` actually mentions. -/
theorem sign_prodComm :
    Equiv.Perm.sign (Equiv.prodComm ι ι : Equiv.Perm (ι × ι))
      = (-1) ^ (Fintype.card ι * (Fintype.card ι - 1) / 2) :=
  sign_prodSwap

/-! ### Concrete checks

`decide` evaluates the signature by brute force, without going through the cycle-type
argument above.  `d = 1` gives `1`; `d = 2` and `d = 3` both give `-1`, matching
`(-1)^(d(d-1)/2)` at `(-1)^0`, `(-1)^1` and `(-1)^3`.  These are genuinely decidable finite
computations, not a `native_decide` escape. -/

example : Equiv.Perm.sign (prodSwap (Fin 1)) = 1 := by decide

example : Equiv.Perm.sign (prodSwap (Fin 2)) = -1 := by decide

example : Equiv.Perm.sign (prodSwap (Fin 3)) = -1 := by decide

end QOU.MathlibExt
