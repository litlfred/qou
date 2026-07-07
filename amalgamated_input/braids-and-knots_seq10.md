<!-- FILE_START: knot-fundamental-groups-intro.md -->
The fundamental group of a knot complement is the central
topological invariant the chapter uses to convert categorical
braid data into geometric statements.  This section records the
knot-complement group construction, surveys the Kronheimer–Mrowka
results on its instanton homology, and characterises the reducible
representations that play a structural role in the chapter's
Hecke decomposition.
<!-- FILE_END: knot-fundamental-groups-intro.md -->

<!-- FILE_START: knot-complement-group.md -->
For a knot $K\subset S^3$ (or, more generally,
$K\subset\mathbb{P}^1(\mathbb{C})$), the fundamental group
$\pi_1(\mathbb{P}^1(\mathbb{C})\setminus K)$ encodes the topology of the
complement.  A representation

$$
  \rho\colon\pi_1(\mathbb{P}^1(\mathbb{C})\setminus K)
   \longrightarrow \mathrm{PSL}(2,\mathbb{C})
$$

maps each meridian generator to a Mobius transformation of the
Riemann sphere.  The image of $\rho$ characterises the geometric
structure on the knot complement.
<!-- FILE_END: knot-complement-group.md -->

<!-- FILE_START: kronheimer-mrowka.md -->
Kronheimer and Mrowka proved that the fundamental group of every
non-trivial knot admits a non-trivial representation into
$\mathrm{SU}(2)$, and hence into
$\mathrm{PSL}(2,\mathbb{C})$.  In the
QOU context, this guarantees that every non-trivial knot type
contributing to the fibre bundle carries a non-abelian gauge holonomy.
The restriction to traceless elements of $\mathrm{SU}(2)$ aligns with
the category-theoretic setup of [Section](#sec:enveloping-algebras),
where the representation factors through the adjoint form.
<!-- FILE_END: kronheimer-mrowka.md -->

<!-- FILE_START: reducible-reps.md -->
When a representation
$\rho\colon\pi_1(\mathbb{P}^1(\mathbb{C})\setminus K)\to\mathrm{PSL}(2,\mathbb{C})$
is reducible, all generators fix the same point on $\mathbb{P}^1(\mathbb{C})$ ---
they are simultaneously conjugate to upper-triangular matrices, hence
all rotations around a common axis.  In the category-theoretic
formulation this corresponds to the abelianisation of the knot group.
Further generalisations via the Poincare--Birkhoff--Witt theorem and
unital Gröbner--Shirshov bases ([Section](#sec:enveloping-algebras)) describe
the passage from the reducible to the irreducible sector.

Concretely, the PBW filtration on
$\mathcal{U}_q(\mathfrak{su}(2))$ equips the associated graded algebra
$\mathrm{gr}\mathcal{U}_q$ with a commutative product.  A
Groebner--Shirshov basis for the $q$-deformed relations then exhibits
$\mathcal{U}_q$ as a flat deformation of $\mathrm{gr}\mathcal{U}_q$:
the leading monomials of the $q$-Serre relations provide a set of
non-overlapping obstructions whose resolution (composition lemma) yields
a normal-form basis coinciding with the Lusztig divided-power
basis.  In positive characteristic this construction
produces the distribution algebra $\mathrm{Dist}(G)$ of the lifted
formal group $G$ as a deformation of the commutative
$\mathrm{Dist}(H)$; the strong multiplicativity
condition guarantees that the Frobenius relation is preserved at every
filtration degree
([skew poisson integration](#prop:skew-poisson-integration)).

When the representation $\rho$ is reducible, all monomials in the
Groebner--Shirshov basis reduce to the abelian (Cartan) subalgebra; the
passage to irreducible $\rho$ corresponds to activating the
off-diagonal generators $E_\pm$, whose normal-form monomials generate
the full non-commutative algebra.
<!-- FILE_END: reducible-reps.md -->

