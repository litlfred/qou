
By the construction of the recursive brane tower
([Definition](#def:recursive-brane-tower)), $E_{n+1}$ is the bundle of
orthonormal frames of the first jet bundle $J^1 E_n$
([Proposition](#prop:jet-prolongation)).  The Euler characteristic of a
fibre bundle $F \hookrightarrow E_{n+1} \to E_n$ satisfies the
multiplicativity formula
$$
  \chi(E_{n+1}) \;=\; \chi(E_n) \cdot \chi(F),
$$
provided the fibre $F$ has the homotopy type of a finite CW-complex and the
base acts trivially on $H^*(F;\, \mathbb{Q})$.  In the brane tower the fibre
is $\mathrm{SU}(2) \cong S^3$, which has $\chi(S^3) = 0$ for the odd-dimensional
sphere.  However, the relevant bundle is not $\mathrm{SU}(2)$ itself but the
*projectivised* frame bundle, whose typical fibre is
$\mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ with
$\chi(S^2) = 2$.  Nonetheless, the Euler characteristic is preserved for the
following reason.

The Leray--Serre spectral sequence of
$S^2 \hookrightarrow E_{n+1} \to E_n$ has $E_2^{p,q} = H^p(E_n;\,
H^q(S^2;\, \mathbb{Z}))$.  The quantum characteristic classes $\kappa_n$
([Definition](#def:quantum-characteristic-classes)) are precisely the
obstructions to trivial monodromy of the fibre cohomology $H^*(S^2)$.  By
the vanishing condition of the quantum observable universe axioms---which
forces $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$---the monodromy
representation of $\pi_1(E_n)$ on $H^*(S^2;\, \mathbb{Z})$ is trivial (the
adjoint bundle has no invariant sections to twist the fibre cohomology).
Consequently the spectral sequence collapses at the $E_2$ page.  The
preservation of the Euler characteristic follows from the following
observation.  The base manifold $M_0$ is invariant under jet prolongation:
each level of the brane tower changes the bundle data but not the base
geometry.  Hence $\chi(M_0)$ is preserved at every level.
