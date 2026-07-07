**Proposition (rigidity of the three-strand color winding).**
*On the $2$-dimensional $(2,1)$ Hoefsmit block of $H_3(q)$, the uniform
three-strand rotation $M = \rho_{(2,1)}(\sigma_1\sigma_2)$ has*

$$
\mathrm{tr}\,M = -1, \qquad \det M = 1, \qquad M^3 = \mathrm{Id},
$$

*for every $q$ with $q^4 \neq 1$. The eigenvalues of $M$ are the primitive
cube roots of unity, independently of $q$.*

The proof is Cayley–Hamilton: trace $-1$ and determinant $1$ give the
$\zeta_3$ quadratic $M^2 = -M - 1$, hence $M^3 = \mathrm{Id}$. The trace
identity is a rational-function identity in $q$ alone; the determinant
identity is exactly the Hoefsmit constraint
$\beta^2 = a_2 a_{-2} + 1$ on the binding amplitude
([prop:hoefsmit-binding-amplitude](hoefsmit-binding-amplitude.md)). The
Lean sibling states both over a generic field with $\beta$ carried as a
constrained variable (no square root, no $\mathbb{R}$), and derives the
cube identity from the two scalar facts.

Since the closures of $(\sigma_1\sigma_2)^k$ are the $(3,k)$ torus links,
the proposition says the compact winding of the three-strand torus-link
tower is **topological**: a $\zeta_3$ (color/triality) rotation that does
not flow with the substrate modulus, in contrast to the modulus-carrying
hyperbolic winding pair $q^{\pm 2k}$ of the $1$-dimensional channels. The
level-lattice and vortex readings — winding pair $(k,\ k \bmod 3)$ for the
three-strand (Borromean/nucleon) carrier, and the alternating-word
deformation of the same rotation — are developed in the channel-
interpolation audit and its witnesses
(`toroidal-level-selection-three-strand-probe`,
`alternating-tower-borromean-winding-probe`).
