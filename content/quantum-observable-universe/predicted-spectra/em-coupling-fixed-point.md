**Theorem (conditional on the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization class).**
*Let $q$ be the substrate parameter and write*

$$
  T \;=\; q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi},
  \qquad
  H \;=\; \frac{[2]_q}{8\pi},
  \qquad
  h \;=\; \frac{q-1}{q}.
$$

*Assume the typeclass [`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean) is inhabited at $(q,\alpha)$. The exact $\mathcal{O}(\alpha^2)$ self-energy normalization of the coupling equation is $H\cdot(1-h^2\alpha)$. This is the archimedean image of a class in the Bloch group $B_3(\mathbb{C})$. Consequently, $\alpha$ solves the self-consistent fixed point:*

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

## Proved results and assumptions

The fine-structure constant emerges as the symbolic root of a self-consistent fixed-point equation. This path is additive and self-consistent. The formulation avoids the refuted multiplicative Chern–Simons or gluon-octet forms.

The equation integrates three components. Only the third remains open:

1. **Tree term $q\cdot[9]_q\cdot[10]_q$**: The bare inverse coupling from [`prop:em-coupling-projection`](#prop:em-coupling-projection). Lean verifies its categorical-trace refactoring ([`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)).
2. **Zero-mode shift $2/(3\pi) = 2g/(4\pi(g-1))\big|_{g=4}$**: The photon infrared harmonic-$1$-form contribution on Bring's surface. Lean proves this in [`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring). The normalization $8\pi = \pi b_1 = \pi\dim H^1(M_{\text{Bring}})$ maintains the harmonic count.
3. **$\mathcal{O}(\alpha^2)$ normalization $H\cdot(1-h^2\alpha)$**: The Habiro deformation $(1-h^2\alpha)$ with coefficient $H = [2]_q/(8\pi)$. Identifying the exact $\mathcal{O}(\alpha^2)$ correction to $H$ with a class in $B_3(\mathbb{C})$ is the single open input. The `b3_normalization` class field axiomatises this.

## Genuine derivation, not projection

The class carries the hypothesis, and the theorem derives the conclusion. The lemma [`QOU.ArchimedeanUniverse.fixedPoint_iff_cubic`](em-coupling-fixed-point.lean) establishes the equivalence between the fixed-point equation and the cubic root for $\alpha \neq 0$. The main theorem [`QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root`](em-coupling-fixed-point.lean) composes this equivalence with the `b3_normalization` field. The proof is a genuine derivation.

## Numerical context

At $q_0$, the tree term and zero-mode reproduce $1/\alpha$ to $-4.2\times 10^{-6}$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)). The $\mathcal{O}(\alpha^2)$ self-consistency term supplies the residual $\mathcal{O}(\alpha)$ correction. The conjectural $B_3(\mathbb{C})$ Bloch-class content supplies its exact form. The cubic $P$ features a real root near $1/137.036$. CODATA-consistency provides the empirical foundation of the conjecture.

## Status

The sole open element remains the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization. Lean proves the tree/zero-mode assembly of $T$, the algebraic equivalence of the fixed-point, and the derivation of $P(\alpha)=0$. The class remains uninhabited. No fabricated instance attempts to close the primary conjecture.
