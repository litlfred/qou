import QOU.Knot.WhiteheadLemma1RootOfUnity
import QOU.Mass.QuantumSl2ZhengFormula

/-!
# van der Veen's tangle formula for the Whitehead link, derived

`WhiteheadLemma1RootOfUnity.lean` states van der Veen's generic-`t` formula for the Whitehead
link `W_{0,1,1,0}` as the definition `vdvWhiteheadLinkJones`, and derives its value at the
Kashaev point. The formula itself was cited. Here it is connected to the representation
theory of `U_q(sl₂)` in `QOU/Mass/QuantumSl2*.lean`:

    vdvWhiteheadLinkJones (σ²) N = (−1)^{N−1} · [N]⁻¹ tr_q(B · φX)      on `V_N ⊗ V_N`,

where `B` is the belt, `X` the clasp (cap·(1⊗M⊗1)·cup, `M` the monodromy `Ř²`), `φ = q^{N²−1}`
the framing factor and `tr_q(Y) = tr(Δ(K) Y)` (`whiteheadLinkJones_eq_trace`). The variable of
`vdvWhiteheadLinkJones` is `s = t^{1/2} = q`, so `σ` is a square root of `q`.

**The sign `(−1)^{N−1}`.** The cup and cap of `V_N` carry the factor `(−1)^{N−1}`
(`capCoefQ`), so the clasp scalar is `(−1)^{N−1}` times van der Veen's printed `C(n,t)`.
At `N = 2` the trace side gives the Jones polynomial with `V(1) = −2`, the standard value for
a two-component link, while the printed formula gives `+2`. The sign does not affect `|J_N|`,
hence not the volume conjecture.

**What is not formalised.** That the quantum trace of the composed tangle operators is the
coloured Jones polynomial of the closed link is the Reshetikhin–Turaev functor applied to van
der Veen's tangle decomposition of `W_{a,b,c,d}`; it is not proved here.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1 and its proof
-/

namespace QOU.Knot.FigureEightVolume

open Matrix QOU.Mass.QuantumSl2

theorem vdvQnum_natCast (s : ℂ) (k : ℕ) : vdvQnum s k = qint s k := by
  unfold vdvQnum qint
  rw [zpow_neg, zpow_natCast, inv_pow]

/-- The fused belt factor is `[N(2n+1)]/[N]`. -/
theorem vdvBeltFused_eq (s : ℂ) (hs : s ≠ 0) (N n : ℕ) (hN : qint s N ≠ 0) :
    vdvBeltFused s N n = qint s (N * (2 * n + 1)) / qint s N := by
  have h := vdvBeltFused_spec s hs N n
  rw [show ((N : ℤ) * (2 * n + 1)) = ((N * (2 * n + 1) : ℕ) : ℤ) by push_cast; ring,
    vdvQnum_natCast, vdvQnum_natCast] at h
  rw [eq_div_iff hN, mul_comm, h]

