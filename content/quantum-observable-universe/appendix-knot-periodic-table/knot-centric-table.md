The standard periodic table organizes elements by electron
configuration (rows = periods, columns = groups).  A
**knot-centric periodic table** reorganizes by the underlying
knot topology: nuclear Borromean shell structure and electron
trefoil resonance modes.

**Organizing principles.**

1. **Rows**: nuclear HO level $N$ with intruder splits
   ([nuclear shell intruder](#prop:nuclear-shell-intruder)).
   Each row boundary is a stability pair.

2. **Columns**: electron Fourier mode $\ell$ and writhe
   level $n$
   ([orbital Fourier decomposition](#prop:orbital-fourier-decomposition)).
   Sub-blocks for $s$ ($\ell = 0$), $p$ ($\ell = 1$),
   $d$ ($\ell = 2$), $f$ ($\ell = 3$).

3. **Color coding**: $k_\alpha$ (number of $\alpha$ sub-links
   in the nucleus), intruder status (which HO level the last
   nucleon occupies).

**Row structure (nuclear side).**

| Row | Stability pair | $N$ | Intruder? | Elements |
|----:|---------------:|----:|:---------:|----------|
| 1 | 2 | 0 | — | H, He |
| 2 | 8 | 1 | — | Li $\to$ Ne |
| 3 | 20 | 2 | — | Na $\to$ Ca |
| 4 | 28 | 3 intruder | $1f_{7/2}$ drops | Sc $\to$ Ni |
| 5 | 50 | 4 intruder | $1g_{9/2}$ drops | Cu $\to$ Sn |
| 6 | 82 | 5 intruder | $1h_{11/2}$ drops | Sb $\to$ Pb |
| 7 | 126 | 6 intruder | $1i_{13/2}$ drops | Bi $\to$ U+ |

Rows 1--3 are pure HO closures.  Rows 4--7 are
intruder-created closures where the Borromean spin-orbit
coupling ($\mathcal{B}_3$ crossing number $= 3$) pushes the
highest-$j$ sub-level into the previous shell.

**Column structure (electron side).**

| Block | $\ell$ | Orbitals | Writhe modes | Visual |
|------:|-------:|---------:|-------------|--------|
| $s$ | 0 | 1 | Uniform (no oscillation) | Sphere |
| $p$ | 1 | 3 | 1-wavelength standing wave | Dumbbells |
| $d$ | 2 | 5 | 2-wavelength | Cloverleaf |
| $f$ | 3 | 7 | 3-wavelength | Complex |

Each column shows the electron trefoil's Fourier mode —
how the writhe excitation oscillates around the $(2,3)$
torus.

**Element card.**

Each element would display:

- **Symbol** and atomic number
- **Nuclear knot**: $p\,\mathcal{B}_3 \bowtie n\,\mathcal{B}_3$
  with $k_\alpha$ sub-links highlighted
- **Electron knot**: trefoil writhe diagram showing occupied
  shells and the current Fourier mode
- **$n_{\mathrm{pred}}$ vs $n_{\mathrm{obs}}$**: predicted
  and observed neutron number
- **Intruder indicator**: if the last nucleon is in an
  intruder sub-level, mark it

**Visualization specification (for implementation).**

The visualization should be an interactive HTML page
(`folio-assistant/simulators/knot_periodic_table.html`) with:

1. **Layout**: 7 rows (one per stability-pair interval), with
   row height proportional to the number of elements in that
   interval.  Columns grouped by $s$, $p$, $d$, $f$ blocks.

2. **Element tiles**: clickable tiles showing the element
   symbol, $p$, $n$, $k_\alpha$, and a small SVG of the
   nuclear Borromean structure.

3. **Nuclear side panel**: when an element is selected, show
   the full Borromean baryon composition:
   - Number of $\alpha$ clusters ($k_\alpha$)
   - Which HO level the last nucleon occupies
   - Whether it's an intruder sub-level
   - Stability pair membership ($\diamond$, $\star$)

4. **Electron side panel**: show the trefoil writhe diagram:
   - Current shell $n$ and sub-shell $\ell$
   - Occupied Fourier modes as standing waves on the trefoil
   - Visual: animated trefoil spinning around a Borromean
     anchor, with the current mode highlighted

5. **Controls**:
   - Toggle between standard and knot-centric layouts
   - Filter by stability pair, intruder status, $k_\alpha$
   - $q$ slider to show how the table changes with substrate
     parameter (at $q = 1$: all rows equal width, no
     intruders; at $q = 1.1097$: observed table)

6. **Knot notation**: use the visual conventions from
   [knot atom diagrams](#rem:knot-atom-diagrams):
   - Solid trefoil = forward-time fermion
   - Outlined trefoil = backward-time (antiparticle)
   - Circle = unknot (neutrino / neutron)
   - Interlocked circles = Hopf link
   - Borromean symbol = 3 interlocked rings (quark composite)

7. **Data source**: read from the knot-periodic table
   ([knot-periodic table](#rem:knot-periodic-table)) for
   $p$, $n$, $n_{\mathrm{pred}}$, $\Delta n$, $k_\alpha$,
   masses, and $B/A$.
