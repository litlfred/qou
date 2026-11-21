Write $[2]_q = q + q^{-1}$. By convention D, $[2]_q \neq 0$ (the [pair Skein mass formula](#lem:pair-skein-mass-formula) gives $(q - z)[2]_q = 1$). Substituting $\mathcal{S}_{ab} = (q^2\mu_a + q^{-2}\mu_b)/[2]_q$ into the two nucleon sums gives

$$
  [2]_q\,m_p = (3q^2 + q^{-2})\,\mu_{\mathfrak{u}} + 2q^{-2}\,\mu_{\mathfrak{d}},
  \qquad
  [2]_q\,m_n = 2q^2\,\mu_{\mathfrak{u}} + (q^2 + 3q^{-2})\,\mu_{\mathfrak{d}}.
$$

*Part (i).* The cross term $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ appears in both sums and cancels in the difference, leaving

$$
  m_n - m_p = \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}
  = \frac{(q^2 + q^{-2})(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})}{[2]_q}.
$$

Since $[4]_q = (q^2 + q^{-2})[2]_q$, the coefficient is $[4]_q/[2]_q^2$.

*Part (ii).* The coefficient matrix of the linear form above has determinant

$$
  (3q^2 + q^{-2})(q^2 + 3q^{-2}) - (2q^{-2})(2q^2) = 3q^4 + 6 + 3q^{-4} = 3\,(q^2 + q^{-2})^2 .
$$

Dividing by $[2]_q^2$ gives the determinant of the map. Under the hypotheses ($3$ and $q^2 + q^{-2}$ invertible), the determinant is invertible, and Cramer's rule gives the two-sided inverse

$$
  \mu_{\mathfrak{u}} = \frac{[2]_q\bigl((q^2 + 3q^{-2})\,m_p - 2q^{-2}\,m_n\bigr)}{3\,(q^2 + q^{-2})^2},
  \qquad
  \mu_{\mathfrak{d}} = \frac{[2]_q\bigl((3q^2 + q^{-2})\,m_n - 2q^2\,m_p\bigr)}{3\,(q^2 + q^{-2})^2}.
$$

Substituting these into the linear form returns $(m_p, m_n)$, and substituting the linear form into these returns $(\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}})$, so the map is a bijection. Both parts are identities in $q$; no value of $q$ and no measured mass is used. $\square$
