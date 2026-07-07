<!-- FILE_START: witness-4he.md -->
The **Pauli witness** records how strongly a nucleus's Hecke normal form
is dominated by the antisymmetric channel.  For ${}^4\mathrm{He}$ ($Z=2$,
$N=2$, $A=4$), it is the exact Gröbner normal form in $H_4(q)$ after
quotient ideals $I_8 + I_9$.

$$
  F_{\mathrm{Pauli}}^{(4)} \approx 0.812
$$

The polynomial $\mathrm{net}(t)$ has $12$ terms in $\mathbb{Z}[t, t^{-1}]$,
matching the $q$-multinomial coefficient $[2]_t^2 \cdot [3]_t = 12$.
Both $Z=2$ and $N=2$ are magic, so ${}^4\mathrm{He}$ is doubly magic.

The high Pauli factor reflects the strong antisymmetric channel
dominance of the $\alpha$-particle.  In the
Hecke normal form, the alternating trace $\mathrm{tr}_{\mathrm{alt}}$
captures the full multi-generator correlation that the $2 \times 2$
transfer matrix cannot resolve.
<!-- FILE_END: witness-4he.md -->

<!-- FILE_START: witness-8be.md -->
The **Pauli witness** for ${}^8\mathrm{Be}$ ($Z=4$, $N=4$, $A=8$)
captures the antisymmetric channel of the reduced configuration, whose
weight dilutes as it spreads across the braid generators. It is the
exact Gröbner normal form in $H_8(q)$ after quotient ideals $I_8 + I_9$:

$$
  F_{\mathrm{Pauli}}^{(8)} \approx 0.368
$$

The polynomial $\mathrm{net}(t)$ has $5{,}040$ terms before reduction
($8! / 8 = 5{,}040$) and collapses to $8$ terms in the optimal basis
$\{\mathbf{1}, \sigma_0, \ldots, \sigma_6\}$ after $I_8 + I_9$
stripping.

The lower Pauli factor compared to ${}^4\mathrm{He}$ reflects the
dilution of the antisymmetric channel across $7$ generators.
${}^8\mathrm{Be}$ is even-even but not doubly magic; its instability
(decay into two $\alpha$-particles) is visible in the weight
distribution: the $\ell = 7$ fully correlated term carries less
relative amplitude than in neighbouring stable nuclei.
<!-- FILE_END: witness-8be.md -->

<!-- FILE_START: witness-12c.md -->
${}^{12}\mathrm{C}$ is the frontier of the exact symbolic witness: the
largest nucleus for which the full symbolic normal form has been computed,
and the one whose Pauli factor is the smallest in the light-nuclei table —
tracking the rapid dilution of the antisymmetric channel as $A$ grows.  Its
**Pauli witness** ($Z=6$, $N=6$, $A=12$) is the exact Gröbner normal form in
$H_{12}(q)$ after quotient ideals $I_8 + I_9$.

$$
  F_{\mathrm{Pauli}}^{(12)} \approx 0.129
$$

The polynomial $\mathrm{net}(t)$ has $479{,}001{,}600$ terms before
reduction ($12!$) and collapses to $12$ terms in the optimal basis
$\{\mathbf{1}, \sigma_0, \ldots, \sigma_{10}\}$ after $I_8 + I_9$
stripping.  The computation is exact in $\mathbb{Z}[t, t^{-1}]$.

The Hoyle state ($0_2^+$ at $7.65 \text{MeV}$) is not captured by the
ground-state normal form; it would require a separate witness at an
excited braid configuration.
<!-- FILE_END: witness-12c.md -->

