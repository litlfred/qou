import QOU.Mass.QuantumSl2PlanarMoves
import QOU.Mass.QuantumSl2MirrorClasp

/-!
# Flipping a clasp

The clasp `X = rot(Ř²)` and the mirror clasp `X̄ = rot(Ř⁻²)` on `V_{m+1} ⊗ V_{m+1}` differ by one
crossing and a framing scalar:

    X̄ = (−1)^m s^{m(m+2)} · Ř · X        (`claspBar_eq_rCheck_mul_clasp`).

Turning the hook of a clasp over costs one crossing and the inverse of the Reidemeister I kink
(`rCheck_cupVec`). This is the local move behind the flype in the Whitehead link (issue #7912).

The proof is by eigenvalues on the string basis. Van der Veen's summand satisfies the reflection
`vdvTerm s⁻¹ k a n = (−1)ⁿ s^{2n(n+1)} vdvTerm s a k n` (`vdvTerm_inv`), so
`C(n, s⁻¹) = (−1)ⁿ s^{2n(n+1)} C(n, s)` (`claspSc_inv`), and the monomial is the framing scalar
times the braiding eigenvalue `λ_j` (`braidEigen_eq`).

All statements are over a generic field `𝕜`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Reflection

variable (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hs hq2 in
/-- **Reflection of van der Veen's summand** under `s ↦ s⁻¹`, `k ↔ a`. -/
theorem vdvTerm_inv (k a n : ℕ) (hint : ∀ i, 0 < i → i ≤ k + a + n → qint (s ^ 2) i ≠ 0) :
    vdvTerm s⁻¹ k a n = (-1) ^ n * s ^ (2 * (n * (n + 1))) * vdvTerm s a k n := by
  have hint' : ∀ i, 0 < i → i ≤ a + k + n → qint (s ^ 2) i ≠ 0 := fun i h1 h2 =>
    hint i h1 (by omega)
  rw [vdvTerm_closed s⁻¹ (inv_ne_zero hs) (hq2_inv s hq2) k a n (hint_inv s _ hint),
    vdvTerm_closed s hs hq2 a k n hint']
  simp only [inv_pow, qfact_inv, inv_inv]
  have hf := qfact_ne_zero' s (k + a + n) hint
  have hfn := hf n (by omega)
  have hfk := hf k (by omega)
  have hfa := hf a (by omega)
  rw [show (s ^ 2)⁻¹ - s ^ 2 = -(s ^ 2 - (s ^ 2)⁻¹) by ring, neg_pow,
    show n + a = a + n from add_comm _ _, show k + n = n + k from add_comm _ _,
    show ((-1 : 𝕜)) ^ (a + k) = (-1) ^ (k + a) by rw [add_comm]]
  generalize s ^ 2 - (s ^ 2)⁻¹ = X at hq2
  generalize qfact (s ^ 2) (n + k) = A
  generalize qfact (s ^ 2) (a + n) = B
  generalize qfact (s ^ 2) n = D at hfn
  generalize qfact (s ^ 2) k = E at hfk
  generalize qfact (s ^ 2) a = F at hfa
  have hs' : ∀ e : ℕ, s ^ e ≠ 0 := fun e => pow_ne_zero e hs
  field_simp
  ring

include hs hq2 in
/-- **The clasp scalar at `s⁻¹`:** `C(n, s⁻¹) = (−1)ⁿ s^{2n(n+1)} C(n, s)`, `n = m − j`. -/
theorem claspSc_inv (m j : ℕ) (hj : j ≤ m) (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    claspSc s⁻¹ m j = (-1) ^ (m - j) * s ^ (2 * ((m - j) * (m - j + 1))) * claspSc s m j := by
  unfold claspSc
  rw [Finset.mul_sum, ← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hk' := Finset.mem_range.mp hk
  rw [show j + 1 - 1 - k = j - k by omega, show j - (j - k) = k by omega,
    vdvTerm_inv s hs hq2 (j - k) k (m - j) (fun i h1 h2 => hint i h1 (by omega))]

end Reflection

section Flip

variable (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (m : ℕ)
  (hint : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- **`Ř` on the string through `w_j`:** the braiding eigenvalue
`λ_j = (−1)^j s^{m² − 4jm + 2j² − 2j}`. -/
theorem rCheck_strVec (x : StrIdx m) :
    rCheckMat s hs m m *ᵥ strVec (s ^ 2) m x
      = ((-1) ^ (x.1 : ℕ) * s ^ ((m : ℤ) ^ 2 - 4 * (x.1 : ℕ) * m + 2 * ((x.1 : ℕ) : ℤ) ^ 2
          - 2 * (x.1 : ℕ))) • strVec (s ^ 2) m x := by
  have hj : (x.1 : ℕ) ≤ m := by omega
  have hr : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0 := fun k hk =>
    hint (k + 1) (by omega) (by unfold rOrder at hk; omega)
  have hc : ∀ p < (x.1 : ℕ), qint (s ^ 2) (m - p) ≠ 0 := fun p hp =>
    hint (m - p) (by omega) (by omega)
  have hF : Commute (rCheckMat s hs m m) (deltaF (s ^ 2) m m ^ (x.2 : ℕ)) :=
    Commute.pow_right (rCheckMat_deltaF s hs hq2 m m hr) _
  have hw := rCheck_hwVec s hs hq2 m m x.1 hj hj hr hc hc
  rw [braidEigen_eq s hs m x.1 hj hc] at hw
  rw [strVec, mulVec_mulVec, hF.eq, ← mulVec_mulVec, rCheckMat_mulVec, hw, mulVec_smul]

include hq2 hint in
/-- **Flipping a clasp.** The mirror clasp is the clasp followed by one crossing, times the
inverse of the Reidemeister I scalar: `X̄ = (−1)^m s^{m(m+2)} · Ř · X`. -/
theorem claspBar_eq_rCheck_mul_clasp :
    claspBar s hs m = ((-1) ^ m * s ^ (m * (m + 2))) • (rCheckMat s hs m m * clasp s hs m) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  apply Matrix.toLin'.injective
  refine (strBasis (s ^ 2) hq m hq2 hint).ext fun x => ?_
  have hj : (x.1 : ℕ) ≤ m := by omega
  rw [strBasis_apply, Matrix.toLin'_apply, Matrix.toLin'_apply, smul_mulVec, ← mulVec_mulVec,
    clasp_strVec s hs hq2 m hint x, mulVec_smul, rCheck_strVec s hs hq2 m hint x,
    claspBar_strVec s hs m hq2 hint x, smul_smul, smul_smul,
    claspSc_inv s hs hq2 m x.1 hj (fun i h1 h2 => hint i h1 (by omega))]
  congr 1
  obtain ⟨n, hn⟩ : ∃ n, m = (x.1 : ℕ) + n := ⟨m - x.1, by omega⟩
  generalize (x.1 : ℕ) = j at hn ⊢
  subst hn
  rw [show j + n - j = n by omega]
  have h1 : s ^ (2 * (n * (n + 1))) = s ^ ((j + n) * (j + n + 2))
      * s ^ ((((j + n : ℕ) : ℤ)) ^ 2 - 4 * (j : ℤ) * ((j + n : ℕ) : ℤ) + 2 * (j : ℤ) ^ 2
          - 2 * (j : ℤ)) := by
    rw [← zpow_natCast, ← zpow_natCast, ← zpow_add₀ hs]
    congr 1
    push_cast
    ring
  have h2 : ((-1 : 𝕜)) ^ n = (-1) ^ (j + n) * (-1) ^ j := by
    rw [pow_add, mul_comm ((-1 : 𝕜) ^ j), mul_assoc, ← pow_add, ← two_mul, pow_mul]
    simp
  rw [h1, h2]
  push_cast
  ring

end Flip

end QOU.Mass.QuantumSl2
