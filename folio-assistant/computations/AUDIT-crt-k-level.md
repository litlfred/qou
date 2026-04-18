# CRT Markov-trace computation audit

## What we are computing (currently)

Function: `crt_markov.markov_trace_symbolic_eval(Z, N, include_inter, m_pp, m_pn, m_nn, q_val)`

Per generator $i$ of $H_{3A}(q)$:
```
a, b := 0, 1
for (c, d) in crossings[i]:
    a, b := a·c·h + a·d + b·c,  a·c + b·d
V_s := z·a + b            # standard channel (2-dim rep (2,1))
```
Result: $\mathrm{tr}_M := \prod_i V_{s,i}$

**This is k = 3 standard-channel-per-generator**, taking product across all generators.
In tower-formula terms, it computes only the descended term $|\Pi V̂|$ — and
only the V_s component, not the full Wedderburn sum V_full.

## What the tower formula requires

From `prop:mass-endomorphism-tower`:

$$\mathfrak{m}(W) = \underbrace{|\Pi V̂_i^{\text{full}}|}_{\text{descended}} + \underbrace{\sum_i \Phi_q(|V̂_i|)}_{\text{single-gen tower}} + \underbrace{z^2 \sum_{|i-j|=1} \Phi_q(|V̂_i V̂_j|)}_{\text{adjacent-pair tower}}$$

where $V̂_i^{\text{full}} = w_{\text{sym}} V_{\text{sym},i} + w_{\text{std}} V_{s,i} + w_{\text{alt}} V_{\text{alt},i}$.

## Missing components

| Component | Status | Impact |
|-----------|--------|--------|
| V_s (std, 2-dim) | ✓ in code | dominant for pair correlations |
| V_sym (1-dim) | ✗ missing | sym-channel asymmetry (parity) |
| V_alt (1-dim) | ✗ missing | alt-channel asymmetry |
| V_full = w·V aggregate | ✗ incorrect (only V_s) | wrong channel mixing |
| Wedderburn weights at H_{3A} | ✗ uses H_3 weights | approximation |
| Σ Φ_q(\|V̂_i\|) | ✗ missing | **~99% of mass** (per mass-endomorphism conj) |
| z²Σ Φ_q(\|V̂_i V̂_j\|) | ✗ missing | adjacent cross-coupling |

## Why |Δm/m|% ~ 0.9% (consistent with missing tower)

The mass-endomorphism conjecture states:
> Single-level Markov trace contributes < 0.5% of total mass.

Our CRT |Δm/m|% = 0.04-0.91% matches this:
- Small atoms (D): near 0.04% — single-level captures most
- Heavy atoms (40Ca): 0.91% — single-level captures ~99.1%, tower gives the other 0.9%
- **The 0.9% IS the missing tower contribution** (B_AME ≈ 0.9% of atomic rest mass)

## Fix priority

1. **V_full replacement**: add V_sym, V_alt accumulation, combine via Wedderburn weights. Easy.
2. **Single-gen Φ_q sum**: add `Σ Phi_q(|V_full_i|)`. Needs careful convergence control.
3. **Adjacent-pair Φ_q sum**: add `z² Σ Phi_q(|V_full_i · V_full_j|)`. Similar.
4. **Full H_{3A} Wedderburn**: sum over all λ ⊢ 3A with correct w_λ. Expensive; use CRT reconstruction.

## k designation

Currently **k = 3, std channel only, descended Markov trace**.
For full tower: **k = 3A per atom**, all Wedderburn blocks summed with correct w_λ.
