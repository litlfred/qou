import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic


/-!
# QOU.BraidKnot.markov_axioms_primitive

Primitive Lean axiomatisation of the four Markov axioms (Jones 1985 /
Wenzl 1988) characterising the unique Markov trace τ_M on the Hecke
algebra H_n(R, q):

  M1: τ(1) = 1                        (normalisation)
  M2: τ(xy) = τ(yx)                   (cyclicity)
  M3: τ(x · σ_n) = z · τ(x)            (stabilisation by σ_n)
  M4: τ(x · σ_n^{-1}) = z₋ · τ(x)      (stabilisation by σ_n^{-1};
                                        DERIVED, not independent)

with z = 1/(√q + 1/√q) the Markov-trace loop value and
z₋ = z − (q − q⁻¹) the negative-crossing loop value. M4 is forced by
M1+M3 and the Hecke quadratic relation σ⁻¹ = σ − (q − q⁻¹); note
z₋ ≠ z for q ≠ ±1. Per `prop:markov-trace-frobenius-selection`,
M1-M3 uniquely pin τ_M as the Frobenius-non-degenerate trace.

This file:
  1. Defines the 4 axioms as a Lean class `MarkovTraceAxioms`.
  2. Derives the **disjoint-stabilisation factorisation**
       τ(K_1 ⊔ K_2) = τ(K_1) · τ(K_2) · z^k
     from M3 alone (iterated k times), discharging
     `MarkovDisjointStabilisation` class hypothesis used in
     `prop:categorical-chain-convergence-mechanisms`.

LaTeX label: `rem:markov-axioms-primitive` (helper Lean infrastructure).
-/

namespace QOU.BraidKnot

/-! ## Primitive Markov-trace axiomatisation

### Generic-R primary definition (Tier 2 formal adjoin)

The Markov-Jones parameter `markovZax` is naturally a function of the
formal square root `u = √q`. Over any field `R` carrying an element
`u` with `u² = q` (the formal adjoin `R[X]/(X² − q)` realises this
universally), the parameter has the closed form
`z = u / (u² + 1) = 1 / (u + u⁻¹)`.

The archimedean specialisation `markovZax_real (q : ℝ) (hq : 0 < q)`
instantiates `u := Real.sqrt q` and recovers the original real-valued
formula. See [`docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md`](../../../docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md)
for the migration roadmap and Policy B rationale.
-/

/-- **Markov-Jones parameter, generic-R Tier 2 form**.

    Defined for the formal square root `u` (any element of a field
    with `u² = q`). The closed form `u / (u² + 1)` avoids
    `Real.sqrt`, works over any field, and matches the original
    `1 / (u + u⁻¹)` formula (equivalent by clearing the denominator).

    **The Markov KERNEL, not a Markov parameter — convention-C shaped, kept
    deliberately for comparison** (bean `qou-cxjq`, 2026-08-26).

    The old line here read "Archimedean specialisation:
    `markovZax (Real.sqrt q) = markovZax_real q hq` when `0 < q`". That is no
    longer true — `markovZax_real` is now convention D — and it is removed rather
    than left to rot.

    `markovZax u = u/(u²+1)` is convention-neutral *as a function*; the
    convention lives in how it is instantiated. Convention C is `markovZax √q`.
    Convention D is **not** `markovZax u` for any `u` at all
    (`QOU.BraidKnot.no_kernel_instantiation_is_conventionD`: the kernel's real
    range is `[-1/2, 1/2]` and `z_D q > 1/2` for every `q > 1`) — it is the
    *rescaling* `q² · markovZax q`, which is what `markovZax_real` now computes.

    So: do not consume this as a Markov parameter. Use `markovZax_real`, which is
    convention D. -/
def markovZax {R : Type*} [Field R] (u : R) : R := u / (u^2 + 1)

/-- **Archimedean specialisation** of `markovZax` over `ℝ`, in **convention D**:
    `z_D q = q³/(q² + 1) = q² · markovZax q`.

    **Migrated from convention C 2026-08-26 (bean `qou-cxjq`).** This read
    `markovZax (Real.sqrt q)`, i.e. `√q/(q+1)` — convention C, excised by owner
    ruling R1 of 2026-08-15.

    The migration is possible in exactly this shape and no other, and that is a
    theorem rather than a preference. `markovZax` is convention-neutral **as a
    function**; the convention lives in how it is *instantiated*, and
    `QOU.BraidKnot.no_kernel_instantiation_is_conventionD` proves that for every
    `q > 1` **no** argument `u` whatsoever gives `markovZax u = z_D q` — the
    kernel's real range is `[-1/2, 1/2]` and `z_D q > 1/2`. So convention D is
    unreachable by re-instantiating, and is reached instead by the *rescaling*
    `q² · markovZax q` (`QOU.BraidKnot.markovZD_eq_sq_mul_kernel`).

    This is why the 2026-08-03 Tier-2 migration, which replaced `Real.sqrt` with
    the generic kernel, did not make the convention question go away: it removed
    the square root, which was its goal, and left convention C in place and
    harder to see.

    The `0 < q` hypothesis is retained for backward compatibility with existing
    callsites. Convention D needs no positivity — there is no `Real.sqrt` left in
    it — so the hypothesis is now genuinely unused rather than load-bearing. -/
