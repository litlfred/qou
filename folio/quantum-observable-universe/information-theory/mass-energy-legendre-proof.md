*Part 1.*
In the [categorical Dirac operator](#def:categorical-dirac-operator) $\mathcal{D}_\nabla = q^{-1}\nabla + \hbar_q\,\iota_\xi\nabla$ with $\hbar_q = 1 - q^{-1}$, the ratio of horizontal spatial weight to Reeb temporal weight for $q > 1$ is $q^{-1}/(1 - q^{-1}) = 1/(q - 1) = c_q > 0$. For $|v| < c_q$, squaring gives $v^2 < c_q^2$ so $c_q^2 - v^2 > 0$. Differentiating $g(v) = c_q^2 - v^2$ yields $g'(v) = -2v$, and applying the chain rule for the square root to $L(v) = -m_{\mathrm{in}}\,c_q\sqrt{c_q^2 - v^2}$ gives

$$
  p(v)
  = \frac{\partial L}{\partial v}
  = (-m_{\mathrm{in}}\,c_q)\,\frac{-2v}{2\sqrt{c_q^2 - v^2}}
  = \frac{m_{\mathrm{in}}\,c_q\,v}{\sqrt{c_q^2 - v^2}}.
$$

Evaluating the Legendre transform ([categorical Hamiltonian](#def:categorical-hamiltonian)) over $\mathbb{R}$ by clearing the non-zero radical $\sqrt{c_q^2 - v^2}$ and using $(\sqrt{c_q^2 - v^2})^2 = c_q^2 - v^2$ gives

$$
  E(v)
  = p(v)\,v - L(v)
  = \frac{m_{\mathrm{in}}\,c_q\,v^2 + m_{\mathrm{in}}\,c_q\,(c_q^2 - v^2)}{\sqrt{c_q^2 - v^2}}
  = \frac{m_{\mathrm{in}}\,c_q^3}{\sqrt{c_q^2 - v^2}}
  = \frac{m_{\mathrm{in}}\,c_q^2}{\sqrt{1 - v^2/c_q^2}}.
$$

Setting $v = 0$ yields $E(0) = m_{\mathrm{in}}\,c_q^2 = m_{\mathrm{in}}/(q - 1)^2$. Subtracting $p(v)^2\,c_q^2$ from $E(v)^2$ over the common denominator $c_q^2 - v^2 > 0$ gives

$$
  E(v)^2 - p(v)^2\,c_q^2
  = \frac{m_{\mathrm{in}}^2\,c_q^4\,(c_q^2 - v^2)}{c_q^2 - v^2}
  = \bigl(m_{\mathrm{in}}\,c_q^2\bigr)^2.
$$

Finally, for every $\varepsilon > 0$, choosing $\delta = \sqrt{\varepsilon} > 0$ ensures that $0 < |q - 1| < \delta$ implies $0 < (q - 1)^2 < \varepsilon$, whence $c_q^2 = 1/(q - 1)^2 > 1/\varepsilon$.

*Part 2.*
Under the boost-invariance equivalence hypothesis $m_{\mathrm{in}}(\beta) = \mathfrak{m}(\beta)$ for each braid class $\beta$, substituting this equality into the rest-frame evaluation $E(0) = m_{\mathrm{in}}\,c_q^2$ of Part 1 yields $\mathfrak{E}(\beta) = \mathfrak{m}(\beta)\,c_q^2 = \mathfrak{m}(\beta)/(q - 1)^2$. $\square$
