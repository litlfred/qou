The QOU framework's algebraic substrate appears through two faces: the [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) and the [adelic substrate](#def:adelic-substrate). Both realize a single underlying object: the **motivic substrate**, a Grothendieck-ring datum equipped with a tower of realization functors.

**Definition (motivic substrate, axiom).**
The **motivic substrate** of the QOU framework is the triple
$$
  \mathcal{S}_{\mathrm{mot}}
  \;:=\;
  \bigl(K_0(\mathrm{Var}_k),\; \mathbb{L},\; \{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}\bigr),
$$
consisting of:
1. the **Grothendieck ring of varieties** $K_0(\mathrm{Var}_k)$ over the base field $k$. It is the free abelian group on isomorphism classes $[X]$ of $k$-varieties modulo the scissor relations $[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with product $[X] \cdot [Y] = [X \times_k Y]$.
2. the **Lefschetz motive** $\mathbb{L} := [\mathbb{A}^1_k] \in K_0(\mathrm{Var}_k)$, with the localized ring $\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ and its dimension-completion $\widehat{\mathcal{M}}$.
3. a **realization tower** $\{\rho_v \colon \widehat{\mathcal{M}} \to \widehat{\mathcal{M}}_v\}$. One assigns one realization functor per place $v$ of $\mathbb{Q}$. The non-archimedean realizations $\rho_p$ at a finite prime $p$ produce local cyclotomic data compatible with the Habiro-ring framework.

The motivic substrate is taken axiomatically: the ring $K_0(\mathrm{Var}_k)$, the Lefschetz class $\mathbb{L}$, the localization $\widehat{\mathcal{M}}$, and the realization functors are posited as given data, and every downstream construction is stated conditionally on this substrate.
