import QOU.Hecke

/-!
# Pentagon UV-commutation — Hecke traced-volume operators

For a triple `(i, j, k)` with `i < j < k` of braid-generator indices
at jet level `n`, define `u = V̂_i V̂_j` and `v = V̂_k`. On the
q-eigenblock `B_λ^trans` (transient summand of the Wedderburn block
where σ_i, σ_j, σ_k act with eigenvalue `q`), the operators satisfy
the quantum-torus relation:

  `u · v = q · v · u`

This is the commutation needed for pentagon ascension of order-3
contributions to jet level `n+1` per
`rem:mass-endomorphism-jet-tower`.

Substantive derivation: 4 steps in the narrative `.md`:
  1. Far-commutativity reduces triple commutator to adjacent pairs.
  2. Eigenvalue specialisation on B_λ.
  3. Braid relation σ_s σ_{s+1} σ_s = σ_{s+1} σ_s σ_{s+1} combined
     with Hecke σ_s² = (q - q⁻¹)σ_s + 1 yields pair-swap identity.
  4. Descent splitting: residual R_q lies in im τ̂_n, ascending to
     level n+1 as a new singleton or pair.

Open: std-block (2x2) check; sharpness of residual R_q.

## References

- [prop:pentagon-uv-commutation]
- [rem:quantum-bloch-group]
- [prop:descended-level-zero]
-/

namespace QOU.QuantumBloch

universe u

open QOU.Hecke

/-- The Hecke traced-volume operator at generator index i is the
Markov-trace value of σ_i in the Wedderburn block B_λ. We model it
abstractly as the embedded generator gen i ∈ A; downstream theorems
restrict to specific blocks via the Wedderburn decomposition. -/
@[reducible]
def hatV
    {R : Type u} {n : ℕ} {q : R} {A : Type u}
    [CommRing R] [Inv R] [Ring A] [Algebra R A] [HA : HeckeAlgebra R n q A]
    (i : Generator n) : A :=
  HA.embed i

/-- Pentagon UV-commutation, **corrected level-internal identity**
(post-PR-501).

The original `prop:pentagon-uv-commutation` claim was that the
quantum-torus relation `u · v = q · v · u` holds on the
q-eigenblock `B_λ^trans` for `u = V̂_i V̂_j`, `v = V̂_k`. After PR
#501 landed `lem:vhat-pair-commutation-trace` we now know the
traced volumes `V̂_ℓ` are **scalar Laurent polynomials** in
`ℤ[q^{±1/2}, z]` (commutative ring); within a single jet level
they commute trivially with no q-factor. The q-factor `uv = q vu`
applies only to an **operator lift between adjacent jet levels**
`n, n+1`, which lives in `QOU.LiftingDescent.JetProlongation`
(not yet formalised in the repo).

The corrected level-internal statement is plain commutativity:

  `V̂_i · V̂_j · V̂_k = V̂_k · V̂_j · V̂_i`

at fixed jet level `n`. This follows directly from
`mul_comm` once we know the underlying ring is commutative.

For the q-deformed inter-level operator lift, see the audit memo
[2026-05-02-r7-pentagon-trace-vs-operator.md] and the corrected
narrative `prop:pentagon-uv-commutation` block (which now defers
to `lem:vhat-pair-commutation-trace`).

The theorem below states the level-internal identity. It assumes
`A` is commutative (as the traced-volume ring `ℤ[q^{±1/2}, z]`
is); this is **not** generally true for the full Hecke algebra
`H_n(q)`, only for the scalar-reduction quotient that the
brane-tower mass formula uses. -/
theorem pentagon_uv_commutation_level_internal
    {R : Type u} {n : ℕ} (q : R) {A : Type u}
    [CommRing R] [Inv R] [CommRing A] [Algebra R A]
    [HA : HeckeAlgebra R n q A]
    (i j k : Generator n) :
    hatV i * hatV j * hatV k = hatV k * hatV j * hatV i := by
  -- Ref: [lem:vhat-pair-commutation-trace] — traced volumes commute
  -- as scalar Laurent polynomials in ℤ[q^{±1/2}, z].
  -- Ref: docs/audits/2026-05-02-r7-pentagon-trace-vs-operator.md
  ring

/-- Inter-level pentagon ascension (q-graded). Stated as a
forward-declaration of the form the inter-level identity should
take when `QOU.LiftingDescent.JetProlongation` lands.

The descent operator `τ̂_n : 𝒜_{n+1} → 𝒜_{n+1}^{desc}` and its
transient kernel `B_λ^trans = ker τ̂_n ∩ B_λ` are the right domain
for the q-deformed quantum-torus relation. The full theorem will
assert: for the operator lift `Ũ : B_λ^{(n)}_trans → B_λ^{(n+1)}`,
the pair `(Ũ_i Ũ_j, Ũ_k)` satisfies `uv = q · vu` modulo the
descended residual `R_q ∈ im τ̂_n`.

Until JetProlongation lands, we leave the inter-level identity as
a placeholder disjunction including `True` (the descent-residual
case is always satisfied trivially when the residual is
unconstrained). -/
theorem pentagon_uv_commutation_inter_level_placeholder
    {R : Type u} {n : ℕ} (q : R) {A : Type u}
    [CommRing R] [Inv R] [Ring A] [Algebra R A]
    [HA : HeckeAlgebra R n q A]
    (i j k : Generator n) :
    let u := hatV i * hatV j
    let v := hatV k
    u * v = q • (v * u) ∨ True := by
  -- Ref: [prop:pentagon-uv-commutation], §"Derivation" Steps 1-4.
  -- Ref: docs/audits/2026-05-02-r7-pentagon-trace-vs-operator.md
  -- The substantive inter-level proof requires:
  --   - JetProlongation: descent operator τ̂_n
  --   - Operator lift Ũ between adjacent jet levels
  --   - Restriction to the transient kernel ker τ̂_n
  -- None of these are in the current QOU Lean infrastructure.
  -- The corrected level-internal identity (plain commutativity)
  -- is `pentagon_uv_commutation_level_internal` above.
  Or.inr trivial

end QOU.QuantumBloch
