Continuing [quantum universe on SU(2)](#ex:quantum-universe-su2), the left-invariant
calculus on $A = \mathcal{O}(\mathrm{SU}(2))$ has
$\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$
(three left-invariant $1$-forms, dual to the Lie algebra
$\mathfrak{su}(2) = \mathrm{span}\{e_1, e_2, e_3\}$). This example
realizes [def:higher-forms](#def:higher-forms) concretely: because the
group is three-dimensional, the exterior tower is finite and truncates
at the top degree $k = 3$. Ascending through it degree by degree, the
higher forms are:

- $\Omega^0(A) = A = \mathcal{O}(\mathrm{SU}(2))$ (functions on the group).
- $\Omega^1(A) = A \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$
  (left-invariant $1$-forms, dimension $3$ over $A$).
- $\Omega^2(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2, \omega_1 \wedge \omega_3, \omega_2 \wedge \omega_3\}$
  (dimension $3$ over $A$).
- $\Omega^3(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2 \wedge \omega_3\}$ (the volume form, dimension $1$ over $A$).
- $\Omega^k(A) = 0$ for $k \geq 4$.

The top degree $\Omega^3(A)$ carries the single invariant volume form,
and the differential $d$ closes the tower: it is determined by
$d\omega_i = -\tfrac{1}{2} \epsilon_{ijk}\omega_j \wedge \omega_k$ (the
Maurer--Cartan equation of $\mathfrak{su}(2)$).
