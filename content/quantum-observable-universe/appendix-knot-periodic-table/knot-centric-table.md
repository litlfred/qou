The standard periodic table organizes elements by electron
configuration (rows = periods, columns = groups).  A
**knot-centric periodic table** reorganizes by the underlying
knot topology: nuclear Borromean shell structure and electron
trefoil resonance modes.  Under this reorganization shell
structure and magic numbers become *emergent*: they
follow from the Borromean crossing count rather than being read
off an empirical table.

**Organizing principles.**

1. **Rows**: nuclear HO level $N$ with magic splits
   ([shell-transition knot](#conj:shell-transition-knot)).
   Each row boundary is a magic number (stability pair).

2. **Columns**: proton sub-shell filling order
   (Mayer--Jensen), left to right, with sub-shells
   separated by gaps and elements filling sequentially
   by $Z$ within each sub-shell (the left-to-right
   magic-receptive-to-magic pattern is detailed under
   *Column structure* below).

   The sub-shell capacities follow the spin-orbit
   splitting of the harmonic oscillator levels
   ([shell-transition knot](#conj:shell-transition-knot)):
   each sub-level $nl_j$ accommodates $2j + 1$ protons.
   The electron shell structure is determined by the
   eigenvalues of the photon-electron transfer matrix
   $T_{\gamma e}(q)$
   ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)):
   at the substrate parameter $q$, the larger eigenvalue
   $\lambda_+ \approx 1.1073$ governs shell energy scaling via a
   Chebyshev recurrence.

3. **Color coding**: $k_\alpha$ (number of $\alpha$ sub-links
   in the nucleus), magic-receptive status (whether the element
   is in a spin-orbit magic shell).

**Row structure (nuclear side).**

See [Table 1](#tbl:knot-centric-table-table1-data).

Rows 1--3 close at pure HO shell boundaries.  Rows 4--7
are magic shells created by spin-orbit coupling
($\mathcal{B}_3$ crossing number $= 3$): the highest-$j$
sub-level drops into the previous HO shell, creating a
new stability pair.  Elements in these rows are
**magic-receptive** — they fill the spin-orbit-split
sub-shell that leads to the next magic number.

**Column structure (proton sub-shell filling).**

Within each row, elements fill left to right through the
Mayer--Jensen sub-shells.  The sub-shell sequence for
each row is:

See [Table 2](#tbl:knot-centric-table-table2-data).

Each sub-shell group is separated by a gap in the grid.
The first element in a row (far left) is the
magic-receptive element — the first proton past the
previous stability pair.  The last element (far right) is
the magic number that closes the shell.

**Transfer matrix backbone.**

The computational backbone of the table is the transfer matrix
product ([transfer matrix operator](#def:transfer-matrix-operator)).
Each nucleon pair contributes a $2 \times 2$ matrix $T_{ij}(q)$
with three crossing types:

See [Table 3](#tbl:knot-centric-table-table3-data).

The nuclear Skein polynomial
$P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$
([Skein polynomial](#prop:skein-polynomial-transfer-matrix))
is computed in factored form by $\binom{A}{2}$ matrix
multiplications.  Beta decay shifts each crossing by the
universal matrix $\Delta_\beta(q)$
([beta decay matrix](#prop:beta-decay-transfer-matrix)),
independent of partner nucleon type.

**Knot coverage.**

The generation completeness theorem
([generation completeness](#thm:generation-completeness))
guarantees that every knot with Seifert genus $\leq 4$ is
reachable from the seven torus generators via Skein crossing
changes.  Detection is complete via Alexander surjectivity and
Markov non-degeneracy
([knot exhaustiveness](#rem:knot-exhaustiveness)).

**Element card.**

Each element displays:

- **Symbol** and atomic number
- **Nuclear knot**: $Z\mathcal{B}_3 \oplus N\mathcal{B}_3$
  with $k_\alpha$ sub-links highlighted
- **Electron knot**: trefoil writhe diagram showing occupied
  shells and the current Fourier mode
- **Transfer matrix data**: $\binom{A}{2}$ steps,
  $\deg P_{\mathcal{N}} \leq A^2 - 1$
- **Shell eigenvalues**: dominant $\lambda_+^n$ and Chebyshev
  index at the element's outermost shell
- **$N_{\mathrm{pred}}$ vs $N_{\mathrm{obs}}$**: predicted
  and observed neutron number
- **Magic-receptive indicator**: a row labelled
  *(magic-receptive)* indicates the element is in a
  spin-orbit magic shell
