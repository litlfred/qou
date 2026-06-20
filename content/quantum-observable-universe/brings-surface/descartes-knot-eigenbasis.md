*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a Descartes universe
([Descartes condition](#def:archimedean-condition)) with
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental
representation.  Then the knot-type eigenbasis is complete:

1. **(Iwahori--Hecke algebra instantiation.)**  The Descartes condition forces
   $\chi(A) = -6$, giving genus $g = 4$ and gauge group
   $\mathrm{SU}_q(2)$ of rank $2$.  The $R$-matrix of
   $\mathcal{U}_q(\mathfrak{su}(2))$
   ([$R$-matrix braiding](#rem:r-matrix-braiding)) furnishes a braiding
   $c_{V,V}$ on $\mathbf{C}$ whose eigenvalues are $q$ and $-q^{-1}$.
   The quotient by the quadratic relation
   $(c_{V,V} - q)(c_{V,V} + q^{-1}) = 0$ yields the Iwahori--Hecke algebra
   $H_n(q)$ acting on $V^{\otimes n}$.

2. **(Schur--Weyl decomposition.)**  Since the Descartes condition
   requires $q$ not a root of unity (via $6 \in R^{\times}$ and the
   non-degeneracy of the Frobenius form), $H_n(q)$ is semisimple
   (Jimbo's theorem), and the $q$-Schur--Weyl decomposition
   ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(1))
   applies: every $V^{\otimes n}$ decomposes into irreducible summands
   labelled by two-part partitions $\lambda \vdash n$.

3. **(Braid representation.)**  The faithful representation
   $\rho_3 \colon B_3 \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes 3})$
   ([braid-group structure](#cor:descartes-braid-structure)(1))
   extends to $\rho_n \colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$
   for all $n$ via
   [braid action on tensor products](#prop:braid-action-tensor).
   The Markov trace on the Iwahori--Hecke algebra tower detects every irreducible
   summand (Jones, 1987).

4. **(Completeness.)**  By the combining theorem
   ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)),
   the three inputs --- Schur--Weyl decomposition, Alexander
   surjectivity, and Markov trace detection --- yield a complete
   knot-type eigenbasis for the algebraic direct limit
   $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$.
   The Feynman path integral is replaced by a finite categorical trace
   over knot-labelled summands.
