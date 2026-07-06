# Q_β closed forms are LEADING-ORDER approximations, not symbolic identities

**Date:** 2026-05-19
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user direction "prove the closed forms from first-principles categorical machinery" — on this PR.

## TL;DR

The closed forms for c_4..c_7 (`c_3·b⁴`, `-(b²+1/2)`, `4·b²`, `-8`) are **NOT symbolic identities** — they are **leading-order approximations** that match empirical c_k at q_0 to varying precision:

| Rung | Closed form | Empirical at q_0 | Match |
|------|-------------|------------------:|------:|
| c_2 | −1 | (definition) | exact |
| c_3 | −2 = J_Hopf(q=1) | (definition) | exact |
| c_4 | c_3·b⁴ = −2·b⁴ | −1.1435 | **0.9%** ✓ |
| c_5 | −(b² + 1/2) | −1.2229 | 2.4% |
| c_6 | c_3²·b² = 4·b² | +3.4976 | **14%** |
| c_7 | c_3³ = −8 | +57.149 | **86% off** ✗ |

**c_7 = −8 is decisively wrong.** The empirical c_7 = +57 at q_0 differs from the closed-form by 8× in magnitude and opposite sign. The "closed form c_7 = c_3³" is a pattern guess that breaks at N=7.

**c_4 ≈ c_3·b⁴ is the cleanest match** (0.9%); c_5 and c_6 have larger deviations.

## What "prove the closed forms" actually means

The framework's chain for proving c_k:

| Rung | Status | Categorical mechanism |
|------|--------|----------------------|
| c_2 = −1 | **proven** | Factor convention: (1 − b²·ℏ_q⁴) absorbs b² Kashiwara intra-block |
| c_3 = −2 | **proven** | Fact 3 of `q-beta-c3-hopf-three-fold-markov.md`: 2-strand sub-braids of β have Hopf-link Markov closure; J_Hopf(q=1) = −2 |
| c_4 = c_3·b⁴ | **conjectural** | Would need: extension of Fact 3 to k=4 (3-strand sub-braids = β itself, closure = trefoil with J_trefoil(q=1)=−3, NOT −2) |
| c_5 = −(b²+½) | **conjectural** | Would need: identification of categorical source for the "+1/2 Hopf-half offset" |
| c_6 = c_3²·b² | **conjectural** | Would need: 5-strand sub-braid pattern (which doesn't exist in B_3!) |
| c_7 = c_3³ = −8 | **WRONG** | Empirical c_7 = +57 contradicts this form |

## Why "Fact 3 extension to higher k" fails

The framework's Fact 3 (the only proven derivation, for c_3) states:

> At order ℏ_q^(2k), the dominant contribution to τ_M(β_p) − τ_M(β_n) comes from all (n choose k) choices of k-strand sub-braids of β. For each such k-strand sub-braid, the Markov closure is the Hopf link.

For β ∈ B_3, the maximum strand count is 3. So:
- k=2 sub-braids: C(3,2) = 3 of them, closure = Hopf link, J(1) = −2 → c_3 = −2 ✓
- k=3 sub-braids: C(3,3) = 1 (the whole braid), closure = trefoil, J(1) = −3 → c_4 = −3 (predicted by Fact 3)
- k=4 sub-braids: C(3,4) = 0 — DOESN'T EXIST in B_3

So Fact 3 naturally limits to c_3 (k=2) and possibly c_4 (k=3, but gives −3 not c_3·b⁴ = −1.13).

**The framework's Fact 3 is incomplete past c_3.** Higher c_k require:
1. A different categorical mechanism (e.g., spectral-sequence stratification, KLR canonical-basis traces)
2. OR an extension of Fact 3 to NON-sub-braid contributions (multi-loop Kashiwara corrections)

## Numerical evidence the closed forms are approximate

Compute Q_β^cat(q) via the precision-ladder formula with closed forms:

$$
Q_\beta^{\text{cat}}(q) = Q_A(q) \cdot \cos(\alpha - b\hbar_q^2/2) \cdot \prod_{k=2}^{7} (1 + c_k^{\text{closed}}(q) \cdot b^k \cdot \hbar_q^{2k})
$$

At q=q_0 (calibrated), this matches Q_β CODATA. **At q ≠ q_0**, the construction is conjectural. The chain doesn't have an independent Q_β(q) to compare against, so the closed forms can't be FALSIFIED directly — they can only be tested for internal consistency or against new categorical computations.

What we DO see at q=q_0:
- c_4 closed form −2·b⁴ ≈ −1.133, empirical −1.144 (0.9% off)
- c_5 closed form −(b²+½) ≈ −1.253, empirical −1.223 (2.4% off)
- c_6 closed form 4·b² ≈ 3.011, empirical 3.498 (14% off)
- c_7 closed form −8, empirical +57.15 (massively off)

The accumulating residual at higher k (0.9% → 2.4% → 14% → 86%) suggests the closed forms are TRUNCATED — they capture the leading categorical contribution but miss higher-order corrections.

## What ACTUAL proof would require

**For c_4** (best-matched at 0.9%): show that the trefoil closure of β = (σ_1σ_2^{-1})^3's full 3-strand contribution to ℏ_q^8 reduces to J_Hopf(q=1)·b⁴ via a multi-loop Kashiwara decomposition. The b⁴ factor would come from FOUR Kashiwara matrix elements (return amplitude b² squared) on V_(2,1).

**For c_5..c_7:** require either:
1. Khovanov-Rozansky bigraded polynomial of the typed-B_3 braid closure at q=q_0, expanded as polynomial in ℏ_q with c_k coefficients.
2. An explicit categorical-trace formula for τ_M(T_β) where T_β is constructed via the framework's K_K confinement SDP applied with β-decay objective.

Both are research-grade R&D.

## What this audit delivers

1. **Honest assessment**: the closed forms are LEADING-ORDER approximations, with c_4 best and c_7 broken
2. **Categorical status table**: which c_k are proven (c_2, c_3) vs conjectural (c_4..c_7)
3. **Test methodology**: extract c_k from R(q_0) sequentially; compare to closed forms; quantify residual
4. **Concrete next-step requirements**: what categorical computation would prove each closed form

## Cross-references

- [`docs/audits/2026-05-19-qbeta-ladder-sdp-c2-c3-derived.md`](2026-05-19-qbeta-ladder-sdp-c2-c3-derived.md) — c_2, c_3 derivation via SDP-T_β
- [`docs/audits/2026-05-19-qbeta-ladder-closure-path.md`](2026-05-19-qbeta-ladder-closure-path.md) — three-route closure roadmap
- [`docs/audits/2026-05-19-qbeta-ladder-knot-operator-general-statement.md`](2026-05-19-qbeta-ladder-knot-operator-general-statement.md) — general statement on knot operators
- [`content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/braids-and-knots/q-beta-c3-hopf-three-fold-markov.md) — Fact 3 proof for c_3
- [`computations/qbeta/qbeta_decay_sdp_full_ck.py`](../../computations/qbeta/qbeta_decay_sdp_full_ck.py) — full c_k extraction script
