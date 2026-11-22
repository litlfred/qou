import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic
import QOU.MathlibExt.OcneanuTrace


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

This file keeps the Markov-kernel helpers `markovZax` / `markovZax_real`.
The axioms themselves are the fields of
`QOU.MathlibExt.OcneanuTrace.MarkovTrace`. The class `MarkovTraceAxioms`
that stood here until 2026-11-20 carried no trace, and was removed
(bean `qou-ltwg`). See the section near the end of the file.

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

/-! ## Markov axioms M1–M4: carried by `OcneanuTrace.MarkovTrace`

**Removed 2026-11-20 (bean `qou-ltwg`, owner options 2 + 3).** This section
used to define `class MarkovTraceAxioms (u : R)` with two scalar fields pinned
to `1` and `markovZax u`, plus five theorems of the form
`∃ τ', τ' = τ * z ^ k := ⟨_, rfl⟩`. The class mentioned no algebra and no trace
(`⟨1, rfl, markovZax u, rfl⟩` inhabited it), and the theorems were tautologies.
The claim that they "discharge `MarkovDisjointStabilisation`" was therefore
empty. With `u = √q` the class's parameter was also convention C.

The axioms M1–M4 are the fields of `QOU.MathlibExt.OcneanuTrace.MarkovTrace`:
`tr_one`, `tr_mul_comm`, `markov`, `markov_inv`, with an abstract `z`. The
results this file advertised are proved there, for every genuine trace:

* iterated stabilisation, `tr(x · gₙ ⋯ gₙ₊ₖ₋₁) = zᵏ · tr x`:
  `OcneanuTrace.MarkovTrace.tr_mul_genWord` (restated below);
* disjoint-block multiplicativity on a braided tower:
  `QOU.MathlibExt.BraidedBlockShiftTrace.tr_blockProd`;
* ascending-word chain factorisation:
  `OcneanuTrace.MarkovTrace.tr_chainWord`. -/

/-- **k-fold Markov stabilisation**, for every genuine Markov trace `T`:
    appending `gₙ, …, gₙ₊ₖ₋₁` to `x ∈ H n` multiplies the trace by `zᵏ`. -/
-- Ref: [jones1985] doi:10.2307/1971403 (Markov axioms M1–M4)
theorem markov_iterated_stab {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace R A) (n k : ℕ) (x : A) (hx : x ∈ T.H n) :
    T.tr (x * QOU.MathlibExt.OcneanuTrace.stabWord T.g n k) = T.z ^ k * T.tr x :=
  T.tr_mul_genWord n k x hx

end QOU.BraidKnot
