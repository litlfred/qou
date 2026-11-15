import QOU.BraidKnot.WLambdaDefectClosedForm

/-!
# Keystone G2 — the falsifiable defect-gate for a geometric `W_λ` index

The full-Hecke geometric-index program's **decisive gate** (phase G2, see
`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`): an `S¹`-equivariant
(Reeb) index on a geometric realization of the full-Hecke arena reproduces the q-Plancherel weight
family `W_λ` only if its **2nd heat-kernel coefficient** `a₂(n)` equals the proved defect cubic
`144·C(n) = −n(n−1)(2n−13)` (`WLambdaDefectClosedForm`) for **every** rank `n` — including the exact
**n = 7 sign flip**.

This file formalizes that gate as a machine-checkable specification with falsifiable *teeth*. It
does **not** construct the index (that is **G1**, the owner-gated differential-geometric build); it
states precisely what any candidate must satisfy, so a future geometric `a₂` can be checked against
it mechanically — the program's "decisive refute-or-confirm" step.

**On target (4), conjugation symmetry.** The per-partition target `W_λ = W_{λ′}` (now proved on
main: `KeystoneC2QDimTranspose.qPlancherelWeight_conj`, #2794) is an **independent** necessary
condition: it constrains the *per-λ* weights, whereas this defect gate constrains only the *summed*
coefficient `Σ_λ`-defect at each rank. A candidate could match `a₂(n)` without being per-λ
transpose-symmetric, so the two gates are genuinely distinct — recorded here rather than conflated.

Base ring `ℤ` (the coefficient is `144·`-cleared exactly as `n144C`); nothing archimedean, no `q₀`,
no fit.
-/

namespace QOU.BraidKnot.KeystoneG2Gate

open QOU.BraidKnot.WLambdaDefect

/-- A **candidate equivariant index**, abstracted by its cleared 2nd heat-kernel coefficient
`a₂ : ℤ → ℤ` (the `144·`-cleared coefficient at rank `n`, in `n144C`'s normalization). The geometric
content — the actual Seifert–Chern–Simons index — is **G1** (owner-gated DG); this carrier is the
falsifiable *interface* the program gates on. -/
structure HeatKernelCandidate where
  /-- The cleared 2nd heat-kernel coefficient `144·a₂(n)` at rank `n`. -/
  a₂ : ℤ → ℤ

/-- **The G2 defect gate.** A candidate passes iff its cleared 2nd heat-kernel coefficient matches
the proved defect cubic `144·C(n)` (`n144C`) at every rank. -/
def PassesDefectGate (I : HeatKernelCandidate) : Prop := ∀ n, I.a₂ n = n144C n

/-- **The gate pins the coefficient uniquely.** Two indices that pass G2 have identical 2nd
heat-kernel coefficients — the gate leaves no free constant to tune. -/
theorem defectGate_unique {I J : HeatKernelCandidate}
    (hI : PassesDefectGate I) (hJ : PassesDefectGate J) : I.a₂ = J.a₂ := by
  funext n; rw [hI n, hJ n]

/-- **Passing forces the closed-form cubic.** Any index passing G2 has
`a₂(n) = −n(n−1)(2n−13)` — the program's q₀-free target (1). -/
theorem defectGate_forces_cubic {I : HeatKernelCandidate} (hI : PassesDefectGate I) (n : ℤ) :
    I.a₂ n = -(n * (n - 1) * (2 * n - 13)) := by
  rw [hI n, n144C_closed_form]

/-- **The falsifiable n = 7 discriminant.** Any index passing G2 *must* exhibit the exact sign flip:
`a₂` is positive at rank 6 and negative at rank 7. A candidate geometric index whose 2nd heat-kernel
coefficient does not change sign between ranks 6 and 7 is **refuted**. This is the decisive,
parameter-free teeth of the gate. -/
theorem defectGate_forces_sign_flip {I : HeatKernelCandidate} (hI : PassesDefectGate I) :
    0 < I.a₂ 6 ∧ I.a₂ 7 < 0 := by
  refine ⟨?_, ?_⟩
  · rw [hI 6]; exact n144C_pos (by norm_num) (by norm_num)
  · rw [hI 7]; exact n144C_neg (by norm_num)

/-- The framework's own proved cubic, packaged as a candidate. -/
def canonicalCandidate : HeatKernelCandidate := ⟨n144C⟩

/-- **The gate is satisfiable (non-vacuous).** The proved cubic `n144C` is itself a passing
candidate, so the specification is consistent — it is not vacuously unsatisfiable. The open question
(G1) is whether a *geometric* (Seifert–CS) index realizes this `a₂`; the gate is what such a
construction would be tested against. -/
theorem canonicalCandidate_passes : PassesDefectGate canonicalCandidate := fun _ => rfl

end QOU.BraidKnot.KeystoneG2Gate
