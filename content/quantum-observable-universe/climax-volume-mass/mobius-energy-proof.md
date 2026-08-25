The proof proceeds in three steps.

*Step 1: Gauge fixing via the categorical volume constraint.*
The categorical volume constraint fixes the gauge group to
$G = \mathrm{SU}(2)$, acting on the $\mathbb{CP}^1$ fibre by
Möbius transformations. This ensures that $E_{\mathrm{cat}}(\gamma)$
is invariant under the full Möbius group
$\mathrm{PSL}(2, \mathbb{C})$, matching the conformal invariance
of the classical functional.

*Step 2: Expansion of the Frobenius--Hopf kernel.*
By
([classical limit of the Frobenius--Hopf kernel](#lem:mobius-energy-frobenius-kernel)),
the integrand collapses to $1/\lvert \gamma(s) - \gamma(t) \rvert^2$
at $q = 1$.

*Step 3: Subtraction of the self-energy.*
The diagonal regularization in the categorical integral (exclusion
of $\mathrm{diag} \subset S^1 \times S^1$) matches the arc-length
subtraction $1/D(\gamma(s),\gamma(t))^2$ in the classical Möbius
energy. In the $q$-deformed setting, this subtraction arises
accordingly from the antipode $S$ of the Hopf structure: the
self-pairing $\int_A(\gamma(s)^* \cdot S(\gamma(s)))$ cancels the
short-distance divergence at $s = t$, leaving a finite integral
that agrees with $E(\gamma)/4$ up to an Euler characteristic
correction $\chi(\Sigma_\gamma) \cdot \mathrm{const}$, where
$\Sigma_\gamma$ is any Seifert surface spanning $\gamma$.

*Scope.* The classical identity
$\lim_{q \to 1} E_{\mathrm{cat}}(\varrho) = E(\varrho)/4 +
\text{const}$ is stated in the archimedean realisation $K =
\mathbb{R}$; the right-hand side $E(\varrho)$ is a Lebesgue
integral on $S^1 \times S^1$. Under a surreal lift (see
[appendix on surreal lift](#app:surreals)), the left-hand side
$E_{\mathrm{cat}}$ lifts verbatim (categorical operations only)
and $\lim_{q \to 1}$ becomes
$\mathrm{st} \circ \text{eval}_{q = 1 + \varepsilon}$; the
right-hand side remains in $\mathbb{R}$ as an external anchor.
Lebesgue measure is not used inside QOU. $\square$
