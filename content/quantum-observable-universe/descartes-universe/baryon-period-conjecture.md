The proton--electron mass ratio $m_p/m_e \approx 1836$ is determined by the ratio of Picard--Lefschetz thimble periods of the Seiberg--Witten differential on the Descartes elliptic curve $\mathcal{E}_q$.

Specifically, define the **degree-$k$ thimble period** as:

$$
\Pi^{(k)} = \sum_\sigma n_\sigma^{(k)} \oint_{\mathcal{J}_\sigma} \lambda_{\mathrm{SW}}^{(k)}\, dz
$$

where $\mathcal{J}_\sigma$ are the Picard--Lefschetz thimbles of the color-tube cubic discriminant, $n_\sigma^{(k)}$ are the intersection numbers at vertical degree $k$, and $\lambda_{\mathrm{SW}}^{(k)}$ is the $k$-th jet prolongation of the Seiberg--Witten differential.

The electron mass arises from $\Pi^{(0)}$ (baseline period, no prolongation), the muon mass from $\Pi^{(1)}$ (first prolongation, capturing the residue at the discriminant pole), and the baryon mass scale from the **simultaneous product of all three color prolongations**.

## Simultaneous 3-root prescription

The baryon has three color channels.  Rather than tracking a single root of the color-tube cubic $F(z,c) = 0$, the baryon period integrates the **product of all three color prolongations simultaneously**:

$$
\lambda_{\mathrm{baryon}}(z) = \prod_{k=1}^{3} \frac{dc_k}{dz} = \prod_{k=1}^{3} \left(-\frac{\partial F/\partial z}{\partial F/\partial c}\bigg|_{c=c_k(z)}\right)
$$

where $c_1(z), c_2(z), c_3(z)$ are the three roots of the color-tube cubic at each $z$.

**Conjecture.** The proton mass is given by

$$
\frac{m_p}{m_e} = \frac{\mathrm{Vol}(\mathfrak{B}_3)}{\hbar_q^2} \times \mathcal{A}(q_0)
$$

where the color-tube amplification factor is the ratio of baryon to electron real-axis periods:

$$
\mathcal{A}(q_0) = \frac{\left|\,\displaystyle\int_{-a}^{a} \prod_{k=1}^{3} \frac{dc_k}{dz}\, dz\,\right|}{\left|\,\displaystyle\int_{-a}^{a} (c_0 + z)\, dz\,\right|}
$$

integrated over the symmetric interval $[-a, a]$ with $a = (4-q)/(4q+3)$.

## Numerical evidence

At $q_0 \approx 1.1100$:

- $a = (4-q_0)/(4q_0+3) \approx 0.3884$
- $\mathcal{A}(q_0) \approx 2.4599$
- $\mathrm{Vol}(\mathfrak{B}_3)/\hbar_q^2 \approx 746.42$
- $m_p \approx 938.267$ MeV (CODATA: $938.272$ MeV, error $\approx 0.0006\%$)

This would reduce the calibration inputs from three ($m_e$, $m_\mu/m_e$, $m_p$) to two ($m_e$, $m_\mu/m_e$), since the proton mass is derived from the substrate parameter $q_0$ and the Borromean link volume alone.
