The proof proceeds in the rigid :refterm[monoidal category]{#monoidal-category} underlying the quantum
observable universe.  Let $A$ denote the Frobenius--Hopf object
representing the gauge-bundle data of $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

The tangent algebra $T(A) := \mathrm{Sym}_A(\Omega^1_{A/R})$ is an object of the
ambient category, and for $A = \mathcal{O}(G)$ it is the coordinate Hopf algebra of
the tangent group $TG$, with Hopf data $(\Delta', \varepsilon', S')$ for which the
structure map $A \to T(A)$ and the augmentation $T(A) \to A$ are Hopf maps.

*Non-degeneracy and vanishing.*
The non-degeneracy of the Frobenius form on $A$ (the pairing
$\varepsilon \circ m$ is a perfect pairing) implies non-degeneracy of the
induced form on $T(A)$, since $A$ is a direct summand of $T(A)$.
For the vanishing condition, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
implies $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(T(A))) = 0$: the adjoint
representation of $T(A)$ contains $\mathrm{Ad}(A)$ as a subobject, and any
invariant in $\mathrm{Ad}(T(A))$ would project to a non-zero invariant in
$\mathrm{Ad}(A)$, contradicting the hypothesis.

*Geometric realisation.*
Applying the fibre functor $\tau\colon \mathbf{C} \to \mathrm{Vect}_k$
recovers the geometric data: $\tau(T(A))$ is the space of sections of the
tangent bundle $T\mathcal{S}$, the frame bundle $P'$ and orthonormal frame
bundle $\mathcal{S}'$ are the geometric counterparts of the Frobenius--Hopf
structure on $T(A)$, and the connection $A'$ is the image under $\tau$
of the comultiplication $\Delta'$.  Its uniqueness follows from the
irreducibility of $A'$, which is guaranteed by the inherited vanishing
condition.  $\square$
