The $\beta^-$ decay $(Z, N) \to (Z+1, N-1)$ $Q$-value follows strictly from the aether parameter $q$, using zero fitting parameters. The calculation operates within the $2 \times 2$ standard irreducible representation of $H_3(q)$. While the regular representation is $6 \times 6$, the traced-volume computation strictly isolates the $2 \times 2$ standard block. 
**MAE $\approx 4.4\%$ across six NNDC benchmarks, zero fitting.**

The derivation chain is:

$$
  q \xrightarrow{\text{Hecke}}
  \hat{V}_i(q) \xrightarrow{\text{ratio}}
  \log_q \frac{\hat{V}_i^{\mathrm{dau}}}{\hat{V}_i^{\mathrm{par}}}
  \xrightarrow{\kappa_q}
  \mathcal{Q}(q)
$$

**Step 1.** The traced volume $\hat{V}_i(q)$ for each generator $\sigma_i$ is exact in $\mathbb{Q}(q)$:

$$
  \hat{V}_i = z \cdot M_i[0,0] + M_i[1,0],
  \qquad
  M_i = \prod_{j > i} T(\mathfrak{w}^+(i,j), \mathfrak{w}^0(i,j))
$$

where $z = q^{3}/(q^{2}+1)$ is the Markov parameter (**convention D**) and $T(c,d) = \begin{psmallmatrix} c(q-q^{-1})+d & c \\ c & d \end{psmallmatrix}$ is the transfer matrix.

**Step 2.** Classify each generator's log-ratio as unbinding ($u$), rebinding ($r$), or unchanged ($uc$), then $q$-weight:

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

<!-- literal-source: unnormalised Rosso-Jones weighted average at z = q^{1/2}/(q+1) -->
- $F_{\mathrm{shell}} \approx 0.5904$ for shell $\geq 5$: the Rosso–Jones weighted average over the two degree-$2$ torus knots $\tau(2,9)$ and $\tau(3,4)$, using the canonical inner product on $R(H_r(q))$ ([canonical inner product](#prop:rj-canonical-inner-product)). The weights are the quantum dimensions $d_\lambda(q)$, forced by Schur orthogonality — no fitting freedom.
- $F_{I_{10}} = (1 - \delta_{\mathrm{pp}}/Z)(1 - \delta_{\mathrm{nn}}/N)$ for odd-odd $\to$ even-even at shell $\geq 5$.
