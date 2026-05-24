# Higgs categorical formula — research-path for the residual ~0.5%

**Date:** 2026-05-24
**Trigger:** Item 4 from PR #1181 pending list: "Higgs formula residual ~0.5% — PR #1167 NEGATIVE on single h^6; needs deeper Yekutieli MI work"
**Status:** Audit doc identifying the research-grade path. NOT a derivation.

## §1. The current state

Per PR [#1159](https://github.com/litlfred/qou/pull/1159) (constructed Higgs categorical formula):

$$m_H = m_W \cdot \frac{P_4(h_0)}{P_2(h_0)} \cdot \frac{6}{5} \cdot \left(1 - h_0^4 \cdot \frac{\text{Vol}(\mathcal{B}_3)}{4}\right)$$

| anchor | predicted m_H | dev |
|---|---:|---:|
| from m_W | 124.26 GeV | −0.67% |
| from m_Z | 125.64 GeV | +0.44% |

Residual ~0.5% per anchor.

PR [#1167](https://github.com/litlfred/qou/pull/1167) probed h^6 closure: **NEGATIVE.** Required C_6 differs significantly between W and Z anchors. Single-coefficient h^6 term cannot close the residual.

## §2. Why h^6 alone fails

The W and Z anchors have DIFFERENT required C_6 because the W and Z are predicting m_H via DIFFERENT chains:
- W chain: m_H = m_W · (P_4/P_2) · ...
- Z chain: m_H = m_Z · (P_4/P_3) · ...

If these two chains agreed perfectly, the formula would close. They differ by 1.11% — the same gap as the W/Z anchor asymmetry identified in PR #1176 Item 3.

**Diagnosis**: the residual is NOT a missing higher-order h^k correction. It's a propagated artifact of the WZ anchor asymmetry, which is itself the SM electroweak mixing not captured by the H_2(q) trace formula alone.

## §3. Research-grade closure paths

### Path A: Direct categorical mass formulas (no anchor)

Construct categorical formulas for m_W, m_Z, m_H individually from substrate, without using one mass as anchor for another. Per PR #1176 Item 1:

$$m_W = (\pi \cdot h_0) \cdot v_{\text{substrate}} / 2$$

If v_substrate is independently derived, m_W is independent. Then m_H from a similar chain (with Higgs self-coupling λ instead of g):

$$m_H = \sqrt{2 \lambda_{\text{substrate}}} \cdot v_{\text{substrate}}$$

Both formulas reduce to substrate quantities WITHOUT anchor-based propagation. The residual collapses to whatever precision the substrate derivations achieve.

**Effort**: research-grade (1-2 weeks). Requires:
1. Substrate derivation of v (declined 2026-05-08; would need reopening)
2. Substrate derivation of g (PR #1143 empirical g ≈ π·h_0 at +0.26%; categorical proof open)
3. Substrate derivation of λ (no current candidate)

### Path B: Yekutieli MI tessellation at jet grade k ≥ 3

Per PR #1100's audit `2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md` §2:
| jet grade | tessellation k | cells | h-order |
|---:|---:|---:|---:|
| 0 | coarsest | 1 | leading |
| 1 | first refinement | 4 | h² |
| 2 | second refinement | 16 | h^4 |
| **3** | **third refinement** | **64** | **h^6** |
| j | k=j | 4^j | h^{2j} |

The h^6 correction structurally exists at Yekutieli MI tessellation level 3 (64 cells). PR #1167 tried to FIT a single h^6 coefficient empirically and failed (W/Z inconsistency).

The categorical derivation would:
1. Compute the Yekutieli MI Riemann product at k=3 explicitly (64-cell tessellation of 𝓑_3 with appropriate refinement)
2. Extract the h^6 coefficient as a STRUCTURAL value (not anchor-dependent)
3. Apply to Higgs (T(2,8)) directly

**Effort**: research-grade (~1 month). The k=2 calculation (h^4) was already partial; k=3 adds substantial combinatorial complexity.

### Path C: Bar-anti-symmetric Q_m channel contribution

Per PR #1181 Pythagorean identity:

$$P_m^2 - Q_m^2 = \frac{1}{[2]_q^2}$$

If the "true" mass formula uses BOTH P_m and Q_m components (not just P_m), then the residual ~0.5% might come from the Q_m contribution to the W or Z (where it's nonzero) but not to the Higgs (where it might be different).

For the Higgs T(2, 8):
- Q_4(h_0) = sinh(9 η_0) / (2 cosh η_0) ≈ 0.537 (per PR #1153)
- This is a non-negligible component

If the mass formula is something like:
$$m_K = m_e \cdot \sqrt{P^2 + Q^2}_{\text{appropriate}} \cdot \text{factor}$$

then the W (small Q_2) and H (larger Q_4) get different contributions, and the residual reflects this.

**Effort**: research-grade (~1-2 weeks). Requires identifying how Q_m enters the mass formula structurally.

### Path D: Direct H_4(q) → H_2(q) bridge

The Higgs is T(2, 8) in B_2 (H_2(q)). But the FRAMEWORK's derivation of the 6/5 ratio uses H_4(q) (5 partitions). The bridge between H_2 and H_4 trace structures might supply the missing 0.5%.

Specifically: the c_{2j}(T(2, 2m)) = C(m+j, 2j)/2 pattern lives at H_2(q), but the 6/5 = |S_3|/|partitions(4)| invokes |partitions(4)| from H_4. The cross-algebra bridge is implicit.

**Effort**: research-grade (~2 weeks). Less obvious than A/B/C but potentially more elegant.

## §4. Honest assessment

All four paths are research-grade open. The current state:
- Higgs formula matches within 1% (constructed, validated)
- Residual ~0.5% is NOT noise (W/Z anchor asymmetry → 1% from electroweak mixing)
- No path is below 1-2 weeks of focused work
- Path A requires reopening substrate-derivation of v (declined 2026-05-08)

**Recommendation**: keep the formula at its current "structurally grounded, empirically validated within 1%" status. Don't pursue closure to higher precision without a specific research-grade allocation. The remaining ~0.5% is the framework's precision boundary at the current categorical-chain depth.

## §5. What this audit ENABLES

The four paths are now documented; future agents have specific entry points:
- Path A → reopen substrate-derivation of v (policy decision)
- Path B → Yekutieli MI k=3 computation (concrete research target)
- Path C → Q_m channel contribution analysis (extends PR #1181)
- Path D → H_4 ↔ H_2 bridge (the cross-algebra structural step)

Documenting these as audit makes the open frontiers EXPLICIT rather than hidden in commit messages.

## §6. Cross-references

- [PR #1159](https://github.com/litlfred/qou/pull/1159) — Higgs formula constructed
- [PR #1167](https://github.com/litlfred/qou/pull/1167) — h^6 single-coefficient closure NEGATIVE
- [PR #1176](https://github.com/litlfred/qou/pull/1176) — W/Z anchor asymmetry analysis
- [PR #1181](https://github.com/litlfred/qou/pull/1181) — Pythagorean identity + Q_m
- [`2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`](2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md) — jet-grade tessellation
- [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md) — Yekutieli MI machinery
- [`content/quantum-observable-universe/lean/QOU/BraidKnot/HiggsCategoricalMassFormula.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/HiggsCategoricalMassFormula.lean) — Lean encoding (PR #1164)
