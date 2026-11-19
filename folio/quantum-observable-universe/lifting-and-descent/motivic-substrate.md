The QOU framework's algebraic aether appears through two faces: the [Frobenius–Hopf aether](#def:frobenius-hopf-substrate) and the [adelic aether](#def:adelic-substrate). Both realize a single underlying object: the **motivic aether**, a Grothendieck-ring datum equipped with a tower of realization functors.

**Definition (motivic aether, axiom).**
The **motivic aether** of the QOU framework is the triple
$$
  \mathcal{S}_{\mathrm{mot}}
  \;:=\;
  \bigl(K_0(\mathrm{Var}_k),\; \mathbb{L},\; \{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}\bigr),
$$
consisting of:
1. the **Grothendieck ring of varieties** $K_0(\mathrm{Var}_k)$ over the base field $k$. It is the free abelian group on isomorphism classes $[X]$ of $k$-varieties modulo the scissor relations $[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with product $[X] \cdot [Y] = [X \times_k Y]$.
2. the **Lefschetz motive** $\mathbb{L} := [\mathbb{A}^1_k] \in K_0(\mathrm{Var}_k)$, with the localized ring $\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ and its dimension-completion $\widehat{\mathcal{M}}$ ([motivic mass measure](#def:motivic-mass-measure)).
3. a **realization tower** $\{\rho_v \colon \widehat{\mathcal{M}} \to \widehat{\mathcal{M}}_v\}$, with one realization functor assigned per place $v$ of $\mathbb{Q}$ ([adelic aether](#def:adelic-substrate)). The archimedean realization $\rho_\infty$ is the [archimedean realization functor](#def:archimedean-realization-functor), landing in $\mathbb{R}$. The non-archimedean realizations $\rho_p$ at a finite prime $p$ produce local cyclotomic data compatible with the Habiro-ring framework ([Habiro completion](#prop:full-pole-structure-mass-trace)).

The motivic aether is taken axiomatically: the ring $K_0(\mathrm{Var}_k)$, the Lefschetz class $\mathbb{L}$, the localization $\widehat{\mathcal{M}}$, and the realization functors are posited as given data, and every downstream construction is stated conditionally on this aether.
