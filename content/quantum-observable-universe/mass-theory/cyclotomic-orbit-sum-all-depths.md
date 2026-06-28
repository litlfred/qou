**Proposition (general orbit-sum identity at every depth $n$).**

[`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
established the orbit sum at $n = 3$. *This proposition extends to
all depths $n \geq 2$:*

$$
  \boxed{\;
    \sum_{k = 1}^{N - 1} \mathrm{Cl}_n\!\left(\tfrac{2\pi k}{N}\right)
    \;=\;
    \begin{cases}
      \bigl(N^{1 - n} - 1\bigr)\, \zeta(n) & \text{$n$ odd}, \\[4pt]
      0 & \text{$n$ even},
    \end{cases}
  \;}
$$

*where $\mathrm{Cl}_n$ is the Glaisher Clausen function*:

- *$\mathrm{Cl}_n(\theta) = \mathrm{Re}\,\mathrm{Li}_n(e^{i\theta})$
 for $n$ odd*
- *$\mathrm{Cl}_n(\theta) = \mathrm{Im}\,\mathrm{Li}_n(e^{i\theta})$
 for $n$ even.*
### Significance

**For $n$ odd**: orbit sum reduces to $\zeta(n)$ — one dim of
genuinely-new content "absorbed" into the classical $\zeta(n)$-line
of $\mathcal{P}_n / \mathcal{P}_{n-1}$ (when $n$ is odd, $\zeta(n)$ is
NOT Tate-rational, conjecturally transcendental over $\mathbb{Q}$).

**For $n$ even**: orbit sum vanishes by definition. The individual
$\mathrm{Cl}_n$ values are bar-anti-symmetric (Glaisher convention),
They pair-cancel. No reduction occurs — all $(N - 1)/2$ distinct
$\mathrm{Cl}_n$ magnitudes are independent (modulo Beilinson).

### Generalises Theorem B

Theorem B ([`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general))
is the $n = 3$ case. This proposition extends the pattern to all $n$
with a single proof.

### Dimension consequences

Combined with
[`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality):

See [Table 2](#tbl:cyclotomic-orbit-sum-all-depths-table2-data).

The depth-3 case (round 3 + round 4 of ) gave $(K - 3)/2$.
The general formula here is parity-dependent: $(K - 3)/2$ for $n$
odd, $(K - 1)/2$ for $n$ even.

### Cross-references

- Special case $n = 3$: [`prop:cyclotomic-cl3-orbit-sum-general`](#prop:cyclotomic-cl3-orbit-sum-general)
- Tate-rationality companion: [`prop:jonquiere-cyclotomic-tate-rationality`](#prop:jonquiere-cyclotomic-tate-rationality)
- Dimension synthesis: [`prop:cyclotomic-dimension-synthesis-all-depths`](#prop:cyclotomic-dimension-synthesis-all-depths)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
