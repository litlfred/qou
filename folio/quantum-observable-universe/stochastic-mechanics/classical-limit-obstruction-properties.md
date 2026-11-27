The [classical limit obstruction](#def:classical-limit-obstruction) sits in a Hochschild tower whose vanishing controls flatness of the $q \to 1$ deformation.

**The Hochschild tower.** The Hochschild cohomology groups $HH^n(\mathcal{U}_q, \mathrm{Ad})$ govern the deformation theory of the aether family $\{A_q\}_{q \in \mathbb{G}_m}$:
- $HH^0(\mathrm{Ad})$: hidden symmetries.
- $HH^1(\mathrm{Ad})$: outer derivations.
- $HH^2(\mathrm{Ad})$: obstructions to extending deformations across $q = 1$.
- $HH^3(\mathrm{Ad})$: secondary obstructions.

A property $\mathcal{P}(q)$ persists through $q = 1$ if and only if its obstruction class $[\mathcal{P}] \in HH^2(\mathrm{Ad})$ vanishes.

**Control of the classical limit by $HH^2$.** The classical limit $q \to 1$ is a deformation-theoretic specialisation. The obstructions to flatness at each order in $(q-1)$ live in $HH^2$. Expanding $A_q = A_1 + (q-1)\phi_1 + (q-1)^2\phi_2 + \cdots$, the first-order deformation $\phi_1$ is a Hochschild 2-cocycle. The second-order term $\phi_2$ exists iff $[\phi_1] \cup [\phi_1] = 0$ in $HH^3$. The total obstruction to the classical limit is the formal sum $\mathrm{obs}_\infty = \sum_{n \geq 1} (q-1)^n [\phi_n] \in HH^2(\mathrm{Ad})[[q-1]]$. This formal power series converges iff all Massey products vanish through the tower.

**Connection to the brane tower.** The Hochschild obstruction $[\phi_n]$ maps to the quantum characteristic class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ under the Hochschild-to-sheaf comparison map. The abstract Hochschild obstruction is computed concretely by the Euler class $\kappa_0 = e(\xi)$ and its Kummer filtration.
