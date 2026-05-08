The proof proceeds in the rigid monoidal category underlying the quantum
observable universe.  Let $A$ denote the Frobenius--Hopf object
representing the gauge-bundle data of $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

By
([categorical jet object inherits Frobenius--Hopf structure](#lem:jet-prolongation-categorical-jet)),
$J^1(A) := A \otimes \Omega^1(A)$ is an object of the ambient category
and inherits the Frobenius--Hopf data $(\Delta', \varepsilon', S')$
from $A$.

*Non-degeneracy and vanishing.*
The non-degeneracy of the Frobenius form on $A$ (the pairing
$\varepsilon \circ m$ is a perfect pairing) implies non-degeneracy of the
induced form on $J^1(A)$, since $\Omega^1(A)$ is a direct summand.
For the vanishing condition, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
implies $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(J^1(A))) = 0$: the adjoint
representation of $J^1(A)$ contains $\mathrm{Ad}(A)$ as a subobject, and any
invariant in $\mathrm{Ad}(J^1(A))$ would project to a non-zero invariant in
$\mathrm{Ad}(A)$, contradicting the hypothesis.

*Geometric realisation.*
Applying the fibre functor $\tau\colon \mathbf{C} \to \mathrm{Vect}_k$
recovers the geometric data: $\tau(J^1(A))$ is the space of sections of the
first jet bundle $J^1 \mathcal{S}$, the frame bundle $P'$ and orthonormal frame
bundle $\mathcal{S}'$ are the geometric counterparts of the Frobenius--Hopf
structure on $J^1(A)$, and the connection $A'$ is the image under $\tau$
of the comultiplication $\Delta'$.  Its uniqueness follows from the
irreducibility of $A'$, which is guaranteed by the inherited vanishing
condition.  $\square$
