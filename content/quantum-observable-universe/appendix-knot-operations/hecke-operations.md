The Hecke algebra $H_3(q)$ has three fundamental relations
governing all knot operations.  Together they are exactly the
rewriting rules needed to drive any composite operation down to
the six-element normal form basis: Relation 1 lowers the degree
of any generator that appears squared, Relation 2 reorders
adjacent generators into a canonical word, and Relation 3
eliminates inverse crossings in favour of positive ones.  Every
composite operation reduces to the six-element normal form basis
by repeated application of these three rules.

**Relation 1 (Hecke).**
$\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$
for each generator $\sigma_i$.  Squaring a crossing is never a
normal-form word, so this relation trades it for a linear
combination whose highest-degree term is a single crossing: the
identity (photon) plus a crossing weighted by $q - q^{-1}$.  Each
application therefore strictly lowers the number of repeated
generators, which is what makes the reduction terminate.

**Relation 2 (braid relation / Yang--Baxter).**
$\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$.
This is the braid relation on adjacent generators; it is the
combinatorial (constant-coefficient) form of the Yang--Baxter
equation for the crossings.  Because both sides are the two
generator orderings of the trefoil word, the relation identifies
those two orderings, letting the reduction choose a single
canonical ordering when generators must be commuted past one
another.

**Relation 3 (Hecke inverse).**
$\sigma_i^{-1} = \sigma_i - (q - q^{-1})\mathbf{1}$.
A normal-form word uses only positive crossings, so this relation
rewrites every inverse crossing as a positive one minus a multiple
of the identity: inverting a crossing subtracts $q - q^{-1}$ from
the identity channel.  Applied throughout a word, it clears all
inverse generators, leaving only positive crossings for
Relations 1 and 2 to normalise.

**Table K.2: Composite operations and their normal forms.**

See [Table 1](#tbl:hecke-operations-table1-data).

**Borromean operations** (confinement/gluon field):

See [Table 2](#tbl:hecke-operations-table2-data).
