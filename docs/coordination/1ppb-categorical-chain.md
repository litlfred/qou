# Coordination ledger: 1 ppb categorical-chain frontier

Tracking PRs working toward the 1 ppb $Q_\beta$ / mass-table goal.

## Scope map (2026-05-17)

| PR | Branch | Author | Role |
|---|---|---|---|
| [#665](https://github.com/litlfred/qou/pull/665) | `claude/knot-volumes-review-Pgt8o` | claude (this session) | N=4 + σ_1 + n-strand foundation + scaffolds |
| [#672](https://github.com/litlfred/qou/pull/672) | `claude/post-665-open-rd-hoefsmit-matrices` | claude (this session) | R&D inventory + YB d_1↔d_2 finding |
| [#664](https://github.com/litlfred/qou/pull/664) | `claude/post-662-c3-chain-anti-staleness` | claude (other session) | `prop:hopf-jones-c3-categorical` (alternate c_3 = −2 proof) |
| [#671](https://github.com/litlfred/qou/pull/671) | `claude/post-670-story-b-mp-c5-c6` | claude (other session) | Story B forced audit + m_p chain closure gap |
| [#663](https://github.com/litlfred/qou/pull/663) | `claude/isotope-mass-witness-data-x5lCh` | claude (other session) | isotope-mass-table + anti-staleness infra |

## Classification

| pair | overlap | dependency | cherry-pick |
|---|---|---|---|
| #665 ↔ #672 | HIGH (#672 follows #665) | #672 depends on #665 | — |
| #665 ↔ #664 | HIGH (same c_3 = −2, different proof paths) | independent | none planned; cross-ref both after merge |
| #665 ↔ #671 | MEDIUM (same Story B framing) | independent | none |
| #665 ↔ #663 | LOW (different files, different topic) | #663 consumes substrate Q_β; could swap to N=4 once #665 lands | none |
| #672 ↔ #664 | MEDIUM (#672 documents YB anomaly; #664 may implicitly need YB) | independent | none |

## Coordination comments posted

- [#664 — coordination from #665+#672](https://github.com/litlfred/qou/pull/664#issuecomment-4469105688)
- [#671 — coordination from #665+#672](https://github.com/litlfred/qou/pull/671#issuecomment-4469149330)
- [#663 — Q_β substrate swap opportunity](https://github.com/litlfred/qou/pull/663#issuecomment-4468003754) (earlier)

## Cross-PR findings affecting siblings

### YB cubic d_1↔d_2 anomaly (PR #672)

Symbolic computation shows the chapter `hoefsmit_sigma1` matrices
fail YB cubic with `σ_0 = diag(q, −q⁻¹)`. Analytical fix: swap
`hoefsmit_d1` and `hoefsmit_d2` in
`hoefsmit-V21-cos-symmetrization.lean`. Zero downstream regressions
(basis-permutation preserves all scalar invariants).

**Implications for siblings**:
- #664: Step 2 ("Frobenius selection picks V_(2,2,2) at order h⁶")
  may or may not depend on YB-compatible σ_1 conventions. Coordination
  comment posted asking; awaiting response.
- #665: cross-PR fix commit `df5621609` removes the vacuous
  `yangBaxter_H3 := ⟨0, rfl⟩` instance to avoid asserting a falsehood
  under current conventions.

## Open questions for the author

1. **Q_β substrate swap on #663**: ship #663 as-is with `form_a_cos`
   (residual +306 ppm), or wait for #665 to land then swap to the
   N=4 ladder (residual ~7e-6 ppm)?
2. **c_3 cross-references**: after #665 and #664 both land, should
   `prop:q-beta-c3-hopf-three-fold-markov` (#665) cite
   `prop:hopf-jones-c3-categorical` (#664) as upstream, or vice-versa?

## Next concrete task (non-overlapping)

Await Gemini/Copilot review responses on #665 and #672; address as
they come in. R&D items 1-5 (from #672's inventory) are queued for
follow-up branches; none touch sibling PR scopes.

## 2026-05-19 — Δ_λ categorical closure (branch `claude/closed-forms-first-principles`, no PR)

| Date | Branch / PR | Phase | Status | Cherry-pick |
|---|---|---|---|---|
| 2026-05-19 | `claude/closed-forms-first-principles` (no PR) | Phase 1a — conjecture block | landed `66c655ed` | `conj:delta-lambda-categorical-closure` content triple |
| 2026-05-19 | same | Phase 1b — verification on deuteron | landed `8da9ca67`; **NEGATIVE** — naive form misses by 33× | `delta_lambda_categorical_verification.py` + witness |
| 2026-05-19 | same | Δ_λ exploration | landed `7f82b0c9` | 3 Galois orbits via reciprocal cubic $16w^3+24w^2-13w+2=0$; $k=2$-residue-zero anomaly; per-knot factor required (T/³He degeneracy falsifies universal-c) |

**Findings load-bearing for the 1ppb / 1ppm thread:**

1. **Δ_λ depends on knot K beyond χ^λ.** Cross-atom test: T (c=20.7) vs ³He (c=7.14) at same n=9. Universal-c hypothesis falsified. Δ_λ closure requires a per-knot factor (likely JSJ volume).

2. **Discriminant 3-orbit structure** (palindromic Δ(z) → reciprocal cubic) is the categorical refinement of PR #779's "principal pair". 3 orbits available for per-block selection.

3. **$k=2$ residue vanishes** identically across all 3 orbits. Constrains the k(λ) mapping to $\{0, 1, 3\}$.

**Proposed Phase 2 closure form:**

$$\Delta_\lambda(K) = \mathrm{Vol}_{\mathrm{hyp}}^{(\lambda)}(K) \cdot \tau_q\!\Bigl(\sum_{p \in \mathcal{O}^{(\lambda)}} \mathrm{Res}^{\mathrm{alg}}_p (\lambda^{(k(\lambda))}_{\mathrm{SW}})\Bigr)$$

**Coordination posts:**
- [PR #777 comment](https://github.com/litlfred/qou/pull/777) — intent + 2 asks
- [PR #781 comment](https://github.com/litlfred/qou/pull/781) — light-touch downstream-consumer notice

**Holding** Phase 2 until PR #777's owner confirms (i) the closure is outside the 6 banned fit ansätze and (ii) PR #708's `Vol_hyp^(λ)(K)` machinery is accessible.

## 2026-05-19 — Δ_λ Phase 2 + Phase 3 (branch `claude/closed-forms-first-principles`, [PR #787](https://github.com/litlfred/qou/pull/787))

| Date | Phase | Status | Cherry-pick |
|---|---|---|---|
| 2026-05-19 | Phase 2 (two-factor V(K)·c_λ) | landed `b4e196e2`; **FALSIFIED** on 8 V(K) candidates | `delta_lambda_two_factor_phase2.py` + falsification doc |
| 2026-05-19 | Phase 3 (JSJ Vol via SnapPy) | landed `b7b11519`; **FALSIFIED** (rel_std 1.4) but reveals **Vol(canonical(K)) clusters by Z** | `delta_lambda_jsj_phase3.py` + Vol_hyp(D)=Vol(T)=12.776; Vol(³He)=Vol(⁴He)=12.554 |
| 2026-05-19 | Coord on #777 | comment posted (this round) | asks #1 (f64-vs-mpmath knot-vol audit) and #2 (per-JSJ-piece quantum-invariant infrastructure) |

**Hard categorical finding (Phase 3):** Vol_hyp of the canonical atomic braid closure is **invariant under adding nucleons at fixed Z**. The N-direction is Seifert-fibered (Vol contribution = 0). Per-N binding-energy structure must live in Seifert-piece quantum invariants, not in the hyperbolic core.

This **constrains** PR #781's Kashaev mass-table formula (ρ_F · Vol_hyp) — same-Z isotopes should use the same Vol per my Phase 3 measurement; if PR #781 assigns different Vol to D vs T (same Z=1), that's a discrepancy worth surfacing.

**Status**: Δ_λ thread **paused** at PR #787 pending owner answers on the per-JSJ-piece-quantum-invariant infrastructure (ask #2). If no such infrastructure, the branch lands as a diagnostic package (3 phases of productive negatives + Z-clustering structural finding) and the thread pivots to another closed-form option.
