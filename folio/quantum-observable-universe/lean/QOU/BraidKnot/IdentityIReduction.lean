/-
# Identity I — reduction to content second moment + elementary residual (no hook-length formula)

The `W_λ` keystone's `q₀`-free defect sub-target `144·C(n)` carries **Identity I**

    M(n) = (1/n!) · Σ_{λ⊢n} (f^λ)² · ( Σ_{c∈λ} h_c² )  =  n(3n−1)/2

as its one representation-theoretic input. The s5-so3 ledger flagged its proof as needing the
hook-length *formula* (research-grade, multi-session). The probe
`computations/substrate/wlambda_identity_i_structure_probe.py` (audit
`docs/audits/2026-06-28-wlambda-identity-i-rescope-no-hlf.md`) shows the gap is **narrower**:
writing `E[g] := (1/n!) Σ_λ (f^λ)² g(λ)`,

    E[Σ_c h_c²]  =  E[Σ_c content(c)²]  +  n²  =  C(n,2)  +  n²  =  n(3n−1)/2,

with `E[Σ content²] = C(n,2)` the Jucys–Murphy / Kerov content second moment (RSK + the centre of
`ℂ[Sₙ]`; **no hook-length formula**) and the `n²` residual elementary. This file formalises that
reduction:

* `identityI_arithmetic` — the closed arithmetic core `C(n,2) + n² = n(3n−1)/2`, sorry-free.
* `identityI_of_inputs` — Identity I (`E[Σ h²] = n(3n−1)/2`) **conditional** on the two narrowed
  inputs (the content second-moment law and the `n²` residual), §3b-cond style. The remaining gap
  is exactly those two hypotheses — the content moment and the elementary residual — *not* the
  hook-length formula.

Generic field-valued (`ℚ`); purely algebraic. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-28-wlambda-identity-i-rescope-no-hlf.md
-/
import Mathlib.Tactic

namespace QOU.BraidKnot.IdentityIReduction

/-- **Arithmetic core of the reduction.** `C(n,2) + n² = n(3n−1)/2`, written with the content
second moment `C(n,2) = n(n−1)/2` in field form. -/
theorem identityI_arithmetic (n : ℚ) : n * (n - 1) / 2 + n ^ 2 = n * (3 * n - 1) / 2 := by
  ring

/-- **Identity I, conditional on the two narrowed inputs.** Let `Emom2 n` be the Plancherel mean
`E[Σ_c content(c)²]` and `Ehook2 n` be `E[Σ_c h_c²]`. Given
  * `h_content` : the content second-moment law `Emom2 n = C(n,2) = n(n−1)/2`
    (Jucys–Murphy / Kerov — no hook-length formula), and
  * `h_residual` : the elementary residual `Ehook2 n − Emom2 n = n²`,
Identity I follows: `Ehook2 n = n(3n−1)/2`. The hook-length formula `f^λ = n!/∏ h_c` is **not**
used — the dependency is exactly `h_content` and `h_residual`. -/
theorem identityI_of_inputs (Emom2 Ehook2 : ℕ → ℚ)
    (h_content : ∀ n, Emom2 n = (n : ℚ) * ((n : ℚ) - 1) / 2)
    (h_residual : ∀ n, Ehook2 n - Emom2 n = (n : ℚ) ^ 2) (n : ℕ) :
    Ehook2 n = (n : ℚ) * (3 * (n : ℚ) - 1) / 2 := by
  have e := h_residual n
  rw [h_content n] at e
  have hE : Ehook2 n = (n : ℚ) * ((n : ℚ) - 1) / 2 + (n : ℚ) ^ 2 := by linarith
  rw [hE, identityI_arithmetic]

end QOU.BraidKnot.IdentityIReduction
