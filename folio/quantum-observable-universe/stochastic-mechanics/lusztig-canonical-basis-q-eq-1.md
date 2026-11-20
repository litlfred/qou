**Conjecture (Lusztig canonical basis closure, conditional on [`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)).**

*At the classical limit $q = 1$, the Kashiwara crystal of $H_n(q)$ ([Crystal-limit isospin degeneracy](#prop:crystal-isospin-degeneracy), at $q \to 0$) **decategorifies** to the Lusztig canonical basis of the group algebra $\mathbb{Z}[S_n]$. The Kazhdan–Lusztig basis polynomials $\{P_{y, w}(q)\}$ are the structure constants of this decategorification. At $q = 1$, they reduce to integer multiplicities of canonical-basis elements.*

*Combined with the $q \to 0$ Kashiwara limit and the $q \to \infty$ reverse limit ([Reverse limit $q \to \infty$](reverse-limit-q-to-infinity.md)), this completes the limit-duality picture for $H_n(q)$:*

$$
  \begin{array}{c}
    q \to 0 \text{ (Kashiwara crystal)} \\
    \updownarrow \text{ bar} \\
    q \to \infty \text{ (reverse crystal)} \\
    \\
    q = 1 \text{ (Lusztig canonical basis, this conjecture)} \\
    \updownarrow \text{ specialise} \\
    q = q_0 \text{ (substrate, framework production)} \\
  \end{array}
$$

## The full limit-duality picture

| Limit | Categorical structure |
|-------|----------------------|
| $q = 1$ (classical) | Lusztig canonical basis / KL polynomials (this conjecture) |
| $q = q_0$ (substrate $\approx$ 1.11) | full Hecke algebra |
| $q \to 0$ (Kashiwara) | crystal basis / 0-Hecke |
| $q \to \infty$ (reverse) | bar-image of Kashiwara |

This conjecture ties the Kashiwara limit to the bar involution via the decategorification functor: the Lusztig canonical basis at $q = 1$ is the bar-invariant Kazhdan–Lusztig basis of the group algebra. The Kashiwara crystal at $q \to 0$ is its quantum lift via canonical-basis-preserving deformation.

## Connection to isospin and Type-B folding

- The isospin $\mathbb{Z}/2$ swap acts on the Lusztig canonical basis as the sign character of the abelianised $S_n$. This provides a classical-limit picture of the canonical isospin.
- Type-B folding provides the symmetric-crystal structure that descends to a bar-invariant Lusztig basis at $q = 1$. This closes the Cluster A (CPT) story at the decategorification level.

## Diagnostics

- **GB filtration**: KL polynomials are filtered by length $\ell(w)$, the same filtration as the Hecke algebra.
- **Jet order**: evaluated at $q = 1$, the KL polynomials are integers (the canonical-basis multiplicities).
- **Bar-symmetry**: bar-symmetric by construction.
