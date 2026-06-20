# Crystal-R-matrix Lean simplification survey

**Date:** 2026-05-08
**Scope:** Survey what the merged crystal-R-matrix infrastructure
(PR #567 + this PR's `CrystalRMatrixSubLemma` extensions) can
simplify in existing Lean proofs, and where it cannot.

**Source class:**
[`QOU.BraidKnot.CrystalRMatrixSubLemma`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CrystalRMatrixSubLemma.lean)
— provides `column_syt_pole_per_cycle p` (= `p − 1` for `p ≥ 1`)
plus three theorems (`cycle_pole_torus_knot`, `axkia_pole_product`,
`inter_nucleon_interface_pole`).

## Candidates surveyed

### `alpha-shift-torus-knot.lean` — **constrained**

Two `sorry`s in the existing instances:

```lean
instance : HasAlphaShiftTorus 2 9 where
  alpha_shift_eq := by sorry  -- alphaShift 2 9 = 9 * (2 - 1) = 9

instance : HasAlphaShiftTorus 3 5 where
  alpha_shift_eq := by sorry  -- alphaShift 3 5 = 5 * (3 - 1) = 10
```

The class field is `alpha_shift_eq : alphaShift p k = k * (p − 1)`.
`alphaShift` is declared **opaque** in the existing file (line 54),
abstracting the maximum-over-irreps pole order
$\max_{\lambda \vdash p} \mathrm{ord}_{q=0}^{(-)} \chi_\lambda((\sigma_1 \cdots \sigma_{p-1})^k)$.

**Limitation:** because `alphaShift` is opaque, no Lean-side
simplification can discharge the two `sorry`s without changing the
abstraction. The crystal-R-matrix machinery proves
`column_syt_pole_per_cycle 2 = 1` and `axkia_pole_T_2_9` etc., but
these are facts about the *crystal-counted* pole order — the
opaque `alphaShift` is a *separate* Lean entity that requires its
own axiom to be equal.

**Two refactor paths (both out of scope for this PR):**

1. **Drop `opaque alphaShift`, redefine as the closed form:**
   ```lean
   def alphaShift (p k : ℕ) : ℕ := k * (p - 1)
   ```
   Both instance `sorry`s collapse to `rfl`. **Cost:** the file's
   docstring intent ("alphaShift is the abstract max-over-irreps
   pole order") is lost; the formula becomes the *definition*
   rather than a *theorem* about the abstract value.

2. **Bridge axiom:** add an axiom stating
   `alphaShift p k = k * column_syt_pole_per_cycle p`. The instance
   `sorry`s discharge via `cycle_pole_torus_knot`. **Cost:** moves
   one axiom to a different file with no net reduction in axiom
   count; only re-locates the axiomatic content.

**Verdict:** No clean simplification path. The two `sorry`s are
properly §3b-cond-axiomatised already (they cite the witness
`alpha-shift-torus.witness.json` per `-- Ref: [manuscript]`). Marginal
improvement is possible by **adding** a cross-reference to the new
crystal audit doc — see "Recommended one-line update" below.

### `confinement-nf-partial-proof.lean` — **also constrained**

Two `sorry`s for the LP-theory inputs (`strong_duality`,
`complementary_slackness`). Out of crystal-R-matrix scope —
fundamentally a Mathlib-LP-duality wiring concern. See
[`docs/audits/2026-05-08-mathlib-lp-duality-roadmap.md`](2026-05-08-mathlib-lp-duality-roadmap.md)
and [`def:lp-duality-hypothesis-class`](../../content/quantum-observable-universe/braids-and-knots/lp-duality-hypothesis-class.md).

### Other Lean files using `alphaShift` — **none affected**

A grep of `content/quantum-observable-universe/lean/` for
`alphaShift` callers reveals only the two test-bench instances
above. No downstream consumer can be simplified.

### Other Lean files using seminormal Hoefsmit arguments — **none in QOU branch**

The audit Step 1 of
[`2026-05-08-crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md)
identifies the seminormal-basis route as 95-line vs the crystal
route's 25 lines. The 95 lines are in the **audit doc**, not in
Lean — there is no Hoefsmit-based Lean proof in the QOU repo
that the crystal route could replace.

## Recommended one-line update

Update the `-- Ref:` citations on the two `alpha-shift-torus-knot.lean`
instance `sorry`s to also cite the crystal-R-matrix audit doc:

```lean
-- Ref: [manuscript] alpha-shift-torus.witness.json (T_2_9, 14 assertions all passed)
-- Ref: [manuscript] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md  (* NEW *)
sorry
```

This documents that *two independent audit paths* (numerical witness
+ categorical crystal-R-matrix proof) support the same formula. No
math changes; pure provenance.

**Decision:** **defer** even this one-line update to a follow-up
PR — the existing citations are AGENTS.md §1-compliant and the
addition is cosmetic.

## Verdict on option 6 (Lean simplification pass)

**Substantive simplification is not feasible** without either
(a) refactoring `opaque alphaShift` (changes file semantics) or
(b) Mathlib-LP-duality wiring (research-grade scope). The crystal
R-matrix infra adds **provenance** for the existing axioms but
cannot collapse them at the Lean level.

The merged #567 work + this PR's extensions remain the right
deliverables; further Lean simplification belongs to:
- A focused **`alphaShift`-redefinition** PR (small but semantic).
- A **Mathlib-LP-duality wiring** PR (research-grade — see roadmap).
- The future `mathlibModel` instance for `HasFiniteLPDuality`
  (zero-edit swap when Mathlib LP lands).
