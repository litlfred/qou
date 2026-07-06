# Non-abelian Stokes surface→boundary map — proved-pending vs axiom

**Date:** 2026-06-01
**Branch:** `claude/nonabelian-stokes-surface-boundary-2026-06-01` (PR #1633)
**Scope:** complete the Yekutieli surface→boundary Lean derivation
(missing input #3) on top of PR #1627's `braidWordHolonomy`. No fit, no
fabricated proof. Everything **compile-pending** — no Lean toolchain in
this container (network-blocked); the owner must run `lake build QOU`.

Builds on the two just-merged audits naming this as the missing piece:
- `docs/audits/2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md` §4
  ("PROVABLE from existing repo defs" — items 1 and 2).
- `docs/audits/2026-06-01-yekutieli-volume-join-derivation.md` §5
  (missing input #3: "the non-abelian Stokes surface→boundary map, still
  `braidSurfaceMultTrace z n := z^n`").

New file:
[`content/quantum-observable-universe/lean/QOU/BraidKnot/nonabelian_stokes_surface_boundary_stokes.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/nonabelian_stokes_surface_boundary_stokes.lean)
(distinct `-stokes` suffix; added to the `QOU/BraidKnot.lean` aggregator).

---

## What changed since #1627

PR #1627 replaced the toy scalar `braidSurfaceMultTrace z n := z^n` in
`QOU.Mathlib.NonAbelianStokes` with the genuine ordered product
`braidWordHolonomy` (over the per-letter Hecke images), plus
`braidWordHolonomy_append` / `_append_letter` / `_nil` /
`_cyclic_one`. That gave the *machinery*. This branch supplies the
*surface→boundary derivation* that consumes it: the boundary holonomy
IS the braid Hecke image `ρ(β)`, and the q-Reeb phase IS the eigenphase
of the figure-eight operator on `V_(2,1)`.

---

## Lemma-by-lemma status

### Part 1 — boundary holonomy = braid Hecke image (audit item 1)

| Lemma | Status | Tactic / source | Confidence | Statement |
|---|---|---|---|---|
| `braidWordHolonomy_eq_heckeImage` | proved-pending | `rfl` | confident | boundary holonomy = `heckeImage` (the ordered product) |
| `heckeImage_append` | proved-pending | `braidWordHolonomy_append` (#1627) | confident | `ρ(β₁β₂) = ρ(β₁)·ρ(β₂)` (homomorphism, not scalar power) |
| `heckeImage_nil` | proved-pending | `braidWordHolonomy_nil` | confident | `ρ(1) = 1` |
| `heckeImage_append_letter` | proved-pending | `braidWordHolonomy_append_letter` | confident | Markov cocycle `ρ(β·σ_i) = ρ(β)·ρ(σ_i)` |
| `heckeImage_cyclic_one` | proved-pending | `braidWordHolonomy_cyclic_one` | confident | conjugation/class-function under cyclic rotation |
| `toyModel_is_constant_word` | proved-pending | `braidSurfaceMultTrace_eq_braidWordHolonomy_replicate` | confident | the `z^ℓ` toy = degenerate constant word |
| `surfaceOrderedExp_append_letter` | proved-pending **(conditional on §3b-cond class)** | `rw [stokes_reduction, …]` | confident | surface-ordered exp carries the cocycle, GIVEN the Stokes reduction |
| `surfaceOrderedExp_append` | proved-pending **(conditional)** | `rw [stokes_reduction, …]` | confident | surface-ordered exp multiplicative, GIVEN the Stokes reduction |

### Part 2 — q-Reeb phase = eigenphase of `M_{4₁}` on `V_(2,1)` (audit item 2)

| Lemma | Status | Tactic | Confidence | Statement |
|---|---|---|---|---|
| `Mat2.det_mul` | proved-pending | `simp only; ring` | confident | 2×2 Binet `det(MN) = det M · det N` |
| `HoefsmitGen.matrix_det` | proved-pending | `linarith` | confident | generator block det = −1 (eigenvalues `q`, `−q⁻¹`) |
| `HoefsmitGen.matrix_trace` | proved-pending | `ring` | confident | generator block trace = `h = q − q⁻¹` |
| `HoefsmitGen.invMatrix_det` | proved-pending | `nlinarith` | confident | `σ⁻¹` block det = −1 |
| `figureEightOp_det_one` | proved-pending | `det_mul` ×2 + det facts + `ring` | confident | **det M_{4₁} = 1** on V_(2,1) (concrete matrix; not `(−1)^4` numerology) |
| `eigenphase_exists` | proved-pending | `Real.cos_arccos` + `linarith` | confident | ∃θ, `2 cos θ = tr M` for `|tr M| ≤ 2` |
| `eigenvalue_prod_eq_det` | proved-pending | `Complex.exp_add` + `norm_num` | confident | `e^{iθ}·e^{−iθ} = det M` |
| `eigenvalue_sum_eq_trace` | proved-pending | `Complex.exp_mul_I` (Euler) + `ofReal_cos` cast | **unsure** (cast/Euler step may need minor owner tactic tweak) | `e^{iθ} + e^{−iθ} = 2 cos θ = tr M` |
| `figureEight_eigenphase` | proved-pending | composes the three above | confident | full certificate: `e^{±iθ}` ARE the eigenvalues (product 1, sum tr) |

### The genuinely-open piece — KEPT AXIOMATIC (NOT faked)

| Item | Status | Ref |
|---|---|---|
| `YekutieliSurfaceToBoundary.stokes_reduction` | **§3b-cond class field (axiom)** | `[yekutieli2015]` https://doi.org/10.1142/9537 §3 |

The deep non-abelian Stokes theorem — that the *surface-ordered
exponential* of the categorical connection over the Young-diagram braid
surface equals the boundary holonomy — is the load-bearing analytic
input. The repo has **no** Mathlib infrastructure for it (Lie-valued
forms, multiplicative surface integral). It is carried as the single
class hypothesis `stokes_reduction`, never as `:= True` or a fabricated
proof. The two `surfaceOrderedExp_*` lemmas are derived *from* it and so
are honestly conditional (they would be `sorry`-free modulo the one
class instance, per AGENTS.md §3b-cond).

The pre-existing CS/volume correspondence axiom
`chernSimons_volume_correspondence` (in `NonAbelianStokes.lean`, added by
#1627, cited to Kashaev/Murakami–Murakami) is the *other* genuinely-open
input (Volume Conjecture); this branch does not touch it.

---

## What this closes vs. what stays open

**Closed (surface→boundary algebraic + finite-matrix pieces):**
- The boundary holonomy is the braid Hecke image `ρ(β)` and carries the
  full Markov/conjugation structure — a homomorphism, not the toy `z^ℓ`
  scalar.
- The q-Reeb phase is rigorously the eigenphase of a concrete real 2×2
  Hoefsmit block: det = 1, real trace, eigenvalues `e^{±iθ}` with
  `2 cos θ = tr`. This is strictly stronger than the existing
  `figure-eight-reeb-rotation.lean` (`(2:ℕ)=2` filler).

**Stays open (deep analytic / categorical input):**
- The non-abelian Stokes theorem itself (surface-ordered exp = boundary
  holonomy) — `[yekutieli2015]` §3, no Mathlib infra. **Axiom.**
- The CS/volume correspondence (boundary-holonomy trace → `Vol(K)`) —
  Volume Conjecture, open in general. Untouched here (lives in #1627's
  `chernSimons_volume_correspondence`).
- The A-vs-B volume reconciliation (`8G` vs `ln|tr_M|`) and the
  per-crossing `V̂_i` transfer chain — sibling branches
  `claude/volume-def-reconcile-8g-vs-trm-2026-06-01` (item 1) and
  `claude/vhat-per-crossing-transfer-chain-2026-06-01` (item 2).

---

## Discipline notes

- **Compile-pending on EVERYTHING.** No Lean toolchain available
  (`lean_diagnostic_messages` reports "not found in any Lean project").
  Nothing claimed proven without a build. The `eigenvalue_sum_eq_trace`
  Euler/cast step is the single proof flagged **unsure**; all others
  reduce to `ring` / `linarith` / `norm_num` / reuse of #1627 lemmas and
  are high-confidence.
- No theorem weakened to `:= True` / `rfl`-on-trivial. Every `Prop` is
  content-bearing; the only axiom is the named Yekutieli class field
  with a `-- Ref:` / docstring citation.
- Branched from a commit containing #1627. If `main`'s tip diverges,
  rebase before merge.
