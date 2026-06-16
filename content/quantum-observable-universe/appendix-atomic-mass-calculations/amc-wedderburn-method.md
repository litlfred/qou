## Derived computation method

The calculations in this appendix use the three-invariant mass
formula ([Theorem](#thm\:wedderburn-mass-formula)) with all
quantities derived from $q_0$ and $m_e$.  No AME2020 binding
energies are used as input.

### Computation procedure for each element

For element $Z$ with most stable isotope mass number $A = Z + N$:

**Step 1.** Find the nuclear ground-state ordering by minimising
$\Phi_1$ over all $\binom{A}{Z}$ permutations of $Z$ protons and
$N$ neutrons.  For $\binom{A}{Z} \leq 50000$: exact search.  For
larger atoms: steepest-:refterm[descent]{#descent} local search from multiple starting
configurations.

**Step 2.** Insert $Z$ electrons by greedy minimisation of
$\Phi_1$: for each electron, try all positions in the current
ordering and choose the one with lowest $\Phi_1$.  This produces
the atomic braid ordering ([atomic braid](#def\:atomic-braid))
with ep pairs.

**Step 3.** For each generator $i$ of the atomic braid
($i = 0, \ldots, A + Z - 2$), compute the $2 \times 2$ transfer
matrix $M_i$ by chaining crossing matrices
$\bigl[\begin{smallmatrix}
  c \cdot H_A + d & c \\ c & d
\end{smallmatrix}\bigr]$
for all strands $j > i$.  Extract:

* $\hat{V}_i = z \cdot (M_i)_{12} + (M_i)_{22}$ (traced volume),
* $\det M_i = (M_i)_{11}(M_i)_{22} - (M_i)_{12}(M_i)_{21}$
  (determinant),
* $\lambda_i^{\mathrm{sym}} / \lambda_i^{\mathrm{alt}}$
  (eigenvalue ratio from per-crossing products).

**Step 4.** Sum to obtain $\Phi_1$, $\Phi_2$, $\Phi_3$.

**Step 5.** Evaluate:

$$
  \mathcal{M}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha(\Phi_1 - 2[3]_q \cdot \Phi_2 + H_A^2 \cdot \Phi_3)
$$

### Input parameters

See [Table: Input parameters for the three-invariant computation](#tbl:amc-wedderburn-method-table-data).

Fitted parameters: **none**.

### Reproducibility

The Python implementation is in
`computations/atom_mass_combined.py`.  The Rust
Gröbner–Shirshov engine
([reduction methods](#rem\:groebner-reduction-methods)) computes
exact normal forms and $F_{\mathrm{Pauli}}$ certificates.  All
witness files are committed to the repository.
