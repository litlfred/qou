Write $D = q^{1/2} + q^{-1/2}$. Substituting $\mathcal{S}_{ab} = (q\mu_a + q^{-1}\mu_b)/D$ from the [pair Skein mass formula](#lem:pair-skein-mass-formula) into the two nucleon sums gives

$$
  D\,m_p = (3q + q^{-1})\,\mu_{\mathfrak{u}} + 2q^{-1}\,\mu_{\mathfrak{d}},
  \qquad
  D\,m_n = 2q\,\mu_{\mathfrak{u}} + (q + 3q^{-1})\,\mu_{\mathfrak{d}}.
$$

*Part (i).* The cross term $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ appears in both sums and cancels in the difference, leaving

$$
  m_n - m_p = \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}
  = \frac{(q + q^{-1})(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})}{D}.
$$

*Part (ii).* The coefficient matrix of the linear form above has determinant

$$
  (3q + q^{-1})(q + 3q^{-1}) - (2q^{-1})(2q) = 3q^2 + 6 + 3q^{-2} = 3\,[2]_q^2 .
$$

Dividing by $D^2$ gives the determinant of the map. Under the hypotheses ($3$, $D$ and $[2]_q$ invertible), the determinant is invertible, and Cramer's rule gives the two-sided inverse

$$
  \mu_{\mathfrak{u}} = \frac{D\bigl((q + 3q^{-1})\,m_p - 2q^{-1}\,m_n\bigr)}{3\,[2]_q^2},
  \qquad
  \mu_{\mathfrak{d}} = \frac{D\bigl((3q + q^{-1})\,m_n - 2q\,m_p\bigr)}{3\,[2]_q^2}.
$$

Substituting these into the linear form returns $(m_p, m_n)$, and substituting the linear form into these returns $(\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}})$, so the map is a bijection. Both parts are identities in $q$; no value of $q$ and no measured mass is used. $\square$
