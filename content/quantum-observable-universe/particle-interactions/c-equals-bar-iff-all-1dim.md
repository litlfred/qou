**Proposition ($C = \mathrm{bar}$ iff all irreps are one-dimensional).**
*On the Iwahori–Hecke algebra $H_n(q)$, charge conjugation
$C\colon \sigma_i \mapsto \sigma_i^{-1}$ and the bar involution
$\mathrm{bar}\colon q \mapsto q^{-1}$ agree on all irreducible
characters if and only if every irreducible representation of
$H_n(q)$ is one-dimensional.*

*At $H_2(q)$ (leptons): $C = \mathrm{bar}$.
At $H_3(q)$ (mesons, baryons): $C \ne \mathrm{bar}$.*

## Why $H_2$ is unique

The Artin–Wedderburn decomposition forces
$n! = \sum_\lambda (\dim V_\lambda)^2$.  For $n = 2$:
$2 = 1^2 + 1^2$ is the ONLY decomposition of $2$ as a sum of
positive-integer squares.  There is no room for a multi-dimensional
irrep.

For $n \ge 3$: $n! \ge 6 > 1^2 + 1^2 = 2$, so multi-dimensional
irreps are **forced**.  The standard representation $(n-1, 1)$ has
dimension $n - 1 \ge 2$, and Artin–Wedderburn requires its square
$(n-1)^2$ in the sum.  No rearrangement avoids it.

The 1-dimensional irreps are **always exactly 2** for $n \ge 2$
(trivial and sign), because $S_n$ has exactly 2 homomorphisms
to $\mathbb{Z}/2\mathbb{Z}$.  The hook-length formula gives
$\dim V_\lambda = 1$ only for $\lambda = (n)$ or $\lambda = (1^n)$.

**Corollary.** $H_2$ is the **unique** Hecke level where $C = \mathrm{bar}$.
The lepton sector is algebraically distinguished: it occupies the one
level where matter–antimatter conjugation coincides with CPT.
Everything above ($H_3, H_4, \ldots$) has $C \ne \mathrm{bar}$,
forced by the Artin–Wedderburn theorem.

| $H_n$ | Irrep dimensions | $C$ vs bar | Physical sector |
|--------|-----------------|------------|-----------------|
| $H_2$ | $1, 1$ | $C = \mathrm{bar}$ | leptons |
| $H_3$ | $1, 2, 1$ | $C \ne \mathrm{bar}$ | mesons + baryons |
| $H_4$ | $1, 3, 2, 3, 1$ | $C \ne \mathrm{bar}$ | nuclear binding |

The standard representation $(n-1, 1)$ (dimension $n-1$) is the
**locus where $C$ and bar diverge**.  At $H_2$, $\dim V_{(1,1)} = 1$
(still 1-dim), so no divergence.  At $H_3$, $\dim V_{(2,1)} = 2$
(first multi-dim), and $C \ne \mathrm{bar}$.

This explains:

1. **Why leptons are simpler** — $C = \mathrm{bar}$ means
   matter/antimatter symmetry is identical to CPT.  No independent
   chiral structure.

2. **Why mesons need CAL-3** — $C \ne \mathrm{bar}$ means the
   meson sector has structure (the bar-odd NF component) not
   reachable from the bar-symmetric lepton world.  The bar-odd
   component carries the chiral/Goldstone scale.

3. **Why the standard rep is universal** — $(2,1)$ is the active
   set for baryons AND mesons (SDP shadow prices), and it is WHERE
   $C$ and bar split.  The mass-carrying partition is the same
   partition that breaks the $C = \mathrm{bar}$ equivalence.
