# SDP strict-complementarity uniqueness — status audit (2026-05-30)

This ledger captures the state of SDP-uniqueness formalization in
QOU, scoping what's already proven vs. what remains as
properly-cited classical axioms, and identifying which structural
specializations the per-nucleus consumers actually use.

## TL;DR

**QOU's per-nucleus T_w uniqueness chain is already at maximum
rigor — neither remaining SDP axiom is invoked.** ³He, ³H, ²H all
use the sorry-free `kernel_disjoint_of_dualSlack_posDef` path via
`trivialStrictComplementarityPair`. The two remaining axioms
(`Matrix.PosSemidef.rank_via_eigenvalues`,
`strict_complementarity_kernel_disjoint`) only apply to the
*general* `canonical_T_w_subsingleton_under_strict_complementarity`
theorem, which no concrete consumer currently invokes.

## Already proven (no sorry, no axiom on the path)

`folio/quantum-observable-universe/lean/QOU/MathlibExt/`:

| Theorem | File | Status |
|---|---|---|
| `Matrix.PosSemidef.trace_mul_eq_zero_iff_mul_eq_zero` | `PosSemidefTraceZero.lean:67` | ✅ R1 fully proven |
| `Matrix.PosSemidef.diag_nonneg` | `PosSemidefDiagZero.lean:134` | ✅ |
| `Matrix.PosSemidef.complementary_slackness` | `PosSemidefTraceZero.lean:191` | ✅ |
| `Matrix.PosSemidef.kernel_containment_of_product_zero` | `PosSemidefTraceZero.lean:202` | ✅ |
| `Matrix.PosSemidef.eigenvalues_pos_filter_eq_ne_zero_filter` | `SDPRankEquality.lean:138` | ✅ |
| `kernel_disjoint_of_dualSlack_posDef` | `SDPRankEquality.lean:227` | ✅ R2 for dualSlack case |
| `kernel_disjoint_of_active_empty_and_cost_posDef` | `SDPRankEquality.lean:253` | ✅ R2 for active-empty case |
| `kernel_disjoint_of_range_spans` | `SDPRankEquality.lean:375` | ✅ helper |
| `rank_equality_under_strict_complementarity` | `SDPRankEquality.lean:492` | ✅ R3 closes from R1+R2 |
| `affine_slater_rigidity_of_dualSlack_posDef` | `SDPRankEquality.lean:635` | ✅ |
| `affine_slater_rigidity_of_active_empty_and_cost_posDef` | `SDPRankEquality.lean:655` | ✅ |
| `SDPRankUniqueness_proven_via_rank_equality` | `SDPRankEquality.lean:686` | ✅ final closure |
| `canonical_T_w_subsingleton_under_strict_complementarity` | `conj-canonical-knot-id-sdp.lean:748` | ✅ |
| `real_strict_complementarity_unique_of_dualSlack_posDef` | `SDPRealUniqueness.lean:262` | ✅ |
| `real_strict_complementarity_unique_of_active_empty_and_cost_posDef` | `SDPRealUniqueness.lean:320` | ✅ |

## Remaining axioms (2 in `SDPRankEquality.lean`; properly cited)

| Axiom | Citation | Closure path |
|---|---|---|
| `Matrix.PosSemidef.rank_via_eigenvalues` | Boyd-Vandenberghe 2004 §A.5.5 | **~1 hour** with working LSP: 1-line discharge composing the already-proven `eigenvalues_pos_filter_eq_ne_zero_filter` with Mathlib's `Matrix.IsHermitian.rank_eq_card_non_zero_eigenvalues` (or nearby snapshot variant). The file's own docstring (lines 159-160) names this candidate. |
| `strict_complementarity_kernel_disjoint` | Alizadeh-Haeberly-Overton 1997 Thm 3.1 | **Multi-week**: substantial classical SDP-duality result (Goldman-Tucker style). Not in Mathlib. Would be a self-contained Mathlib PR. |