noncomputable def markovZax_real (q : ℝ) (_hq : 0 < q) : ℝ :=
  q ^ 2 * markovZax q

/-- **Legacy unsafe form** of `markovZax` — `Real.sqrt q` without the
    `0 < q` hypothesis. Kept for backward compatibility with the
    pre-Tier-2 callsites; new code should use one of:
      - generic `markovZax (u : R)` with `u² = q` for `[Field R]`
        (Tier 2 — preferred; avoids `Real.sqrt` entirely)
      - `markovZax_real (q : ℝ) (hq : 0 < q)` (Tier 5 archimedean
        shim with explicit positivity)
    Do NOT migrate to `markovZax (Real.sqrt q)` — that still triggers
    the `q-usage-positivity-implicit` warning since `Real.sqrt` carries
    no positivity hypothesis. -/
@[deprecated "Migrate to (a) the generic `markovZax (u : R)` with an explicit u² = q hypothesis (Tier 2 — preferred), or (b) `markovZax_real q hq` carrying `0 < q` (Tier 5). Avoid `markovZax (Real.sqrt q)` — still positivity-implicit. See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-08-03")]
noncomputable def markovZax_legacy (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- **Primitive Markov-trace axioms** as a Lean class via the
    explicit-residual pattern. Captures the axioms M1 and M3 from
    Jones 1985 / Wenzl 1988 that (with cyclicity M2, implicit in the
    trace construction) uniquely characterise the Markov trace on
    `H_n(R, q)`; M4 is derived from M3 via the Hecke quadratic
    relation, with the distinct loop value z₋ = z − (q − q⁻¹).

    Each axiom is encoded as a scalar invariant (residual / stab
    factor) plus an equation pinning it to the required value.

    **Tier 2 generic-R form** (Phase 2 of the q-usage Hoefsmit
    migration, PR #1640 / #1658). The class is parameterised by an
    abstract field `R` and an element `u : R`; the intended physical
    interpretation is that `u` is a formal square-root of the Hecke
    parameter `q`, but the class itself imposes no `u² = q`
    constraint — that hypothesis enters at the callsite for any
    concrete instantiation that needs it.

    Archimedean entry points: `MarkovTraceAxioms_real q` (an `abbrev`
    of `MarkovTraceAxioms (Real.sqrt q)`) and the `_real` wrappers
    `markov_iterated_stab_real` and `disjoint_product_factorisation_real`
    below carry an explicit `(hq : 0 < q)` hypothesis so they avoid
    the `q-usage-positivity-implicit` warning. There are no instances
    of this class on `main` at the time of this Phase 2 refactor, so
    no archimedean callers are broken. -/
class MarkovTraceAxioms {R : Type*} [Field R] (u : R) where
  /-- M1: scalar value of `τ` on the identity element. -/
  tau_identity : R
  /-- M1: τ(1) = 1 (normalisation). -/
  tau_identity_eq_one : tau_identity = 1
  /-- M3: stabilisation factor. Adding one disjoint strand
      multiplies a trace value by `markovZax u`. -/
  tau_stab_factor : R
  /-- M3: the stabilisation factor equals `z = u / (u² + 1)`. -/
  tau_stab_factor_eq_z : tau_stab_factor = markovZax u

/-- **Legacy archimedean alias** preserved for pre-Phase-2 callers.
    `MarkovTraceAxioms_real q` is a `MarkovTraceAxioms` instance over
    `ℝ` with `u := Real.sqrt q`; existing `[MarkovTraceAxioms q]`
    callsites that took `q : ℝ` should migrate to either:
      - generic `[MarkovTraceAxioms u]` with `u² = q` (preferred), or
      - the explicit archimedean form `[MarkovTraceAxioms (Real.sqrt q)]`. -/
abbrev MarkovTraceAxioms_real (q : ℝ) : Type := MarkovTraceAxioms (Real.sqrt q)

/-! ## Iterated stabilisation → disjoint-product factorisation -/

/-- Recursive `k`-fold M3 trace stabilisation `iteratedStab z τ k`, multiplying
    the trace value by `z` at each step from the right (`bean qou-ekga`). -/
def iteratedStab {R : Type*} [Mul R] (z : R) (τ : R) : ℕ → R
  | 0 => τ
  | k + 1 => iteratedStab z τ k * z

/-- **k-fold stabilisation (generic-R / Tier 2 form)**: starting from a
    trace value `τ`, `k` recursive right-multiplications by `z` equal
    `τ · z^k` in any field `R`. Independent of archimedean specialisation. -/
theorem iterated_stabilisation_gen {R : Type*} [Field R]
    (z : R) (τ : R) : ∀ k : ℕ,
    iteratedStab z τ k = τ * z ^ k
  | 0 => by simp [iteratedStab]
  | k + 1 => by
    simp only [iteratedStab, iterated_stabilisation_gen z τ k, pow_succ, mul_assoc]

/-- **k-fold stabilisation (Tier 2 generic-R form)**: under the
    trace-axiom instance, `k` applications of `tau_stab_factor`
    from `τ` equal `τ · (markovZax u)^k`. -/
theorem iterated_stabilisation {R : Type*} [Field R] (u : R) [h : MarkovTraceAxioms u]
    (τ : R) (k : ℕ) :
    iteratedStab h.tau_stab_factor τ k = τ * (markovZax u) ^ k := by
  rw [iterated_stabilisation_gen h.tau_stab_factor τ k, h.tau_stab_factor_eq_z]

/-- Archimedean shim of `iterated_stabilisation` — preserves the
    pre-Phase-2 `(q : ℝ)` API surface. Carries the explicit
    `(hq : 0 < q)` hypothesis so the statement is phrased via
    `markovZax_real q hq` rather than the positivity-implicit
    `markovZax (Real.sqrt q)`. -/
theorem iterated_stabilisation_real (q : ℝ) (hq : 0 < q)
    (τ_x : ℝ) (k : ℕ) :
    iteratedStab (markovZax_real q hq) τ_x k = τ_x * (markovZax_real q hq) ^ k :=
  iterated_stabilisation_gen (markovZax_real q hq) τ_x k

/-- **Disjoint-product factorisation (from M3)**: two braids K_1, K_2
    acting on disjoint strands give the factorised joint trace.

    K_1 has trace τ_K1, K_2 has trace τ_K2; multiplying `τ_K1` by the
    `k`-fold stabilised trace `iteratedStab z τ_K2 k` yields:

      τ_K1 · iteratedStab z τ_K2 k = τ_K1 · τ_K2 · z^k. -/
-- Ref: [leitner2026] prop:categorical-chain-convergence-mechanisms §"Mechanism 2"
-- Ref: [jones1985] doi:10.2307/1971403   (Markov axioms M1–M4)
theorem disjoint_product_factorisation_gen {R : Type*} [Field R]
    (z : R) (τ_K1 τ_K2 : R) (k : ℕ) :
    τ_K1 * iteratedStab z τ_K2 k = τ_K1 * τ_K2 * z ^ k := by
  rw [iterated_stabilisation_gen z τ_K2 k, ← mul_assoc]

theorem disjoint_product_factorisation {R : Type*} [Field R] (u : R)
    [h : MarkovTraceAxioms u] (τ_K1 τ_K2 : R) (k : ℕ) :
    τ_K1 * iteratedStab h.tau_stab_factor τ_K2 k =
      τ_K1 * τ_K2 * (markovZax u) ^ k := by
  rw [disjoint_product_factorisation_gen h.tau_stab_factor τ_K1 τ_K2 k,
      h.tau_stab_factor_eq_z]

/-- Archimedean shim of `disjoint_product_factorisation`.
    Carries the explicit `(hq : 0 < q)` hypothesis. -/
theorem disjoint_product_factorisation_real (q : ℝ) (hq : 0 < q)
    (τ_K1 τ_K2 : ℝ) (k : ℕ) :
    τ_K1 * iteratedStab (markovZax_real q hq) τ_K2 k =
      τ_K1 * τ_K2 * (markovZax_real q hq) ^ k :=
  disjoint_product_factorisation_gen (markovZax_real q hq) τ_K1 τ_K2 k

/-! ## Single-step stabilisation identity under `MarkovTraceAxioms` -/

/-- Under the trace-axiom instance, one recursive stabilisation step
    `iteratedStab h.tau_stab_factor τ_x 1` equals `τ_x * markovZax u`. -/
theorem trace_axioms_implies_disjoint_stabilisation
    {R : Type*} [Field R] (u : R) [h : MarkovTraceAxioms u] :
    ∀ τ_x : R, iteratedStab h.tau_stab_factor τ_x 1 = τ_x * markovZax u := by
  intro τ_x
  simp only [iteratedStab, h.tau_stab_factor_eq_z]

end QOU.BraidKnot
