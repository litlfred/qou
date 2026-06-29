## Named surreals

Fix an infinitesimal $\varepsilon = 1/\omega \in \mathbf{No}$
(equivalently, $\omega = 1/\varepsilon$ is the first infinite
ordinal regarded as a surreal). Then:

See [Table](#tbl:surreal-blowup-calculus-table-data).

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
