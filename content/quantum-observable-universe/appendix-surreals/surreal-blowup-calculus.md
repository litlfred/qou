A persistent informal device in physics is the use of an
unspecified $\infty$ to denote an unrenormalised divergence:
$\Lambda \to \infty$, $1/\varepsilon$, $\delta(0)$, etc. These
*should* be specific elements of an extended number system; the
surreal numbers $\mathbf{No}$ provide one.

This definition records a small dictionary of named surreals and
the resulting calculus.

## Named surreals

Fix an infinitesimal $\varepsilon = 1/\omega \in \mathbf{No}$
(equivalently, $\omega = 1/\varepsilon$ is the first infinite
ordinal regarded as a surreal). Then:

| Object | Surreal name | Birthday |
|---|---|---|
| Infinitesimal unit | $\varepsilon = 1/\omega$ | $\omega$ |
| First infinity | $\omega$ | $\omega$ |
| Second infinity | $\omega^2$ | $\omega \cdot 2$ |
| First transfinite infinity | $\omega^\omega$ | $\omega^\omega$ |
| Squared infinitesimal | $\varepsilon^2 = 1/\omega^2$ | $\omega \cdot 2$ |
| Logarithmic infinity | $\log \omega$ (Berarducci--Mantova transseries; infinite but strictly less than every positive power of $\omega$) | $\omega + 1$ |
| Cutoff $\Lambda$ | choice: typically $\Lambda := \omega$ | $\omega$ |
| Renormalisation scale $\mu$ | choice of finite surreal | $\leq \omega$ |

These are all specific elements of $\mathbf{No}$ — every name
above corresponds to a unique element under Conway's recursive
construction.

## The blow-up calculus

A **blow-up of a divergent expression** is the act of evaluating
the expression at one of the named infinite surreals, then taking
the standard-part of a renormalised version. Schematically:

1. Write the divergent expression $X$ as a function of a parameter
   that becomes a named surreal: $X = X(\Lambda)$ with $\Lambda
   \to \omega$.
2. Identify a **counterterm** $C(\Lambda)$ — typically a polynomial
   in $\Lambda$ — such that $X(\Lambda) - C(\Lambda)$ is a finite
   surreal.
3. Define the renormalised value:
   $X_{\mathrm{ren}} := \mathrm{st}(X(\omega) - C(\omega)) \in \mathbb{R}$.

The role of $\mathbf{No}$ is to make every step *literal*: the
cutoff $\Lambda$ is a specific element, the counterterm is a
specific surreal-valued function, and the standard-part is a
specific real.

## Examples

### Möbius energy diagonal

The diagonal-regularised Möbius energy
([Möbius energy proof](#prf:mobius-energy)) computes

$$
  E(\varrho) = \iint_{S^1 \times S^1}
    \!\!\left(\frac{1}{|\varrho(s) - \varrho(t)|^2}
    - \frac{1}{D(\varrho(s), \varrho(t))^2}\right) \!ds\, dt.
$$

In the surreal lift, the inner integrand at $s = t$ has value
$1/0^2 = \omega^2$. The arc-length subtraction $1/D^2$ has
matching value $\omega^2$ at $s = t$. The difference is a finite
surreal whose standard-part is the renormalised energy.

### $c_q$ at $q = 1$

The speed of light $c_q = 1/(q-1)$ at $q = 1 + \varepsilon$ is
exactly $\omega \in \mathbf{No}$. The classical-limit divergence
"$c_q \to \infty$ as $q \to 1$" becomes the literal identity
$c_q\big|_{q = 1 + \varepsilon} = \omega$.

### Vacuum normalisation

The empty-link Markov trace evaluates to $\mathrm{tr}_M(1) = z =
1/(\sqrt{q} + 1/\sqrt{q})$. At $q = 1 + \varepsilon$ this is
$1/2 + O(\varepsilon)$ — finite. But in the *unnormalised*
convention $\mathrm{tr}_M(1) = 1$, which then becomes $1/0$ in
some normalisation factors. The named-surreal calculus makes
these distinctions explicit rather than papering over them.

## Cohomological aspect

The blow-up calculus respects the birthday grading: the
counterterm $C(\omega)$ has the same birthday as $X(\omega)$, so
their difference lives at strictly lower birthday, and the
standard-part collapses it to $\mathbb{R}$. This gives a
*birthday-graded* refinement of the BPHZ subtraction algorithm,
where each subtraction reduces the birthday by a controlled
ordinal amount.

## Why this matters for QOU

The QOU mass formula has, by design, no divergences — Hoefsmit
seminormal form and the Markov trace produce finite rational
expressions in $q$. So the blow-up calculus is **not** needed for
the main computation. It serves three secondary purposes:

1. **Möbius energy comparison** — turns the informal classical
   $\infty$ into a named $\omega^2$.
2. **Classical-limit $q \to 1$** — makes "$c_q \to \infty$"
   literal: $c_q|_{q = 1+\varepsilon} = \omega$.
3. **Future renormalisation work** — gives a setting for any
   future Yang--Mills or Sobolev-completion arguments that
   genuinely require regularisation (see
   [outlook](#sec:surreal-appendix-conclusion)).
