Fix an infinitesimal $\varepsilon = 1/\omega \in \mathbf{No}$. Equivalently, $\omega = 1/\varepsilon$ is the first infinite ordinal regarded as a surreal. See [Table](#tbl:surreal-blowup-calculus-table-data) for named surreals; every name corresponds to a unique element under Conway's recursive construction.

A **surreal blow-up** of a divergent expression evaluates the expression at a named infinite surreal, then takes the standard part of a renormalised version:
1. Write the divergent expression $X$ as a function of a parameter that becomes a named surreal: $X = X(\Lambda)$ with $\Lambda \to \omega$.
2. Identify a counterterm $C(\Lambda)$ such that $X(\Lambda) - C(\Lambda)$ is a finite surreal.
3. Define the renormalised value: $X_{\mathrm{ren}} := \mathrm{st}(X(\omega) - C(\omega)) \in \mathbb{R}$.
