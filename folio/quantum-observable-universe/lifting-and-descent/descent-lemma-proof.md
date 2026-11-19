The proof mirrors the ascent
([jet prolongation](#prop:jet-prolongation)) in reverse, working inside $\mathbf{C}$.

*Step 1: Frobenius restriction.*
The jet object $J^1(A) = A \otimes \Omega^1(A)$ at level $n$ contains $A$
as a direct summand via the unit section
$\eta \otimes \mathrm{id}\colon \Omega^1(A) \hookrightarrow A \otimes \Omega^1(A)$.
Composing with the counit $\varepsilon\colon A \to \mathbf{1}$ on the
first tensor factor gives the restriction map $r_n\colon J^1(A) \to A$.
Because $A$ is Frobenius, $r_n$ is a coalgebra morphism --- $\Delta$
commutes with restriction by the Frobenius relation, and the counit
restricts by construction --- so the restricted object inherits a
Frobenius--Hopf structure.

*Step 2: Connection restriction.*
The connection $A_n$ on $\mathcal{S}_n$ is determined by the comultiplication
$\Delta'$ on $J^1(A)$ (jet prolongation, Step 2).  Restricting $\Delta'$
along $r_n$ recovers the original $\Delta$ on $A$, which corresponds to
the connection $A_{n-1}$ on $\mathcal{S}_{n-1}$.  Hence $A_{n-1}$ satisfies the
Hermitian Yang--Mills equations on $\mathcal{S}_{n-1}$ as it did at level $n{-}1$.

*Step 3: Non-degeneracy and vanishing.*
Non-degeneracy of the Frobenius form on the restricted object follows
from the direct-summand inclusion $A \hookrightarrow J^1(A)$.  The
vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is
unchanged since $A$ is recovered.

*Step 4: The :refterm[descent]{#descent} homomorphism.*
Applying $\tau$ to $r_n$ yields
$\mathfrak{d}_n\colon \Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2)) \to \Gamma(J^1 \mathcal{S}_{n-1}, \mathrm{SU}_{q_{n-1}}(2))$,
a $*$-homomorphism because $r_n$ preserves multiplication and antipode.
Surjectivity follows from the injectivity of the ascent map $\ell_n$
(it embeds $A$ into $J^1(A)$ as a direct summand), so its categorical
adjoint $r_n$ is surjective.

*Step 5: Equivariance.*
The $\mathrm{SU}(2)$-action on sections at level $n$ is the adjoint
representation of the Hopf algebra; since $r_n$ is a Hopf algebra
morphism, it intertwines the adjoint actions at levels $n$ and $n{-}1$.
$\square$
