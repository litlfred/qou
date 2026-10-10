*Proof.*
(1) **Extension.**  At level $n$, the Hecke basis of $A_n$
is a monomial basis $B_n$ in the generators
$\sigma_1^{(n)}, \ldots, \sigma_{d_n - 1}^{(n)}$.  The jet
prolongation $A_{n+1} = A_n \otimes \Omega^1(A_n)$ introduces
$\dim(\Omega^1) = 3$ new directions (in the $\mathrm{SU}(2)$
case: $\omega_1, \omega_2, \omega_3$).  Define $\prec_{n+1}$
by degree-lexicographic extension: monomials in $B_n$ keep
their relative order; new generators $\omega_i$ are ordered
after all level-$n$ generators.  This preserves the ordering
on the image of $\ell_n$ and well-orders the new monomials.

(2) **Compatibility.**  The Frobenius–Hopf structure on
$A_{n+1}$ is inherited from $A_n$ by jet prolongation
([jet prolongation](#prop:jet-prolongation)).  The
comultiplication $\Delta_{n+1}$ and multiplication
$\mu_{n+1}$ satisfy the same Hecke relation
$T^2 = (q - q^{-1})T + 1$ at level $n+1$.
Degree-lexicographic orderings are compatible with any
associative multiplication whose defining relations have
leading terms of bounded degree — the Hecke relation is
quadratic, so this holds.

(3) **Well-foundedness.**  The degree-lexicographic ordering
on $B_{n+1}$ is well-ordered because: (a) total degree is
bounded below by $0$; (b) at fixed degree, lexicographic
ordering on a finite alphabet is well-ordered.  The
finiteness of the alphabet at each level is guaranteed by
the Frobenius–Hopf axioms (the algebra is finitely generated
at each level).

(4) **Direct limit.**  For any $a \in \mathcal{A}_\infty$,
there exists $n$ such that $a \in \mathrm{End}(A_n)$.  The
leading monomial $\mathrm{LM}(a)$ is computed in $B_n$ with
respect to $\prec_n$.  By (1), $\mathrm{LM}(a)$ is the same
whether computed in $B_n$ or in $B_m$ for any $m \geq n$ —
the embedding $\ell_n$ preserves leading monomials.  The
Gröbner--Shirshov reduction algorithm applied to $a$ in $A_n$
terminates by (3); the same reduction is valid in
$\mathcal{A}_\infty$.  $\square$

**Consequence for time.**  The braiding-induced ordering $\prec_c$ on
$A_0$ propagates through the entire jet tower.  At every
brane level, "forward time" (Gröbner--Shirshov reduction, braiding)
and "backward time" (anti-involution, unbraiding) are
well-defined and compatible with the algebraic structure.
The arrow of time is inherited from the initial ordering;
it does not need to be re-imposed at each level.
