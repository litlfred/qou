*Filter $H_3(R, q)$ by Coxeter length, $F_k = \mathrm{span}_R\{T_w : \ell(w) \le k\}$, and pass to the cocentre $\mathrm{HH}_0(H_3) = H_3/[H_3, H_3]$, through which every trace factors. Write the quadratic relation as $\sigma_i^2 = a\,\sigma_i + b$ (so $a = h = q - q^{-1}$, $b = 1$). The pages are explicit:*

| length $k$ | $E_1$ basis | killed by $d$ | $E_\infty$ basis |
|:--:|--|--|--|
| $0$ | $\mathbf{1}$ | none | $[\mathbf{1}]$ |
| $1$ | $\sigma_1,\ \sigma_2$ | $\sigma_1 - \sigma_2$ | $[\sigma_1]$ |
| $2$ | $\sigma_1\sigma_2,\ \sigma_2\sigma_1$ | $\sigma_1\sigma_2 - \sigma_2\sigma_1$ | $[\sigma_1\sigma_2]$ |
| $3$ | $\sigma_1\sigma_2\sigma_1$ | $\sigma_1\sigma_2\sigma_1 - a\,\sigma_1\sigma_2 - b\,\sigma_2$ | none |

*so the $E_1$ ranks are $1, 2, 2, 1$ and the $E_\infty$ ranks are $1, 1, 1, 0$. The kills are explicit identities modulo commutators:*

$$
  b\,(\sigma_1 - \sigma_2) \;=\; [\sigma_1, \sigma_2\sigma_1] - [\sigma_2, \sigma_1\sigma_2] - a\,[\sigma_1, \sigma_2],
  \qquad
  \sigma_1\sigma_2\sigma_1 \;\equiv\; a\,\sigma_1\sigma_2 + b\,\sigma_2 \pmod{[H_3, H_3]}.
$$

*The three surviving classes are independent: the trivial, sign and reflection characters separate them with determinant $(Q+1)(Q^2+Q+1)$, $Q = q^2$. Hence $\mathrm{HH}_0(H_3)$ has rank $3$, the number of partitions of $3$, whenever $[2]_Q[3]_Q$ is not a zero divisor.*

Every identity holds over a generic commutative ring with the Hecke and braid relations, and the Lean sibling proves each one. A trace $\tau$ is therefore fixed by $\tau(\mathbf{1})$, $\tau(\sigma_1)$ and $\tau(\sigma_1\sigma_2)$. On the six standard basis words it takes the values $t_0, t_1, t_1, t_2, t_2, a t_2 + t_1$.
