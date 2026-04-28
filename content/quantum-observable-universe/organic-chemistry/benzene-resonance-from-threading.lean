/-!
# QOU.Organic.BenzeneResonanceFromThreading — Benzene resonance corollary

The benzene aromatic resonance energy as the Alexander-weight
residual `(3 - Δ_{T(2,6)}(q₀)) · |q+q⁻¹|_mol`.  In the classical
limit q → 1 this is exactly zero, so the leading-order topological
contribution to the resonance vanishes — the experimental
stabilisation must therefore arise from sub-leading or coherent
contributions.

## References

- [manuscript] Ch. 10, Corollary `cor:benzene-resonance-from-threading`
- [manuscript] Ch. 10, Proposition `prop:ring-closure-barrier-quantitative`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

namespace QOU.Organic

/-- Benzene resonance energy as a real-valued function of the
    threading Alexander weight at q₀ and the molecular crossing
    quantum.  Kekulé reference is 3 (three C=C bonds). -/
-- Ref: [manuscript] Ch. 10, Corollary cor:benzene-resonance-from-threading
def benzeneResonanceFromThreading (delta_q0 e_mol : ℝ) : ℝ :=
  (3 - delta_q0) * e_mol

/-- In the classical limit Δ_{T(2,6)}(1) = 3, the leading-order
    resonance contribution vanishes. -/
-- Ref: [manuscript] Ch. 10, Corollary cor:benzene-resonance-from-threading
theorem benzeneResonance_classical_zero (e_mol : ℝ) :
    benzeneResonanceFromThreading 3 e_mol = 0 := by
  unfold benzeneResonanceFromThreading
  ring

/-- Sign rule: when Δ_{T(2,6)}(q₀) > 3 the resonance is negative
    (Kekulé is favoured at q ≠ 1). -/
-- Ref: [manuscript] Ch. 10, Corollary cor:benzene-resonance-from-threading
theorem benzeneResonance_sign
    (delta_q0 e_mol : ℝ) (h_e : 0 < e_mol) (h_d : 3 < delta_q0) :
    benzeneResonanceFromThreading delta_q0 e_mol < 0 := by
  unfold benzeneResonanceFromThreading
  have : 3 - delta_q0 < 0 := by linarith
  exact mul_neg_of_neg_of_pos this h_e

end QOU.Organic
