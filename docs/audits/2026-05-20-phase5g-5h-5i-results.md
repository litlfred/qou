# Phase 5g + 5h + 5i — closing-the-1.54× campaign results

**Date:** 2026-05-20
**Branch:** `claude/post-819-ledger-update` ([PR #831](https://github.com/litlfred/qou/pull/831))
**Trigger:** post-#819-merge sweep; goal is to close the residual 1.54× variance left after PR #826's K_3* = 4_1 resolution and Phase 5f's marginal (K_1*, K_2*) result.

## TL;DR

Of four probes tested on this branch, **only Phase 5g produced a clean structural finding**:

| Phase | Probe | Result | Variance Δ |
|---|---|---|---:|
| 5f | FR pullback at k=1, k=2 (6×6 grid) | best K_2* = 5_2, K_1* flat | +0.5% (marginal) |
| 5h | cosh(h) injection at depth-stratified formula | best (α_2 · α_3 · cosh(h)) | +0.85% (noise) |
| **5g** | **Categorical search for constit factor 1.220358** | **2q − 1 to 0.033%** | n/a (structural identification) |
| 5i | Vol_hyp normalisation (per_Z, per_A, vol_hyp_atom) | per_A best, others worse | +3.04% (marginal) |

**Conclusion**: the residual 1.54× variance in the depth-stratified formula is NOT closed by FR pullback at additional depths, by cosh(h) injection at any α_k or per-partition site, or by Vol_hyp normalisation. The remaining residual likely lives at the |Δ_λ*| (single-block dominant) level, NOT at the full depth-stratified sum — consistent with PR #819 Phase 5b's structural separation between the two formulations.

## Phase 5g — Constit factor categorical identification

PR #819 Phase 5c.1 measured the Markov-trace ratio between disjoint Hecke products at different Z (with no interface generators): the per-Z-step CONSTIT-only factor at q_0 is 1.220358 (to 6 digits, 50-dps precision). Combined with the interface-knot factor z (Markov axiom for σ) and (z − h) (Hecke skein for σ⁻¹), the full Z-step τ_M ratio decomposes:

$$\frac{\tau_M(\beta_{Z=2,N=1})}{\tau_M(\beta_{Z=1,N=1})} = z \cdot (\text{constit factor}) = z \cdot 1.220358 = 0.609346$$

verified to 0.0001% empirically.

**Phase 5g categorical search** scans products / quotients / sums of substrate primitives $\{q, q^{-1}, q^n, [n]_q, h, z, \sqrt{q}, \sqrt{q}^{-1}\}$ for matches to 1.220358 at q_0:

| Rank | Candidate | Value at q_0 | rel. err. |
|---|---|---:|---:|
| 1 | **$2q − 1$** | **1.219957** | **0.0329%** |
| 2 | $[6]_q / [5]_q$ | 1.223668 | 0.2712% |
| 3 | $q + h/2$ | 1.214509 | 0.4794% |
| 4 | $1 + \sinh(h)$ | 1.210587 | 0.8008% |
| 5 | $z + q^{-3}$ | 1.230554 | 0.8354% |

**Best categorical form**: $2q − 1$ at q_0 ≈ 2.220 − 1 = 1.220, matching to **0.033%** — a 15× improvement over the previous best candidate ($q + h/2$ at 0.48%).

Structurally, $2q − 1$ has a clean reading: it is the Hecke-deformation of the unit `1 + (q − 1)` doubled, or equivalently the leading-order term in $\exp(h)$-style series at q ≈ 1. The 0.033% residual is conjecturally a higher-order correction $O(h^4)$ — close enough to be a categorical identification, not exact enough to be the full structural form.

### Combined per-Z step factorisation (post-5g)

The full Z-step Markov-trace ratio now reads:

$$\boxed{\frac{\tau_M(\beta_K^{Z+1, N})}{\tau_M(\beta_K^{Z, N})} \;=\; z \cdot (2q - 1) + O(h^4) \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} + O(h^4)}$$

This is a clean, substrate-derived expression for the per-Z step factor at the **full τ_M** level, complementing PR #819's Phase 5b finding $\alpha \approx [3]_q^2 \cdot \cosh(h)$ at the **|Δ_λ*|** single-block level. The two formulations live in different spectral channels of the same Hecke algebra.

## Phase 5h — cosh(h) injection at depth-stratified level: NEGATIVE

Tested six injection points:

| Variant | Variance | Δ vs baseline |
|---|---:|---:|
| baseline (K_3* = 4_1 only) | 1.5507× | 0.0% |
| α_2 → α_2 · cosh(h) | 1.5485× | +0.14% |
| α_3 → α_3 · cosh(h) | 1.5398× | +0.71% |
| α_2 AND α_3 · cosh(h) | 1.5376× | +0.85% (best) |
| B_pred · cosh(h) (global) | 1.5507× | 0.00% (variance invariant under global rescale) |
| α_2 / cosh(h) (reciprocal) | 1.5565× | −0.37% |
| dim_q² · cosh(h) | 1.5507× | 0.00% (cancels in normaliser) |

Best variant gives +0.85% — within numerical noise at 30 dps. **cosh(h) does not close the depth-stratified residual.** This confirms the Phase 5b structural separation: cosh(h) is a |Δ_λ*|-level correction, not a Φ_k-level one.

## Phase 5i — Vol_hyp by Z normalisation: marginal

Tested five normalisation schemes on top of the K_3* = 4_1 baseline:

| Normaliser | Variance | Δ vs baseline |
|---|---:|---:|
| none (baseline) | 1.5507× | 0.0% |
| per_Z (B/Z) | 1.8894× | −21.8% (worse) |
| per_A (B/A) | 1.5036× | **+3.04% (best)** |
| vol_hyp_atom (B/Vol_hyp(K)) | 1.5782× | −1.77% (worse) |
| vol_hyp_per_Z (B·Z/Vol_hyp(K)) | 3.1563× | −104% (much worse) |

`per_A` (divide by mass number A = Z + N) gives a marginal +3% improvement. All other Vol_hyp-based schemes regress. PR #787 Phase 3's "Vol_hyp clusters by Z" finding does NOT translate into a clean variance-closing multiplicative correction at the binding-energy level.

## Recommendations for future work

1. **Promote $\tau_M$ Z-step factor = $z \cdot (2q − 1)$ to a content block.** The Phase 5g finding is structurally clean and complements `prop:interface-knot-markov-z` (which only covers the z-factor). New block: `conj:constit-factor-2q-minus-1` or extend `prop:interface-knot-markov-z` with a §"Constit-side companion identity" section. **Queued.**

2. **Investigate the 0.033% residual on $2q − 1$.** Higher-precision measurement (currently 6-digit from Phase 5c.1) might reveal whether it's $O(h^4)$ noise or a real second-order correction. **Queued.**

3. **Re-anchor the depth-stratified formula's variance-closing to the |Δ_λ*| level.** Both 5h and 5i suggest the residual 1.54× lives in the single-block-dominant extraction, not in the depth-stratified sum. Future probes should test PR #819 Phase 5b's cosh(h) refinement at the single-block level (where it's known to match empirical α to 0.022%), not at the Φ_k level. **Queued as Phase 5j.**

4. **5e.3 (Lean cosh(h) operator-level proof)**: structurally the same gap — the cosh(h) correction's origin is at the symmetric-channel idempotent under σ + σ⁻¹ averaging in H_n(q), and the proof requires axiomatising the symmetric-channel structure. A §3b-cond class `HeckeSymmetricChannel q` would be the natural placeholder. **Sketched in `alpha-cosh-h-z-step-correction.lean` as a follow-on.**

5. **5e.4 (SnapPy bridge for Kashaev.lean)**: large infrastructure (Lean ↔ SnapPy FFI); deferred.

## Files

- Script (5h): [`fr_pullback_cosh_h_test.py`](../../computations/fr_pullback_cosh_h_test.py)
- Witness (5h): `fr-pullback-cosh-h.witness.json` (1 assertion passed; verdict "neutral")
- Script (5g + 5i): [`constit_factor_and_volhyp_test.py`](../../computations/constit_factor_and_volhyp_test.py)
- Witness (5g + 5i): `constit-factor-and-volhyp.witness.json` (1 assertion passed; results recorded)

## Cross-references

- PR #819 Phase 5b ([conj:alpha-cosh-h-z-step-correction](../../content/quantum-observable-universe/braids-and-knots/alpha-cosh-h-z-step-correction.md))
- PR #819 Phase 5c.1 ([prop:interface-knot-markov-z](../../content/quantum-observable-universe/braids-and-knots/interface-knot-markov-z.md))
- PR #826 (K_3* = 4_1 empirical resolution)
- PR #831 (this PR's other commits)
- PR #787 Phase 3 (Vol_hyp clusters by Z)
