Write $w_+ = q^3/(q^2+1)$ and $w_- = q^{-1}/(q^2+1)$ for the two crossing weights of the [pair Skein mass formula](#lem:pair-skein-mass-formula), so that $\mathcal{S}_{ab} = w_+\mu_a + w_-\mu_b$ and $w_+ + w_- = \kappa$. Substituting into the two nucleon sums gives

$$
  m_p = (3w_+ + w_-)\,\mu_{\mathfrak{u}} + 2w_-\,\mu_{\mathfrak{d}},
  \qquad
  m_n = 2w_+\,\mu_{\mathfrak{u}} + (w_+ + 3w_-)\,\mu_{\mathfrak{d}}.
$$

*Part (i).* The cross term $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ appears in both sums and cancels in the difference, leaving

$$
  m_n - m_p = \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}
  = (w_+ + w_-)(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}})
  = \kappa\,(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}).
$$

*Part (ii).* The coefficient matrix of the linear form above has determinant

$$
  (3w_+ + w_-)(w_+ + 3w_-) - (2w_-)(2w_+) = 3(w_+ + w_-)^2 = 3\kappa^2 .
$$

Under the hypotheses, $\kappa = (q^4+1)/\bigl(q(q^2+1)\bigr) \neq 0$ and $3$ is invertible, so the determinant is invertible, and Cramer's rule gives the two-sided inverse

$$
  \mu_{\mathfrak{u}} = \frac{(w_+ + 3w_-)\,m_p - 2w_-\,m_n}{3\kappa^2},
  \qquad
  \mu_{\mathfrak{d}} = \frac{(3w_+ + w_-)\,m_n - 2w_+\,m_p}{3\kappa^2}.
$$

Substituting these into the linear form returns $(m_p, m_n)$, and substituting the linear form into these returns $(\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}})$, so the map is a bijection. Both parts are identities in $q$; no value of $q$ and no measured mass is used. $\square$
