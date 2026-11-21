import QOU.Basic
import QOU.FlavorDressing.FlavorDressingFunctor

/-!
# QOU.FlavorDressing.dressed_mass_from_substrate_split

The substrate-pure derivation of the down–up dressed-quark
mass splitting:

```
μ_d − μ_u = M_N · (q-1)²·(1 − q⁻⁴)/3 · (q^{1/2} + q⁻^{1/2})/(q + q⁻¹)
            + O((Δm/M_N)²)
```

This is the categorical lift of `prop:flavor-split-substrate` to
the level of the flavor-dressing functor.

LaTeX: `\label{prop:flavor-dressed-mass-from-substrate-split}`
-/

namespace QOU.FlavorDressing

open Flavor

/-- The leading-order substrate factor

    `s(q) = (q − 1)² · (1 − q⁻⁴) / 3 · (√q + 1/√q) / (q + 1/q)`

    that multiplies `M_N` to give the dressed-quark splitting at
    substrate parameter `q ∈ ℝ`, `0 < q`.  Defined as a function on
    `ℝ` (we are at the archimedean / numerical layer here per
    AGENTS.md §7c). -/
noncomputable def substrate_split_factor (q : ℝ) : ℝ :=
  ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3) *
    ((Real.sqrt q + Real.sqrt q⁻¹) / (q + q⁻¹))

