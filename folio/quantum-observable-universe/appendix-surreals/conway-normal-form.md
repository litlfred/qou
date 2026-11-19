Every surreal $x \in \mathbf{No}$ admits a unique Conway normal form:

$$
  x = \sum_{i < \lambda} \omega^{y_i} \, r_i
$$

where $y_0 > y_1 > \cdots$ is a strictly decreasing sequence of surreals, $r_i \in \mathbb{R} \setminus \{0\}$, and $\omega$ is the first infinite surreal. The sum has well-ordered support. This embeds $\mathbf{No}$ into the Hahn field $\mathbb{R}((\omega^{\mathbf{No}}))$.

For $x \neq 0$, define the leading exponent and leading coefficient:

$$
  \ordw(x) := y_0, \qquad \mathrm{lc}(x) := r_0.
$$

The map $\ordw$ is a group homomorphism $(\mathbf{No}^\times, \cdot) \to (\mathbf{No}, +)$:

$$
  \ordw(x \cdot y) = \ordw(x) + \ordw(y).
$$

It is the non-archimedean valuation associated to the valuation ring $\mathcal{O}$ of finite surreals ([valuation ring](#rem:valuation-ring-finite-surreals)):

| Regime | Condition on $\ordw(x)$ | Meaning |
|---|---|---|
| $x$ infinitesimal | $\ordw(x) < 0$ | $x \in \mathfrak{m}$ |
| $x$ finite non-inf. | $\ordw(x) = 0$ | $\mathrm{st}(x) \neq 0$ |
| $x$ infinite | $\ordw(x) > 0$ | $x \notin \mathcal{O}$ |

Classical asymptotic notation is a leading-exponent statement in disguise. For $f, g$ evaluated at $q = 1 + \varepsilon$ (equivalently, for $f, g$ in the Hahn field):

| Classical | Surreal | Proposed notation |
|---|---|---|
| $f = O(g)$ | $\ordw(f) \leq \ordw(g)$ | $f \preceq g$ |
| $f = o(g)$ | $\ordw(f) < \ordw(g)$ | $f \prec g$ |
| $f = \Theta(g)$ | $\ordw(f) = \ordw(g)$ | $f \asymp g$ |
| $f \sim g$ | $\ordw(f) = \ordw(g)$ and $\mathrm{lc}(f) = \mathrm{lc}(g)$ | $f \simeq g$ |
| $f = g + O(h)$ | $\ordw(f - g) \leq \ordw(h)$ | $f \equiv g \pmod{\preceq h}$ |

Classical Big-O has three pathologies:
1. $f = O(g)$ is an abuse of equality; $O(g)$ is a set.
2. $O(f) + O(g) = O(f+g)$ is asymmetric and not an algebraic identity.
3. It cannot distinguish sub-polynomial behaviours: $e^{-1/\varepsilon}$ and $\varepsilon^\omega$ are both $o(\varepsilon^n)$ for all $n \in \mathbb{N}$.

The surreal valuation replaces these with:
1. A strict inequality $\ordw(f) \leq \ordw(g)$ in the ordered group $(\mathbf{No}, +)$.
2. Algebraic laws: $\ordw(f \cdot g) = \ordw(f) + \ordw(g)$ and $\ordw(f + g) \leq \max(\ordw(f), \ordw(g))$.
3. Strict refinement by birthday. When leading exponents match, the birthday of the exponent gives an ordinal-valued depth gauge. $\ordw(e^{-1/\varepsilon})$ and $\ordw(\varepsilon^\omega)$ are both negative infinite, but at different birthdays.

Example translations:

| Classical | Surreal |
|---|---|
| $f(x) = x^2 + 5x + O(1)$ as $x \to \infty$ | $f(x) = x^2 + 5x + r$ where $r \prec 1$ |
| $f(q) = g(q) + O((q-1)^2)$ as $q \to 1$ | $f \equiv g \pmod{\prec \varepsilon^2}$ |
| $\int_0^1 e^{-x/\varepsilon} dx \sim \varepsilon$ as $\varepsilon \to 0^+$ | $\int_0^1 e^{-x/\varepsilon} dx \simeq \varepsilon$ |

The surreal valuation serves three specific purposes in QOU:
1. **Experimental fits**: Writing predictions as $\mathfrak{m}_{\mathfrak{H}} = \hat{\mathfrak{m}}_{\mathfrak{H}} + r$ with $r \prec 1$ makes the order of the residual an explicit surreal exponent rather than a hidden Big-O.
2. **Spectral gaps and singularity formation**: The leading exponent determines whether a $q$-deformed spectral gap closes algebraically or transcendentally as $q \to 1$.
3. **Renormalisation counterterms**: Each counterterm in the blow-up calculus has a specific leading exponent. Matching counterterms to divergences means matching leading exponents.

Throughout this appendix, the relations $\preceq, \prec, \asymp, \simeq$ are used uniformly.
