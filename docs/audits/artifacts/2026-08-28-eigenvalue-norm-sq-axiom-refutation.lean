import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

/-!
# Machine-checked refutation of `eigenvalue_norm_sq_axiom`

Preserved artifact (bean `qou-lsib`, 2026-08-28) for the third inconsistent
axiom found in this corpus, after the two removed in PR #5505.

It stood in
`content/quantum-observable-universe/q-geometric-langlands/hasse-weil-bound.lean`,
in a file that had never compiled — which is why nobody had looked at it. Its
own comment records how it got there: *"since `lake build` is prohibited for
this task, the exact mathlib lemma names ... cannot be safely verified.
Retaining the axiom fallback."* That is an axiom standing in for a proof, not
an external citation like the two beside it (Weil 1948, Rosen 2002).

**The defect.** The axiom omits `αᵢ ≠ 0`. The all-zeros datum satisfies every
field of the structure and both hypotheses — `‖0‖² = 0 ≤ q`, and `(q : ℂ)/0 = 0`
in Lean so the functional equation holds with `j = i` — and the conclusion then
reads `0 = q`, against `q_pos`.

**Reproducing.** Self-contained on Mathlib alone. It carries its own copies of
the pre-fix `LocalQZetaFunction` and of the axiom, deliberately: the live
structure has since gained `eigenvalues_ne_zero`, which makes `zeroWitness`
inadmissible — that field *is* the fix — so a version importing the real
structure would stop compiling and stop demonstrating anything.

    export PATH="$HOME/.elan/bin:$PATH"
    export LEAN_PATH=<mathlib oleans>:<content/*/lean build dirs>
    lean docs/audits/artifacts/2026-08-28-eigenvalue-norm-sq-axiom-refutation.lean

Expect exit 0 and `#print axioms` naming `eigenvalue_norm_sq_axiom` alongside
only `propext`, `Classical.choice`, `Quot.sound`.

**Disposition.** The axiom was not deleted but discharged: the eigenvalue paired
to `αᵢ` by the functional equation has norm `q/‖αᵢ‖`, so Castelnuovo–Severi
applied to *it* gives the reverse bound `q ≤ ‖αᵢ‖²`, and with the forward bound
that is equality.
-/

open Polynomial Complex
namespace QOU.Audits.EigenvalueNormSqRefutation

/-- Genus of Bring's curve, as in the original. -/
def bringsGenus : ℕ := 4

/-- The structure as it stood, plus `q : ℝ` and `q_pos` (both of which the
    refutation needs to state a contradiction at all) but WITHOUT
    `eigenvalues_ne_zero`. -/
structure LocalQZetaFunction where
  q : ℝ
  q_pos : 0 < q
  eigenvalues : Fin 8 → ℂ
  charPoly : ℂ[X]
  charPoly_degree : charPoly.natDegree = 2 * bringsGenus
  charPoly_roots : charPoly = ∏ i : Fin 8, (X - C (eigenvalues i))

/-- The axiom exactly as it was declared. -/
axiom eigenvalue_norm_sq_axiom :
    ∀ (Z : LocalQZetaFunction) (i : Fin 8)
      (_h_cs : ‖Z.eigenvalues i‖ ^ 2 ≤ Z.q)
      (_h_fe : ∃ j, Z.eigenvalues j = ↑Z.q / Z.eigenvalues i),
      ‖Z.eigenvalues i‖ ^ 2 = Z.q

/-- Every eigenvalue zero. Satisfies every field, `q_pos` included. -/
noncomputable def zeroWitness : LocalQZetaFunction where
  q := 1
  q_pos := by norm_num
  eigenvalues := fun _ => 0
  charPoly := X ^ 8
  charPoly_degree := by simp [bringsGenus]
  charPoly_roots := by simp

theorem axiom_is_false : False := by
  have h_cs : ‖zeroWitness.eigenvalues 0‖ ^ 2 ≤ zeroWitness.q := by
    simp [zeroWitness]
  have h_fe : ∃ j, zeroWitness.eigenvalues j
      = ↑zeroWitness.q / zeroWitness.eigenvalues 0 := ⟨0, by simp [zeroWitness]⟩
  have := eigenvalue_norm_sq_axiom zeroWitness 0 h_cs h_fe
  simp [zeroWitness] at this

#print axioms axiom_is_false

end QOU.Audits.EigenvalueNormSqRefutation