/-- **van der Veen's clasp is `(−1)^{N−1}` times the clasp scalar, framed.** -/
theorem vdvClasp_eq (σ : ℂ) (hσ : σ ≠ 0) (m n : ℕ) (hn : n ≤ m) :
    vdvClasp (σ ^ 2) (m + 1) n
      = (-1) ^ m * ((σ ^ 2) ^ ((m : ℤ) * (m + 2)) * claspSc σ m (m - n)) := by
  have hs : σ ^ 2 ≠ 0 := pow_ne_zero 2 hσ
  unfold vdvClasp claspSc
  rw [show m - (m - n) = n by omega, show m + 1 - n = m - n + 1 by omega,
    show ((((m + 1 : ℕ) : ℤ)) ^ 2 - 1) + ((m + 1 : ℕ) : ℤ) * (((m + 1 : ℕ) : ℤ) - 1)
      = (m : ℤ) * (m + 2) + (((m + 1) * m : ℕ) : ℤ) by push_cast; ring,
    zpow_add₀ hs, Finset.mul_sum, Finset.mul_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hk' := Finset.mem_range.mp hk
  unfold vdvTerm
  rw [show k + (m - n - k) + n = m by omega, ← Finset.Ico_add_one_right_eq_Icc,
    Finset.prod_Ico_eq_prod_range, Nat.add_sub_cancel]
  have hprod : ∀ j ∈ Finset.range n,
      (1 - (σ ^ 2) ^ (2 * (((m + 1 : ℕ) : ℤ) - ((j : ℤ) + 1) - k)))
          * (1 - (σ ^ 2) ^ (2 * ((j : ℤ) + 1 + k))) / (1 - (σ ^ 2) ^ (2 * ((j : ℤ) + 1)))
        = (1 - ((σ ^ 2) ^ 2) ^ (m + 1 - (1 + j) - k)) * (1 - ((σ ^ 2) ^ 2) ^ (1 + j + k))
          / (1 - ((σ ^ 2) ^ 2) ^ (1 + j)) := by
    intro j hj
    have hj' := Finset.mem_range.mp hj
    rw [show (2 * (((m + 1 : ℕ) : ℤ) - ((j : ℤ) + 1) - k)) = ((2 * (m + 1 - (1 + j) - k) : ℕ) : ℤ)
        by push_cast [show 1 + j + k ≤ m + 1 by omega]; omega,
      show (2 * ((j : ℤ) + 1 + k)) = ((2 * (1 + j + k) : ℕ) : ℤ) by push_cast; ring,
      show (2 * ((j : ℤ) + 1)) = ((2 * (1 + j) : ℕ) : ℤ) by push_cast; ring,
      zpow_natCast, zpow_natCast, zpow_natCast, pow_mul, pow_mul, pow_mul]
  rw [Finset.prod_congr rfl hprod,
    show (-(2 * ((m + 1 : ℕ) : ℤ) * ((n : ℤ) + k))) = -(((2 * ((m + 1) * (n + k))) : ℕ) : ℤ)
      by push_cast; ring,
    zpow_neg, zpow_natCast, zpow_natCast, ← pow_mul, ← pow_mul, ← pow_mul]
  have hpm : ((-1 : ℂ)) ^ m * (-1) ^ m = 1 := by rw [← mul_pow]; norm_num
  have hz : (σ ^ 2) ^ ((m : ℤ) * (m + 2)) ≠ 0 := zpow_ne_zero _ hs
  simp only [← pow_mul]
  generalize ∏ x ∈ Finset.range n, (1 - σ ^ (2 * 2 * (m + 1 - (1 + x) - k)))
      * (1 - σ ^ (2 * 2 * (1 + x + k))) / (1 - σ ^ (2 * 2 * (1 + x))) = P
  field_simp
  linear_combination (-P * σ ^ (4 * ((m + 1) * (n + k)))) * hpm

/-- van der Veen's Whitehead-link formula is `(−1)^{N−1}` times `zhengJ` at `(a,b,c,d) = (0,1,1,0)`. -/
theorem vdvWhiteheadLinkJones_eq_zhengJ (σ : ℂ) (hσ : σ ≠ 0) (m : ℕ)
    (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0) :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1) = (-1) ^ m * zhengJ σ m 0 1 1 0 := by
  have hs : σ ^ 2 ≠ 0 := pow_ne_zero 2 hσ
  have hN : qint (σ ^ 2) (m + 1) ≠ 0 := hint _ (by omega) (by omega)
  unfold vdvWhiteheadLinkJones zhengJ vdvC framingSc
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun n hn => ?_
  have hn' := Finset.mem_range.mp hn
  have h2n : qint (σ ^ 2) (2 * n + 1) ≠ 0 := hint _ (by omega) (by omega)
  rw [show ((m + 1 : ℕ) : ℕ) = m + 1 from rfl, vdvBeltFused_eq (σ ^ 2) hs (m + 1) n hN,
    vdvClasp_eq σ hσ m n (by omega), if_pos (by norm_num)]
  field_simp

/-- **van der Veen's Whitehead-link formula is a quantum trace.** On `V_N ⊗ V_N`
(`N = m + 1`, `q = σ²`), with `B` the belt and `X` the clasp,
`vdvWhiteheadLinkJones q N = (−1)^{N−1} [N]⁻¹ tr(Δ(K) · B · q^{N²−1} X)`. -/
theorem vdvWhiteheadLinkJones_eq_trace (σ : ℂ) (hσ : σ ≠ 0) (m : ℕ)
    (hq2 : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0) (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0) :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1)
      = (-1) ^ m * (qint (σ ^ 2) (m + 1))⁻¹ * trace (deltaK (σ ^ 2) m m
          * (beltW σ hσ m * ((σ ^ 2) ^ ((m : ℤ) * (m + 2)) • clasp σ hσ m))) := by
  rw [vdvWhiteheadLinkJones_eq_zhengJ σ hσ m hint, zhengJ_eq_trace m hσ hq2 hint 0 1 1 0]
  simp only [framingSc, Nat.add_zero, if_true, pow_zero, pow_one, Matrix.one_mul,
    Matrix.mul_one]
  ring

end QOU.Knot.FigureEightVolume
