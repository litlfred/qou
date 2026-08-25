# Vacuous existentials — a third vacuity shape (17 found, 7 drained, 10 live)

Date: 2026-08-07. Detector:
[`scripts/lean-vacuous-existential-audit.py`](../../scripts/lean-vacuous-existential-audit.py).
Scanned 2588 `.lean` files under `content/`. **Originally 17 candidates in 15 files**,
**17/17** discharged by handing the right-hand side straight back. **7 are now drained; 10 remain** — see Disposition below.

Found while triaging the `wall-side-correct` shortlist (PR #4693 item 3):
several files flagged for a gratuitous `ℝ` turned out to carry a much
worse defect than the base-ring question that surfaced them.

## The shape

```lean
theorem knot_factor_spectral_form (n : ℕ) (β β_mirror : HeckeExpansion n) :
    ∃ a : ℝ, a = knotFactor n β β_mirror :=
  ⟨knotFactor n β β_mirror, rfl⟩
```

`∃ x, x = e` is provable by `⟨e, rfl⟩` for **any** well-typed `e`. The
statement survives replacing the definition of `e` with anything else of
the same type, so it asserts nothing whatsoever about `e` — only that a
name for it exists, which in a total type theory is free. Per the
CLAUDE.md derive-then-check standard: *"could this be wrong?"* No. It is
not a theorem.

The recurring cause is a declaration that wants to record *"quantity Q is
well-defined"* or *"Q has the displayed closed form"* and reaches for an
existential where the honest statement is an equation against an
independently-defined `Q`.

## Why neither existing detector sees it

| shape | detector |
|---|---|
| `: True := trivial` | `content/pipeline/lean-vacuity-axiom-audit.ts` |
| `(h : P) … : P := h` | `scripts/lean-self-assuming-audit.py` |
| `: ∃ x, x = e := ⟨e, rfl⟩` | **this pass** |

The conclusion is not `True`, and the proof term is an anonymous
constructor rather than a bare hypothesis identifier, so it falls
between the two. The tactic form `by exact ⟨e, rfl⟩` is classified
identically — the wrapper is not evidence of content.

## The 17 as first found (4 since drained — see Disposition)

| file:line | declaration | conclusion |
|---|---|---|
| `information-theory/p-vs-np-boundary.lean:198` | `torsion_effective_tree_bounded` | `∃ bound, bound = t.order ^ n` |
| `knots-particles-confinement/compound-beta-shell-calibration.lean:39` | `magic_crossing_Q_value` | `∃ Q_beta, Q_beta = E_0 * (…)` |
| `knots-particles-confinement/compound-beta-shell-calibration.lean:48` | `compound_beta_y_target_extraction` | `∃ y_target, y_target = (…)` |
| `lean/QOU/BraidKnot/KnotFactorAmphicheiral.lean:44` | `knot_factor_amphicheiral` | `∃ a, a = 1 - w·h²` |
| `lean/QOU/BraidKnot/KnotFactorAmphicheiral.lean:57` | `knot_factor_amphicheiral_value` | `∃ a, a = 1 - h ^ 2` |
| `lean/QOU/BraidKnot/KnotFactorSpectralDerivation.lean:44` | `knot_factor_spectral_form` | `∃ a, a = knotFactor n β β_mirror` |
| `mass-theory/knot-factor-borromean-composite.lean:39` | `knot_factor_borromean_value` | `∃ a, a = (1 - h ^ 2) ^ k` |
| `mass-theory/knot-factor-shell-closed.lean:62` | `knot_factor_shell_closed_value` | `∃ a, a = 1` |
| `mass-theory/mass-formula-regime-switching.lean:83` | `regime_switched_binding_defined` | `∃ B, B = regimeSwitchedBinding Z N` |
| `mass-theory/mass-tower-coefficient-stratification.lean:48` | `mass_tower_coefficient_stratification` | `∃ depth, depth = stratumDepth term` |
| `mass-theory/nuclear-knot-classification.lean:33` | `nuclear_knot_classification` | `∃ K, K = .borromean` |
| `mass-theory/pauli-factor-wedderburn.lean:35` | `pauli_factor_wedderburn` | `∃ F, F = W.trAlt / W.trSym` |
| `mass-theory/zeta8-witness-level2-su2.lean:151` | `wenzl_annihilator` | `∃ chi_lambda_at_zeta, chi_lambda_at_zeta = 0` |
| `nuclear-interactions/q-zero-stokes-region-identification.lean:165` | `q_0_well_defined` | `∃ q, q = inst.q_0` |
| `predicted-spectra/spectral-decomposition-qvalue.lean:85` | `spectral_decomposition_qvalue` | `∃ Q_q, Q_q = bareQValue … * knotOperator` |
| `quantum-observable-universes/categorical-action-exists.lean:56` | `CategoricalAction.exists` | `∃ S, S = categoricalAction Φ swap` |
| `quantum-observable-universes/q-jacobiator.lean:83` | `leibniz_coeff_exists` | `∃ c, c = j.q⁻¹ * (1 - j.q⁻¹)` |

Machine JSON twin:
[`2026-08-07-lean-vacuous-existential-audit.json`](2026-08-07-lean-vacuous-existential-audit.json).

## Three worth reading first

**`nuclear_knot_classification`** — the docstring claims *"For A ≥ 4, the
nuclear braid is Borromean-like."* The hypothesis `hA : Z + N ≥ 4` is
**never used**; the proof exhibits the constructor `.borromean`. Nothing
ties the classification to `A ≥ 4`, and the statement would hold
verbatim with the hypothesis deleted or negated.

**`q_0_well_defined`** — the docstring reads *"This is FULLY VERIFIED BY
LEAN — no sorrys at the conditional-result level. The conjectural content
is contained in the class hypotheses."* The theorem proves `∃ q, q =
inst.q_0`, which holds for any `inst`. This is the "sorry-free ≠ derived"
laundering that AGENTS.md §Axiomatization-is-NOT-a-Proof exists to
prevent: a true claim about the *absence of sorries* standing in for a
claim about *content*.

**`wenzl_annihilator`** — `∃ chi_lambda_at_zeta, chi_lambda_at_zeta = 0`.
The name asserts an annihilation result at a root of unity; the statement
asserts that zero exists.

## Scope of this claim

Scope-(b) structural, in the sense of AGENTS.md
§Before-declaring-refuted: `∃ x, x = e` is provable by `⟨e, rfl⟩` for any
`e` by the introduction rule for `Exists` and `rfl` — this is a proved
property of the shape, not a numerical observation about these 17 files.
What is *not* claimed: that the surrounding definitions are wrong, or
that the intended mathematics is false. `knotFactor`, `regimeSwitchedBinding`,
and `stratumDepth` are real definitions doing real work; only the
theorems purporting to state something *about* them are empty.

## Disposition — 7 drained, 10 remain

**17 → 10 (15 → 8 files).** Every replacement is verified `lean`-direct
against the restored olean cache (exit 0, sorry-free); none is asserted.

### Round 2 (2026-08-08)

| was | now |
|---|---|
| `knot_factor_borromean_value : ∃ a, a = (1-h²)^k` | *deleted* — `knot_factor_borromean` directly above already proves `composite = (1-h²)^k` and genuinely consumes its `BrunnianDecoupling` hypothesis |
| `torsion_effective_tree_bounded : ∃ bound, bound = t.order ^ n` | *deleted, gap recorded* — see below |
| `CategoricalAction.exists : ∃ S, S = categoricalAction Φ swap` | `categoricalAction (𝟙 A) swap = η_ ≫ swap ≫ ε_` — falsifiable (fails if whiskering by `𝟙` is not the identity); name kept, it is a `lean.ref` target |

**`torsion_effective_tree_bounded` had two faults, not one.** Beyond the
vacuity, its docstring claimed the tree size is *"bounded **polynomially**
in the root-of-unity order"* while the statement said `t.order ^ n` —
exponential in `n`. The statement did not match the claim it was labelled
with. Stating the real proposition needs an effective-tree-size function
to bound, and none exists in that file (`TorsionPoint` carries only
`order`), so it is recorded as a gap rather than replaced by a weaker
theorem.

**`CategoricalAction.exists` is the clearest instance of the pattern.**
Its own docstring conceded *"'exists' and 'equals tr(Φ)' hold by
construction"* — which is precisely the defect. Existence of a named
composite is not a theorem; the `def categoricalAction` above already
supplies it.

### Round 1 (2026-08-07)

| was | now | note |
|---|---|---|
| `leibniz_coeff_exists : ∃ c, c = q⁻¹(1-q⁻¹)` | `leibniz_coeff_eq_zero_iff : q⁻¹(1-q⁻¹) = 0 ↔ q = 1` | the coefficient-level partner of `jacobiator_classical`/`jacobiator_nonzero`, already in the same file |
| `pauli_factor_wedderburn : ∃ F, F = trAlt/trSym` | `pauliFactor W * W.trSym = W.trAlt` | genuinely uses `sym_nonzero`; name kept (it is a `lean.ref` target) |
| `mass_tower_coefficient_stratification : ∃ depth, depth = stratumDepth term` | `stratumDepth term ≤ 4` | falsifiable, by exhaustion; name kept (`lean.ref` target) |
| `knot_factor_shell_closed_value : ∃ a, a = 1` | *(deleted)* | no external references; `knot_factor_shell_closed` above already proves the real statement |

Two notes on the replacements, so the weakening is visible rather than
buried:

- `stratumDepth term ≤ 4` is the **well-definedness half** of what the
  block claims. The full narrative claim — each prefactor *equals* the
  Plancherel-weighted Frobenius integral over its stratum — needs
  Frobenius-integral machinery not yet in Lean, and is **not** proved.
  The docstring now says so. The depth map is also deliberately
  non-injective (`.pair`/`.knotFactor` both at 2), so no uniqueness
  claim is available.
- `knot_factor_shell_closed`'s docstring says the knot factor "equals
  one exactly", but the theorem concludes `= β.weight trivialPartition`.
  Closing that gap needs `weight trivialPartition = 1`, which is not
  established here. Left as-is and flagged.

**Pre-existing breakage fixed in passing:** `knot-factor-shell-closed.lean`
did not compile at the branch base either — `field_simp` is not in its
import cone (which stops at `Mathlib.Data.Real.Basic`), so
`knot_factor_shell_closed` had an unknown-tactic error and an unsolved
goal. Verified red at baseline before the change, green after; the
cancellation is now done explicitly via
`mul_div_assoc` + `div_self (pow_ne_zero 2 triv_nz)`.

## The remaining 13

Each still needs one of: (1) the real equation against an
independently-defined quantity, (2) the real proposition with `sorry` +
`-- Ref:`, or (3) demotion to `conjecture`. Which applies is a per-file
judgement — for several the honest statement requires a second
definition that does not yet exist, so restating them is authoring work,
not a mechanical rewrite. The three called out above
(`nuclear_knot_classification`, `q_0_well_defined`, `wenzl_annihilator`)
are the ones whose docstrings most overclaim relative to what they prove.

The detector is committed so the count is reproducible and cannot
silently regrow.
