# c_8 / c_9 / c_10 silver-anchored closed forms — cross-anchor falsification (2026-06-04)

> **⮕ This falsification is encoded in the authoritative registry**
> [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
> (§3: c_8/c_9/c_10 = EMPIRICAL — silver-anchored, cross-anchor tested). Read
> the registry for the consolidated c_k / d_k status.

> **Finding**: the Pell-Lucas σ-action closed forms for `c_8, c_9, c_10`
> (PR #1793) are **anchor-stable real-q functions** (proton↔muon swing
> 2.4×10⁻⁷ %, well under the §8 1 % threshold) yet **do NOT reproduce the
> substrate-q₀ SDP residual** (miss by 3.4×10³× / 1.5×10⁵× / 6.2×10⁷×).
> They are EXACT only at the silver structural anchor (b² = 7/8). Passing
> the swing sub-test is necessary but **not sufficient** for the
> `canonical` tier; the forms stay `empirical — silver-anchored`. No
> production change.

## What was tested

PR #1793 derived closed forms by extending the documented Pell-Lucas
σ-action pattern (c_4..c_7) by one rung in each parity class:

```
c_8(q)  = c_3²·b⁴ = 4·b⁴   → 49/16   at silver
c_9(q)  = c_3³·b² = -8·b²  → -7       at silver
c_10(q) = c_3²·b⁶ = 4·b⁶   → 343/128  at silver
```

with the canonical Hoefsmit (2,1) parameter
`b²(q) = (q⁴ + q² + 1) / (q² + 1)²` (= 7/8 exactly at q = 1+√2, since the
numerator collapses to 7q² and the denominator to 8q²).

The §8 flip-flop guard requires a passing cross-anchor test before any
rung may leave the `empirical` tier. The registry had recorded these
rungs as "not cross-anchor tested"; this probe runs the test.

## The established cross-anchor facts (PR #1609 infra)

| anchor | q₀ |
|--------|-----|
| proton (m_p) | 1.10997858275… |
| muon (m_μ) | 1.10997859555… |

Anchor separation ≈ **1.28 × 10⁻⁸** (`qou_substrate.constants.q_at` /
`q_muon_at`).

## Result

[`qbeta/qbeta_c8_c10_crossanchor_falsification.py`](../../folio-assistant/computations/qbeta/qbeta_c8_c10_crossanchor_falsification.py)
→ [`qbeta-c8-c10-crossanchor-falsification.witness.json`](../../folio-assistant/computations/qbeta/qbeta-c8-c10-crossanchor-falsification.witness.json)

### Sub-test 1 — §8 literal form swing (proton ↔ muon)

| rung | closed(proton) | closed(muon) | swing |
|------|----------------|--------------|-------|
| c_8 | 2.26624189 | 2.26624189 | −1.58×10⁻⁷ % |
| c_9 | −6.02161691 | −6.02161691 | +7.88×10⁻⁸ % |
| c_10 | 1.70580506 | 1.70580506 | −2.36×10⁻⁷ % |

Max |swing| = **2.4×10⁻⁷ %** ≪ 1 % → the real-q form is **anchor-stable**
(b²(q) is smooth; the anchors differ by only 1.3×10⁻⁸). **PASS.**

### Sub-test 2 — production match vs the q₀ SDP residual

| rung | closed(q₀) | SDP-extracted(q₀) | ratio |
|------|-----------|-------------------|-------|
| c_8 | 2.266 | 7649.1 | 3.4×10³× |
| c_9 | −6.022 | 8.978×10⁵ | 1.5×10⁵× |
| c_10 | 1.706 | 1.054×10⁸ | 6.2×10⁷× |

The closed forms **do not reproduce** the SDP-extracted residual at q₀.
**FAIL.** (The `(R−1)/(b^k·ℏ^{2k})` extraction ladder is hyper-sensitive
/ noise-dominated for k ≥ 8 — PR #1793's own caveat; either way the
O(1) closed forms are nowhere near the extracted values.)

## Interpretation

Canonical = derived-to-precision **and** anchor-stable **and** reproduces
the production residual. The c_8/c_9/c_10 closed forms satisfy the first
two characteristics at the literal level (exact rationals, tiny swing) but
fail the third by 10³–10⁷×. They are **silver-ratio structural
identities**, not q₀ production coefficients.

This is the same shape as the c_3 [3]_q/25 rigidity finding
([`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)):
a smooth real-q form is exact at one structural anchor and rigid
everywhere else, and cannot represent the q₀ residual structure — which,
per CLAUDE.md §"Im(q) at fibre vs observable level", is a fibre-level
object (complex-analytic / root-of-unity), not a real-q O(1) constant.

## Consequences

1. **Tier unchanged.** c_8/c_9/c_10 stay `empirical — silver-anchored`;
   the registry row moves from "not cross-anchor tested" to
   "cross-anchor tested 2026-06-04: anchor-stable but does not reproduce
   the q₀ residual". This *confirms* the labelling rather than promoting
   it — the right §8 outcome.

2. **The silver-ratio result is real but bounded.** The Pell-Lucas
   σ-action closed forms are EXACT at q = 1+√2 (Lean `norm_num`-trivial,
   now built via the Lake mirror `QBetaCnAtSilver.lean`). They are NOT
   q₀ production coefficients. Both statements are true and should be
   stated together.

3. **No production wire.** The §8 flip-flop guard stands: a proton-anchor
   (or silver-anchor) match is `empirical`, never `canonical`, and a
   passing swing sub-test does not by itself license a wire.

## Cross-refs

- c_8/c_9/c_10 closed forms + silver Lean: PR #1793
- registry status rows: PR #1825 + this branch
- c_3 [3]_q/25 cross-anchor rigidity: [`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`](2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md)
- cross-anchor infra: `qbeta/qbeta_singularity_cross_anchor_probe.py` (PR #1727), `qou_substrate.constants.q_muon_at`
- CLAUDE.md §"Critical framing — Im(q) at fibre vs observable level"
