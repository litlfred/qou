*On the $2$-dimensional $(2,1)$ Hoefsmit block of $H_3(q)$, the uniform
three-strand rotation $M = \rho_{(2,1)}(\sigma_1\sigma_2)$ has*

$$
\mathrm{tr}\,M = -1, \qquad \det M = 1, \qquad M^3 = \mathrm{Id},
$$

*for every $q$ with $1 - q^4$ invertible. The eigenvalues of $M$ are the
primitive cube roots of unity, independently of $q$.*

The proof is Cayley–Hamilton: trace $-1$ and determinant $1$ give the
$\zeta_3$ quadratic $M^2 = -M - 1$, hence $M^3 = \mathrm{Id}$. The trace
identity is a Laurent identity in $q$ alone; the determinant
identity is exactly the Hoefsmit constraint
$\beta^2 = a_2 a_{-2} + 1$ on the binding amplitude
([prop:hoefsmit-binding-amplitude](hoefsmit-binding-amplitude.md)). Both
hold over a generic commutative ring with $q$ a unit
and with both $\beta$ and the axial entry $a_{-2}$ carried as constrained
variables — $\beta^2 = a_{-2} a_2 + 1$ and $a_{-2} (1 - q^4) = q - q^{-1}$ — so
neither the square root nor the axial-distance quotient appears (no
division, no $\mathbb{R}$), and the cube identity follows from the two
scalar facts. The hypothesis $1 - q^4$ invertible is what makes the
axial entry $a_{-2} = (q - q^{-1})/(1 - q^4)$ of the Hoefsmit block defined.
With $a_{-2}$ carried as a constrained variable, the argument needs
only $1 - q^2$ invertible and only for the trace; the statement's
hypothesis implies it. At $q^2 = 1$ the defining relation for $a_{-2}$
degenerates and constrains nothing. The determinant identity needs no
hypothesis at all.

Since the closures of $(\sigma_1\sigma_2)^k$ are the $(3,k)$ torus links,
the proposition says the compact winding of the three-strand torus-link
tower is **topological**: a $\zeta_3$ (color/triality) rotation that does
not flow with the substrate modulus, in contrast to the modulus-carrying
hyperbolic winding pair $q^{\pm 2k}$ of the $1$-dimensional channels. The
level-lattice and vortex readings — winding pair $(k,\ k \bmod 3)$ for the
three-strand (Borromean/nucleon) carrier, and the alternating-word
deformation of the same rotation — are developed in the channel-
interpolation cross-check and its witnesses
(`toroidal-level-selection-three-strand-probe`,
`alternating-tower-borromean-winding-probe`).
