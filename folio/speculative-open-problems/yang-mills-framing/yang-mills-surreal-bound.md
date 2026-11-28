**Status: surreal-order relabelling, not a proof.** Evaluating the rational expression $\Delta_q = \tfrac{1}{2}(q - q^{-1})(q - 1)^2$ at $q = 1 + \varepsilon$ for a positive infinitesimal $\varepsilon \in \mathbb{R}(\varepsilon) \subset \mathbf{No}$ \cite{conway1976} gives

$$
  \Delta_q = \varepsilon^3 - \tfrac{1}{2}\varepsilon^4 + \cdots \asymp \varepsilon^3 > 0
$$

in the ordered field $\mathbb{R}(\varepsilon)$, equivalently $\ordw(\Delta_q) = -3 > -\infty = \ordw(0)$.

Earlier exposition described this inequality as making the Yang--Mills mass gap true by categorical construction. It does not, for three independent reasons:

1. **Rational positivity is not a spectral theorem.** Positivity of $\varepsilon^3$ in $\mathbb{R}(\varepsilon)$ restates the algebraic fact that $(q - q^{-1})(q - 1)^2 > 0$ for $q > 1$. No operator on a continuum gauge-field Hilbert space is shown to have spectrum bounded below by $\Delta_q$; in [the categorical dictionary conjecture](#conj:yang-mills-mass-gap), that bound is an input field of the postulated transfer-matrix structure.
2. **Mismatch with the surreal squeeze threshold.** The monomial squeeze $\delta^2 \varepsilon^{-1} > \varepsilon^3$ is equivalent to $|\delta| > \varepsilon^2$. It quantifies over standard-real $\delta > 0$, fails at $\delta = 0$, and sets a threshold $\varepsilon^2$ that is larger than $\Delta_q \asymp \varepsilon^3$ by an infinite factor $\varepsilon^{-1}$, so an excitation at scale $\Delta_q$ does not clear the squeeze.
3. **Vanishing standard part.** Under the standard-part map $\mathrm{st} \colon \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}$, $\mathrm{st}(\Delta_q) = \mathrm{st}(\varepsilon^3) = 0$. Extracting a nonzero real mass gap $\Delta_{\mathrm{YM}} > 0$ on $\mathbb{R}^4$ requires a non-trivial renormalisation scaling together with Osterwalder--Schrader reconstruction \cite{jaffe2006}, neither of which follows from surreal arithmetic in $\mathbb{R}(\varepsilon)$.
