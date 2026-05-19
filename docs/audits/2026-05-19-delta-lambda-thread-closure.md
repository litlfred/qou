# Δ_λ thread — final summary and closure

**Branch**: `claude/closed-forms-first-principles` ([PR #787](https://github.com/litlfred/qou/pull/787))
**Date**: 2026-05-19
**Status**: thread paused at PR #787; diagnostic package is the deliverable.

## What was tested

Per PR #777's open Δ_λ-gate question. The categorical closure conjecture:

$$
  \Delta_\lambda(K) \;:=\; V(K) \cdot \tau_q\!\Bigl(\sum_{p \in \mathcal{O}^{(\lambda)}}
    \mathrm{Res}^{\mathrm{alg}}_p \bigl(\lambda^{(k(\lambda))}_{\mathrm{SW}}\bigr)\Bigr)
$$

tested across 4 atoms (D, T, ³He, ⁴He) under 5 progressively-refined hypothesis classes.

## Five negatives, three structural findings

| Hypothesis | Tested in | Result |
|---|---|---|
| H1: Δ_λ = const per atom (Phase 1b naive) | `delta_lambda_categorical_verification.py` | Miss by ~33× on D |
| H2: Δ_λ = V(K) · c_λ (Phase 2 two-factor separable) | `delta_lambda_two_factor_phase2.py` | Miss; 8 V(K) candidates fail (best rel_std 0.83) |
| H3: V(K) = Vol_hyp(K) (Phase 3 JSJ Vol) | `delta_lambda_jsj_phase3.py` | Miss; |Δ*|/Vol varies 1.8 → 275 |
| H4: Vol_hyp(K) matches a known SnapPy census manifold | census lookup (5k manifolds + link census) | No match |
| H5: Canonical braid closures have legitimate hyperbolic structure | SnapPy `solution_type` probe | **All 4 atoms: `contains degenerate tetrahedra`** |

**Structural findings** (preserved even though hypotheses failed):

1. **Discriminant 3-orbit factorisation over ℚ** via the reciprocal cubic $16w^3 + 24w^2 - 13w + 2 = 0$ — refines PR #779's "principal pair". (Phase 1b exploration.)
2. **$k = 2$ residue identically zero** across all 3 orbits — hard categorical constraint on the k(λ) mapping. (Phase 1b exploration.)
3. **Z-clustering of SnapPy pseudo-volume** — Vol(D) = Vol(T) = 12.776 and Vol(³He) = Vol(⁴He) = 12.554 to 6 sig figs each. **Not legitimate hyperbolic volumes** (degenerate tetrahedra), but a real combinatorial-braid invariant that depends only on Z. (Phase 3 + Phase 3b.)

## Why H5 is the deepest negative

SnapPy reports `solution_type: contains degenerate tetrahedra` for all 4 canonical braid closures. This means:

- The hyperbolic structure SnapPy attempts to find for each braid closure does **not converge** — some tetrahedra in the triangulation collapse to zero volume.
- The reported "volume" values (12.776 / 12.554) are SnapPy's pseudo-volume sum across the degenerate triangulation — they encode a combinatorial-braid invariant of the simplification path, NOT a Mostow-rigidity-protected hyperbolic invariant.
- Identification against the SnapPy census returns **none** for all 4 atoms — these manifolds (if they are manifolds in the hyperbolic sense) are not in the standard census.

**Consequence**: the master formula $B(K) = \sum_{P \in \mathrm{JSJ}(K)} \rho_F(P) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P)$ (from `docs/path-to-1ppb-04-plan.md`) **cannot be straightforwardly evaluated** on canonical atomic braids via SnapPy alone. Either:

- The canonical braids must be modified (e.g., the averaged-crossings → σ⁺ convention is wrong) to recover hyperbolic structure, OR
- The closure form for $\Delta_\lambda$ doesn't actually involve $\mathrm{Vol}_{\mathrm{hyp}}$ but a different (combinatorial) per-knot invariant that SnapPy's pseudo-volume happens to compute as a side-effect.

## Recommendation

**Pause the Δ_λ thread at PR #787 as a diagnostic package**:

- Workplan ([2026-05-19-closed-forms-first-principles-workplan.md](docs/audits/2026-05-19-closed-forms-first-principles-workplan.md))
- Conjecture block ([conj:delta-lambda-categorical-closure](content/quantum-observable-universe/descartes-universe/delta-lambda-categorical-closure.md))
- Phase 1b naive form (negative)
- Phase 1b exploration findings (3 categorical structural results)
- Phase 2 two-factor (negative)
- Phase 3 JSJ Vol via SnapPy (negative — Z-clustering finding)
- Phase 3b census + Seifert probe (no match; degenerate tetrahedra)
- This closure summary

The branch's contribution is **mapping the landscape of failures and finding the structural constraints**. Future Δ_λ-closure work should:

1. Resolve the canonical-braid-not-hyperbolic problem (likely: the averaged-crossings convention `0.5·(σ + σ⁻¹)` needs to be interpreted as a quantum/probabilistic mixture, not as a topological closure).
2. Identify the per-Wedderburn-block × per-JSJ-piece coupling rule (the "$\pi_\lambda^{(P)}$" in my Phase 2 ledger note) — this is not in main yet.
3. Compute Seifert-piece quantum invariants (Casson, Reidemeister torsion, per-piece quantum-trace) — also not in main.

These are substantial new infrastructure pieces. The diagnostic package on PR #787 saves future authors from re-attempting the 5 already-falsified hypotheses.

## Pivot options for follow-up work

Per the original 6-option closed-forms list, with B (Δ_λ closure) now paused:

| Option | Description | Effort | Yield |
|---|---|---|---|
| C | m_μ closure (6.5× → 100×) | small-medium | First L2 sub-empirical success |
| D | LP → SDP gluon decoration (mass-1ppm-workplan §2.1) | medium | ~1 MeV on D |
| E | F1 non-vanishing Lean theorem (`categorical_dq_squared_nonvanishing`) | medium-large | Completes d²A categorical story |
| F | Coordinate with PR #781 mass-table alignment | small | Downstream consumer |
| (B revival) | Resolve the canonical-braid-not-hyperbolic problem first | large | Reopens Δ_λ thread |

**Most strategic**: C (m_μ) is the cheapest path to the first L2 sub-empirical success. E (F1) is independent of L2 progress and completes a different categorical thread.
