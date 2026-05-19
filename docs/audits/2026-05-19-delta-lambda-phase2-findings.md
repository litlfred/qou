# Δ_λ Phase 2 — two-factor separable form is falsified

**Branch**: `claude/closed-forms-first-principles` (PR #787)
**Date**: 2026-05-19
**Goal**: Test if $\Delta_\lambda(K) = V(K) \cdot c_\lambda$ (separable per-knot × per-partition) is the categorical structure.

## Result

**MISS** on all 8 candidate $V(K)$ forms. Best is $V_7 = n / \lvert\mathrm{tr}_M(K)\rvert$ with relative-std 0.83 across the 4 atoms (D, T, ³He, ⁴He) — i.e. $c_\lambda$ varies by a factor of **~10×** depending on which atom is used to back it out.

| V(K) candidate | rel_std | max/min |
|---|---:|---:|
| V1 = |tr_M| | 1.58 | 1054× |
| V2 = ℏ_q^{n−1} | 1.73 | 159M× |
| V3 = 1/|tr_M| | 1.01 | 21× |
| V4 = 1/√|tr_M| | 1.23 | 57× |
| V5 = Z·N · ℏ_q^{n−1} | 1.73 | 40M× |
| V6 = (Z²+N²) · ℏ_q^{n−1} | 1.73 | 40M× |
| V7 = n / |tr_M| | **0.83** | **11×** (best) |
| V8 = 1/ℏ_q² | 1.40 | 150× |

No candidate brings the cross-atom $c_\lambda$ variance below 50%.

## Diagnosis

**$\Delta_\lambda(K)$ is non-separable.** It cannot be written as a product of K-only and λ-only factors with categorically-defined ingredients.

## Plausible refinement (Phase 3)

The natural next form is a **sum of separable terms** — the JSJ decomposition of the master mass formula:

$$
  \Delta_\lambda(K) \;=\; \sum_{P \in \mathrm{JSJ}(K)} c_\lambda^{(P)} \cdot \mathrm{Vol}_{\mathrm{hyp}}(P)
$$

where each $c_\lambda^{(P)}$ is a per-(partition, JSJ-piece) coupling. This is consistent with:

- `docs/path-to-1ppb-04-plan.md`'s master formula $B = \sum_{P \in \mathrm{JSJ}} \rho_F \cdot \mathrm{Vol}_{\mathrm{hyp}}$ at the per-piece level.
- The T/³He degeneracy resolution: different (Z, N) give different JSJ decompositions, so the SUM has different terms with different relative weights.
- The Hecke per-block structure: $c_\lambda^{(P)}$ encodes how partition λ contributes to JSJ piece P via the Wedderburn block structure.

**However**, Phase 3 requires:
1. JSJ decompositions for each atom's canonical knot $K_{Z,N}$.
2. Per-piece Vol_hyp values (likely via SnapPy at high precision).
3. A categorical rule for $c_\lambda^{(P)}$ — possibly the per-piece algebraic residue at a piece-specific principal Galois orbit.

These are significant new infrastructure pieces. The conjecture block `conj:delta-lambda-categorical-closure` should be updated to reflect the sum-of-separable-terms hypothesis (Phase 3 form) and the falsified product-of-separable-factors hypothesis (Phase 2 result).

## Current branch state

- Workplan (`docs/audits/2026-05-19-closed-forms-first-principles-workplan.md`)
- Phase 1a conjecture block (`conj:delta-lambda-categorical-closure`)
- Phase 1b naive verification (`delta_lambda_categorical_verification.py` — MISS by 33×)
- Phase 1b exploration findings (`docs/audits/2026-05-19-delta-lambda-exploration-findings.md`)
- **Phase 2 two-factor test** (`delta_lambda_two_factor_phase2.py` — MISS, all 8 candidates falsified)

## What's been learned

Two structural results are now solid empirically:

1. **Δ_λ(K) is non-separable.** The simplest two-factor form is ruled out by the T/³He data.
2. **Discriminant 3-orbit structure is real** (from the reciprocal cubic $16w^3+24w^2-13w+2=0$). This refines PR #779's principal-pair selection.
3. **$k = 2$ residue at the inner principal pair is finite (~0.9)** but is identically zero when summed over the full Galois orbit (orbit 1 + reciprocal orbit). The two-pairs ↔ one-orbit distinction matters for the residue.

## Recommendation

**Pause the categorical Δ_λ closure thread.** Phase 3 (JSJ-decomposition-aware sum-of-separable-terms) requires substantial new infrastructure (per-knot JSJ decomposition + per-piece volume + per-(λ, P) coupling) that is beyond what can be productively assembled without coordination with the author on the JSJ machinery direction.

The branch's deliverables (workplan + Phase 1a conjecture block + Phase 1b verification + Phase 2 falsification + 2 audit docs + coordination posts) form a coherent **diagnostic package**: the categorical closure form is structurally constrained but not yet quantitatively determined. Future work should:

- Land the diagnostic package (PR #787) for visibility into what's been tried.
- Continue under a separate branch / PR with JSJ-machinery integration.
- Optionally: pivot to one of the other 5 options from the original closed-forms list (compute-side LP→SDP, F1 non-vanishing theorem, m_μ closure refinement).