/-- **External Skein-side hypothesis** (axiomatised).  The
    pair-Skein mass formula of `lem:pair-skein-mass-formula`
    applied to the Borromean baryon braids of the proton and
    neutron gives

      `m_n − m_p = (q + q⁻¹)/(q^{1/2} + q⁻^{1/2}) · (μ_d − μ_u)`.

    Combined with the substrate identity
    `(m_n − m_p)/M_N = (q-1)² · (1 − q⁻⁴) / 3` (from
    `prop:flavor-split-substrate`), this rearranges to
    `μ_d − μ_u = M_N · substrate_split_factor q`.  The closed-form
    statement is recorded as this axiom; promoting it to a theorem
    requires Lean formalisations of both upstream lemmas.
    **This was an `axiom` until 2026-08-08, and it made the library
    inconsistent.** It read

    ```lean
    axiom dressed_mass_split_substrate_closed_form
        (F : FlavorDressingFunctor) (M_N q : ℝ) (_hM : 0 < M_N) (_hq : 1 < q) :
        F.μ Flavor.down - F.μ Flavor.up = M_N * substrate_split_factor q
    ```

    `F`, `M_N` and `q` are all universally quantified and mutually
    unrelated: nothing ties `M_N` to `F`. The left side is fixed by `F`
    alone, the right side varies freely with `M_N`. Take the constant
    dressing `μ ≡ 1` (the class is trivially inhabited, `μ_pos` is
    `one_pos`), so the left side is `1 − 1 = 0`, and instantiate at
    `M_N = 1`, `q = 2`:

    ```lean
    theorem dressed_mass_axiom_is_inconsistent : False := by
      have h := dressed_mass_split_substrate_closed_form flatF 1 2 one_pos (by norm_num)
      simp [flatF, substrate_split_factor] at h
      …  -- √2 + (√2)⁻¹ = 0, false since √2 > 0
    ```

    That compiled, with `#print axioms` naming this axiom. Because
    `substrate_split_factor` is a *concrete* strictly-positive expression
    rather than an opaque symbol, the forced `factor = 0` is refutable, so
    the defect is `False` rather than mere collapse.

    Worth noting how it got here: the docstring below records that a review
    (Gemini #696) flagged the downstream theorem as a **tautology**, and the
    repair was to introduce this axiom. The tautology fix over-corrected into
    unsoundness — the statement stopped being empty by starting to be false.

    The repair is the §3b-cond hypothesis class below, with **no instance**:
    the relation holds for a *particular* `(F, M_N, q)` — the nucleon-mass
    scale belonging to that dressing — not for arbitrary triples. -/
-- Ref: [leitner2026] mass-theory/pair-skein-mass-formula
--      braids-and-knots/flavor-dressed-mass-from-substrate-split § "Derivation"
class DressedMassSubstrateSplit
    (F : FlavorDressingFunctor) (M_N q : ℝ) : Prop where
  /-- The nucleon-mass scale is positive. -/
  M_N_pos : 0 < M_N
  /-- The substrate parameter is above the classical point. -/
  q_gt_one : 1 < q
  /-- The closed form itself: `μ_d − μ_u = M_N · s(q)`, for *this* `M_N`
      (the nucleon-mass scale of *this* dressing `F`) — the content of
      `prop:flavor-split-substrate` combined with
      `lem:pair-skein-mass-formula`, pending Lean formalisations of both. -/
  split : F.μ Flavor.down - F.μ Flavor.up = M_N * substrate_split_factor q

/-- **Classical limit at `q = 1` (proved):** the substrate splitting factor
    `substrate_split_factor q` vanishes identically at `q = 1` because of the
    `(q - 1)^2` prefactor. -/
theorem substrate_split_factor_at_one :
    substrate_split_factor 1 = 0 := by
  unfold substrate_split_factor
  norm_num

/-- **Rearranged dressed down-quark mass identity (proved):** under
    `[DressedMassSubstrateSplit F M_N q]`, the down-quark dressed mass equals
    the up-quark dressed mass plus `M_N * substrate_split_factor q`. -/
theorem dressed_mass_down_eq_up_add_split
    (F : FlavorDressingFunctor) (M_N q : ℝ)
    [h : DressedMassSubstrateSplit F M_N q] :
    F.μ Flavor.down = F.μ Flavor.up + M_N * substrate_split_factor q := by
  linarith [h.split]

/-- **Substrate-pure derivation of the dressed-quark mass
    splitting.**  Combines `prop:flavor-split-substrate` (substrate
    side) with `lem:pair-skein-mass-formula` (Skein side) to
    express `μ_d − μ_u` and `μ_d` in terms of `M_N` and `q` alone.

    **Assumed, not derived here:** the closed-form splitting
    `F.μ Flavor.down - F.μ Flavor.up = M_N * substrate_split_factor q` is
    carried as the `split` field of the explicit `[DressedMassSubstrateSplit F M_N q]`
    hypothesis class (pending Lean formalisations of `prop:flavor-split-substrate`
    and `lem:pair-skein-mass-formula`); this theorem pairs `h.split` with the
    derived additive decomposition `dressed_mass_down_eq_up_add_split`
    (bean `qou-bvo3`).

    Not a tautology (the original Gemini #696 finding): the conclusion
    is a substantive equality drawn from the hypothesis class. Not
    unconditional either (the over-correction that followed, and which
    made the library inconsistent — see the class docstring above): the
    relation is asserted only for a triple that carries the instance,
    not for arbitrary `(F, M_N, q)`. -/
-- Ref: [leitner2026] braids-and-knots/flavor-dressed-mass-from-substrate-split
theorem dressed_mass_from_substrate_split
    (F : FlavorDressingFunctor) (M_N q : ℝ)
    [h : DressedMassSubstrateSplit F M_N q] :
    F.μ Flavor.down - F.μ Flavor.up = M_N * substrate_split_factor q ∧
    F.μ Flavor.down = F.μ Flavor.up + M_N * substrate_split_factor q := by
  exact ⟨h.split, dressed_mass_down_eq_up_add_split F M_N q⟩


/-! ### Removed 2026-08-30 — self-assuming projections

- `dressed_mass_split_hypotheses` — body was `⟨h.M_N_pos, h.q_gt_one⟩`: the conclusion was the
  projected field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, asserting the same proposition under the same hypotheses; only the
restatement goes. That is the vacuity ledger's recorded disposition for this
category — *"drop the pseudo-theorem and project the field at use sites"* — and
there were no use sites: each had **zero references anywhere in the corpus**.
Bean `qou-z9ws`.
-/

end QOU.FlavorDressing
