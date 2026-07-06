**Theorem (conditional on the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization class).**
*Let $q$ be the substrate parameter and write*

$$
  T \;=\; q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi},
  \qquad
  H \;=\; \frac{[2]_q}{8\pi},
  \qquad
  h \;=\; \frac{q-1}{q}.
$$

*Assume the typeclass [`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean) is inhabited at $(q,\alpha)$ — i.e., the exact $\mathcal{O}(\alpha^2)$ self-energy normalization of the coupling equation is $H\cdot(1-h^2\alpha)$, the archimedean image of a class in the Bloch group $B_3(\mathbb{C})$. Consequently, $\alpha$ solves the self-consistent fixed point:*

$$
  \frac{1}{\alpha}
  \;=\;
  T + \alpha\,H\,\bigl(1 - h^2\alpha\bigr).
$$

*Then $\alpha$ constitutes a root of the characteristic cubic:*

$$
  P(\alpha)
  \;=\;
  -h^2 H\,\alpha^3 + H\,\alpha^2 + T\,\alpha - 1
  \;=\; 0,
$$

*and its inverse yields CODATA-consistency: $\lvert \alpha^{-1} - 137.035999084\rvert < 10^{-3}$.*

## What is proved vs. what is assumed

We present the fine-structure constant as the symbolic root of a self-consistent fixed-point equation, not as a fitted product. The path is additive and self-consistent. It eschews the refuted multiplicative Chern–Simons / gluon-octet form ([`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons)); we neither use nor restate that form.

The equation integrates three components. Only the third remains open:

1. **Tree term $q\cdot[9]_q\cdot[10]_q$**: The bare inverse coupling from [`prop:em-coupling-projection`](#prop:em-coupling-projection). Lean verifies its categorical-trace refactoring ([`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)).
2. **Zero-mode shift $2/(3\pi) = 2g/(4\pi(g-1))\big|_{g=4}$**: The photon IR harmonic-$1$-form contribution on Bring's surface, $b_1/\mathrm{Area}$. Lean proves this sorry-free in [`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring) and reuses it here as `QOU.Archimedean.bringZeroModeValue`. The normalization $8\pi = \pi b_1 = \pi\dim H^1(M_{\text{Bring}})$ maintains the same harmonic count.
3. **$\mathcal{O}(\alpha^2)$ normalization $H\cdot(1-h^2\alpha)$**: The Habiro deformation $(1-h^2\alpha)$ with $h = (q-1)/q = \hbar_q$, alongside coefficient $H = [2]_q/(8\pi)$. Identifying the exact $\mathcal{O}(\alpha^2)$ correction to $H$ with a class in $B_3(\mathbb{C})$ forms the **single open input**. We axiomatise this as the §3b-cond class field `b3_normalization`.

## Genuine derivation, not projection

Per AGENTS.md §3b-cond item 5, the class carries the *hypothesis* (the self-consistency relation), and the theorem *derives* the conclusion. The sorry-free lemma [`QOU.ArchimedeanUniverse.fixedPoint_iff_cubic`](em-coupling-fixed-point.lean) establishes for every $\alpha \neq 0$:

$$
  \Bigl(\tfrac{1}{\alpha} = T + \alpha H(1-h^2\alpha)\Bigr)
  \;\Longleftrightarrow\;
  P(\alpha) = 0,
$$

by clearing the denominator ($\alpha \neq 0$ from `alpha_pos`) and applying `linear_combination`. The main theorem [`QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root`](em-coupling-fixed-point.lean) composes this equivalence with the class's `b3_normalization` field. No stored `alphaCubic_zero` field exists to short-circuit the proof, rendering the derivation non-degenerate.

## Numerical context

At $q_0$, the tree term and zero-mode reproduce $1/\alpha$ to $-4.2\times 10^{-6}$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)). The $\mathcal{O}(\alpha^2)$ self-consistency term supplies the residual $\mathcal{O}(\alpha)$ correction; the conjectural $B_3(\mathbb{C})$ Bloch-class content (encoded in the class field) supplies its exact form. The cubic $P$ features a real root near $1/137.036$. CODATA-consistency provides the empirical foundation of the conjecture, enforced by the class field `codata_consistent`.

## Status

The sole open element remains the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization (the class field `b3_normalization`). Lean proves everything else sorry-free: the tree/zero-mode assembly of $T$, the algebraic equivalence fixed-point $\Leftrightarrow$ cubic, and the derivation of $P(\alpha)=0$ from the class. We leave the class uninhabited (the honest open state, §3b-tax); no fabricated instance attempts to close the primary conjecture.