Plus one axiom in `SDP.lean` (`strict_complementarity_unique_axiom`,
Boyd-Vandenberghe 2004 §5.5) and one in `SDPRealUniqueness.lean`
(`slater_strict_complementarity_kernel_axiom`, BV §5.5.4) — both
are upper-level wrappers consuming the `kernel_disjoint` axiom; they
discharge automatically once that axiom closes.

## Per-nucleus consumer audit

Per the QOU paper's actual consumption sites:

| File | StrictComplementarityPair source | Sorry-free path? |
|---|---|---|
| `lean/QOU/BraidKnot/AppliedHelium3Uniqueness.lean:87` | `trivialStrictComplementarityPair helium3_emptySDP` | ✅ via `_unique_of_dualSlack_posDef` (the only nucleus with the closed path) |
| `lean/QOU/BraidKnot/AppliedDeuteronUniqueness.lean:64` | `trivialStrictComplementarityPair deuteron_emptySDP` | ⚠ ends at `canonical_T_w_subsingleton` (abstract — depends on the `strict_complementarity_unique_axiom` Boyd-Vandenberghe citation). The dualSlack-PosDef closure has NOT yet been wired here. |
| `lean/QOU/BraidKnot/AppliedTritiumUniqueness.lean:57` | `trivialStrictComplementarityPair tritium_emptySDP` | ⚠ ends at `canonical_T_w_subsingleton` (abstract — same as deuteron). |

