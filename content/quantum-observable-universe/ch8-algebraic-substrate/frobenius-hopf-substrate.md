Let $\mathbf{C}$ be a rigid monoidal category. A *Frobenius--Hopf
substrate* is a sextuple $(A, \mu, \eta, \Delta, \varepsilon, S)$ in
$\mathbf{C}$ equipped with a Frobenius form
$\lambda \colon A \to \mathbf{1}$ satisfying the following axioms.

**Algebra structure.** The morphisms $\mu \colon A \otimes A \to A$
(multiplication) and $\eta \colon \mathbf{1} \to A$ (unit) make $A$
into an associative unital algebra object in $\mathbf{C}$.

**Coalgebra structure.** The morphisms
$\Delta \colon A \to A \otimes A$ (comultiplication) and
$\varepsilon \colon A \to \mathbf{1}$ (counit) make $A$ into a
coassociative counital coalgebra object, with antipode
$S \colon A \to A$ satisfying the Hopf compatibility:

$$
\varepsilon \circ \mu = \varepsilon \otimes \varepsilon
$$

as a coalgebra map.

**Frobenius relation.** The Frobenius form $\lambda$ satisfies:

$$
\mu \circ \Delta
= (\Delta \otimes \mathrm{id}) \circ \alpha \circ (\mathrm{id} \otimes \mu)
$$

where $\alpha$ is the associator in $\mathbf{C}$.

**Non-degeneracy.** The Frobenius pairing
$\langle a, b \rangle_F = \lambda(\mu(a \otimes b))$ is non-degenerate:
the induced map $A \to A^\vee$ is an isomorphism, equivalently the
snake identities hold with respect to a coevaluation
$\tilde{\eta} \colon \mathbf{1} \to A \otimes A$.

**Self-duality.** The algebra $A$ is *self-dual as a substrate*: the
non-degenerate Frobenius pairing identifies $A$ with its dual $A^\vee$
canonically, so that the observer trace $\Phi = \lambda \circ \mu$ and
the observed state space are intrinsically paired.
