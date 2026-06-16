# F_n categorical derivation — scope analysis + new structural result

**Date:** 2026-05-17
**Branch:** `claude/post-670-story-b-mp-c5-c6`
**Status:** Per user request "do F_3, F_n categorical derivation". Ships
a substantive new structural result on the canonical Markov trace of the
Hopf+ braid, and surfaces the gap between bare-Markov Taylor
coefficients and the framework's claimed F_n values.

## Substantive new result — closed form for `tr_M(σ_1²)`

Computed via `markov_trace_canonical.tr_M_word((1,1), n, z, h)` for
n = 3, 4, 5, 6 (all give identical result, confirming Markov-
invariance):

$$
\boxed{\quad
  \mathrm{tr}_M(\sigma_1^2)
  \;=\; \frac{q^{5/2} - q^{1/2} + q^2 + q}{q^2 + q}
  \;=\; 1 + \frac{q - 1}{q^{1/2}}
  \;=\; 1 + \varepsilon \cdot (1+\varepsilon)^{-1/2}
\quad}
$$

where $\varepsilon = q - 1$.

This is verified **symbolically** (the difference between the
implementation's output and the closed form is zero in sympy).

## Taylor expansion at q = 1 + ε

Expanding $\mathrm{tr}_M(\sigma_1^2) - 1 = \varepsilon \cdot (1+\varepsilon)^{-1/2}$
gives the binomial series:

| k | ε^k coefficient | binomial form |
|---:|---:|---|
| 0 | 1 | — |
| 1 | 1 | C(-1/2, 0) |
| 2 | -1/2 | C(-1/2, 1) |
| 3 | 3/8 | C(-1/2, 2) |
| 4 | -5/16 | C(-1/2, 3) |
| 5 | 35/128 | C(-1/2, 4) |
| 6 | -63/256 | C(-1/2, 5) |
| 7 | 231/1024 | C(-1/2, 6) |
| 8 | -429/2048 | C(-1/2, 7) |
| 9 | 6435/32768 | C(-1/2, 8) |
| 10 | -12155/65536 | C(-1/2, 9) |

Pattern (verified all 10): the $\varepsilon^k$ coefficient equals
$\binom{-1/2}{k-1} = \frac{(-1)^{k-1} (2k-2)!}{4^{k-1} ((k-1)!)^2}$ for $k \ge 1$.

## Comparison to framework's claimed F_n

The framework's Q_β precision-ladder is:

$$
Q_\beta = Q_A \cdot \cos(\alpha - b\hbar_q^2/2) \cdot (1 - b^2 \hbar_q^4) \cdot (1 + c_3 \hbar_q^6) \cdot (1 + c_4 \hbar_q^8) \cdot \ldots
$$

with claimed F_n values (at q = q_0 ≈ 1.110, $b^2 = 3/4$, etc.):

| n | Framework F_n | Value at q=1 | Source |
|---|---|---:|---|
| 2 | b² | 3/4 = 0.7500 | PR #661 (derived from V_(2,1) Hoefsmit Kashiwara) |
| 3 | -2·b³ | -3√3/4 ≈ -1.2990 | PR #657 Track-C (claimed, hand-waved by PR #664) |
| 4 | b² + 1/2 | 5/4 = 1.2500 | PR #665 (claimed) |

Bare-Markov ε^{2n} coefficients of $\mathrm{tr}_M(\sigma_1^2) - 1$:

| n | bare-Markov F_n | Value |
|---|---|---:|
| 2 | C(-1/2, 3) | -5/16 ≈ -0.3125 |
| 3 | C(-1/2, 5) | **-63/256 ≈ -0.2461** |
| 4 | C(-1/2, 7) | -429/2048 ≈ -0.2095 |

**MISMATCH.** The bare-Markov coefficients DO NOT equal the framework's
claimed F_n values. They differ in sign (F_2 is positive, bare ε^4 is
negative) and magnitude (F_3 = -1.299 vs ε^6 = -0.246).

## What this proves

The framework's F_n are **NOT** the bare-Markov-trace Taylor
coefficients of the Hopf+ braid σ_1². They are a **different
decomposition** of $Q_\beta$ — specifically:

- Q_β = Q_A · (factor product) involves dividing/factoring out
  lower-order corrections to isolate each F_n.
- The factor product structure (cos × (1 - b²ℏ_q^4) × (1 - 2b³ℏ_q^6) ×…)
  is an ASSUMPTION about how Q_β decomposes, not a derivation.
- The c_n values extracted by PR #655's empirical fit are the
  residual after lower-order factors are divided out from the
  empirical Q_β data — not from a bare-Markov computation.

## What a "genuine F_3 derivation" requires

For each F_n in the Q_β ladder:

(i) Identify the categorical object β_n whose Markov trace produces
    the order-h^{2n} contribution to Q_β.
(ii) Symbolically compute tr_M(β_n) with the appropriate writhe /
     framing convention.
(iii) Verify it equals 1 + c_n · ℏ_q^{2n} + O(h^{2n+2}) modulo the
      already-fixed lower-order factors.

For F_3 specifically (per PR #657 Track-C):

- β_3 = "the V_(2,2,2) channel inside Hoefsmit V_(2,1) ⊗ V_(2,1)
  embedded in H_6, projected via Markov stabilization"
- The "−2b³" form is claimed to arise from this V_(2,2,2)
  contribution + Kashiwara b³ factor
- The bare-Markov of σ_1² in H_6 (= H_n for any n ≥ 2 by Markov-
  invariance) is the FULL trace; the V_(2,2,2) channel is a
  PER-WEDDERBURN-BLOCK projection

Neither PR #657 Track-C nor PR #664 actually performed this
projection symbolically. The hand-wave step is: "the V_(2,2,2)
channel contributes the Hopf-Jones value via the embedding". Without
the explicit projector + projected-trace calculation, F_3 = 1 - 2·b³·ℏ_q^6
is an ANSATZ, not a derivation.

## Next-PR scope (genuine F_3 derivation)

A follow-up PR (~50-100 lines + symbolic compute) should:

1. Compute the symbolic projector P_{(2,2,2)} onto the V_(2,2,2)
   Wedderburn block in H_6 (use the cached chi-deuteron-h6.witness.json
   for the χ^{(2,2,2)} value and dim_q⊕dim_q for the projector
   normalization).
2. Compute P_{(2,2,2)} · σ_1² · P_{(2,2,2)} symbolically.
3. Take its trace; expand at q = 1+ε.
4. Verify the order-ε^6 leading equals -2·b³(q=1) = -3√3/4.
5. If verified: write the result as the F_3 derivation block in the
   paper, citing this projection chain explicitly.
6. Extend to F_4, F_5, ... via the alternating Kashiwara × Jones-at-q=1
   pattern PR #665 sketched.

This is **substantial** but tractable on the chi-deuteron-h6 cache
infrastructure.

## Implications for PR #664

PR #664's "c_3 = J_Hopf(q=1) = -2 from V_(2,1) seminormal Markov
trace of σ_1²" claim is now triply-clarified:

(a) **Dual-tr_M**: σ_1²'s canonical Markov trace at q=1 = +1, not -2.
    (Confirmed in my probe_hopf_markov_trace_genuine.py.)
(b) **Two "c_3 = -2"s**: the symbol-coefficient '-2' in F_3 = 1 - 2·b³·ℏ_q^6
    vs the q=1 limit of textbook J_Hopf = -2. (Surfaced in my
    probe_c3_categorical_consistency_check.py.)
(c) **F_3 = -2·b³ form itself is an ansatz**, not derived: the bare-
    Markov tr_M(σ_1²) ε^6 coefficient is -63/256, not -2·b³(q=1) =
    -3√3/4. (This probe.)

To genuinely close PR #664's claim, the V_(2,2,2) projection chain
above is the required work.

## Cross-references

- [`probe_F_n_categorical_derivation.py`](../../computations/probe_F_n_categorical_derivation.py) — this probe
- [`probe_c3_categorical_consistency_check.py`](../../computations/probe_c3_categorical_consistency_check.py) — F_3 ε^6 extraction from 1 - 2·b³·ℏ_q^6 ansatz
- [`probe_hopf_markov_trace_genuine.py`](../../computations/probe_hopf_markov_trace_genuine.py) — σ_1² Markov vs Plancherel comparison
- [`2026-05-17-pr-664-c3-c4-critical-review.md`](2026-05-17-pr-664-c3-c4-critical-review.md) — full critical review
- [`2026-05-17-dual-tr-m-discrepancy.md`](2026-05-17-dual-tr-m-discrepancy.md) — dual-trace + production-scope correction
