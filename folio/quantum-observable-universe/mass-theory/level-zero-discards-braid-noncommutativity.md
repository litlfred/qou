The statement records that for $n \geq 4$ the Hecke algebra carries irreducible
representations beyond the three extremal ones, and that the invariants they
produce are not captured by the $2 \times 2$ transfer matrix. That is a
statement about the *count of blocks*. It is not a statement that the
transfer-matrix construction is complete below $n = 4$, and reading it as one
overstates the theorem.

A second approximation is present at every $n \geq 3$, independent of the block
count. Step 2 of the proof forms the chained element
$X_i = \prod_{j > i} X_j$ inside the two-dimensional crossing algebra
$R[\sigma] = R[x] / \bigl((x - q)(x + q^{-1})\bigr)$, which is commutative, and
sets $M_i = T(X_i)$. The crossings so chained belong to *different strand
pairs*, and the corresponding braid generators do not commute in $H_n(q)$ for
any $n \geq 3$. The Level-0 reduction therefore discards braid
non-commutativity as well as the non-extremal blocks, and only the second of
those is an $n \geq 4$ effect.

The two are easy to conflate because the dimensions agree at $n = 3$: the
standard block of $H_3(q)$ has dimension $n - 1 = 2$, and so does
$R[\sigma]$. This is a coincidence of dimension rather than an identification. By
Step 2 the two eigenvalues of $M_i$ are the symmetric and alternating
characters $\lambda_i^{\mathrm{sym}}$ and $\lambda_i^{\mathrm{alt}}$, so the
standard representation does not act on $M_i$ at all; the row labelled
*standard* in the correspondence table records the Markov functional
$\mathrm{tr}_M(X_i) = z \, (M_i)_{12} + (M_i)_{22}$ on the crossing algebra
rather than an image of the two-dimensional block.

Deuterium is the unique atom with $n = A + Z = 3$. It is therefore both the
smallest atom carrying two distinct braid generators and the only one at which
the extremal blocks exhaust the partitions, which makes it the single point at
which the two approximations can be separated. Evaluating the functional there
gives

$$
  \alpha\bigl(
    \Phi_1 - 2[3]_q \cdot \Phi_2 + h_{\mathrm{A}}^2 \cdot \Phi_3
  \bigr)
  \approx -6.214 \; \mathrm{MeV},
$$

against a measured $-B(\mathrm{D}) \approx -2.225 \; \mathrm{MeV}$. Since no
non-extremal block exists at $n = 3$, the discrepancy is attributable to the
Level-0 reduction alone. It bounds the magnitude of that one approximation and
excludes no ingredient of the construction. The evaluation, together with
checks of the Step 2 readouts and of the commutativity of $R[\sigma]$ against
the non-commutativity of $H_3(q)$, has been carried out exactly.
