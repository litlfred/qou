Where the static appendix table freezes the periodic structure at
the observed substrate value, an interactive rendering lets a reader
watch the row and shell structure deform continuously as $q$ slides
from $1$ to $q_0$: the equal-width rows and absent magic
shells at $q = 1$ reorganize into the observed table with its
magic-receptive shells.

**Visualization specification (for implementation).**

The visualization should be an interactive HTML page
(`simulators/knot_periodic_table.html`).  Its feature
groups fall into three physical layers the static table cannot expose
side by side — the nuclear Borromean composition of each element, the
shell structure of its electrons (the level words $e_n$), and the way both respond to
the substrate parameter $q$ — so the specification below unfolds from
layout and tiles through the nuclear and electron panels to the $q$
control that ties them together:

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

4. **Electron side panel**: show the electron level word:
   - Current shell $n$ and sub-shell $\ell$
   - The level word $e_n = \sigma_0\sigma_1\sigma_0\sigma_2\cdots\sigma_n$ and its
     writhe $n + 2$
   - Visual: the closure of $e_n$, starting from the Hopf link at $n = 1$,
     linked to a Borromean anchor

5. **Controls**:
   - Toggle between standard and knot-centric layouts
   - Filter by stability pair, magic-receptive status, $k_\alpha$
   - $q$ slider to show how the table changes with substrate
     parameter (at $q = 1$: all rows equal width,
     no magic shells; at $q = q_0$: observed table)

6. **Knot notation**: use the visual conventions from
   [knot atom diagrams](#rem:knot-atom-diagrams):
   - Solid glyph = forward-time particle
   - Outlined glyph = backward-time (antiparticle)
   - Circle = unknot (neutrino)
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
   $\mathfrak{E}_{\mathrm{bind}} \propto \lambda_+^{-n}$.
