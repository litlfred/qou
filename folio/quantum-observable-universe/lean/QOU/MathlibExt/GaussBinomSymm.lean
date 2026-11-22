import QOU.QBeta.HabiroTailStar

/-!
# Gaussian binomials: symmetry and the classical limit

The Gaussian binomial `[n,k]_q` already exists in the tree, with both Pascal rules
(`QOU.QBeta.HabiroTailStar.gaussBinom`, `gaussBinom_succ_succ`, `gaussBinom_succ_succ'`,
`gaussBinom_eq_zero_of_lt`, `gaussBinom_self`), over any commutative ring. This file adds the two
identities bean `qou-kbjc` asks for that are not yet there, on the same definition rather than a
new copy:

* `gaussBinom_symm`: `[a+b, a]_q = [a+b, b]_q`;
* `gaussBinom_one`: `[n,k]_1 = (n choose k)`.

Both by induction from the two Pascal rules. Generic `CommRing`, no field, no ordering.

-- Ref: [kassel1995] C. Kassel, *Quantum Groups*, GTM 155, Springer 1995, Prop. IV.2.1
--   (symmetry and the two q-Pascal identities of the Gaussian binomial).
-/

namespace QOU.MathlibExt.GaussBinomSymm

open QOU.QBeta.HabiroTailStar

variable {R : Type*} [CommRing R]

/-- **Symmetry**: `[a+b, a]_q = [a+b, b]_q`. -/
theorem gaussBinom_symm (q : R) : ∀ a b : ℕ, gaussBinom q (a + b) a = gaussBinom q (a + b) b := by
  intro a
  induction a with
  | zero => intro b; simp [gaussBinom_self]
  | succ a iha =>
    intro b
    induction b with
    | zero => simp [gaussBinom_self]
    | succ b ihb =>
      -- `[a+b+2, a+1]` by the primary rule, `[a+b+2, b+1]` by the dual rule.
      have e : a + 1 + (b + 1) = (a + b + 1) + 1 := by omega
      rw [e, gaussBinom_succ_succ, gaussBinom_succ_succ' q (a + b + 1) b]
      have h1 : gaussBinom q (a + b + 1) a = gaussBinom q (a + b + 1) (b + 1) := by
        have := iha (b + 1); rwa [show a + (b + 1) = a + b + 1 by omega] at this
      have h2 : gaussBinom q (a + b + 1) (a + 1) = gaussBinom q (a + b + 1) b := by
        have := ihb; rwa [show a + 1 + b = a + b + 1 by omega] at this
      have e2 : a + b + 1 - b = a + 1 := by omega
      rw [h1, h2, e2]; ring

/-- Symmetry in the `k ≤ n` form: `[n, k]_q = [n, n - k]_q`. -/
theorem gaussBinom_symm' (q : R) {n k : ℕ} (hk : k ≤ n) :
    gaussBinom q n k = gaussBinom q n (n - k) := by
  have := gaussBinom_symm q k (n - k)
  rwa [Nat.add_sub_cancel' hk] at this

/-- **Classical limit**: `[n,k]_1 = (n choose k)`. -/
theorem gaussBinom_one : ∀ n k : ℕ, gaussBinom (1 : R) n k = (n.choose k : R)
  | 0, 0 => by simp
  | 0, k + 1 => by simp
  | n + 1, 0 => by simp
  | n + 1, k + 1 => by
    rw [gaussBinom_succ_succ, gaussBinom_one n k, gaussBinom_one n (k + 1), Nat.choose_succ_succ]
    push_cast; ring

end QOU.MathlibExt.GaussBinomSymm
