The Hoefsmit scattering pipeline assigns to each link $L$ a
*geometric energy* $\mathrm{Geom}(L) \in \mathbb{R}$
([Hoefsmit scattering pipeline](#prop:hoefsmit-scattering-pipeline)).
The vacuum normalisation requires $\mathrm{Geom}(\unicode{9737}) = 0$
on the unknot, so that the empty link contributes nothing to
particle masses.

This strict-zero condition is awkward in two ways:

1. It introduces a *boundary case* — the unknot must be
   special-cased in the geometric-energy formula.
2. It is *physically suspicious* — a "vacuum energy" of exactly
   zero is the textbook signature of a fine-tuned theory, and is
   thought by many to be the wrong setting (cosmological
   constant problem, vacuum-fluctuation arguments, etc.).

Under a surreal lift, the strict zero can be relaxed.

## Conjecture

The **$\varepsilon$-relaxed vacuum axiom** is:

$$
  \mathrm{Geom}(\unicode{9737}) \;=\; \varepsilon \in \mathbf{No},
$$

a single positive infinitesimal. The conjecture: every surreal
QOU satisfies this relaxation with some choice of $\varepsilon
> 0$, and the standard-part recovers the strict vacuum:
$\mathrm{st}(\varepsilon) = 0$.

## Consequences

If the conjecture holds, several existing results lift:

1. **Geometric-energy formula** simplifies: the special case for
   $\unicode{9737}$ is absorbed into the general formula, giving
   $\mathrm{Geom}(L) = (\text{generic formula}) +
   \varepsilon \cdot (\text{number of unknot components})$.

2. **Möbius energy regularisation** maps cleanly: the diagonal
   subtraction in the Möbius energy is exactly the
   $\varepsilon$-vacuum contribution.

3. **Mass spectrum** acquires an infinitesimal shift: every
   particle mass $\mathfrak{m}(\mathfrak{H})$ becomes
   $\mathfrak{m}(\mathfrak{H}) + \varepsilon \cdot c_{\mathfrak{H}}$
   for some standard-real $c_{\mathfrak{H}}$. Standard-part of
   this shift is zero, so archimedean predictions are unchanged.

## Why this matters

Two reasons:

1. **Cleaner axioms**: the strict-zero vacuum is a fine-tuning
   that would-be reviewers can object to. The
   $\varepsilon$-vacuum is a parameter, not a fine-tuning, and
   the archimedean theory is recovered by standard-part.

2. **Möbius regularisation absorbed**: the diagonal-subtraction
   trick in the Möbius energy
   ([Möbius energy proof](#prf:mobius-energy)) becomes a special
   case of $\varepsilon$-vacuum subtraction. This unifies two
   regularisations into one.

## Status

**Open**. The conjecture is the most directly testable of the
appendix's relaxation conjectures: pick an
$\varepsilon \in \mathbf{No}$, recompute the QOU mass spectrum,
and check whether the archimedean image agrees with the strict-
vacuum prediction. The arithmetic is rational in $\varepsilon$,
so the test reduces to a comparison of two polynomials in
$\varepsilon$ at the standard-part.
