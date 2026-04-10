The proton--electron mass ratio $m_p/m_e \approx 1836$ is determined by the ratio of Picard--Lefschetz thimble periods of the Seiberg--Witten differential on the Descartes elliptic curve $\mathcal{E}_q$.

Specifically, define the **degree-$k$ thimble period** as:

$$
\Pi^{(k)} = \sum_\sigma n_\sigma^{(k)} \oint_{\mathcal{J}_\sigma} \lambda_{\mathrm{SW}}^{(k)}\, dz
$$

where $\mathcal{J}_\sigma$ are the Picard--Lefschetz thimbles of the color-tube cubic discriminant, $n_\sigma^{(k)}$ are the intersection numbers at vertical degree $k$, and $\lambda_{\mathrm{SW}}^{(k)}$ is the $k$-th jet prolongation of the Seiberg--Witten differential.

The electron mass arises from $\Pi^{(0)}$ (baseline period, no prolongation), the muon mass from $\Pi^{(1)}$ (first prolongation, capturing the residue at the discriminant pole), and the baryon mass scale from a degree-2 or degree-3 period $\Pi^{(\mathrm{baryon})}$ that integrates over all three color channels simultaneously.

**Conjecture.** There exist canonical intersection numbers $n_\sigma^{(\mathrm{baryon})}$ such that

$$
\frac{m_p}{m_e} = \frac{|\Pi^{(\mathrm{baryon})}|}{|\Pi^{(0)}|} = \frac{\mathrm{Vol}(\mathfrak{B}_3)}{\hbar_q^2} \times \mathcal{A}(q_0)
$$

where $\mathrm{Vol}(\mathfrak{B}_3) \approx 7.328$ is the Borromean link volume, $\hbar_q = 1 - q^{-1}$, and $\mathcal{A}(q_0) \approx 2.460$ is the **color-tube amplification factor** arising from the thimble geometry:

$$
\mathcal{A}(q_0) = \frac{\sum_\sigma n_\sigma^{(\mathrm{baryon})} \operatorname{Res}_{z_c^\sigma}(\lambda_{\mathrm{SW}}^{(2)})}{\sum_\sigma n_\sigma^{(0)} \oint_{\mathcal{J}_\sigma} \lambda_{\mathrm{SW}}^{(0)}\, dz} \cdot \frac{\hbar_q^2}{\mathrm{Vol}(\mathfrak{B}_3)}.
$$

This would reduce the calibration inputs from three ($m_e$, $m_\mu/m_e$, $m_p$) to two ($m_e$, $m_\mu/m_e$), since the proton mass would be derived from the substrate parameter $q_0$ alone.
