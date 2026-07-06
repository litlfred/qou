Although surreal numbers lack a Hilbert-space completion and a canonical Lebesgue measure ([analytic obstructions](#rem:analytic-obstructions)), a substantial fragment of differential and formal integral calculus lifts to $\mathbf{No}$ up to an infinitesimal correction. This block records these calculus lifts and shows how the standard-part map recovers classical analysis.

### Differential Calculus: Jackson Derivative as the Native $d/dx$

Fix a positive infinitesimal $\varepsilon \in \mathbf{No}$ and set $q = 1 + \varepsilon$. The Jackson $q$-derivative is a native difference quotient on $\mathbf{No}$:

$$
  d_q f(x) = \frac{f(q x) - f(x)}{(q - 1)\, x}
           = \frac{f((1+\varepsilon) x) - f(x)}{\varepsilon\, x}.
$$

Both numerator and denominator are surreals. Their ratio is well-defined wherever $\varepsilon \, x \neq 0$.

For a standard function $f : \mathbb{R} \to \mathbb{R}$ lifted polynomially to $\mathbf{No}$, the classical derivative is exactly recovered by:

$$
  \frac{df}{dx}(x_0) = \mathrm{st}\!\left(d_q f(x_0)\right)
  \qquad (x_0 \in \mathbb{R},\; q = 1 + \varepsilon).
$$

This observation is central. The [classical limit functor](#def:classical-limit-functor), which breaks as an honest limit under surreal replacement, is replaced by the standard-part map evaluated at a specific surreal $q$.

Berarducci–Mantova [@berarducci-mantova2018] construct a genuine derivation $D : \mathbf{No} \to \mathbf{No}$ extending $d/dx$ on $\mathbb{R}$, making $\mathbf{No}$ a differential field. Under this derivation, transcendental identities involving $\exp$, $\log$, and $\mathrm{Li}_2$ extend accordingly.

### Formal Integration: Antiderivative Exists, Measure Does Not

Berarducci–Mantova also show that $\mathbf{No}$ admits a right inverse to $D$. Every $f \in \mathbf{No}$ has an antiderivative $F$ such that $D(F) = f$. This provides an honest indefinite integral $\int f \, dx \in \mathbf{No}$, determined up to a constant of integration.

However, there is no definite integral $\int_a^b f \, dx$ that canonically agrees with Lebesgue integration on $\mathbb{R}$-valued inputs. Bagayoko's hyperseries program offers one natural extension, but it is not canonical and does not uniformly agree with Riemann sums on $\mathbb{R}$.

Therefore, we:
- Use $d_q$ as the native derivative.
- Reserve $\int$ for the categorical Frobenius integral (which is algebraic) or for the standard part of Riemann sums computed on $\mathbf{No}$-valued partitions.

### Limits Become Evaluations

Every classical sequential limit $L = \lim_{n \to \infty} a_n$ translates to:

$$
  L = \mathrm{st}(a_\omega)
$$

where $\omega \in \mathbf{No}$ is the first infinite ordinal and $a_\omega$ is the surreal obtained by transfer of the formula defining $a_n$. This applies whenever the classical limit exists.

This turns formal limiting processes into named values. For example, $\lim_{q \to 1}$ becomes an evaluation at $q = 1 + \varepsilon$, with the classical limit recovered via the standard part. Double limits or sups/infs over uncountable index sets require care, as the transfer principle covers first-order statements but not arbitrary topologies.

### Formal Power Series: The Safe Regime

All formal power series identities used in the main paper ($\exp_q, \log_q, \mathrm{Li}_2^q$, quantum dilogarithm, character generating functions) lift directly because they operate in $K[[x]]$ for $K = \mathbf{No}$. Classical convergence is replaced by formal convergence (coefficient stabilization), which is automatic for these $q$-series.

Consequently, the information-theory computations (entropies, Lyapunov exponents, bandwidth formulas) survive intact as rational or formal power series expressions in $q$.

### Measure Up to $\varepsilon$: Loeb Construction

Given a hyperfinite partition of $[0, 1] \subset \mathbf{No}$ into $N = \omega$ equal subintervals, the counting measure divided by $N$ defines a hyperfinite measure on $[0,1]_{\mathbf{No}}$. Its standard part is the Lebesgue measure on $[0, 1] \subset \mathbb{R}$. This Loeb measure [@robinson1966] is non-canonical but well-behaved for standard integrands.

For the Möbius energy integral, one can define a Loeb measure on $S^1 \times S^1 \subset \mathbf{No}^2$, evaluate the divergent integrand $1/|x - y|^2$, subtract the Loeb-equivalent diagonal regularizer, and take the standard part. The outcome matches the classical Möbius energy to infinitesimal precision. Whether this procedure adds value over the classical calculation is unclear.

### Summary

See [Table](#tbl:calculus-up-to-epsilon-table-data).

For the substrate-parameter limit $q \to 1$—the paper's primary analytic operation—the surreal framework represents a sharpening, not a weakening. It names the infinitesimal regime explicitly. The absence of a canonical Lebesgue measure and Hilbert completion is benign. The quantum observable universe (QOU) relies on neither in a load-bearing capacity: integration is categorical (Frobenius counit), decomposition is algebraic (Hoefsmit), and analytic parameters ($d_H(q)$, $c_q$, $\hbar_q$) are rational in $q$.
