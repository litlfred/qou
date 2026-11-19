The subtrahend $1/[k]_q!$ of the [knot operator energy](#def:knot-operator-energy) is $\min_\lambda\, w_\lambda/d_\lambda$, the minimum taken across partitions of $k$ and attained by the trivial $1$-dimensional $(k)$ and $(1^k)$ representations.

**Note (2026-09-05).** The subtrahend $1/[k]_q!$ was once described in the definition as "the LP-dual variable of the normalisation constraint". It is not: the net-constraint dual of [the operator-selection LP](#prop:operator-selection-lp) is identically zero at every $n$ and $q$, because the NF basis contains the identity and so the first Frobenius row is the objective vector. The quantity subtracted above is the weight minimum, which is what the displayed formula computes; the energy $E(\lambda, q)$ is unchanged.

**Values.** The energy takes values in:

- Archimedean realisation $R = \mathbb{R}$: $E(\lambda, q) \in \mathbb{R}_{\geq 0}$ (totally ordered).
- Non-archimedean $\mathbb{Q}_p$: $E(\lambda, q) \in \{p^{-n} : n \in \mathbb{Z}\} \cup \{0\}$ (totally ordered).
- Finite field $\mathbb{F}_p$: no archimedean absolute value exists. The energy filtration is undefined. Confinement falls back to ILP feasibility (see [stable atom](#def:stable-atom)), which *is* base-ring-independent.
