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

This file now carries only the Markov-parameter kernel `markovZax` and its
archimedean shim `markovZax_real` (convention D).

**Retired 2026-10-10 (bean `qou-ekga`, owner decisions A + B).** This file
used to define a class `MarkovTraceAxioms` and claim to derive the
disjoint-stabilisation factorisation `τ(K_1 ⊔ K_2) = τ(K_1)·τ(K_2)·z^k`
from it, "discharging" `MarkovDisjointStabilisation`. None of that held:

- The class had **no trace in it** — two scalars, each pinned by its own
  equation (`tau_identity = 1`, `tau_stab_factor = markovZax u`) — so it
  was inhabited for every `u` by `⟨1, rfl, markovZax u, rfl⟩` and asserted
  nothing about any trace. It survives only as the deprecated
  `MarkovScalarPins`.
- The six theorems built on it (`markov_iterated_stab{_gen,,_real}`,
  `disjoint_product_factorisation{_gen,,_real}`) all had the shape
  `∃ x, x = <expr>`, provable by handing back `<expr>`. They are withdrawn.
- `MarkovTraceAxioms_implies_disjoint_stabilisation` proved
  `∀ τ, ∃ τ', τ' = τ * markovZax u`, which holds for any function in place
  of `markovZax` and never used its instance. It was a theorem, not an
  `instance`, with zero consumers, so nothing downstream was ever
  discharged by it. Withdrawn.

**Where the honest statements now live.** Against the single canonical
content-bearing class `QOU.Hecke.MarkovTraceAxioms`
(`lean/QOU/Hecke/MarkovTraceProduct.lean`), whose field is an actual
`trace : List GeneratorChain → R_q`:

- k-fold stabilisation — `QOU.Hecke.markov_trace_stabilise`:
  `trace (cs ++ is.map stabChain) = trace cs * z ^ is.length`;
- disjoint factorisation — `QOU.Hecke.markov_trace_disjoint_stabilise`:
  `trace (cs ++ ds ++ is.map stabChain) = trace cs * trace ds * z ^ is.length`.

Both are proved from the class fields, with no extra hypothesis. Both are
statements about the chain-list model; neither discharges
`MarkovDisjointStabilisation`, which stays an axiomatic class (see the
docstring of `markov_trace_disjoint_stabilise`).

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

/-- **DEPRECATED — trivially inhabited; asserts nothing about a trace.**

    Formerly `QOU.BraidKnot.MarkovTraceAxioms` (renamed 2026-10-10, bean
    `qou-ekga`, so the name no longer collides with the content-bearing
    `QOU.Hecke.MarkovTraceAxioms`). It holds two scalars, each pinned to a
    fixed value by its own field, so for every `u` it has exactly one
    inhabitant, `⟨1, rfl, markovZax u, rfl⟩`, and a
    `[MarkovScalarPins u]`-conditional statement is unconditional in all
    but name. It does not encode the Markov axioms M1–M3: there is no trace
    function for them to constrain.

    Use `QOU.Hecke.MarkovTraceAxioms` (a real `trace` with `trace_nil` /
    `trace_cons`) instead. Kept, deprecated, only so the retirement is
    visible; it has no consumers. -/
@[deprecated "Trivially inhabited (two self-pinned scalars, no trace). Use the content-bearing `QOU.Hecke.MarkovTraceAxioms`; stabilisation / disjoint factorisation are `QOU.Hecke.markov_trace_stabilise` / `markov_trace_disjoint_stabilise`. Bean qou-ekga." (since := "2026-10-10")]
class MarkovScalarPins {R : Type*} [Field R] (u : R) where
  /-- A scalar, pinned to `1` by the next field. -/
  tau_identity : R
  /-- Pins `tau_identity` to `1`. -/
  tau_identity_eq_one : tau_identity = 1
  /-- A scalar, pinned to `markovZax u` by the next field. -/
  tau_stab_factor : R
  /-- Pins `tau_stab_factor` to `markovZax u`. -/
  tau_stab_factor_eq_z : tau_stab_factor = markovZax u

end QOU.BraidKnot
