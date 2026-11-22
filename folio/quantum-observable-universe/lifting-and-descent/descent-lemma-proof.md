The proof mirrors the ascent
([jet prolongation](#prop:jet-prolongation)) in reverse, working inside $\mathbf{C}$.

*Step 1: Hopf restriction.*
Assume $A$ is commutative, as in the [jet prolongation](#prop:jet-prolongation). The level object $T(A) = \mathrm{Sym}_A(\Omega^1_{A/R})$
([jet prolongation](#prop:jet-prolongation)) contains $A$ as a direct summand:
the structure map $\ell_n\colon A \to T(A)$ and the restriction map
$r_n\colon T(A) \to A$, which kills $\Omega^1_{A/R}$, satisfy
$r_n \circ \ell_n = \mathrm{id}$.
For $A = \mathcal{O}(G)$, $T(A) = \mathcal{O}(TG)$ and $r_n$ is the Hopf map given by pull-back
along the zero section $G \to TG$, so restriction along $r_n$ returns $A$ with its own
Hopf structure. For noncommutative $A$ the ideal $I^2$ is not available. The
two-sided jet $A \ltimes \Omega^1_u(A)$ still splits over $A$, but a Hopf structure on it is not
established in general.

*Step 2: Connection restriction.*
The connection $A_n$ on $\mathcal{S}_n$ is determined by the comultiplication
$\Delta'$ on $T(A)$ ([jet prolongation](#prop:jet-prolongation)).  Restricting $\Delta'$
along $r_n$ recovers the original $\Delta$ on $A$, which corresponds to
the connection $A_{n-1}$ on $\mathcal{S}_{n-1}$.  Hence $A_{n-1}$ satisfies the
Hermitian Yang--Mills equations on $\mathcal{S}_{n-1}$ as it did at level $n{-}1$.

*Step 3: The base level.*
At $n = 1$ the restricted object is $A_0 = A$ itself, so its Frobenius form and the
vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ are those of the
original quantum observable universe. At $n \ge 2$ the object $A_{n-1}$ carries no
required Frobenius form, and nothing further is claimed.

*Step 4: The :refterm[descent]{#descent} homomorphism.*
Since $r_n \circ \ell_n = \mathrm{id}$, the map $e_n = \ell_n \circ r_n$ is an idempotent on $A_n$. For any $\psi \in \mathrm{End}_{\mathbf{C}}(A_{n-1})$ one has
$\mathfrak{d}_n(\ell_n \circ \psi \circ r_n) = \psi$, so $\mathfrak{d}_n$ is surjective, and $\ell_n \circ \psi \circ r_n$ commutes with $e_n$.
If $\varphi$ and $\varphi'$ commute with $e_n$, then
$\mathfrak{d}_n(\varphi \circ \varphi') = r_n \circ \varphi \circ \varphi' \circ \ell_n = r_n \circ \varphi \circ e_n \circ \varphi' \circ \ell_n = \mathfrak{d}_n(\varphi) \circ \mathfrak{d}_n(\varphi')$,
where the middle step uses $\varphi' \circ \ell_n = \varphi' \circ e_n \circ \ell_n = e_n \circ \varphi' \circ \ell_n$. Also $\mathfrak{d}_n(\mathrm{id}) = \mathrm{id}$. Hence $\mathfrak{d}_n$ restricted to $\mathrm{End}_{\mathbf{C}}(A_n)^{e_n}$ is a surjective algebra homomorphism.
Without the commutation hypothesis, multiplicativity fails: for $A_n = \mathbf{1}^{\oplus 2}$, $A_{n-1} = \mathbf{1}$ with $\ell_n$ and $r_n$ the first inclusion and projection, the off-diagonal matrix units $E_{12}$ and $E_{21}$ satisfy $\mathfrak{d}_n(E_{12} E_{21}) = 1$ while $\mathfrak{d}_n(E_{12})\,\mathfrak{d}_n(E_{21}) = 0$.
In the archimedean realisation $r_n = \ell_n^{\dagger}$ with $\ell_n^{\dagger}\ell_n = \mathrm{id}$. Then $\mathfrak{d}_n(\varphi)^{\dagger} = \ell_n^{\dagger}\varphi^{\dagger}\ell_n = \mathfrak{d}_n(\varphi^{\dagger})$, and $e_n = \ell_n\ell_n^{\dagger}$ is self-adjoint, so the commutant of $e_n$ is closed under $\dagger$. The argument above therefore makes $\mathfrak{d}_n$ a surjective $*$-homomorphism on that commutant.

*Step 5: Equivariance.*
The $\mathrm{SU}(2)$-action on sections at level $n$ is the adjoint
representation of the Hopf algebra; since $r_n$ is a Hopf algebra
morphism, $r_n(h_{(1)}\, a\, S(h_{(2)})) = r_n(h)_{(1)}\, r_n(a)\, S(r_n(h)_{(2)})$, using $(r_n \otimes r_n)\Delta = \Delta r_n$ and $r_n S = S r_n$. With $\rho_n(x) = \mathrm{ad}_{\ell_n x}$ and $\rho_{n-1}(x) = \mathrm{ad}_x$ for $x \in A_{n-1}$, and $r_n \ell_n = \mathrm{id}$, this gives $r_n \circ \rho_n(x) = \rho_{n-1}(x) \circ r_n$; the same computation for the Hopf morphism $\ell_n$ gives $\rho_n(x) \circ \ell_n = \ell_n \circ \rho_{n-1}(x)$. For any $a, b$,
$\mathfrak{d}_n(\rho_n(a) \circ \varphi \circ \rho_n(b)) = r_n \circ \rho_n(a) \circ \varphi \circ \rho_n(b) \circ \ell_n = \rho_{n-1}(a) \circ \mathfrak{d}_n(\varphi) \circ \rho_{n-1}(b)$.
The adjoint action $\varphi \mapsto \sum \rho_n(h_{(1)}) \circ \varphi \circ \rho_n(S h_{(2)})$ is a finite sum of such terms, so $\mathfrak{d}_n$ intertwines the adjoint actions at levels $n$ and $n{-}1$. Each $\rho_n(h)$ commutes with $e_n$, so the action preserves the block-diagonal subalgebra.
$\square$
