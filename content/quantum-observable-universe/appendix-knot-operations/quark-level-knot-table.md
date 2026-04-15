Each atom decomposes into the six-element NF basis
$\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ of $H_3(q)$.
The hadron-level representation captures the same Markov trace
$\mathrm{tr}_M$ and Frobenius stability as the full quark-level
braid word, but with 6 coefficients per atom instead of thousands.

$$
  \mathrm{NF}(Z,N) = \sum_{b \in \mathcal{B}} c_b(Z,N) \cdot b,
  \qquad
  \mathrm{tr}_M = \sum_b c_b \, z^{|b|}
$$

| Atom | $A$ | $\mathrm{tr}_M$ | net | $B$ (MeV) | Frobenius |
|------|-----|-----------------|-----|-----------|-----------|
| Proton | 1 | $0.4380$ | $0.999$ | — | $\checkmark$ |
| Neutron | 1 | $0.3205$ | $0.811$ | — | $\checkmark$ |
| Protium | 1 | $0.3104$ | $1.025$ | $0$ | $\checkmark$ |
| Deuterium | 2 | $0.7645$ | $1.827$ | $2.84$ | $\checkmark$ |
| Tritium | 3 | $1.0301$ | $2.979$ | $8.48$ | $\checkmark$ |
| ${}^3$He | 3 | $0.2081$ | $1.973$ | $7.72$ | $\checkmark$ |
| ${}^4$He | 4 | $2.7489$ | $4.150$ | $29.46$ | $\checkmark$ |
| ${}^6$Li | 6 | $3.022$ | $7.996$ | $33.28$ | $\checkmark$ |
| ${}^{12}$C | 12 | $40.93$ | $79.74$ | $92.29$ | $\checkmark$ |
| ${}^{14}$C | 14 | $107.6$ | $227.9$ | $103.8$ | $\checkmark$ |
| ${}^{14}$N | 14 | $58.44$ | $160.5$ | $104.2$ | $\checkmark$ |
| ${}^{16}$O | 16 | $170.7$ | $354.6$ | $128.7$ | $\checkmark$ |
| ${}^{28}$Si | 28 | $1.39 \times 10^4$ | $3.18 \times 10^4$ | $234.4$ | $\checkmark$ |
| ${}^{40}$Ca | 40 | $1.22 \times 10^6$ | $2.88 \times 10^6$ | $343.2$ | $\checkmark$ |
| ${}^{56}$Fe | 56 | $9.09 \times 10^8$ | $2.21 \times 10^9$ | $490.5$ | $\checkmark$ |

All 19 atoms pass the Frobenius positivity check ($G \cdot \vec{c} \geq 0$),
confirming that the hadron-level NF lies in the physical cone of $H_3(q)$.

The NF coefficients for each atom (6 values) are in the computation
witness `hadron-knot-table.witness.json`.
