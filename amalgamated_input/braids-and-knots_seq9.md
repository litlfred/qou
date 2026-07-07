<!-- FILE_START: trefoil-knot-intro.md -->
The trefoil $3_1$ is the simplest non-trivial knot and the
canonical entry point to the categorical knot category: its
fundamental group and operator algebra exhibit the essential
features (non-abelian first homology, two-dimensional irreducible
representation) that the heavier knots inherit.  This short
section records the trefoil's knot group and operator algebra,
fixing the conventions used downstream.
<!-- FILE_END: trefoil-knot-intro.md -->

<!-- FILE_START: trefoil-knot-group.md -->
The trefoil knot $K_{3,2}$ is the simplest non-trivial torus knot.  Its
complement has fundamental group

$$
  \pi_1(S^3\setminus K_{3,2})
  = \langle x,y\mid xyx=yxy\rangle
   \cong B_3,
$$

The trefoil-knot group is isomorphic to the braid group on three
strands ([braid group](#def:braid-group)).  This relation $xyx=yxy$ is
the *braid relation*: it encodes the fact that the three-strand
braid may be closed into the trefoil by identifying the top and bottom of
the braid.
<!-- FILE_END: trefoil-knot-group.md -->

<!-- FILE_START: trefoil-operator-algebra.md -->
In the $\mathrm{SU}(2)$ representation
([SU(2) generators](#def:su2-generators)), the trefoil braid relation
$xyx=yxy$ becomes the operator identity

$$
  \alpha\beta\alpha
  = \beta\alpha\beta
$$

for the generators $\alpha$ and
$\beta$.  Explicitly, using

$$
  \alpha=\begin{pmatrix}e^{i\pi/3}&0\\0&e^{-i\pi/3}\end{pmatrix},
  \qquad
  \beta=\begin{pmatrix}0&i\\i&0\end{pmatrix},
$$

both products evaluate to

$$
  \alpha\beta\alpha
  = \begin{pmatrix}0&ie^{2i\pi/3}\\ie^{-2i\pi/3}&0\end{pmatrix}
  = \beta\alpha\beta.
$$

The eigenvalues of the composite $\alpha\beta$ govern the phases
acquired when quarks exchange colour charges along the trefoil path.
<!-- FILE_END: trefoil-operator-algebra.md -->

