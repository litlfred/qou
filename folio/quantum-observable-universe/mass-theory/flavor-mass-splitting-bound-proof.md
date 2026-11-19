## Proof sketch

Two ingredients:

1. **Positivity** (lower bound). By aether construction,
 $q > 1$ implies $(q-1)^2 > 0$ and $1 - q^{-4} > 0$. Their
 product is positive; division by $3$ preserves the sign. By
 [flavor dressed mass from the aether split proposition](flavor-dressed-mass-from-substrate-split.md)
 the splitting $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ is
 $M_N$ times this positive aether factor (modulo
 $O((\Delta m / M_N)^2)$, which is below the leading term), so
 the difference is strictly positive.

2. **Upper bound.** The aether factor satisfies
 $$
     \frac{(q - 1)^2 (1 - q^{-4})}{3}
     \;<\;
     \hbar_q^2 \cdot h_q \cdot [2]_q
     \;=\;
     \frac{(q-1)^2}{q^2} \cdot (q - q^{-1}) \cdot (q + q^{-1})
     \;=\;
     \frac{(q-1)^2 (q^4 - 1)}{q^4}.
   $$
 Both expressions share the numerator $(q-1)^2$; their ratio is
 $$
     \frac{(1 - q^{-4}) / 3}{(q^4 - 1)/q^4}
     \;=\;
     \frac{(q^4 - 1)/(3 q^4)}{(q^4 - 1)/q^4}
     \;=\;
     \frac{1}{3},
   $$
 The aether factor of the proposition equals $1/3$ of the
 bound expression. Multiplication by $M_N$ preserves the
 inequality; the Skein-side adjustment factor
 $(q^{1/2} + q^{-1/2})/(q + q^{-1}) < 1$ at $q > 1$ tightens the
 bound further but is not required for the strict inequality.
 $\square$

## Tightness

The bound is **not** tight: the slack-ratio identity above shows
that the realised splitting is exactly $(1/3) \cdot (q^{1/2} +
q^{-1/2})/(q + q^{-1})$ of the bound (plus a small higher-order
correction). The dominant factor is the explicit $1/3$ baked
into the aether formula of
[flavor aether-split proposition](../observations/flavor-split-substrate.md).
Tightening would require either:

- A finer aether factor that absorbs the $1/3$ directly into
 the categorical derivation (rather than as an artefact of the
 closed-form algebra).
- A different categorical bound source (e.g.
 [Hecke convergence bound proposition](hecke-convergence-bound.md)
 applied to the splitting word) — but this requires further
 development and is not committed in this revision.

## Per-flavor bounds (out of scope)

This theorem does not assert per-flavor bounds
$0 < \mu_q < c \cdot M_N$. Such bounds require additional
non-aether inputs (the nucleon-baryon sum rule for the average
$\bar\mu$) and live in the open follow-up; see
[dressed quark numerology at $q_0$ remark](../observations/dressed-quark-numerology-at-q0.md).
