> **DEPRECATED on 2026-05-24.** Point-in-time status / workplan snapshot; the plan has been executed or the status superseded by later audits + integrated into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T3 for the deprecation rationale.

# Item-3 + Tier-A batch status (2026-05-09)

Batch on `claude/item3-mathlib-tier-a-batch`. The user's ask was:

> α_5 fit — not derived? do item 3, do Bloch-Suslin and
> ArchimedeanLimit class instance, do Tier A.

This audit records what was deliverable in a single CI-billing-conscious
push and what remains genuinely Mathlib-upstream.

## 1. Item 3 — `gb_filtration_jet_tracker` H_n for n ≥ 4 (DONE)

[`computations/gb_filtration_jet_tracker.py`](../../computations/gb_filtration_jet_tracker.py)
extended with five new test cases:

| Case | n | word | filtration shape |
|------|---|------|------------------|
| `electron-stab σ_1^3 in H_4 (trefoil + 2 unknots)` | 4 | `[1,1,1]` | `{1:1, 0:1}` ✓ |
| `ascending σ_1 σ_2 σ_3 σ_1 σ_2 σ_1 in H_4 (longest)` | 4 | `[1,2,3,1,2,1]` | computed |
| `Borromean ⊗ σ_3 in H_4 (proton-stab)` | 4 | `[1,-2,1,-2,1,-2,3]` | computed |
| `ascending σ_1 σ_2 σ_3 σ_4 in H_5` | 5 | `[1,2,3,4]` | `{4:1}` ✓ |
| `²H disjoint mock (σ_1σ_2^{-1})^3 ⊗ σ_3..σ_5 in H_6` | 6 | `[1,-2,1,-2,1,-2,3,4,5]` | `{3:1, 4:2, 5:2}` |

Run: `python3 computations/gb_filtration_jet_tracker.py`
— **11 cases total**, max steps 31, max grade 6.

This is the gateway compute for Term-7 χ_5 evaluation: with H_n
canonical T_w available through n = 6, the Wedderburn-weight
evaluation in [`term7_chi5_basis.py`](../../computations/term7_chi5_basis.py)
becomes structural rather than fit. The "α_5 currently a fit"
status is now flagged as a workplan item rather than a hidden
assumption.

## 2. `BlochSuslinUniqueness` instance (BLOCKED on Mathlib)

Class declared at
[`content/quantum-observable-universe/descartes-universe/archimedean-functor-uniqueness.lean`](../../content/quantum-observable-universe/descartes-universe/archimedean-functor-uniqueness.lean):69.

Fields:
- `d_pentagon : PentagonCoherent D`
- `d_continuous : Continuous D`
- `d_antisymmetric` (Rogers L-form on real slice)
- `uniqueness` (the Suslin theorem)

**Trivial instance for `D ≡ 0`** — pentagon-coherent and antisymmetric
hold by `0 = -0`, but the uniqueness clause forces `φ ≡ 0`, which
captures none of the QOU content. **Not authored** since it would
mislead consumers into thinking the class is inhabited in a useful
way.

The genuine instance requires `Real.dilog` plus the Suslin
`K_3^{ind}(ℂ) → ℝ` rigidity argument; both are Mathlib upstream.
Tracked in [`docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
as a Tier-B compute-isable item (numerical PSLQ over a candidate
function family is the next step, not theorem-bound).

## 3. `ArchimedeanLimit` instance (boundary done; (0,1) BLOCKED)

Class declared at
[`content/quantum-observable-universe/braids-and-knots/dilogarithm-archimedean-limit.lean`](../../content/quantum-observable-universe/braids-and-knots/dilogarithm-archimedean-limit.lean):106.

`instance archimedeanLimit_zero : ArchimedeanLimit 0` already
authored (line 136), unconditional, sorry-free. The boundary
case `x = 0` reduces both sides to constant zero.

Genuine `x ∈ (0,1)` instance requires the Faddeev-Kashaev
uniform Tauberian theorem with branch-cut control on
`Real.dilog`; not in current Mathlib. Same Tier-B compute-isable
candidate as #2.

## 4. Tier-A items — already class-scaffolded

| Item | File | State |
|------|------|-------|
| Linking properties 2-5 | [`categorical-linking-operation.lean`](../../content/quantum-observable-universe/braids-and-knots/categorical-linking-operation.lean) | All five `Lk*` predicates `True`, all five `*_holds` theorems discharged (`trivial`). The substantive content lives in the `.md` block citing Kassel §X / §XIV. The Lean file is the pre-trace-level discharge per path-α-Bring. Post-trace upgrade for `multiplicativeInK` remains noted as substrate-specific. |
| Weinberg θ_W | [`weinberg-angle-categorical.lean`](../../content/quantum-observable-universe/braids-and-knots/weinberg-angle-categorical.lean) | Class with four `True` predicates (linking discharged, Hoefsmit cell-content discharged, Higgs-vev automorphism, numerical CODATA). Awaits #2 + #5 below. |
| Hoefsmit EW cell-content | [`hoefsmit-ew-cell-content.lean`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-ew-cell-content.lean) | `purePatternMultiplicity` enumerated for all 8 patterns, `totalPureMultiplicity = 20` proved by `decide`. Class hypothesises generic-q + the structural assignment + pairwise orthogonality + EW idempotents. |

The substantive remaining work is *not* class-authoring (already
done) but discharge of the `True`-shaped predicates with the
genuine categorical statements. That is theorem-bound, not
compute-bound, and was not deliverable in this batch.

## Net state

Item 3 is the only substantive movement in this batch. The
Bloch-Suslin / ArchimedeanLimit / Tier-A items are documented
as class-scaffolded with explicit Mathlib-upstream / theorem-bound
gaps; no "fake" instances were authored, and `α_5 fit → derived`
is now reachable via Term-7 χ_5 + canonical T_w through H_6.

Affected files (relative paths):

- [`computations/gb_filtration_jet_tracker.py`](../../computations/gb_filtration_jet_tracker.py)
- [`computations/gb-filtration-jet-order.witness.json`](../../computations/gb-filtration-jet-order.witness.json)
- [`docs/audits/2026-05-09-item3-tier-a-batch-status.md`](2026-05-09-item3-tier-a-batch-status.md)
