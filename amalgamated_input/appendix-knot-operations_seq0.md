<!-- FILE_START: hecke-operations.md -->
The Hecke algebra $H_3(q)$ has three fundamental relations. These relations form the complete set of rewriting rules to reduce any composite knot operation to the six-element normal form (NF) basis. 

**Relation 1 (Hecke).**
$\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$.
This trades any squared crossing for a linear combination of single crossings, strictly lowering the number of repeated generators.

**Relation 2 (Yang--Baxter).**
$\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$.
This braid relation allows the reduction algorithm to choose a single canonical ordering when commuting generators. 

**Relation 3 (Hecke inverse).**
$\sigma_i^{-1} = \sigma_i - (q - q^{-1})\mathbf{1}$.
This replaces every inverse crossing with a positive crossing minus a multiple of the identity, clearing all inverse generators for Relations 1 and 2.

**Table K.2: Composite operations and their normal forms.**

See [Table 1](#tbl:hecke-operations-table1-data).

**Borromean operations** (confinement/gluon field):

See [Table 2](#tbl:hecke-operations-table2-data).
<!-- FILE_END: hecke-operations.md -->

<!-- FILE_START: borromean-gluon-content.md -->
The normal form of the Borromean braid $B_3$ encodes its gluon content and color-singlet status:

$$
  B_3 = +0.998\gamma - 0.010\sigma_0 + 0.009\sigma_1
        + 0.046L_+ - 0.044L_-
$$

The $L_+$ and $L_-$ coefficients measure the gluon content. Their signed sum nearly vanishes ($+0.046 - 0.044 = +0.002$). This vanishing net gluon coefficient is precisely the color-singlet condition. 

The identity coefficient $\gamma \approx +0.998$ places $B_3$ perturbatively close to the identity. The gluon terms thus constitute a small correction to free quarks, yielding net$(B_3) \approx 1$.
<!-- FILE_END: borromean-gluon-content.md -->

