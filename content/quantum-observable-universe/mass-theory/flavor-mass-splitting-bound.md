**Theorem (substrate bound on the dressed-quark splitting).**
*Let $\mu \colon \mathbf{Flavor} \to \mathbb{R}_{>0}$ be the flavor
dressing functor of [`def:flavor-dressing-functor`](flavor-dressing-functor.md),
let $M_N$ be the nucleon-mass average, and let $q > 1$ be the
substrate parameter. Then the down–up splitting satisfies the
two-sided substrate bound*

$$
  0 \;<\; \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  \;<\; M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q,
$$

*where*
$\hbar_q = (q - 1)/q$,
$h_q = q - q^{-1}$,
*and* $[2]_q = q + q^{-1}$
*are the substrate Planck constant, the Hecke crossing scale, and
the doublet quantum integer respectively.*

## Why "splitting-only"

The theorem statement bounds the **difference**
$\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ rather than the
individual masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$. The
splitting-only form is preferred because:

- It is the **directly substrate-derivable** quantity — every factor
 on the right-hand side is a substrate-pure expression in $q$
 (no CODATA inputs, no fits).
- Individual values require an additional input
 $\bar\mu = (\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}})/2$
 pinned by baryon-content sum rules (see
 [`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md)).
 Bounding the individual values would carry that pinning into the
 theorem statement, mixing substrate content with CODATA anchoring.
- The Lean proof factors through the existing substrate
 identities (no new bound props need to be authored).

## Slack ratio (symbolic)

The realised splitting from
[`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md)
relates to the bound expression by

$$
  \frac{\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}}{M_N \cdot \hbar_q^2 \cdot h_q \cdot [2]_q}
  \;=\;
  \frac{1}{3}
  \cdot
  \frac{q^{1/2} + q^{-1/2}}{q + q^{-1}}
  \;+\;
  O\!\left((\Delta m / M_N)^2\right).
$$

The dominant factor is the explicit $1/3$ in the substrate formula
of [`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md);
the Skein-side correction
$(q^{1/2} + q^{-1/2})/(q + q^{-1})$ is close to $1$ at the substrate
regime and contributes a small additional reduction. Together they
explain why the theorem's upper bound is loose: it does not absorb
either the explicit $1/3$ or the Skein correction. Tightening the
bound to match the realised value is open (no canonical closed form
is committed in this revision). The numerical evaluation at $q_0$
of both sides is tabulated in
[`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md).

## Tightness

The bound is **not** tight: the slack-ratio identity above shows
that the realised splitting is exactly $(1/3) \cdot (q^{1/2} +
q^{-1/2})/(q + q^{-1})$ of the bound (plus a small higher-order
correction). The dominant factor is the explicit $1/3$ baked
into the substrate formula of
[`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md).
Tightening would require either:

- A finer substrate factor that absorbs the $1/3$ directly into
 the categorical derivation (rather than as an artefact of the
 closed-form algebra).
- A different categorical bound source (e.g.
 [`prop:hecke-convergence-bound`](hecke-convergence-bound.md)
 applied to the splitting word) — but this requires further
 development and is not committed in this revision.

## Per-flavor bounds (out of scope)

This theorem does not assert per-flavor bounds
$0 < \mu_q < c \cdot M_N$. Such bounds require additional
non-substrate inputs (the nucleon-baryon sum rule for the average
$\bar\mu$) and live in the open follow-up; see
[`rem:dressed-quark-numerology-at-q0`](../observations/dressed-quark-numerology-at-q0.md).
