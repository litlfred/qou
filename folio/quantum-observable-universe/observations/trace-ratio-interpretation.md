**Computational results.**
The trace ratio $\hat{V}^{\mathrm{par}} / \hat{V}^{\mathrm{dau}}$ at each affected generator is tabulated for all six verification nuclei in [Table: Trace ratio per affected generator](#tbl:trace-ratio-interpretation-table-data).

The trace ratio grows with $p$ (the number of affected generators), reflecting the increasing number of crossings that change type. The squared ratio $|\mathcal{M}_q|^2$ spans 10 orders of magnitude. The observed variation in nuclear matrix elements is smaller: $\log ft$ from 3 to 9 corresponds to $|M|^2$ spanning $\sim 10^6$. The two are the same *kind* of quantity and the model range brackets the observed one, but it over-spans it by about four orders of magnitude, so this is a consistency-of-scale remark and not a quantitative match.

The growth of the ratio with $p$ means heavier nuclei have larger topological matrix elements, which drives faster decay rates. This aligns with the observation that allowed beta transitions in heavy nuclei tend to have shorter half-lives (smaller $\log ft$) than those in light nuclei.

**The half-life formula (final form).**
Combining the trace ratio with the phase-space integral yields:

$$
  t_{1/2}
  = 
  \frac{\ln 2 \cdot 2N_v^4}{243\mathfrak{E}_{\times} \cdot \mu_0}
   \cdot 
  \frac{1}{[2]_q  \cdot  s^2}
   \cdot 
  \frac{1}{f(Z_d, Q)}
   \cdot 
  \prod_{i=0}^{p}
  \left|
    \frac{\hat{V}_i^{\mathrm{dau}}}{\hat{V}_i^{\mathrm{par}}}
  \right|^2
$$

Here $s = q^{1/2} - q^{-1/2}$ is the Skein amplitude, $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$ is the crossing energy, $\mu_0$ is the single dimensional scale, and $N_v$ is the effective crossing count of the weak scale ($v = N_v\mathfrak{E}_{\times}\mu_0$). The function $f(Z_d, Q)$ is the Coulomb-corrected phase space integral ([Skein-Coulomb enhancement](#prop:skein-coulomb-enhancement)). The prefactor replaces the standard-physics combination $G_F^2m_e^5/(2\pi^3)$ ([hadron half-life](#prop:hadron-half-life)). The product of volume ratios provides the topological part of $|\mathcal{M}_q|^2$.
