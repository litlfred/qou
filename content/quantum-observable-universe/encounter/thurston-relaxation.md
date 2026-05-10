## Thurston relaxation: SDP as a hyperbolic Newton solver

Once the two vortex cores have merged inside a tubular
neighbourhood $U \subset M$ of the encounter point, the
operative geometry is the complement $U \setminus K$, where $K$
is the link formed by the merged strands.  Thurston's
hyperbolisation programme tells us that, away from a finite list
of exceptional cases, $U \setminus K$ admits a complete
finite-volume hyperbolic structure, encoded by a triangulation
into ideal tetrahedra $\Delta_{z_k}$ and a system of *gluing
equations* in the shape parameters $z_k$.

The point of this section is that the algebraic SDP solver of
[Chapter 12](#chap:particle-interactions) is **not separate from
the hyperbolic-geometry calculation** — it is its
$\mathbb{Z}[q^{\pm 1/2}]$-shadow.  We make this precise in three
correspondences, each already established (or stated) elsewhere
in the manuscript:

* **Cusps from poles.** The roots of the $q$-Pochhammer
  denominator
  $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
  --- which are the natural seeds of the Frobenius
  positivity constraints in the SDP --- are in bijection with
  the ideal vertices of the tetrahedral triangulation of the
  $\Phi_q$-piece $K_S$.  This is the
  [pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)
  (1).

* **Newton iteration on the gluing equations.** The Newton solver
  used numerically to solve Thurston's gluing equations (e.g. by
  SnapPy) starts from these pole-derived seeds and converges to
  the shape parameters $z_k$ realising the complete hyperbolic
  structure.  The same algebraic-residue data feeds the SDP and
  the gluing solver; the two computations are different
  *evaluations* of one categorical object.

* **Steepest descent.** On the Archimedean side, the residue sum
  becomes the Picard--Lefschetz thimble decomposition of the
  Seiberg--Witten action $S(z)$
  ([thimble](#def:picard-lefschetz-thimble)); the Gröbner--Shirshov
  reduction depth maps to the number of ideal tetrahedra used in
  the triangulation
  ([GB--PL bijection](#conj:gb-reduction-pl-thimble-bijection)).
  The SDP's complementary-slackness rank equals the number of
  thimble flows realising the optimum.

In one sentence: **two knots settle into the lowest-energy
operator because that operator is the unique fixed point of
Newton iteration on the Thurston gluing equations seeded by the
$q$-Pochhammer poles, and that fixed point is the Archimedean
realisation of the SDP optimum**.  The algebraic and geometric
solvers are two faces of the same computation; the
[Archimedean realization functor](#def:archimedean-realization-functor)
is the explicit translator between them.

The interpretive content of *why* this is the
"hyperbolic relaxation" picture --- with the SDP dual variables
appearing as thimble depths --- is collected in the next remark.
