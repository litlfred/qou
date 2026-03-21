Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe and let
$\{A_n\}_{n \geq 0}$ be the recursive brane tower
([Definition](#def:recursive-brane-tower)), with $n \geq 1$; let $q$ denote the substrate parameter.  The
restriction morphism $r_n \colon A_n \to A_{n-1}$ yields a Frobenius--Hopf
object $A_{n-1}$ such that $(\mathcal{C}, A_{n-1}, \omega)$ is again a
quantum observable universe.  Moreover, the induced descent homomorphism
$$
  \mathfrak{d}_n \;\colon\;
  \mathrm{End}_{\mathcal{C}}(A_n)
  \;\longrightarrow\;
  \mathrm{End}_{\mathcal{C}}(A_{n-1})
$$
is a surjective algebra homomorphism that intertwines the $G_q$-actions at
levels $n$ and $n{-}1$.  In the archimedean realisation, this recovers
the surjective $*$-homomorphism
$\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2)) \to
\Gamma(J^1 E_{n-1},\, \mathrm{SU}_{q_{n-1}}(2))$.

---

The proof mirrors the ascent ([Proposition](#prop:jet-prolongation)) in
reverse, working inside the rigid monoidal category $\mathcal{C}$.

*Step 1: Frobenius restriction.*
The jet object $J^1(A) = A \otimes \Omega^1(A)$ at level $n$ contains $A$
as a direct summand via the unit section
$\eta \otimes \mathrm{id}\colon \Omega^1(A) \hookrightarrow A \otimes
\Omega^1(A)$.  Composing with the counit $\varepsilon\colon A \to \mathbf{1}$
on the first tensor factor gives the restriction map
$r_n\colon J^1(A) \to A$.  Because $A$ is Frobenius, $r_n$ is a coalgebra
morphism: the comultiplication $\Delta$ commutes with restriction by the
Frobenius relation, and the counit restricts by construction.  Hence the
restricted object inherits a Frobenius--Hopf structure.

*Step 2: Connection restriction.*
The connection $A_n$ on $E_n$ is determined by the comultiplication
$\Delta'$ on $J^1(A)$ ([Proposition](#prop:jet-prolongation), Step 2).
Restricting $\Delta'$ along $r_n$ recovers the original comultiplication
$\Delta$ on $A$, which by the construction of the brane tower corresponds to
the connection $A_{n-1}$ on $E_{n-1}$.  In particular, $A_{n-1}$ satisfies
the Hermitian Yang--Mills equations on $E_{n-1}$ because it did so at level
$n{-}1$ before the ascent.

*Step 3: Non-degeneracy and vanishing.*
Non-degeneracy of the Frobenius form on the restricted object follows from
the direct-summand inclusion $A \hookrightarrow J^1(A)$: the restriction of a
non-degenerate pairing to a direct summand remains non-degenerate.  The
vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is
unchanged since we recover the original object $A$.

*Step 4: The descent homomorphism.*
Applying the fibre functor $\omega$ to $r_n$ yields
$\mathfrak{d}_n\colon
\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2)) \to
\Gamma(J^1 E_{n-1},\, \mathrm{SU}_{q_{n-1}}(2))$.
This is a $*$-homomorphism because $r_n$ preserves multiplication and
the antipode.  Surjectivity follows from the fact that the ascent map
$\ell_n$ of [Proposition](#prop:jet-prolongation) is injective (it
embeds $A$ into $J^1(A)$ as a direct summand), so its categorical adjoint
$r_n$ is surjective.

*Step 5: Equivariance.*
The $\mathrm{SU}(2)$ action on sections at level $n$ is induced by the
adjoint representation of the Hopf algebra.  Since $r_n$ is a Hopf algebra
morphism, it intertwines the adjoint actions at levels $n$ and $n{-}1$.
