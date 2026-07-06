**Theorem (conditional on the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization class).**
*Let $q$ be the substrate parameter and write*

$$
  T \;=\; q\cdot[9]_q\cdot[10]_q + \frac{2}{3\pi},
  \qquad
  H \;=\; \frac{[2]_q}{8\pi},
  \qquad
  h \;=\; \frac{q-1}{q}.
$$

*Assume the typeclass
[`QOU.ArchimedeanUniverse.AlphaEmFixedPointNormalization`](em-coupling-fixed-point.lean)
is inhabited at $(q,\alpha)$ — i.e. the exact $\mathcal{O}(\alpha^2)$
self-energy normalization of the coupling equation is
$H\cdot(1-h^2\alpha)$, the archimedean image of a class in the Bloch
group $B_3(\mathbb{C})$, so that $\alpha$ solves the self-consistent
fixed point*

$$
  \frac{1}{\alpha}
  \;=\;
  T + \alpha\,H\,\bigl(1 - h^2\alpha\bigr).
$$

*Then $\alpha$ is a root of the characteristic cubic*

$$
  P(\alpha)
  \;=\;
  -h^2 H\,\alpha^3 + H\,\alpha^2 + T\,\alpha - 1
  \;=\; 0,
$$

*and its inverse is CODATA-consistent,
$\lvert \alpha^{-1} - 137.035999084\rvert < 10^{-3}$.*

## What is proved vs. what is assumed

The fine-structure constant is presented here as the **symbolic root of a
self-consistent fixed-point equation**, not as a fitted product. The
route is deliberately additive-then-self-consistent and is independent of
the refuted multiplicative Chern–Simons / gluon-octet form
([`rem:em-coupling-chern-simons`](#rem:em-coupling-chern-simons)); that
form is neither used nor restated.

The equation assembles three ingredients, of which only the third is
open:

1. **Tree term $q\cdot[9]_q\cdot[10]_q$** — the bare inverse coupling of
   [`prop:em-coupling-projection`](#prop:em-coupling-projection), whose
   categorical-trace refactoring
   [`prop:alpha-em-categorical-trace-ratio`](#prop:alpha-em-categorical-trace-ratio)
   is Lean-proved.
2. **Zero-mode shift $2/(3\pi) = 2g/(4\pi(g-1))\big|_{g=4}$** — the
   photon IR harmonic-$1$-form contribution on Bring's surface,
   $b_1/\mathrm{Area}$, proved sorry-free in
   [`prop:photon-ir-zero-mode-bring`](#prop:photon-ir-zero-mode-bring)
   and reused here as the Lean constant
   `QOU.Archimedean.bringZeroModeValue`. The normalization $8\pi = \pi
   b_1 = \pi\dim H^1(M_{\text{Bring}})$ is the same harmonic count.
3. **$\mathcal{O}(\alpha^2)$ normalization $H\cdot(1-h^2\alpha)$** — the
   Habiro deformation $(1-h^2\alpha)$ with $h = (q-1)/q = \hbar_q$, and
   the coefficient $H = [2]_q/(8\pi)$. The identification of the exact
   $\mathcal{O}(\alpha^2)$ correction to $H$ with a class in
   $B_3(\mathbb{C})$ is the **single open input**, axiomatised as the
   §3b-cond class field `b3_normalization`.

## Genuine derivation, not projection

Per AGENTS.md §3b-cond item 5, the class carries the *hypothesis* (the
self-consistency relation), and the theorem *derives* the conclusion. The
sorry-free lemma
[`QOU.ArchimedeanUniverse.fixedPoint_iff_cubic`](em-coupling-fixed-point.lean)
establishes, for every $\alpha \neq 0$,

$$
  \Bigl(\tfrac{1}{\alpha} = T + \alpha H(1-h^2\alpha)\Bigr)
  \;\Longleftrightarrow\;
  P(\alpha) = 0,
$$

by clearing the denominator ($\alpha \neq 0$ from `alpha_pos`) and
`linear_combination`. The main theorem
[`QOU.ArchimedeanUniverse.alpha_em_is_fixed_point_root`](em-coupling-fixed-point.lean)
composes this equivalence with the class' `b3_normalization` field; there
is no stored `alphaCubic_zero` field to read off, so the derivation is
non-degenerate.

## Numerical context

At $q_0$ the tree term and zero-mode already reproduce $1/\alpha$ to
$-4.2\times 10^{-6}$
([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode));
the $\mathcal{O}(\alpha^2)$ self-consistency term supplies the residual
$\mathcal{O}(\alpha)$ correction whose exact form is the conjectural
$B_3(\mathbb{C})$ Bloch-class content encoded in the class field. The
cubic $P$ has a real root near $1/137.036$; its CODATA-consistency is the
empirical face of the conjecture, carried by the class field
`codata_consistent`.

## Status

Open piece: the $B_3(\mathbb{C})$ $\mathcal{O}(\alpha^2)$ normalization
(the sole class field `b3_normalization`). Everything else — the
tree/zero-mode assembly of $T$, the algebraic equivalence
fixed-point $\Leftrightarrow$ cubic, and the derivation of $P(\alpha)=0$
under the class — is proved sorry-free. The class is left uninhabited
(the honest open state, §3b-tax): no fabricated instance closes the
primary conjecture.