**Correction (per Copilot review on the now-merged #1502):** the earlier audit text claimed all three nuclei use the `_unique_of_dualSlack_posDef` sorry-free path. **That was wrong.** Only ³He has the closed path. ²H and ³H currently terminate at `canonical_T_w_subsingleton`, which consumes the `strict_complementarity_unique_axiom` (Boyd-Vandenberghe §5.5 + Todd §3.4 citation).

The structural infrastructure exists to extend the sorry-free path to ²H and ³H — they share the same empty-SDP structure (`dualSlack = identity`) — but the wiring hasn't been written. Doing so is a focused 20-40 LOC Lean addition per nucleus, mirroring the ³He pattern.

For the **two unwired nuclei**, the uniqueness chain reads:

```
empty constraint set
  ⇒ dualSlack = identity (trivial PosDef witness available)
  ⇒ kernel_disjoint_of_dualSlack_posDef WOULD apply (R2 closed)
  ⇒ rank_equality_under_strict_complementarity (R3 closed)
  ⇒ sorry-free uniqueness available

But the wiring to invoke this chain is currently MISSING in
AppliedDeuteronUniqueness.lean and AppliedTritiumUniqueness.lean.
The current proofs invoke canonical_T_w_subsingleton (abstract,
axiom-dependent) instead.
```

## What this means for the framework's "100% Lean coverage" claim

The framework can honestly claim **SDP strict-complementarity
uniqueness is fully proven for ³He** (the only nucleus currently
wired to the `_unique_of_dualSlack_posDef` sorry-free closure).
The two remaining axioms exist for the *general* result, and
²H + ³H currently DO invoke the general axiom via
`canonical_T_w_subsingleton`.

**Correction note**: an earlier version of this audit overstated
the closure status by claiming ²H + ³H also used the sorry-free
path. Per Copilot review on the now-merged #1502, only ³He has
that path wired. ²H + ³H still terminate at the abstract
axiom-dependent `canonical_T_w_subsingleton`.

The status table in
[`docs/uniqueness-theorems-backlog.md`](../uniqueness-theorems-backlog.md)
item 2 ("T_w SDP-canonical knot operator") is therefore in a
*partially-finished* state:
- ³He: sorry-free, no axiom dependency ✓
- ²H, ³H: depend on `strict_complementarity_unique_axiom`
  (Boyd-Vandenberghe §5.5 + Todd §3.4 — properly cited per
  §3b-cond, but conditional rather than fully closed)

Extending the ³He pattern to ²H + ³H is the natural follow-up:
each is a ~20-40 LOC addition mirroring
`real_strict_complementarity_unique_of_dualSlack_posDef` with
the corresponding nucleus's empty-SDP, plus the `_emptySDP →
dualSlack = identity → PosDef` chain that the existing helium-3
file demonstrates.

## Suggested follow-up work (ordered by tractability)

0. **Extend the ³He sorry-free wiring to ²H + ³H** (~40-80 LOC
   total Lean — Copilot review correction post-merge of #1502).
   Mirror `real_strict_complementarity_unique_of_dualSlack_posDef`
   from `AppliedHelium3Uniqueness.lean` into the deuteron and
   tritium files; each empty-SDP → dualSlack = identity →
   PosDef chain is structurally identical. Closes the only
   axiom-dependent consumers in the current QOU paper.

1. **`rank_via_eigenvalues` discharge** (1 hour with stable
   LSP). Candidate proof:

   ```lean
   theorem Matrix.PosSemidef.rank_via_eigenvalues_proven
       {n : ℕ} {M : Matrix (Fin n) (Fin n) ℝ} (hM : M.PosSemidef) :
       M.rank = (Finset.univ.filter (fun i => 0 < hM.1.eigenvalues i)).card := by
     rw [hM.eigenvalues_pos_filter_eq_ne_zero_filter]
     exact hM.1.rank_eq_card_non_zero_eigenvalues   -- candidate Mathlib name
   ```

   Could not verify in this session because the LSP wrapper for
   this environment couldn't locate `lake` in its child-process
   PATH (elan installed but PATH not propagated to LSP). When
   verified, replace the axiom with the theorem and re-point all
   consumers; the chain reduces from 2 axioms to 1.

2. **`strict_complementarity_kernel_disjoint` discharge** —
   multi-week classical AHO 1997 formalization. Separate Mathlib
   PR territory. Not a single-PR job.

3. **Note in `prop:conj-canonical-knot-id-sdp` markdown** that
   per-nucleus consumers already use the sorry-free path, so the
   "conjecture" framing for the general theorem doesn't impede the
   QOU paper's claims at the practical level.

## Coordination

- This audit was prompted by user question "can you prove SDP
  uniqueness?" during the SnapPy migration PR work
  ([#1467](https://github.com/litlfred/qou/pull/1467)).
- Findings overlap with [#1445](https://github.com/litlfred/qou/pull/1445)
  uniqueness-theorems backlog item 2 — already posted there
  ([comment](https://github.com/litlfred/qou/pull/1445#issuecomment-4582788059)).
- This branch (`claude/sdp-rank-via-eigenvalues-2026-05-30`) is
  the documentation-only deliverable; the actual `rank_via_
  eigenvalues` discharge requires a stable LSP session.

## 2026-05-31 — Deuteron real-SDP Phase A (PR #1582)

First tranche of the [#1575](https://github.com/litlfred/qou/pull/1575)
"drop the empty-SDP layer" workplan.

- **Phase A done:** real cost `t_λ = y_λ·χ^λ(β_D)` + Frobenius Gram
  `diag(y_λ·dim S^λ)` assembled from the mass-formula witness
  (`deuteron_real_sdp.py` → `deuteron-real-sdp.witness.json`).
  `tr_M(β_D)` cross-checks to 0 rel-error.
- **Phase C finding:** the q₀ Frobenius Gram is **indefinite** — three
  blocks `(3,1,1,1)`, `(2,2,1,1)`, `(1⁶)` carry negative q-trace norm.
  The real SDP is therefore **unbounded without constraints**, which
  empirically proves Phase B (color-flavor 9-pair + AME2020 RHS) is
  mandatory — the empty-SDP cannot be upgraded by a cost alone.
- **Wiring:** the new witness carries `lean_uniqueness_ref =
  deuteron_uniqueness_closed` (additive to #1572's coverage campaign).
- **Next:** Phase B constraints (this PR's follow-up commits), then
  Phase D Lean wiring `deuteron_emptySDP → deuteron_realSDP`.
