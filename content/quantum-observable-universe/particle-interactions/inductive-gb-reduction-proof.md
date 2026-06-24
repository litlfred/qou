At each inductive step, the product
$\mathcal{N}_{\leq k} \cdot C \cdot \mathfrak{N}_{k+1}$ has
at most $|\mathcal{N}_{\leq k}| \times 2 \times 6$ terms
(the crossing $C$ has at most 2 terms, and the nucleon NF has
6 terms).  The Gröbner--Shirshov reduction eliminates all
$\sigma_i^2$ via the Hecke relation and sorts via Yang--Baxter,
producing a normal form of bounded size.

The key identity enabling this is the **Hecke square rule**
for typed crossings:

$$
  C_{pp}^2 = H_A \cdot C_{pp} + \mathbf{1},
  \qquad
  C_{nn}^2 = H_A \cdot C_{nn} + \mathbf{1}
$$

where $H_A = q - q^{-1}$.  These are instances of the Hecke
relation $\sigma_i^2 = H_A\sigma_i + \mathbf{1}$ applied to
typed crossings.  They ensure that consecutive same-type
nucleon pairs do not increase the NF complexity: two $pp$
crossings reduce to a linear combination of a single crossing
and the identity.

For mixed crossings:

$$
  C_{pn}^2
  =
  H_A \cdot C_{pn} + \mathbf{1}
  - \tfrac{1}{4}H_A^2
$$

The extra constant $-\tfrac{1}{4}H_A^2$ is the mixed-crossing
correction, absorbed into the identity channel at each step.
