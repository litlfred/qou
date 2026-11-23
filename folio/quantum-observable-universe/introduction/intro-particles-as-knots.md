The state space on which all of this lives is not free to take any
shape. It is a compact Riemann surface, and its Euler characteristic
$\chi = 2 - 2g$ records its genus $g$. The lifting obstructions of the
foundational chapters force $g \geq 1$; the *Descartes condition*
$\chi = -6$ fixes $g = 4$. Among the universes satisfying that
condition one surface is terminal: Bring's curve of genus four, whose
automorphism group is the symmetric group $S_5$
([Descartes theorem](#thm:descartes);
[Bring's surface](#def:brings-surface)).

Particles are modelled as knots and links in this setting. The
dictionary is a naming convention for constructions inside the model,
in the way a topologist calls a particular knot "the trefoil": a loop
with no crossings is the lightest, most elusive particle, the
neutrino; a single over–under knot, the trefoil, is the electron; two
loops linked once, the Hopf link, is the strong binding of quarks;
three loops linked so that no two are directly joined, the Borromean
rings, is the proton or neutron. The same objects can be read as
vortex lines in a fluid, and the later chapters use both pictures.

The idea that particles are knots has a history. Helmholtz proved in
1858 that in an ideal fluid a vortex tube moves with the flow and keeps
its strength \cite{helmholtz1858}, so a knotted vortex ring keeps its
knot type. In 1867 William Thomson, later Lord Kelvin, proposed that
atoms are knotted and linked vortex rings in the ether, one knot type
for each element \cite{thomson1867vortexatoms}. Maxwell took the idea
seriously and recorded Gauss's integral for the linking number of two
closed curves \cite{maxwell1873treatise2}, and Tait's tables of knots,
begun to give the vortex atoms a periodic table, started knot theory as
a subject \cite{tait1877knots}. The vortex atom was abandoned by about
1900 \cite{kragh2002vortexatom}, but knotted particles have returned,
as knotted solitons in field theory \cite{faddeevniemi1997} and in
Avrin's model, where the unknot and the trefoil bound the bands that
model the elementary fermions \cite{avrin-2012}. This paper keeps the
combinatorics of that lineage, knot and braid types and the algebra of
their crossings, and not the ether or its mechanics; the chapter on
knots and particles gives a fuller account
([Knots, Particles, and Confinement](#chap:knots-particles-confinement)).

Two later programmes share the categorical setting without the knots.
In algebraic quantum field theory in four spacetime dimensions the
superselection sectors form a symmetric tensor category, so the braid
group acts through the symmetric group, and Doplicher and Roberts
reconstruct a compact gauge group from it
\cite{doplicher-haag-roberts1971,doplicher-roberts1989}; only in two or
three dimensions are the statistics braided
\cite{fredenhagen-rehren-schroer1989,frohlich-gabbiani1990}. In
categorical quantum mechanics the commutative special
$\dagger$-Frobenius algebras in finite-dimensional Hilbert spaces are
exactly the orthonormal bases \cite{coecke-pavlovic-vicary2013}. Both
programmes take masses as external data. The present construction
differs in using a braided category with $\sigma_i^2 \neq 1$ and in
asking whether mass ratios can be read off closed braids; how far that
succeeds is the subject of the comparison chapters.

The algebra that describes how such strands cross is the
Iwahori–Hecke algebra $H_n(q)$. Its generator $\sigma_i$ crosses
strand $i$ over strand $i+1$, and the only rule beyond the braid
relations is one quadratic equation,

$$
  (\sigma_i - q)(\sigma_i + q^{-1}) = 0,
$$

which says that a crossing has exactly two eigenvalues, $q$ and
$-q^{-1}$. At $q = 1$ the equation reads $\sigma_i^2 = 1$ and the
algebra is the group algebra $\mathbb{C}[S_n]$ of the symmetric
group, which a first course in representation theory splits into
matrix blocks, one for each irreducible representation. For
$n = 3$ the splitting is
$\mathbb{C}[S_3] \cong \mathbb{C} \oplus \mathbb{C} \oplus M_2(\mathbb{C})$,
of total dimension six; the deformation keeps this shape.

The photon stands apart. It is not a knot but a blend of the four
simplest operations,

$$
  \gamma = 1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^{-1},
$$

the identity together with the elementary crossings $\sigma_0$,
$\sigma_1$ and the pair-production vertex $\sigma_0\sigma_1^{-1}$. This is what lets light build matter:
when two photons meet, their terms multiply out under the quadratic
relation and reach every operator of a six-element basis of
$H_3(q)$ ([pair production](#prop:gamma-gamma-generates-particles)).
The embeddability bound on the genus-four surface keeps the operator
content at exactly that six-dimensional algebra, so the list of
elementary interactions is finite.

One object recurs at the framework's hardest edges: an obstruction
class, the precise measure of when local data fails to extend
globally ([lifting condition](#def:yekutieli-lifting-condition)). In
the $q$-deformed settings of the later chapters, questions about the
smoothness of a fluid, about shortcuts in a computation and about the
zeros of a zeta function are each translated into a question about a
class of this kind. The translations are where the open content lies,
and sharing a class does not by itself make the answers agree.
