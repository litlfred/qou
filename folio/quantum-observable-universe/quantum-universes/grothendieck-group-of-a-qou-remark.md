The group $K_0(\mathbf{C})$ is the *split* Grothendieck group, the one appropriate to an additive category with no exact structure imposed; when $\mathbf{C}$ is semisimple every short exact sequence splits and the two notions agree.

**The block presentation.** Axiom 4 of a quantum universe, Wedderburn semisimplicity, provides a finite set $\widehat{A}$ of blocks and a simple object $V_\lambda$ for each block $\lambda$, such that every object is a finite direct sum of the $V_\lambda$ ([simple objects](#rem:simple-objects-V)). Hence

$$
  K_0(\mathbf{C}) \;=\; \bigoplus_{\lambda \in \widehat{A}} \mathbb{Z}\,[V_\lambda] \;\cong\; \mathbb{Z}^{\widehat{A}},
$$

a free abelian group on the blocks. Two homomorphisms out of it are used in the paper. The *rank* $K_0(\mathbf{C}) \to \mathbb{Z}$ sends $[V_\lambda]$ to $1$, so it counts simple constituents. The *quantum dimension* of a [rigid monoidal category](#def:rigid-monoidal-category), $\dim_q(X) = \mathrm{tr}(\mathrm{id}_X) \in \operatorname{End}(\mathbf{1}) = R$, is additive under direct sums, so it extends to a homomorphism

$$
  \dim_q \colon K_0(\mathbf{C}) \longrightarrow R, \qquad \sum_\lambda n_\lambda [V_\lambda] \longmapsto \sum_\lambda n_\lambda \dim_q(V_\lambda).
$$

**The ring structure.** The tensor product of $\mathbf{C}$ descends to $K_0(\mathbf{C})$, $[X]\cdot[Y] = [X \otimes Y]$, because $\otimes$ distributes over $\oplus$; with it $K_0(\mathbf{C})$ is a commutative ring when $\mathbf{C}$ is braided, the *fusion ring* of $\mathbf{C}$, with unit $[\mathbf{1}]$. The quantum dimension is a ring homomorphism, since $\dim_q(X \otimes Y) = \dim_q(X)\dim_q(Y)$ in a rigid braided category \cite{kassel1995}.
