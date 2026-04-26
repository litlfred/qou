
The proof proceeds in the rigid monoidal category underlying the quantum
observable universe.  Let $A$ denote the Frobenius--Hopf object
representing the gauge-bundle data of $(\mathbf{C}, \varTheta, G, \mathcal{S})$.

*Step 1: Categorical jet object.*
The first jet bundle $J^1 \mathcal{S}$ is represented categorically by the object
$A \otimes \Omega^1(A)$, where
$\Omega^1(A) = \ker(m\colon A\otimes A \to A)$
is the kernel of the multiplication (the bimodule of Kähler
differentials, i.e. the universal first-order differential calculus
over $A$).
Because $A$ is Frobenius, the non-degenerate pairing
$\varepsilon \circ m \colon A \otimes A \to \mathbf{1}$ exhibits
$\Omega^1(A)$ as a direct summand of $A \otimes A$, hence
$J^1(A) := A \otimes \Omega^1(A)$ is again an object of the ambient
category.

*Step 2: Inherited Frobenius--Hopf structure.*
The Frobenius relation
$(\mathrm{Id} \otimes m) \circ (\Delta \otimes \mathrm{Id}) = \Delta \circ m = (m \otimes \mathrm{Id}) \circ (\mathrm{Id} \otimes \Delta)$
ensures that the comultiplication $\Delta\colon A \to A \otimes A$ restricts
to a well-defined comultiplication
$\Delta'\colon J^1(A) \to J^1(A) \otimes J^1(A)$, and the counit
$\varepsilon\colon A \to \mathbf{1}$ induces a counit $\varepsilon'$ on
$J^1(A)$.  The Hopf antipode $S$ extends to $J^1(A)$ by functoriality of the
Kähler differential construction.  Thus $J^1(A)$ is a Frobenius--Hopf object.

This step relies on the *strong multiplicativity* condition: the
co-multiplication must be compatible with the deformed product at every
filtration degree.  Over fields of positive characteristic, the
rigorous proof that this compatibility survives the deformation is the
main theorem of [fred2005], which constructs $\mathrm{Dist}(G)$
as a Gröbner--Shirshov deformation of the commutative
$\mathrm{Dist}(H)$ and verifies the Frobenius relation at each stage
(see also [skew poisson integration](#prop:skew-poisson-integration) in
[Chapter](#chap:descartes-universe)).

*Step 3: Non-degeneracy and vanishing.*
The non-degeneracy of the Frobenius form on $A$ (the pairing
$\varepsilon \circ m$ is a perfect pairing) implies non-degeneracy of the
induced form on $J^1(A)$, since $\Omega^1(A)$ is a direct summand.
For the vanishing condition, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
implies $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(J^1(A))) = 0$: the adjoint
representation of $J^1(A)$ contains $\mathrm{Ad}(A)$ as a subobject, and any
invariant in $\mathrm{Ad}(J^1(A))$ would project to a non-zero invariant in
$\mathrm{Ad}(A)$, contradicting the hypothesis.

*Step 4: Geometric realisation.*
Applying the fibre functor $\tau\colon \mathbf{C} \to \mathrm{Vect}_k$
(where $\mathbf{C}$ is the rigid monoidal category of the quantum
observable universe)
recovers the geometric data: $\tau(J^1(A))$ is the space of sections of the
first jet bundle $J^1 \mathcal{S}$, the frame bundle $P'$ and orthonormal frame bundle
$\mathcal{S}'$ are the geometric counterparts of the Frobenius--Hopf structure on
$J^1(A)$, and the connection $A'$ is the image under $\tau$ of the
comultiplication $\Delta'$.  Its uniqueness follows from the irreducibility
of $A'$, which is guaranteed by the inherited vanishing condition of
Step 3.
