*Let $\mathrm{tr}$ be a Markov trace on $H_3(R, q)$ with parameter $z = q^{3}/(q^{2}+1)$, and let $h = q - q^{-1}$. On the representatives $r_0 = \mathbf{1}$, $r_1 = \sigma_1 - \sigma_2$, $r_2 = \sigma_1\sigma_2$, $r_3 = \sigma_1\sigma_2\sigma_1$, the prefactors $\alpha_k = \mathrm{tr}(r_k)$ are*

$$
  \boxed{\;
    \alpha_0 \,=\, 1, \qquad
    \alpha_1 \,=\, 0, \qquad
    \alpha_2 \,=\, z^2, \qquad
    \alpha_3 \,=\, h\,z^2 + z \,=\, z\,(h\,z + 1) \,=\, \frac{q^{3}(q^{4}+1)}{(q^{2}+1)^{2}}.
  \;}
$$

*Two of these values are structural and hold for every trace, not only the Markov one. $r_1$ is a sum of commutators, so $\alpha_1 = 0$. $r_3 \equiv h\,r_2 + \sigma_2$ modulo commutators, so $\alpha_3 = h\,\alpha_2 + \mathrm{tr}(\sigma_1)$.*

In the length-filtered cocentre ([explicit $H_3$ pages](#prop:spectral-sequence-h3-explicit)), $r_1$ and $r_3$ are not new classes: $r_1$ is killed in length $1$, and $r_3$ drops to lengths $2$ and $1$. The $E_\infty$ classes are $[\mathbf{1}], [\sigma_1], [\sigma_1\sigma_2]$, with traces $1, z, z^2$. The values are $q$-algebraic, and no transcendental constants or fitted numbers appear.
