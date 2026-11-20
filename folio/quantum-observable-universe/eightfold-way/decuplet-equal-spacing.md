The eightfold way's signature triumph was Gell-Mann's 1962 prediction of the
$\Omega^-$.  Within the baryon decuplet the consecutive mass differences

$$
  \mathfrak{m}(\Sigma^*) - \mathfrak{m}(\Delta), \qquad
  \mathfrak{m}(\Xi^*) - \mathfrak{m}(\Sigma^*), \qquad
  \mathfrak{m}(\Omega) - \mathfrak{m}(\Xi^*)
$$

are observed to be nearly equal, so the mass of the then-undiscovered
$\Omega^-$ could be read off from the three lighter states.  The particle was
found in 1964 within $0.6\%$ of the extrapolated value.

**The rule carries no information about the breaking mechanism.**  This is a
theorem, machine-checked in
`QOU/Eightfold/DecupletEqualSpacing.lean`: the three spacings are all equal for
*every* choice of the first-order octet-breaking parameters $a, b, c$, over any
commutative ring.  Their common value is $-4b - 6c$, and the second difference
vanishes identically.  Two arbitrarily different
breaking patterns therefore give the same answer
.

## Why the rule collapses

The Gell-Mann--Okubo mass operator is *quadratic* in the hypercharge,

$$
  \mathfrak{m}(I, Y) = a + bY + c\left(I(I+1) - \tfrac{Y^2}{4}\right).
$$

On the decuplet, and only because of the decuplet's own weight structure, the
isospin is an affine function of the hypercharge:

| State | $Y$ | $I$ | $2I$ | $Y + 2$ |
|---|---|---|---|---|
| $\Delta$ | $+1$ | $3/2$ | $3$ | $3$ |
| $\Sigma^*$ | $0$ | $1$ | $2$ | $2$ |
| $\Xi^*$ | $-1$ | $1/2$ | $1$ | $1$ |
| $\Omega$ | $-2$ | $0$ | $0$ | $0$ |

Substituting $2I = Y + 2$ collapses the quadratic term to a linear one,

$$
  I(I+1) - \tfrac{Y^2}{4} = \tfrac{3Y + 4}{2},
$$

so $\mathfrak{m}$ is affine in $Y$.
Consecutive decuplet states step by $\Delta Y = -1$, hence the mass steps are
equal.  The $\Omega$ is not an independent output at all: identically in
$a, b, c$,

$$
  \mathfrak{m}(\Omega) = 2\,\mathfrak{m}(\Xi^*) - \mathfrak{m}(\Sigma^*),
$$

which means the extrapolation reads off a value the ansatz has already fixed
.

**The collapse is special to the decuplet, not generic.**  On the baryon octet
the isospin is not even a *function* of the hypercharge --- $\Sigma$ and
$\Lambda$ share $Y = 0$ with $I = 1$ and $I = 0$ --- so no such substitution
exists and the argument has nothing to act on
(`octet_casimir_not_function_of_hypercharge`, derived from the octet weight
data rather than asserted).  Without that contrast the result above could be
misread as a fact about every $\mathrm{SU}(3)_{\mathrm{f}}$ multiplet.

## What this means for the framework

The same conclusion as [the meson mass-splitting
remark](#rem:meson-mass-splitting) reaches for Gell-Mann--Okubo, and for the
same structural reason.  Equal spacing is a consequence of the *form* of the
breaking --- octet, first order --- and not of any dynamics realising that
form.  **Reproducing it would therefore be no evidence for this framework, or
for any other.**  It is recorded here so that it is not later counted as one.

The testable content is the **deviation**.  Measured spacings, as comparators
only:

| Spacing | Value (MeV) |
|---|---|
| $\Sigma^* - \Delta$ | $152.6$ |
| $\Xi^* - \Sigma^*$ | $148.8$ |
| $\Omega - \Xi^*$ | $139.1$ |

The spread is $13.6$ MeV, about $9.2\%$ of the mean --- comparable to the
$\approx 6\%$ Gell-Mann--Okubo deviation on the pseudoscalar octet, and
measuring the same thing: the failure of first-order breaking.  The framework
has derived no second-order term and so predicts a spread of $0$.  A derivation
that produced $\approx 9\%$ would be a genuine prediction; one that produced a
materially different value would falsify the mechanism.

Nothing here is fitted, and nothing is wired to any computation.
