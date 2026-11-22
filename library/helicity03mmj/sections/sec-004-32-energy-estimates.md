---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-004-32-energy-estimates
section_title: "Energy estimates."
section_number: 3.2
pages: 6-8
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
toc_source: outline
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
in physics are magnetic ﬁelds.
Imagine a magnetic ﬁeld frozen in an inﬁnitely
conducting, but viscous medium. Then moving according to the system of the MHD
equations, the medium kinetic energy will be dissipating due to the ﬂuid viscosity,
until it comes to a rest. The magnetic energy of the transported magnetic ﬁeld
should tend to its minimal value during the evolution, as any energy excess beyond
the minimum would be converted to further motion, see [1].
It turns out that helicity of a divergence-free (magnetic) vector ﬁeld is that it
bounds from below ﬁeld’s (magnetic) energy, i. e., the square of its L2-norm in some
Riemannian metric. Namely, one has the following
GEOMETRY OF HIGHER HELICITIES
995
Theorem 3.3 [1]. For a divergence-free vector ﬁeld ξ in a compact domain M
Z
M
(ξ, ξ) dx3 ≥c(M) · H(ξ),
where c(M) is a positive constant related to the shape and size of M.
The proof is a composition of the Schwarz inequality and the Poincare inequality,
applied to the potential ﬁeld A := curl−1 ξ. (One can take the constant c(M) to
be reciprocal of the largest modulus of the curl−1 eigenvalues.) Below we discuss
several directions how to sharpen this result and, in particular, to extend it to ﬁelds
with zero helicity, where the above inequality is useless. For explicit estimates for
the constant c(M) for domains in R3, as well as a discussion of the geometry of
extremal vector ﬁelds we refer to [5].
Remark 3.4. In a sense, the above theorem gives an estimate of a geometric quan-
tity via topology. A geometric meaning of this inequality can be seen in the example
of the ﬁeld with closed orbits ﬁlling linked tori, which was discussed in Section 2.
To minimize the energy of a vector ﬁeld with closed orbits by acting on the ﬁeld by
a volume-preserving diﬀeomorphism, one has to shorten the length of most trajec-
tories. (Indeed, the orbit periods are preserved under the diﬀeomorphism action;
therefore, a reduction of the orbits’ lengths shrinks the velocity vectors along the
orbits.) In turn, the shortening of the trajectories implies a fattening of the solitori
(since the acting diﬀeomorphisms are volume-preserving).
For a linked conﬁguration the solitori prevent each other from endless fattening
and therefore from further shrinking of the orbits. Therefore, heuristically, in the
volume-preserving relaxation process the magnetic energy of the ﬁeld supported on
a pair of linked tubes is bounded from below and cannot attain too small values.
In particular, a nonzero helicity (or average linking of the trajectories) of a ﬁeld ξ
provides a lower bound for the energy.
Note that this heuristic argument is somewhat more general than the inequality
in Theorem 3.3 in the following sense. It demonstrates that there exists a lower
bound for the energy for a ﬁeld which has at least one linked pair of solitori as in
the example above. However, the helicity of such a ﬁeld might turn out to be zero,
if, e. g., it has another (“mirror”) pair of solitori linked in the opposite direction
which makes vanish the total averaged self-linking of trajectories of the vector ﬁeld.
This shows that one needs a more subtle energy estimates, where, in particular, the
contribution of any nontrivially linked “tube of trajectories” into the energy bound
could not be canceled out.
For instance, the energy estimate via helicity is not helpful in the case of a
Borromean link. Heuristically, however, there should be some lower energy bound
for this ﬁeld, since the components cannot be unlinked. One can show that indeed,
the energy is bounded away from zero, but direct energy estimates by means of
H(ξ1,2,3) are not very explicit and rather complicated, cf. [18].
Remark 3.5. More direct energy estimates were provided in [9] with the help of
the notion of asymptotic crossing number. The crossing number of two curves is
given by the Gauss integral (1) where, however, one takes the absolute value of the
numerator. Geometrically, such an integral gives the number of over-crossings in
996
B. KHESIN
a plane projection of two curves and averaged over all directions of the projection.
This number is not a homotopy invariant, but one can “force” it to be invariant by
minimizing over all homotopies of two given space curves.
Similarly to the linking number, one deﬁnes an asymptotic version of the crossing
number for two vector ﬁelds. This way one obtains a more subtle invariant than
asymptotic linking, which is, in particular, often applicable to vector ﬁelds with
non-zero divergence. One of the the best energy estimates obtained with the help
of this notion is as follows.
Theorem 3.6 [9]. Suppose a vector ﬁeld ξ in R3 has an invariant torus T forming
a nontrivial knot K. Then
Z
T
(ξ, ξ) dx3 ≥

16
π · Vol(T)
1/3
· |Flux ξ|2 · (2 · genus(K) −1),
where Flux ξ is the ﬂux of ξ through a crossection of T, Vol(T) is the volume of the
solid torus, and genus(K) is the genus of the knot K.
Recall, that for any knot its genus is the minimal number of handles of a spanning
(oriented) surface for this knot. For an unknot the genus is 0, since one can take
a disk as a spanning surface. For a nontrivial knot one has genus(K) ≥1 and,
therefore, the above energy is bounded away from zero:
R
(ξ, ξ) dx3 > 0.
Note that there are no restrictions on the behavior of the divergence-free ﬁeld
inside this invariant torus, and hence this result has a wide range of applicability. In
particular, it is suﬃcient for the ﬁeld to have at least one closed knotted trajectory
of the elliptic type. The latter means that its Poincar´e map has two eigenvalues of
modulus 1. Then the KAM theory implies that a generic elliptic orbit is conﬁned
to a set of nested invariant tori. Hence any such orbit ensures that the energy of
the corresponding ﬁeld has a non-zero lower bound.
Problem 3.7. Does the presence of any nontrivially knotted closed trajectory (of
any type: hyperbolic, non-generic, etc.) or the presence of chaotic behavior of trajec-
tories for a ﬁeld provide a positive lower bound for the energy (even if the averaged
linking of all trajectories totals zero) and therefore prevent a relaxation of the ﬁeld
to arbitrarily small energies?
Remark 3.8. The rotation ﬁeld in the three-dimensional ball is an example of
an opposite type: all its trajectories are pairwise unlinked. It was suggested by
A. Sakharov and Ya. Zeldovich, and proved by M. Freedman [8], that this ﬁeld can
be transformed by a volume-preserving diﬀeomorphism to a ﬁeld whose energy is
arbitrarily close to 0.
