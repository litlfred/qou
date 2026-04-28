The standard periodic table organizes elements by electron
configuration (rows = periods, columns = groups).  A
**knot-centric periodic table** reorganizes by the underlying
knot topology: nuclear Borromean shell structure and electron
trefoil resonance modes.

**Organizing principles.**

1. **Rows**: nuclear HO level $N$ with magic splits
   ([shell-transition knot](#prop:shell-transition-knot)).
   Each row boundary is a magic number (stability pair).

2. **Columns**: proton sub-shell filling order
   (Mayer--Jensen), left to right.  The leftmost element
   in each row has just started filling the new shell
   (magic-receptive); the rightmost element closes the
   shell (magic number).  Sub-shells are separated by
   gaps; within each sub-shell, elements fill
   sequentially by $Z$.

   The sub-shell capacities follow the spin-orbit
   splitting of the harmonic oscillator levels
   ([shell-transition knot](#prop:shell-transition-knot)):
   each sub-level $nl_j$ accommodates $2j + 1$ protons.
   The electron shell structure is determined by the
   eigenvalues of the photon-electron transfer matrix
   $T_{\gamma e}(q)$
   ([shell structure eigenvalues](#prop:shell-structure-eigenvalues)):
   at the substrate parameter $q$, $\lambda_+ = 1.1073$
   governs shell energy scaling via a Chebyshev recurrence.

3. **Color coding**: $k_\alpha$ (number of $\alpha$ sub-links
   in the nucleus), magic-receptive status (whether the element
   is in a spin-orbit magic shell).

**Row structure (nuclear side).**

| Row | Magic $Z$ | $N$ | Magic type | Elements |
|----:|----------:|----:|:----------:|----------|
| 1 | 2 | 0 | HO closure | H, He |
| 2 | 8 | 1 | HO closure | Li $\to$ Ne |
| 3 | 20 | 2 | HO closure | Na $\to$ Ca |
| 4 | 28 | 3 | spin-orbit (magic-receptive) | Sc $\to$ Ni |
| 5 | 50 | 4 | spin-orbit (magic-receptive) | Cu $\to$ Sn |
| 6 | 82 | 5 | spin-orbit (magic-receptive) | Sb $\to$ Pb |
| 7 | 126 | 6 | spin-orbit (magic-receptive) | Bi $\to$ U+ |

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

| Row | Sub-shells (capacity) | Total |
|----:|----------------------|------:|
| 1 | $1s_{1/2}$(2) | 2 |
| 2 | $1p_{3/2}$(4) $\mid$ $1p_{1/2}$(2) $\mid$ $1d_{5/2}$(2) | 8 |
| 3 | $1d_{5/2}$(4) $\mid$ $2s_{1/2}$(2) $\mid$ $1d_{3/2}$(4) | 10 |
| 4 | $1f_{7/2}$(8) | 8 |
| 5 | $2p_{3/2}$(4) $\mid$ $1f_{5/2}$(6) $\mid$ $2p_{1/2}$(2) $\mid$ $1g_{9/2}$(10) | 22 |
| 6 | $1g_{7/2}$(8) $\mid$ $2d_{5/2}$(6) $\mid$ $2d_{3/2}$(4) $\mid$ $3s_{1/2}$(2) $\mid$ $1h_{11/2}$(12) | 32 |
| 7 | $2f_{7/2}$(8) $\mid$ $1h_{9/2}$(2) | 10 |

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

| Crossing | $c$ | $d$ | Physical |
|----------|-----|-----|----------|
| $\mathfrak{p}$-$\mathfrak{p}$ | $1$ | $0$ | repulsive (EM) |
| $\mathfrak{n}$-$\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ | attractive (strong) |
| mixed | $1$ | $-\frac{q - q^{-1}}{2}$ | intermediate |

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
- **Nuclear knot**: $Z\mathcal{B}_3 \bowtie N\mathcal{B}_3$
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

**Visualization specification (for implementation).**

The visualization should be an interactive HTML page
(`folio-assistant/simulators/knot_periodic_table.html`) with:

1. **Layout**: 7 rows (one per stability-pair interval),
   vertically aligned on a shared grid.  Columns follow
   Mayer--Jensen proton sub-shell filling order, with gaps
   between sub-shells.

2. **Element tiles**: clickable tiles showing the element
   symbol, $Z$, $N$, $k_\alpha$, and a small SVG of the
   nuclear Borromean structure.

3. **Nuclear side panel**: when an element is selected, show
   the full Borromean baryon composition:
   - Number of $\alpha$ clusters ($k_\alpha$)
   - Which HO level the last nucleon occupies
   - Whether it's in a magic-receptive shell
   - Stability pair membership ($\diamond$, $\star$)

4. **Electron side panel**: show the trefoil writhe diagram:
   - Current shell $n$ and sub-shell $\ell$
   - Occupied Fourier modes as standing waves on the trefoil
   - Visual: animated trefoil spinning around a Borromean
     anchor, with the current mode highlighted

5. **Controls**:
   - Toggle between standard and knot-centric layouts
   - Filter by stability pair, magic-receptive status, $k_\alpha$
   - $q$ slider to show how the table changes with substrate
     parameter (at $q = 1$: all rows equal width, no
     no magic shells; at $q = q_0$: observed table)

6. **Knot notation**: use the visual conventions from
   [knot atom diagrams](#rem:knot-atom-diagrams):
   - Solid trefoil = forward-time fermion
   - Outlined trefoil = backward-time (antiparticle)
   - Circle = unknot (neutrino / neutron)
   - Interlocked circles = Hopf link
   - Borromean symbol = 3 interlocked rings (quark composite)

7. **Data source**: read from the knot-periodic table
   ([knot-periodic table](#prose:knot-periodic-table)) for
   $Z$, $N$, $N_{\mathrm{pred}}$, $\Delta N$, $k_\alpha$,
   masses, and $B/A$.

8. **Transfer matrix overlay**: optional display mode showing
   the number of transfer matrix steps $\binom{A}{2}$ and
   Skein polynomial degree bound $A^2 - 1$ for each element,
   color-coded by computational complexity.

9. **Shell eigenvalue display**: optional overlay showing
   $\lambda_+^n$ at the element's outermost electron shell,
   with the Chebyshev recurrence index and binding energy
   $\mathbf{E}_{\mathrm{bind}} \propto \lambda_+^{-n}$.
