## Thurston relaxation: SDP as a hyperbolic Newton solver

Once the two vortex cores merge inside a tubular neighbourhood $U \subset M$, the operative geometry is the complement $U \setminus K$. Thurston's hyperbolisation programme proves that, excluding a finite list of exceptions, $U \setminus K$ admits a complete finite-volume hyperbolic structure. A triangulation into ideal tetrahedra $\Delta_{z_k}$ and a system of *gluing equations* in the shape parameters $z_k$ encode this structure.

The algebraic SDP solver of [Chapter 11](#chap:nuclear-interactions) is the $\mathbb{Z}[q^{\pm 1/2}]$-shadow of the hyperbolic-geometry calculation. This rests on three correspondences, which are asserted here, not established; no witness checks them:

* **Cusps from poles.** The roots of the $q$-Pochhammer denominator $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$ seed the Frobenius positivity constraints in the SDP.
* **Newton iteration on the gluing equations.** The Newton solver for Thurston's gluing equations (e.g. SnapPy) seeds from these poles and converges to the shape parameters $z_k$ realising the complete hyperbolic structure. The same algebraic-residue data feeds both the SDP and the gluing solver; they are different *evaluations* of one categorical object.
* **Steepest descent.** On the Archimedean side, the residue sum becomes the Picard--Lefschetz thimble decomposition of the Seiberg--Witten action $S(z)$ (thimble). The Gröbner--Shirshov reduction depth is expected to equal the number of ideal tetrahedra used in the triangulation (the GB--PL bijection). The SDP's complementary-slackness rank equals the number of thimble flows realising the optimum.

In short: **two knots settle into the lowest-energy operator because that operator is the unique fixed point of Newton iteration on the Thurston gluing equations seeded by the $q$-Pochhammer poles, and that fixed point is the Archimedean realisation of the SDP optimum**.

The next remark details why this functions as the "hyperbolic relaxation" picture, mapping SDP dual variables to thimble depths.
