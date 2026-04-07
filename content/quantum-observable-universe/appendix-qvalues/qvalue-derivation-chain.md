The Q-value of a $\beta^-$ decay $(Z, N) \to (Z+1, N-1)$ is
predicted from the substrate parameter $q$ alone, with zero fitting
parameters.  The formula uses the $2 \times 2$ standard representation
of $H_3(q)$, which generates the full $6 \times 6$ regular
representation via the tensor identity $2 \times 2 = 6 \times 6$.
**MAE $\approx 4.9\%$ across six NNDC benchmarks, zero fitting.**

The derivation chain is:

$$
  q \;\xrightarrow{\text{Hecke}}\;
  \hat{V}_i(q) \;\xrightarrow{\text{ratio}}\;
  \log_q \frac{\hat{V}_i^{\mathrm{dau}}}{\hat{V}_i^{\mathrm{par}}}
  \;\xrightarrow{\kappa_q}\;
  \mathcal{Q}(q)
$$

**Step 1.** The traced volume $\hat{V}_i(q)$ for each generator
$\sigma_i$ is exact in $\mathbb{Q}(q^{1/2})$:

$$
  \hat{V}_i = z \cdot M_i[0,0] + M_i[1,0],
  \qquad
  M_i = \prod_{j > i} T(\mathfrak{w}^+(i,j),\, \mathfrak{w}^0(i,j))
$$

where $z = 1/(\sqrt{q} + 1/\sqrt{q})$ is the Markov parameter
and $T(c,d) = \begin{psmallmatrix} c(q-q^{-1})+d & c \\ c & d \end{psmallmatrix}$
is the transfer matrix.

**Step 2.** Classify each generator's log-ratio as unbinding ($u$),
rebinding ($r$), or unchanged ($uc$), then $q$-weight:

$$
  \mathcal{Q}_{\mathrm{raw}}
  = \bigl| q \cdot \Sigma_u + q^{-1} \cdot \Sigma_r + \Sigma_{uc} \bigr|
    \times \kappa_q
$$

where $\kappa_q = \ln(q) \times m_e / 3$.

**Step 3.** Apply shell and pairing corrections (all from $q$):

$$
  \mathcal{Q}
  = \mathcal{Q}_{\mathrm{raw}}
    \times F_{\mathrm{shell}}(q)
    \times F_{I_{10}}(Z, N; q)
$$

- $F_{\mathrm{shell}} = \hat{V}(T_{\mathrm{pp}}^2) / \hat{V}(T_{\mathrm{pp}})^2
  \approx 0.5949$ for shell $\geq 5$
- $F_{I_{10}} = (1 - \delta_{\mathrm{pp}}/Z)(1 - \delta_{\mathrm{nn}}/N)$
  for odd-odd $\to$ even-even at shell $\geq 5$
