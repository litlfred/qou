import QOU.Mass.QuantumSl2Decomposition

/-!
# Closing twists and clasps: Zheng's sum for the twist–clasp part

On `V_{m+1} ⊗ V_{m+1}` (`m = N − 1`) the zero-framed full twist `T = q^{m(m+2)} M` and the
clasp `X` are each scalar on every string `Δ(F)^i w_j`, i.e. on every summand
`V_{2n+1}` (`n = m − j`):

* `T` acts by `q^{2n(n+1)}` (`twist_eq`), van der Veen's `T(n,t) = t^{n(n+1)}` with `t = q²`;
* `X` acts by `Σ_{k ≤ j} vdvTerm k (j−k) n` (`clasp_deltaF_pow_hwVec`), van der Veen's `C(n)`
  before the framing factor.

So `T^a X^c` is scalar on every summand, and by `trace_deltaK_mul` its quantum trace is
`Σ_j [2(m−j)+1] T_j^a C_j^c`. This is Lemma 1 of van der Veen for the twist and clasp boxes
(`b = d = 0`); the belt and the mirror clasp are separate steps.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1 and its proof
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Assembly

variable (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (m : ℕ)
  (hint : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0)

/-- The zero-framed full twist `q^{m(m+2)} Ř′Ř` on `V_{m+1} ⊗ V_{m+1}`. -/
def twist0 : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  (s ^ 2) ^ ((m : ℤ) * (m + 2)) • mono s hs m m

/-- The twist scalar on the summand through `w_j`: `q^{2n(n+1)}`, `n = m − j`. -/
def twistSc (j : ℕ) : 𝕜 := (s ^ 2) ^ (2 * ((m - j : ℕ) : ℤ) * ((m - j : ℕ) + 1))

/-- The clasp scalar on the summand through `w_j`: `Σ_{k ≤ j} vdvTerm k (j−k) (m−j)`. -/
def claspSc (j : ℕ) : 𝕜 := ∑ k ∈ Finset.range (j + 1), vdvTerm s k (j - k) (m - j)

include hq2 hint in
theorem twist0_strVec (x : StrIdx m) :
    twist0 s hs m *ᵥ strVec (s ^ 2) m x = twistSc s m x.1 • strVec (s ^ 2) m x := by
  have hj : (x.1 : ℕ) ≤ m := by omega
  have h := twist_eq s hs hq2 m (m - x.1) x.2 (by omega)
    (fun k hk => hint (k + 1) (by omega) (by unfold rOrder at hk; omega))
    (fun p hp => hint (m - p) (by omega) (by omega))
  rw [show m - (m - (x.1 : ℕ)) = x.1 by omega] at h
  rw [twist0, smul_mulVec, strVec, h, twistSc]

include hq2 hint in
theorem clasp_strVec (x : StrIdx m) :
    clasp s hs m *ᵥ strVec (s ^ 2) m x = claspSc s m x.1 • strVec (s ^ 2) m x := by
  obtain ⟨⟨j, hj⟩, i⟩ := x
  simp only [strVec, claspSc]
  obtain ⟨n, rfl⟩ : ∃ n, m = j + n := ⟨m - j, by omega⟩
  have e : j + n - j = n := by omega
  simp only [e]
  exact clasp_deltaF_pow_hwVec s hs hq2 j n i
    (fun i h1 h2 => hint i h1 (by omega))

/-- A product of string-scalar operators is string-scalar, with the product scalar. -/
theorem mulVec_pow_of_eigen
    (A : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) (v) (μ : 𝕜)
    (h : A *ᵥ v = μ • v) (a : ℕ) : (A ^ a) *ᵥ v = μ ^ a • v := by
  induction a with
  | zero => simp
  | succ a ih => rw [pow_succ', ← mulVec_mulVec, ih, mulVec_smul, h, smul_smul, pow_succ', mul_comm]

include hq2 hint in
/-- **Zheng's sum for twists and clasps.** The quantum trace of `T^a X^c` on
`V_{m+1} ⊗ V_{m+1}` is `Σ_{j ≤ m} [2(m−j)+1] · (q^{2n(n+1)})^a · C_j^c`, `n = m − j`. -/
theorem trace_twist_clasp (a c : ℕ) :
    trace (deltaK (s ^ 2) m m * (twist0 s hs m ^ a * clasp s hs m ^ c))
      = ∑ j : Fin (m + 1),
          twistSc s m j ^ a * claspSc s m j ^ c * qint (s ^ 2) (2 * (m - j) + 1) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  refine trace_deltaK_mul (s ^ 2) hq m hq2 hint _ (fun j => twistSc s m j ^ a * claspSc s m j ^ c)
    fun x => ?_
  rw [← mulVec_mulVec,
    mulVec_pow_of_eigen m _ _ _ (clasp_strVec s hs hq2 m hint x) c, mulVec_smul,
    mulVec_pow_of_eigen m _ _ _ (twist0_strVec s hs hq2 m hint x) a, smul_smul, mul_comm]

end Assembly

end QOU.Mass.QuantumSl2
