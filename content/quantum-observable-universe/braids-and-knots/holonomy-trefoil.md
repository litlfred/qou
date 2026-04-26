Given a branched cover $\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$ with singular fibres
at the critical values, choose two loops
$\gamma_1,\gamma_2$ in $\mathbb{P}^1(\mathbb{C})$ encircling distinct branch
points.  Parallel-transporting the spectral modes $w_k$ around these
loops yields holonomy operators

```tex
\begin{equation}\label{eq:holonomy-generators}
  H_1=\sigma_1,\qquad H_2=\sigma_2,
\end{equation}
```

where $\sigma_1,\sigma_2$ are the braid generators.
In the $\mathrm{SU}(2)$ embedding ([SU(2) generators](#def:su2-generators)) these
become

$$
  H_1=\exp(T\varTheta e_1),\qquad H_2=\exp(T\varTheta e_2),
$$

with $T$ the geometric torsion scalar and $\varTheta$ a branch angle, so
the holonomy group is a representation of $B_3$ inside
$\mathrm{SU}(2)$.

The fundamental group of the trefoil-knot complement admits the
presentation $\langle x,y\mid xyx=yxy\rangle$, which is exactly
$B_3$.  The assignment
$x\mapsto H_1$, $y\mapsto H_2$ is therefore an isomorphism
$\pi_1(S^3\setminus K_{3,2})\xrightarrow{ \sim } \langle H_1,H_2\rangle$: the monodromy group of the branched cover
*is* the trefoil-knot group.

The composite holonomy
$H_1 H_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$ is the
$3$-cycle $\alpha$ and satisfies
$(H_1 H_2)^3=\mathrm{id}$ on $\mathrm{SO}(3)$.
