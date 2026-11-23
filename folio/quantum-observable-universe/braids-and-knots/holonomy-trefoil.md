Given a branched cover $\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$ with singular fibres at the critical values, choose two loops $\gamma_1,\gamma_2$ in $\mathbb{P}^1(\mathbb{C})$ encircling distinct branch points. Parallel-transporting the spectral modes $w_k$ around these loops yields the holonomy operators:
```tex
\begin{equation}\label{eq:holonomy-generators}
  H_1=\sigma_1,\qquad H_2=\sigma_2.
\end{equation}
```
In the $\mathrm{SU}(2)$ embedding, these become:
$$
  H_1=\exp(T\varTheta e_1),\qquad H_2=\exp(T\varTheta e_2),
$$
with $T$ the geometric torsion scalar and $\varTheta$ a branch angle. The holonomy group provides a representation of $B_3$ inside $\mathrm{SU}(2)$.

The fundamental group of the trefoil-knot complement has the presentation $\langle x,y\mid xyx=yxy\rangle \cong B_3$, so the braid monodromy of the cover and the trefoil-knot group are the same abstract group. Transporting the three colour sheets around the six branch points realises the identification: the six local monodromies lift to braids that generate all of $B_3$, so the monodromy group of the branched cover is exactly the trefoil-knot group.

The mapping $x\mapsto H_1$, $y\mapsto H_2$ into $\mathrm{SU}(2)$ is a different matter. It is a surjection $\pi_1(S^3\setminus K_{3,2})\twoheadrightarrow\langle H_1,H_2\rangle$ and not an isomorphism: the relation $(H_1H_2)^3=\mathrm{id}$ recorded below fails in $B_3$, where $(\sigma_1\sigma_2)^3$ is the full twist and generates the infinite cyclic centre. The matrix group is therefore a proper quotient of the trefoil-knot group by a subgroup of that centre, and carries less information than the braid monodromy does.

The composite holonomy $H_1 H_2$ acts as a $3$-cycle in the symmetric-group holonomy $S_3$ — the order-$3$ generator built in [the $\mathrm{SU}(2)$ generators](#def:su2-generators) — and satisfies $(H_1 H_2)^3=\mathrm{id}$ on $\mathrm{SO}(3)$.
