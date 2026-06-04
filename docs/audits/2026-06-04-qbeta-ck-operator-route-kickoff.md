# Q_β c_k operator route — bar-even framing + probe-B (N=k reading) spec

**Date:** 2026-06-04
**Branch:** `claude/qbeta-ck-habiro-operator-route-2026-06-04`
**Status:** ROADMAP — the obstruction and the matrix infra are already on main; this records the one new framing (bar-evenness / α_EM contrast) and pins the single open research step (probe B)
**Builds on:** scalar-route obstruction + Stage A matrix infra (PR #1840), precision floor (#1844), α_EM Habiro (#1521)

> **Course-correction note.** An earlier commit on this branch added a
> `qbeta_ck_scalar_reversion_obstruction.py` probe; it **duplicated** the
> already-merged `qbeta_ck_scalar_route_singularity_probe.py` (PR #1840) and was
> removed. The obstruction is established; this doc keeps only the genuinely new
> framing and the open-step specification.

## What is already done (do NOT re-derive)

| Piece | Where | Status |
|---|---|---|
| Scalar route is singular (`u = b·ℏ_q²` ~ `(q−1)²`, no linear term ⇒ `t(u)` needs `u^{1/2}`) | `qbeta_ck_scalar_route_singularity_probe.py` (PR #1840) | done |
| c_k are operator-valued (T_β level structure, not scalar Taylor) | same | done |
| **Stage A** — Hoefsmit `T_β` per Wedderburn block; per-block `Tr ρ_λ(β)`; Wenzl recombination validated against canonical `Δ(net)` at q₀ | `qbeta_hoefsmit_tbeta_matrix_build_probe.py` (PR #1840) | done |
| Per-block symbolic traces | `qbeta_per_block_symbolic.py` | done |
| `c_2 = −1` (scalar, proved) / `c_3 = −2` (bias-corrected) anchors | PR #1786 / #1824 | done |
| Necessity (c_k≥4 below the measured-Q_β floor ⇒ must be derived) | precision floor, #1844 | done |

## The one new framing — bar-evenness sharpens *why* the operator route

The scalar singularity has a clean bar-involution reading that also explains why
the **α_EM** programme succeeded with a *scalar* Habiro element while **Q_β**
cannot:

- `q ↦ q⁻¹` acts on `t = q−1` as `t ↦ −t + O(t²)`. Since `u = b·ℏ_q²` has a
  double zero (`u = b(1)t² + O(t³)`), the reversion needs `u^{1/2}`, so
  `R = ∏(1+c_k u^k)` is a clean **integer-`u`** series **iff `R` is bar-even**
  (even in `t`).
- **α_EM:** `H(q) = [2]_q·(1 − h²α)` is manifestly bar-even (`[2]_q = q+q⁻¹`,
  `h² = (q−q⁻¹)²` are bar-invariant) ⇒ its scalar `u`-series is clean ⇒ the
  scalar identification *worked*.
- **Q_β:** the residual trace-difference is **not** bar-fixed at the archimedean
  level (registry §5; `docs/coordination/1ppq-qbeta.md`) ⇒ odd-in-`t` content ⇒
  the `u^{1/2}` branch is genuinely present ⇒ the scalar `c_k` series is
  singular, and only the **operator-level grading** (which supplies integer
  `u`-powers structurally) recovers the `c_k`.

This is the bar-involution statement of the PR #1840 obstruction; it is the
discriminant between the two programmes, and it is the reason the Hoefsmit `T_β`
construction is *irreducible* for Q_β.

## The single open step — probe B (N=k operator-level reading)

Both the recipe
([`2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md`](2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md))
and Stage A's own docstring defer one step: **how each `N=k` operator correction
enters `T_β`** so that level `N=k` carries `u^k = b^k·ℏ_q^{2k}`. Precise spec:

1. **Define the level grading.** Construct `T_β` from Stage A's `ρ_λ(σ_i)` and
   exhibit a decomposition `T_β = Σ_{N≥0} T_β^{(N)}` in which `T_β^{(N)}` scales
   as `u^N` under the substrate scaling `(b, ℏ_q²) → (s·b, s·ℏ_q²)` — i.e. the
   grading must be by the substrate parameter `u`, **not** by powers of `(q−1)`
   (which is what makes the scalar reversion singular).
2. **Read the ladder.** `R = ∏_k(1 + c_k u^k)` from the graded `Markov`-trace
   `tr_M(T_β) = Σ_λ y_λ Tr T_β^{(N)}_λ`; `c_k` = the `u^k` coefficient of `log R`
   read **off the grading**, never off a scalar `u`-reversion.
3. **Gates (mandatory, stop on failure).** `N=2 ⇒ c_2 = −1` (PR #1786) and
   `N=3 ⇒ c_3 = −2` (PR #1824). A graded reading that misses either gate is
   wrong — debug before trusting `c_4..c_8`.
4. **Failure modes** (recipe §"Failure modes"): `Abs`-branch of `Q_A` valid only
   for `1 < q < 1+√2`; factorial `c_k` blow-up ⇒ the `1/u^k` ill-conditioning
   re-entered; `Δ(net)` convention mismatch ⇒ `Q_β(q₀)` off by O(1).

**This step is research, not a coding task:** the substrate-graded decomposition
of `T_β` is not yet specified anywhere in-tree, and a rushed probe risks emitting
a subtly-wrong `c_k` that passes no structural gate. It should be attacked as a
dedicated formalize-first effort (define the grading + prove the `N=2` gate
first), not bolted on.

## Coordination

- **#1840** owns the obstruction + Stage A matrix infra (this doc does not duplicate either).
- **#1844** (precision floor) — the necessity; this is its constructive sequel.
- **#1521** (α_EM Habiro) — the bar-even template this framing contrasts against.
- **#1839** (residue-A kernel deepening) — overlapping operator/`c_k` work; coordinate before probe B.
