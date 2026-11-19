**Proof.**

*Forward direction.* In a one-dimensional representation $V_\lambda$ with eigenvalue $\alpha$ (either $q$ or $-q^{-1}$), the generator $\sigma_i^{-1}$ has eigenvalue $\alpha^{-1}$. This follows from $\sigma^2 = h\sigma + 1$, which gives $\sigma^{-1} = \sigma - h$. Thus, the eigenvalue of $\sigma^{-1}$ is $\alpha - h$. For $\alpha = q$, $q - h = q^{-1}$; for $\alpha = -q^{-1}$, $-q^{-1} - h = -q$.

Under the bar involution $q \mapsto q^{-1}$, the eigenvalue $q$ maps to $q^{-1}$ and $-q^{-1}$ maps to $-q$. These exactly match the action of $C$:

$$
  C\colon q \mapsto q^{-1},\quad -q^{-1} \mapsto -q
  \qquad = \qquad
  \mathrm{bar}\colon q \mapsto q^{-1},\quad -q^{-1} \mapsto -q.
$$

Thus, $\chi^\lambda(C(\beta)) = \chi^\lambda(\mathrm{bar}(\beta))$ for all one-dimensional $\lambda$.

*Reverse direction.* In $H_3(q)$, the standard representation $(2,1)$ has dimension 2. The Hoefsmit seminormal matrix for $\sigma_1$ contains a $2 \times 2$ block with the off-diagonal entry $b = \sqrt{a_\rho \cdot a_{-\rho} + 1}$, which is irrational in $q$. Under $C$, $\sigma_1 \mapsto \sigma_1 - h \cdot I$. This shifts the diagonal by $-h$ but leaves $b$ unchanged. Conversely, the bar involution $q \mapsto q^{-1}$ modifies both diagonal and off-diagonal entries, since $b$ depends on $q$ through $a_\rho = h/(1-q^{-2\rho})$. These operations yield different matrices and consequently different traces.

Explicitly evaluated at $q_0$: $\chi^{(2,1)}(\pi^+, q_0) = -(h^2+1) \approx -1.044$, $\chi^{(2,1)}(\pi^-, q_0) \approx +1.892$ (charge conjugate), and $\chi^{(2,1)}(\pi^+, q_0^{-1}) = -(h^2+1) \approx -1.044$ (bar). Since $+1.892 \ne -1.044$, $C \ne \mathrm{bar}$ on the $(2,1)$ representation. $\square$

## Uniqueness of $H_2$

The Artin--Wedderburn decomposition requires $n! = \sum_\lambda (\dim V_\lambda)^2$. For $n = 2$, the only decomposition of $2$ into positive-integer squares is $1^2 + 1^2$. The algebra accommodates no multi-dimensional irreducible representations.

For $n \ge 3$, $n! \ge 6 > 1^2 + 1^2 = 2$. Multi-dimensional irreducible representations are strictly required. The standard representation $(n-1, 1)$ has dimension $n - 1 \ge 2$, and Artin--Wedderburn strictly requires its square $(n-1)^2$ in the sum.

The number of one-dimensional irreducible representations remains exactly two (trivial and sign) for all $n \ge 2$, because $S_n$ admits exactly two homomorphisms to $\mathbb{Z}/2\mathbb{Z}$. The hook-length formula yields $\dim V_\lambda = 1$ only for $\lambda = (n)$ or $\lambda = (1^n)$.

**Corollary.** $H_2$ is the unique Hecke level where $C = \mathrm{bar}$.
The lepton sector is algebraically distinguished as the only level where matter--antimatter conjugation coincides with CPT. For all higher levels ($H_3, H_4, \ldots$), the Artin--Wedderburn theorem forces $C \ne \mathrm{bar}$.

| $H_n$ | Irrep dimensions | $C$ vs bar | Physical sector |
|--------|-----------------|------------|-----------------|
| $H_2$ | $1, 1$ | $C = \mathrm{bar}$ | leptons |
| $H_3$ | $1, 2, 1$ | $C \ne \mathrm{bar}$ | mesons + baryons |
| $H_4$ | $1, 3, 2, 3, 1$ | $C \ne \mathrm{bar}$ | nuclear binding |

The standard representation $(n-1, 1)$ establishes the locus where $C$ and bar diverge. At $H_2$, $\dim V_{(1,1)} = 1$, averting divergence. At $H_3$, $\dim V_{(2,1)} = 2$, forcing $C \ne \mathrm{bar}$.

This clarifies three structural features:

1. **Leptonic simplicity:** $C = \mathrm{bar}$ establishes matter--antimatter symmetry as identical to CPT, requiring no independent chiral structure.
2. **Mesonic CAL-3 necessity:** $C \ne \mathrm{bar}$ demands a structure (the bar-odd normal-form component) inaccessible from the bar-symmetric lepton sector. This bar-odd component carries the chiral scale.
3. **Standard representation universality:** The active set for both baryons and mesons (via SDP shadow prices) is $(2,1)$, precisely where $C$ and bar split. The mass-carrying partition inherently breaks the $C = \mathrm{bar}$ equivalence.
