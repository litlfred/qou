import QOU.Mass.QuantumSl2MirrorClasp

/-!
# Zheng's formula for the four boxes, with framing and normalisation

Stage 4d-iv of the derivation of van der Veen's Lemma 1 (Zheng's formula). With `N = m + 1`,
`q = s²`, `t = q²` and `n = m − j`, van der Veen writes

    J_N(W_{a,b,c,d})(t) = Σ_{n=0}^{N−1} ([2n+1]/[N]) T(n,t)^a B(n,t)^b C(n,t)^c C(n,t⁻¹)^d,

    T(n,t) = t^{n(n+1)},   B(n,t) = [N(2n+1)]/[2n+1],
    C(n,t) = t^{(N²−1)/2 + N(N−1)/2} Σ_{k=0}^{N−1−n} t^{−N(n+k)}
               Π_{j=1}^{n} (1−t^{N−j−k})(1−t^{j+k})/(1−t^j).

The factor `t^{(N²−1)/2} = q^{m(m+2)}` is a framing correction, included only when both strands
of the clasp belong to one component, which for Whitehead chains means `c + d = 1`
(`framingSc`). The remaining factor `t^{N(N−1)/2} Σ_k …` is `claspSc`, whose summands are
`vdvTerm` (`QuantumSl2Clasp.lean`).

`zhengJ_eq_trace` shows that the right-hand side, as a function of `(a, b, c, d)`, is the
normalised quantum trace `[N]⁻¹ tr_q(T^a B^b (φ X)^c (φ̄ X̄)^d)` on `V_N ⊗ V_N` of the
zero-framed twist `T`, the belt `B`, the clasp `X` and the mirror clasp `X̄`, with `φ, φ̄` the
framing scalars. This is the algebraic content of Lemma 1. Reading the trace as the coloured
Jones polynomial of the closed link `W_{a,b,c,d}` is the Reshetikhin–Turaev functor applied to
the tangle decomposition, which is not formalised here.

All statements are over a generic field `𝕜`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1 and its proof
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Zheng

variable (s : 𝕜) (m : ℕ)

/-- The framing scalar `t^{(N²−1)/2} = q^{m(m+2)}`, used only when `c + d = 1`. -/
def framingSc (c d : ℕ) : 𝕜 := if c + d = 1 then (s ^ 2) ^ ((m : ℤ) * (m + 2)) else 1

/-- van der Veen's `C(n, t)` with `N = m + 1`, including the framing factor when `c + d = 1`. -/
def vdvC (n c d : ℕ) : 𝕜 := framingSc s m c d * claspSc s m (m - n)

/-- **The right-hand side of van der Veen's Lemma 1**, with `N = m + 1`:
`Σ_{n<N} ([2n+1]/[N]) t^{a n(n+1)} ([N(2n+1)]/[2n+1])^b C(n,t)^c C(n,t⁻¹)^d`. -/
def zhengJ (a b c d : ℕ) : 𝕜 :=
  ∑ n ∈ Finset.range (m + 1), qint (s ^ 2) (2 * n + 1) / qint (s ^ 2) (m + 1)
    * (((s ^ 2) ^ 2) ^ (n * (n + 1))) ^ a
    * (qint (s ^ 2) ((m + 1) * (2 * n + 1)) / qint (s ^ 2) (2 * n + 1)) ^ b
    * vdvC s m n c d ^ c * vdvC s⁻¹ m n c d ^ d

variable {s}

theorem framingSc_inv (c d : ℕ) : framingSc s⁻¹ m c d = (framingSc s m c d)⁻¹ := by
  unfold framingSc
  split_ifs
  · rw [inv_pow, inv_zpow]
  · rw [inv_one]

theorem twistSc_reflect (n : ℕ) (hn : n ≤ m) :
    twistSc s m (m - n) = ((s ^ 2) ^ 2) ^ (n * (n + 1)) := by
  unfold twistSc
  rw [show m - (m - n) = n by omega, ← pow_mul,
    show (2 * ((n : ℕ) : ℤ) * ((n : ℕ) + 1)) = ((2 * (n * (n + 1)) : ℕ) : ℤ) by push_cast; ring,
    zpow_natCast]

theorem beltSc_reflect (n : ℕ) (hn : n ≤ m) :
    beltSc s m (m - n) = qint (s ^ 2) ((m + 1) * (2 * n + 1)) / qint (s ^ 2) (2 * n + 1) := by
  unfold beltSc
  rw [show m - (m - n) = n by omega, mul_comm]

/-- **van der Veen's Lemma 1, algebraic form.** The sum `zhengJ` equals the normalised
quantum trace on `V_N ⊗ V_N` (`N = m + 1`) of `T^a B^b (φ X)^c (φ̄ X̄)^d`, where `T` is the
zero-framed full twist, `B` the belt, `X` the clasp, `X̄` the mirror clasp, and
`φ = framingSc s`, `φ̄ = framingSc s⁻¹` are the framing scalars. -/
theorem zhengJ_eq_trace (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
    (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (s ^ 2) i ≠ 0) (a b c d : ℕ) :
    zhengJ s m a b c d
      = (qint (s ^ 2) (m + 1))⁻¹ * trace (deltaK (s ^ 2) m m
          * (twist0 s hs m ^ a * beltW s hs m ^ b * (framingSc s m c d • clasp s hs m) ^ c
            * (framingSc s⁻¹ m c d • claspBar s hs m) ^ d)) := by
  simp only [smul_pow, Matrix.mul_smul, Matrix.smul_mul, smul_smul, trace_smul, smul_eq_mul]
  rw [trace_twist_belt_clasp_mirror s hs hq2 m hint a b c d,
    Fin.sum_univ_eq_sum_range (fun j => twistSc s m j ^ a * beltSc s m j ^ b
      * claspSc s m j ^ c * claspSc s⁻¹ m j ^ d * qint (s ^ 2) (2 * (m - j) + 1)),
    ← Finset.sum_range_reflect, Finset.mul_sum, Finset.mul_sum]
  unfold zhengJ vdvC
  refine Finset.sum_congr rfl fun n hn => ?_
  have hn' := Finset.mem_range.mp hn
  rw [show m + 1 - 1 - n = m - n by omega, twistSc_reflect m n (by omega),
    beltSc_reflect m n (by omega), show m - (m - n) = n by omega]
  ring

end Zheng

end QOU.Mass.QuantumSl2
