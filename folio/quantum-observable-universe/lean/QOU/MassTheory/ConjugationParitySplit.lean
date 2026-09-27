/-
# The bar-even / bar-odd split of the deuteron binding is the **signed** partition-conjugation parity
# of the H₆ Wedderburn sum

The canonical categorical deuteron object is the Frobenius-paired Markov trace over the Wedderburn
blocks of `H₆(q)` (`build_markov_trace_assembly_deuteron_chain.py`):

```
tr_M(β_D) = Σ_{λ ⊢ 6} w_λ(q) · χ^λ_q(β_D),   (the Δ_λ-dressed form B = m_e Σ_λ w_λ χ^λ Δ_λ is the binding)
```

The bar involution `q ↦ q⁻¹` acts on the per-block term `T_λ(q) = w_λ(q) χ^λ_q(β_D)` by

```
T_λ(q⁻¹) = (−1)^{n-1} · T_{λ'}(q),
```

where `λ ↦ λ'` is Young-diagram transpose. This combines **two verified identities** — the weight is
conjugation-invariant, `w_λ(q) = w_{λ'}(q)` (transpose permutes the hook multiset), and partition
conjugation *is* the bar involution on characters, `χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹)` — **with the
weight's own bar-parity** `w_λ(q⁻¹) = (−1)^{n-1} w_λ(q)` (from the `(q−q⁻¹)^{n-1}` prefactor). For the
deuteron `n = 6`, so the **sign is `(−1)⁵ = −1`**: `T_λ(q⁻¹) = −T_{λ'}(q)` (verified to 25 dps).

The crucial consequence — **corrected** from an earlier sign-dropped draft of this file: because the
physical bar carries the `−1`, the parity roles are governed by `sgn = (−1)^{n-1}`, and for the
self-conjugate partition `(3,2,1)` (the unique `λ = λ'` for `n = 6`),

```
T_{(3,2,1)}(q⁻¹) = −T_{(3,2,1)}(q)   ⇒   (3,2,1) is bar-ODD  ⇒  it feeds the bar-odd impurity t, NEVER g₂.
```

So the **bar-even coefficient `g₂` is carried entirely by the conjugate-pair *asymmetries***
`Δ_λ − Δ_{λ'}` (which vanish on the self-conjugate), while the **bar-odd `t` is carried by the
conjugate-pair *symmetric* parts plus the whole self-conjugate `(3,2,1)`**. (For a hypothetical
odd-`n` atom with `sgn = +1` the roles would swap; the sign is the load-bearing datum.)

Model: an index type `I` (partitions), an involution `c : I → I` (conjugation, `c∘c = id`), a sign
`sgn : R` with `sgn·sgn = 1` (`= (−1)^{n-1}`), and a block quantity `g : I → R` (`= w_λ χ^λ`). The
physical bar image of block `p` is `sgn · g (c p)`. This file proves the parity backbone; it does
**not** compute the `Δ_λ` magnitudes (the Track-A gate).
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.ConjugationParity

variable {I : Type*} {R : Type*} [CommRing R]

/-- The physical **bar image** of the block quantity `g` at block `p`: conjugation `c` dressed by the
weight sign `sgn = (−1)^{n-1}`. This is `T_λ(q⁻¹)` re-expressed in the `q`-basis. -/
def barImage (sgn : R) (c : I → I) (g : I → R) (p : I) : R := sgn * g (c p)

/-- (Twice) the **physical bar-even** part — the channel carrying the bar-even coefficient `g₂`. -/
def pEven (sgn : R) (c : I → I) (g : I → R) (p : I) : R := g p + sgn * g (c p)

/-- (Twice) the **physical bar-odd** part — the channel carrying the bar-odd impurity `t`. -/
def pOdd (sgn : R) (c : I → I) (g : I → R) (p : I) : R := g p - sgn * g (c p)

/-- **Decomposition:** twice the block quantity is bar-even ⊕ bar-odd (independent of `sgn`). -/
theorem two_mul_eq (sgn : R) (c : I → I) (g : I → R) (p : I) :
    2 * g p = pEven sgn c g p + pOdd sgn c g p := by
  unfold pEven pOdd; ring

/-- **Covariance under conjugation** (needs `sgn·sgn = 1` and `c` an involution): the bar-even part
picks up the sign under `p ↦ c p`. So a conjugate pair `{p, c p}` combines coherently in the
bar-even channel with relative sign `sgn`. -/
theorem pEven_conj (sgn : R) (c : I → I) (g : I → R) (p : I)
    (hs : sgn * sgn = 1) (hc : c (c p) = p) :
    pEven sgn c g (c p) = sgn * pEven sgn c g p := by
  unfold pEven; rw [hc]
  have expand : sgn * (g p + sgn * g (c p)) = sgn * g p + (sgn * sgn) * g (c p) := by ring
  rw [expand, hs]; ring

/-- **The corrected key fact — a self-conjugate block feeds the bar channel selected by `sgn`.**
For `c p = p`, the bar-even part is `(1 + sgn)·g p` and the bar-odd part is `(1 − sgn)·g p`. -/
theorem pEven_selfConj (sgn : R) (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    pEven sgn c g p = (1 + sgn) * g p := by
  unfold pEven; rw [hself]; ring

theorem pOdd_selfConj (sgn : R) (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    pOdd sgn c g p = (1 - sgn) * g p := by
  unfold pOdd; rw [hself]; ring

/-- **Deuteron case `n = 6`, `sgn = −1`: the self-conjugate `(3,2,1)` has ZERO bar-even part** — its
Wedderburn contribution is purely bar-odd, so it feeds the impurity `t` and NEVER the bar-even
coefficient `g₂`. (This corrects the sign-dropped earlier draft, which had the channel reversed.) -/
theorem selfConj_barEven_zero_deuteron (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    pEven (-1 : R) c g p = 0 := by
  rw [pEven_selfConj (-1 : R) c g p hself]; ring

/-- Companion: for `sgn = −1` the self-conjugate's bar-odd part is `2·g p` (its full contribution
lands in the bar-odd `t` channel). -/
theorem selfConj_barOdd_double_deuteron (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    pOdd (-1 : R) c g p = 2 * g p := by
  rw [pOdd_selfConj (-1 : R) c g p hself]; ring

/-- Sanity check that the sign is load-bearing: for a hypothetical odd-`n` atom (`sgn = +1`) the
self-conjugate would instead have ZERO bar-odd part (feeding `g₂`) — the opposite channel. -/
theorem selfConj_barOdd_zero_oddN (c : I → I) (g : I → R) (p : I) (hself : c p = p) :
    pOdd (1 : R) c g p = 0 := by
  rw [pOdd_selfConj (1 : R) c g p hself]; ring

end QOU.MassTheory.ConjugationParity
