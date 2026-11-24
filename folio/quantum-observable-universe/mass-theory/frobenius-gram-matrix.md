## Gram matrix (symbolic in $q$)

**Proposition.**
*Let $h = q - q^{-1}$ and let $z = \mathrm{tr}_M(\sigma_0)$ be the Markov parameter, so that by [the three-strand Markov trace identity](#prop:corrected-markov-trace) the longest-word trace is $e := \mathrm{tr}_M(e^-) = \mathrm{tr}_M(\sigma_0\sigma_1\sigma_0) = hz^2 + z$. The $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ over the normal-form basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ of $H_3(q)$ is*

$$
  G
  =
  \begin{pmatrix}
    1     & z     & z     & z^2     & z^2     & hz^2+z \\
    z     & hz+1  & z^2   & hz^2+z  & hz^2+z  & g_{15} \\
    z     & z^2   & hz+1  & hz^2+z  & hz^2+z  & g_{15} \\
    z^2   & hz^2+z & hz^2+z & g_{15} & g_{34} & g_{35} \\
    z^2   & hz^2+z & hz^2+z & g_{34} & g_{15} & g_{35} \\
    hz^2+z & g_{15} & g_{15} & g_{35} & g_{35} & g_{55}
  \end{pmatrix}
$$

*where, substituting $e = hz^2 + z$ into each reduced basis product:*
- $g_{15} = h\,e + z^2 = (h^2 + 1)z^2 + hz$ (from $\sigma_0 \cdot e^- = he^- + L_-$ and $\sigma_1 \cdot e^- = L_+ L_+ = he^- + L_+$)
- $g_{34} = h\,e + hz + 1 = (hz + 1)^2$ (from $L_+ \cdot L_- = he^- + h\sigma_0 + \gamma$)
- $g_{35} = h^2 e + 2hz^2 + z = (h^3 + 2h)z^2 + (h^2 + 1)z$ (from $L_+ \cdot e^- = h^2e^- + hL_+ + hL_- + \sigma_1$)
- $g_{55} = (h^3+h)e + 2h^2z^2 + 2hz + 1 = (h^4 + 3h^2)z^2 + (h^3 + 3h)z + 1$ (from $e^- \cdot e^- = (h^3+h)e^- + h^2L_+ + h^2L_- + h\sigma_1 + h\sigma_0 + \gamma$)

*The matrix is **symmetric** ($G_{ij} = G_{ji}$, by cyclicity of the
Markov trace), with determinant $\det G(q, z) = -(z - q)^5(qz + 1)^5\bigl((q^2 + 1)z - q^3\bigr)(q^3 z + qz + 1)/q^8$. At the Markov parameter $z = q^3/(q^2 + 1)$, the $(1^3)$ Wedderburn block carries $y_{(1^3)} = 0$ symbolically, so that block lies in the radical of the form, $\det G = 0$ identically, and $G^{-1}$ does not exist on $H_3(q)$ (the induced pairing is non-degenerate on the $5$-dimensional Temperley--Lieb quotient $\mathrm{TL}_3(q)$). Any statement about the **signature** must name its pairing. On the
bilinear pairing $\mathrm{tr}_M(b_i b_j)$ above, the spectrum
at $q_0$ is $(-0.75270211,\ 0,\ +0.75270211^{\times 3},\ +4.23033923)$.
On the **star** pairing $\mathrm{tr}_M(b_i b_j^*)$ — where
the Hecke star $T_w^* = T_{w^{-1}}$ exchanges $L_+ \leftrightarrow L_-$
on this basis — the form is positive semidefinite of signature $(5,0,1)$.
An indefinite signature appears
only on the untwisted bilinear pairing; what survives both pairings at $z = q^3/(q^2 + 1)$ is the single null
direction.*

The Markov-trace computation of the NF basis elements, the
operator-identification via the Frobenius dual, and the annihilation
identity $e^- \cdot e^+ = \gamma$ are collected in
[the Frobenius Gram-matrix context](#rem:frobenius-gram-matrix-context).
