<!-- FILE_START: archimedean-condition-leptons-intro.md -->
The preceding sub-section stated the Descartes condition $\chi = -6$ and proved that its descent chain forces a maximally-descended genus. This sub-section extracts the immediate physical consequences: the lepton spectrum, the chirality assignment that distinguishes leptons from anti-leptons, the affine-light-cone parameterisation underlying the chirality measurement, and the trefoil-chirality correspondence that anchors the chirality assignment in braid data. The Brings-curve block closes the sub-section by pointing forward to the genus-completeness derivation that the next sub-section unfolds.
<!-- FILE_END: archimedean-condition-leptons-intro.md -->

<!-- FILE_START: archimedean-leptons.md -->
The Reeb decomposition ([Reeb decomposition](#ex:reeb-decomposition)) applied to a Descartes universe yields two classes of fermionic excitations ([fermion](#def:fermion-boson-decomposition)). The degree of the vertical component $\alpha_V$ distinguishes them. Forms with $\deg\alpha_V = 1$ correspond to electrons, while forms with $\deg\alpha_V = 2$ correspond to muons. More generally, each additional unit of vertical degree identifies a successive lepton generation. The constraint $\chi(\mathcal{S}) = -6$ bounds the number of such generations, since the Hodge decomposition of $\mathcal{S}$ admits only finitely many independent vertical harmonic forms. This generation-dependent structure produces testable predictions, including a $q$-correction to the proton charge radius that differs between muonic and electronic hydrogen ([Section](#ssec:proton-radius)).
<!-- FILE_END: archimedean-leptons.md -->

<!-- FILE_START: archimedean-chirality.md -->
The Reeb vector field $\xi$ on the CR manifold $M$ carries a natural orientation. The sign of the contact form $\varTheta(\xi) = 1$ singles out a preferred direction along the vertical distribution. Left-handed and right-handed chiralities correspond to the two orientations of $\xi$ relative to the complex structure of $M$. For fermions ([fermion](#def:fermion-boson-decomposition)), the vertical component $\alpha_V$ transforms with a definite sign under reversal of $\xi$. Chirality is therefore encoded in the $\pm$-eigenspaces of the Reeb involution $\xi \mapsto -\xi$. Bosons ([boson](#def:fermion-boson-decomposition)), being purely horizontal, are chirality-blind. This is consistent with the observed parity invariance of the electromagnetic and strong interactions. Cf. \cite{nicolaescu2005, petit-2005}.
<!-- FILE_END: archimedean-chirality.md -->

<!-- FILE_START: light-cone-affine.md -->
Consider an open subset $U \subset M_0$ representing a portion of the descended universe between two regime boundaries. An *affine chart* on $U$ is a local coordinate patch in which the metric on the base manifold $M_0$ defines a causal structure. The *light cone* of the affine chart forms the boundary of the causal future in $U$. The metric on $M_0$ determines this light cone, which ensures no singularity of the ambient space is visible from within the chart. In this way, the affine chart provides a non-singular window onto a portion of the Descartes universe.
<!-- FILE_END: light-cone-affine.md -->

<!-- FILE_START: chirality-trefoil.md -->
The chirality of the observable universe—manifest in the three colour charges of quantum chromodynamics—is encoded in the symmetry group of the descended surface $M_0$. [genus-maximal :refterm[descent]{#descent}](#prop:genus-maximal-descent) identifies $M_0$ as a genus-$4$ Riemann surface. We require a genus-$4$ surface whose automorphism group contains three subgroups isomorphic to $S_3$. These are quotients of the trefoil knot group $\pi_1(S^3 \setminus K) \cong \langle x, y \mid x^2 = y^3 \rangle$, and they correspond to the three colour charges (red, green, blue). These $S_3$ subgroups generate a subgroup of the monodromy group. The remaining generators of the full automorphism group act by conjugation, permuting the three $S_3$ subgroups among themselves.
<!-- FILE_END: chirality-trefoil.md -->

<!-- FILE_START: brings-curve.md -->
Bring's curve is the unique Riemann surface of genus $4$ with the maximal automorphism group $S_5$ (order $120$) for its genus. It is defined by the intersection of three symmetric hypersurfaces in $\mathbb{P}^4$:

$$
  \sum_{j=0}^{4} x_j = 0,
  \qquad
  \sum_{j=0}^{4} x_j^2 = 0,
  \qquad
  \sum_{j=0}^{4} x_j^3 = 0.
$$

The symmetric group $S_5$ acts by permuting the five homogeneous coordinates. This action realises the monodromy structure described in [chirality and trefoil](#rem:chirality-trefoil). The group $S_5$ contains three copies of $S_3$ (quotients of the trefoil knot group) corresponding to the three colour charges. Elements outside these subgroups act by conjugation, permuting the three copies among themselves.
<!-- FILE_END: brings-curve.md -->

<!-- FILE_START: brings-q-hyperbolic-geometry.md -->
**Remark.** The classical hyperbolic geometry of Bring's curve (genus $g=4$) admits a canonical $q$-deformation governed by the quantum hyperbolic plane $SU_q(1,1)$.

While the Euclidean sector ($E_q(2)$) of the theory is governed by the Hahn–Exton $q$-Bessel function (the third kind, $J_\nu^{(3)}(x;q)$) as seen in the ladder coefficients, the $q$-hyperbolic geometry on the Bring's surface fibre is intrinsically described by **Jackson's $q$-Bessel functions of the first and second kinds** ($J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$). These functions appear as matrix elements of the representations of $SU_q(1,1)$ and encode the "radial" components of the deformed hyperbolic structures.

The first-order contiguity recurrences satisfied by these coefficients ([`prop:jackson-q-bessel-contiguity-recurrence`](../mass-theory/jackson-q-bessel-contiguity-recurrence.md)) supply the natural orthogonal basis for the $q$-hyperbolic deformation of Bring's curve. Their $q$-weights are adapted to the $SU_q(1,1)$ Casimir invariants, unlike the third kind's $q^{k(k-1)/2}$ weight.
<!-- FILE_END: brings-q-hyperbolic-geometry.md -->

