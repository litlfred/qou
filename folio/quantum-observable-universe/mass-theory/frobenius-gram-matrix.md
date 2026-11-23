## Gram matrix (symbolic in $q$)

**Proposition (symbolic entries, with the $z^3$ substitution still to be
propagated).**
*The $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
over the NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$
has the structural form below. The entries containing $z^3$ or
higher $z^k$ powers from $\mathrm{tr}_M(e^-)$ are written using the naive
length rule $\mathrm{tr}_M(T_w) = z^{\ell(w)}$, which fails on adjacent
triples; the correction $z^3 \mapsto hz^2 + z$ has still to be propagated
through them:*

$$
  G
  =
  \begin{pmatrix}
    1     & z     & z     & z^2     & z^2     & z^3 \\
    z     & hz+1  & z^2   & hz^2+z  & z^3  & g_{15} \\
    z     & z^2   & hz+1  & z^3  & hz^2+z  & g_{15} \\
    z^2   & hz^2+z & z^3 & g_{15} & g_{34} & g_{35} \\
    z^2   & z^3 & hz^2+z & g_{34} & g_{15} & g_{35} \\
    z^3 & g_{15} & g_{15} & g_{35} & g_{35} & g_{55}
  \end{pmatrix}
$$

*where (subject to the same uncorrected $z^3$ entries):*
- $g_{15} = hz^3 + z^2$ (from $\sigma_0 \cdot e^- = he^- + L_-$)
- $g_{34} = hz^3 + hz + 1$ (from $L_+ \cdot L_- = he^- + h\sigma_0 + \gamma$)
- $g_{35} = h^2z^3 + 2hz^2 + z$ (from $L_+ \cdot e^- = h^2e^- + hL_+ + hL_- + \sigma_1$)
- $g_{55} = (h^3+h)z^3 + 2h^2z^2 + 2hz + 1$ (from $e^- \cdot e^- = (h^3+h)e^- + h^2L_+ + h^2L_- + h\sigma_1 + h\sigma_0 + \gamma$)

*The matrix is **symmetric** ($G_{ij} = G_{ji}$, by cyclicity of the
Markov trace). It is **degenerate**: under the production convention D the
$(1^3)$ Wedderburn block carries $y_{(1^3)} = 0$ symbolically, so that block
lies in the radical of the form and $\det G = 0$ identically — measured
$2.89\times10^{-51}$ at 50 dps, against
$\det G = -0.18920521914403668$ under the excised convention C. $G^{-1}$ does
not exist. Any statement about the **signature** must name its pairing. On the
bilinear pairing $\mathrm{tr}_M(b_i b_j)$ that this table builds, the spectrum
at $q_0$ is $(-0.75270211,\ 0,\ +0.75270211^{\times 3},\ +4.23033923)$ under D
and $(-0.85506726,\ +0.10179667,\ +0.85506726^{\times 3},\ +3.47694980)$ under
C. On the **star** pairing $\mathrm{tr}_M(b_i b_j^*)$ — the correct one, since
the Hecke star is $T_w^* = T_{w^{-1}}$, which swaps $L_+ \leftrightarrow L_-$
on this basis — the form is positive: $(6,0,0)$ under C, $(5,0,1)$ under D.
So the form is not indefinite or Lorentzian; an indefinite signature appears
only on the bilinear pairing. What survives both pairings is the single null
direction under D.*

The Markov-trace computation of the NF basis elements, the
operator-identification via the Frobenius dual, and the annihilation
identity $e^- \cdot e^+ = \gamma$ are collected in
[the Frobenius Gram-matrix context](#rem:frobenius-gram-matrix-context).
