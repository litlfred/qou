The molecular Hopf chain framework
([molecular Hopf chain](#def:molecular-hopf-chain)) generates the
standard classes of organic molecules by varying two parameters:
the **bond-order pattern** $(k_1, \ldots, k_{N-1})$ along the
backbone, and whether the chain is **open or closed**.

**Bond-order classification.**

| Class | Bond-order pattern | Free sites per C | Hydrogen capacity |
|-------|-------------------|:---:|:---:|
| Alkane (saturated) | $(1, 1, \ldots, 1)$ | 2 (interior), 3 (endpoint) | $2N + 2$ (chain), $2N$ (ring) |
| Alkene | $(\ldots, 2, \ldots)$ | 1 at double bond | $2N$ (one double bond) |
| Alkyne | $(\ldots, 3, \ldots)$ | 0 at triple bond | $2N - 2$ (one triple bond) |
| Cumulene | $(2, 2, \ldots, 2)$ | 0 (interior), 2 (endpoint) | 4 |
| Polyyne (carbyne) | $(1, 3, 1, 3, \ldots)$ | 0 (interior) | 2 |

**Saturation as linking-site occupancy.**
An alkane uses only single bonds ($k = 1$), leaving the maximum
number of free linking sites for hydrogen.  Each additional unit
of bond order ($k \to k + 1$) at one position consumes one free
site per adjacent carbon, reducing the hydrogen capacity by 2.
In the Hopf chain picture:

- **Saturated** = all backbone bonds are single Hopf links;
  maximum hydrogen attachment.
- **Unsaturated** = some backbone bonds are double or triple
  Hopf links; reduced hydrogen attachment.

**Open vs. closed (chain vs. ring).**

| Topology | Backbone bonds | Hydrogen formula | Naming |
|----------|:-:|---|---|
| Open chain | $N - 1$ | $\mathrm{C}_N\mathrm{H}_{2N+2-2d}$ | $n$-alkane, $n$-alkene, $\ldots$ |
| Closed ring | $N$ | $\mathrm{C}_N\mathrm{H}_{2N-2d}$ | cycloalkane, cyclohexane, $\ldots$ |

where $d = \sum_i (k_i - 1)$ is the **total degree of
unsaturation** (number of extra Hopf links beyond single bonds).

**Aromatic rings.**
A closed ring with $d = N/2$ (one extra Hopf link per two
edges — bond order $3/2$ on average) is the aromatic case
([benzene](#ex:benzene-ring)).  The secondary Hopf ring formed
by the extra trefoils is closed, producing the resonance
stabilisation.  Hückel's rule ($4n + 2$ $\pi$ electrons for
aromaticity) should correspond to the **sub-Hopf link closure
condition** applied at the molecular scale: only certain numbers
of trefoils can form a closed secondary ring, and $4n + 2$ is
the molecular analogue of the shell capacity $2n^2$.
