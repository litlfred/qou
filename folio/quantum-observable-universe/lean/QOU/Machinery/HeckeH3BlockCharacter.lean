import QOU.Machinery.HeckeH3BlockRep

/-!
# QOU.Machinery.HeckeH3BlockCharacter — the 2-dim Wedderburn character of H₃(q)

`HeckeH3Characters` supplied the two **1-dimensional** characters `χ₊, χ₋`
of `H₃(q) ≅ K × K × M₂(K)`; `HeckeH3BlockRep` supplied the `M₂` block
representation `blockRep`. This file completes the **H₃ character table**
with the missing **2-dimensional** character `χ_M = tr ∘ blockRep`, and
proves it is a genuine class function (cyclic), by pure representation
theory — the trace of an algebra representation is cyclic
(`Matrix.trace_mul_comm`), no `Fin 6` computation needed.

Contents (all sorry-free over a field `K`):

* `chiM` — the 2-dim character `χ_M(x) = tr(blockOf x)`.
* `chiM_add` / `chiM_smul` — linearity.
* `chiM_cyclic` — `χ_M(u·v) = χ_M(v·u)`: the class-function / cyclicity
  property, from `blockOf_mulNF` + `Matrix.trace_mul_comm`.
* `chiM_gamma … chiM_top` — the **character values on the NF basis**
  `[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`:
  `[2, h, h, −1, −1, 0]` with `h = q − q⁻¹`.

This is the representation-route cyclicity of the `M₂` block — the
2-dim companion to the two 1-dim characters, and the concrete rank-3
witness that each Wedderburn block's trace is a class function. It does
**not** by itself assemble the Markov trace `tr_M = Σ w_λ χ_λ` (that
needs the Markov weights `w_λ`); it supplies the last character.
-/

namespace QOU.Machinery.H3

open Matrix

variable {K : Type*} [Field K]

/-- The **2-dimensional Wedderburn character** of `H₃(q)`: the trace of the
`(2,1)`-block seminormal representation on NF coordinates. -/
noncomputable def chiM (q : K) (v : Fin 6 → K) : K := (blockOf q v).trace

/-- `χ_M` is additive. -/
theorem chiM_add (q : K) (u v : Fin 6 → K) :
    chiM q (u + v) = chiM q u + chiM q v := by
  have hb : blockOf q (u + v) = blockOf q u + blockOf q v := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp only [blockOf, Matrix.add_apply, Matrix.smul_apply, Pi.add_apply, smul_eq_mul] <;> ring
  unfold chiM
  rw [hb, Matrix.trace_add]

/-- `χ_M` is homogeneous. -/
theorem chiM_smul (q c : K) (v : Fin 6 → K) :
    chiM q (c • v) = c * chiM q v := by
  have hb : blockOf q (c • v) = c • blockOf q v := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp only [blockOf, Matrix.add_apply, Matrix.smul_apply, Pi.smul_apply, smul_eq_mul] <;> ring
  unfold chiM
  rw [hb, Matrix.trace_smul, smul_eq_mul]

/-- **`χ_M` is a class function (cyclic).** `χ_M(u·v) = χ_M(v·u)`, from the
multiplicativity of the block representation (`blockOf_mulNF`) and the
cyclicity of the matrix trace (`Matrix.trace_mul_comm`). Pure representation
theory — no `Fin 6` expansion. -/
theorem chiM_cyclic (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (u v : Fin 6 → K) :
    chiM q (mulNF (q - q⁻¹) u v) = chiM q (mulNF (q - q⁻¹) v u) := by
  unfold chiM
  rw [blockOf_mulNF q hq h2, blockOf_mulNF q hq h2, Matrix.trace_mul_comm]

/-! ### The character values on the NF basis `[γ, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]` -/

/-- `χ_M(γ) = 2` (the identity block, `tr 1₂`). -/
theorem chiM_gamma (q : K) : chiM q (Pi.single 0 1) = 2 := by
  simp [chiM, blockOf]

/-- `χ_M(σ₀) = q − q⁻¹ = h` (`tr S₀`, `S₀ = diag(q, −q⁻¹)`). -/
theorem chiM_sigma0 (q : K) : chiM q (Pi.single 1 1) = q - q⁻¹ := by
  simp [chiM, blockOf, Matrix.trace_fin_two, S0]
  ring

/-- `χ_M(σ₁) = q − q⁻¹ = h` (`tr S₁`; conjugate to `S₀`). -/
theorem chiM_sigma1 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    chiM q (Pi.single 2 1) = q - q⁻¹ := by
  simp [chiM, blockOf, Matrix.trace_fin_two, S1]
  field_simp
  ring

/-- `χ_M(σ₁σ₀) = −1` (`tr(S₁S₀)`). -/
theorem chiM_L (q : K) (_hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    chiM q (Pi.single 3 1) = -1 := by
  simp [chiM, blockOf, Matrix.trace_fin_two, S0, S1]
  field_simp
  ring

/-- `χ_M(σ₀σ₁) = −1` (`tr(S₀S₁)`). -/
theorem chiM_L' (q : K) (_hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    chiM q (Pi.single 4 1) = -1 := by
  simp [chiM, blockOf, Matrix.trace_fin_two, S0, S1]
  field_simp
  ring

/-- `χ_M(σ₀σ₁σ₀) = 0` (`tr(S₀S₁S₀)`; the top word is trace-free). -/
theorem chiM_top (q : K) (_hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    chiM q (Pi.single 5 1) = 0 := by
  simp [chiM, blockOf, Matrix.trace_fin_two, S0, S1]
  field_simp
  ring

end QOU.Machinery.H3
