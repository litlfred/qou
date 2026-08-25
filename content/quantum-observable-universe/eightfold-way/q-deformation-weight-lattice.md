A persistent confusion in the literature and in early drafts of this
framework conflates two occurrences of the number $2$ in the $A_2$
Serre relation.  Resolving this confusion is essential for
understanding what the substrate parameter $q_0$ does and does not do
to the eightfold-way classification.

**The two $2$s.**
The classical Serre relation for $A_2$ reads
$$
  e_i^2 e_j - 2\, e_i e_j e_i + e_j e_i^2 = 0,
$$
where the coefficient $2$ is the binomial coefficient
$\binom{2}{1} = \binom{1 - a_{ij}}{1}$, with $a_{ij} = -1$ the
off-diagonal Cartan entry.  Meanwhile, the diagonal Cartan entry is
$a_{ii} = 2$, which appears in the root angle formula
$\cos\theta = a_{ij}/a_{ii} = -1/2$, giving $\theta = 120°$.

The Drinfeld--Jimbo quantization replaces the binomial $2$ by the
Gaussian binomial $[2]_q = q + q^{-1}$:
$$
  e_i^2 e_j - [2]_q\, e_i e_j e_i + e_j e_i^2 = 0.
$$
The Cartan entry $a_{ii} = 2$ is *untouched*.  The angle
$\cos\theta = -1/2$ does not become $\cos\theta_q = -(q + q^{-1})/2$.
These are two different mathematical objects that coincide numerically
at $q = 1$: one is a binomial coefficient, the other is a normalization
constant.

**What is $q$-independent — machine-checked.**
The following are proved sorry-free in
`QOU/Eightfold/WeylInvarianceQDeformation.lean`:

- The off-diagonal entry $a_{12} = -1$ and the Serre exponent
  $1 - a_{12} = 2$ (`cartan_A2_offdiag`, `serre_exponent_A2`).
- The $q$-Serre coefficient $[2]_q$ genuinely *moves* with $q$ ---
  witnessed at $q = 2$, where the framed binomial is $5$ and the framed
  Cartan diagonal is $4$ (`qSerre_not_constant`) --- while the
  Cartan datum does not (`cartanMatrixAt_const`).  The conjunction
  of the two is the "two $2$s" separation
  (`cartan_fixed_while_qSerre_moves`), and it is the conjunction,
  not either half alone, that carries the content: constancy of the Cartan
  datum is true *by construction* and is compatible with both sides
  being constant, which is exactly the confusion at issue.
- For $(q-1)^2 \neq 0$ the two differ
  (`qSerre_neq_cartan_diag`); they agree at $q = 1$
  (`qSerre_eq_cartan_at_classical`).
- The root-angle ratio $\cos\theta = a_{ij}/a_{ii} = -1/2$
  (`root_angle_ratio_A2`).

**What the Lean does not establish.**
That Drinfeld--Jimbo quantisation leaves the root datum invariant is a
theorem of Lusztig/Kashiwara, cited here and *not* formalised in this
corpus; it belongs to the "standard, but not formalised" list below, not
to the machine-checked list above.  What is machine-checked is the
*arithmetic* of the separation on the $A_2$ datum, which is a weaker
statement and should not be cited for the stronger one.

**What is $q$-independent — standard, but not formalised here.**
These follow from the Drinfeld--Jimbo construction and are cited here, not
machine-checked:

- The root lattice $\Lambda_R = \mathbb{Z}\alpha_1 \oplus
  \mathbb{Z}\alpha_2$ and the weight lattice $\Lambda_W =
  \mathbb{Z}\omega_1 \oplus \mathbb{Z}\omega_2$.
- The Weyl group $W(A_2) \cong S_3$.
- Weight multiplicities: for generic $q$ the representation category
  $\mathrm{Rep}\,\mathcal{U}_q(\mathfrak{g})$ is tensor-equivalent to
  $\mathrm{Rep}\,\mathfrak{g}$.  Crystal bases exist precisely because
  the weight combinatorics is $q$-independent (the $q \to 0$ limit
  retains the same lattice).

**What $q$ does deform.**

- The braiding: the $R$-matrix of $\mathcal{U}_q(\mathfrak{sl}_3)$
  depends on $q$ and governs the braid group action on tensor products.
- The quantum dimensions: $\dim_q(V_\lambda) = \prod_{\alpha > 0}
  [\langle \lambda + \rho, \alpha^\vee \rangle]_q /
  [\langle \rho, \alpha^\vee \rangle]_q$.
- The Markov trace: $\tau_q(\beta)$ on $H_n(q)$ varies with $q$,
  producing $q$-dependent link invariants (Jones polynomial, HOMFLY-PT).
- The crossing energy: $\mathfrak{E}_\times(q) =
  \tfrac{1}{2}(q - q^{-1})$, which governs mass splittings in the
  framework.

**Consequence for the eightfold way.**
The hexagonal weight lattice of $A_2$ is rigid under $q$-deformation.
The octet and decuplet patterns do not "bend" or become hyperbolic
at $q = q_0$.  What changes is the *dynamics on* the lattice:
transition amplitudes, mass splittings, and mixing angles all depend
on $q_0$ through the Hecke algebra representations, while the
classification pattern itself --- which states go where on the
hexagon --- is $q$-independent.

The classification thus holds for any $q$, while the quantitative
predictions (mass ratios, decay rates) are specific to $q = q_0$.
