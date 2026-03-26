The following table shows representative elements spanning the
periodic table, comparing the continuous beta-stability prediction
$p^*(A)$ ([beta-stability](#prop:beta-stability)) with the
observed stable proton number, the neutron-to-proton ratio, and
the Diophantine error $\varepsilon = |p_{\mathrm{stab}} - p^*|$.

| Element | $A$ | $p$ | $n$ | $p^*(A)$ | $\varepsilon$ | $n/p$ | Notes |
|---------|----:|----:|----:|---------:|------:|------:|-------|
| Helium | 4 | 2 | 2 | 1.97 | 0.03 | 1.00 | $\diamond\star$ |
| Carbon | 12 | 6 | 6 | 5.88 | 0.12 | 1.00 | |
| Calcium | 40 | 20 | 20 | 19.24 | 0.76 | 1.00 | $\diamond\star$ |
| Iron | 56 | 26 | 30 | 25.68 | 0.32 | 1.15 | Peak $B/A$ |
| Tin | 120 | 50 | 70 | 49.23 | 0.77 | 1.40 | $\diamond$ |
| Lead | 208 | 82 | 126 | 81.35 | 0.65 | 1.54 | $\diamond\star$ |
| Uranium | 238 | 92 | 146 | 91.58 | 0.42 | 1.59 | |

**Observations.**

1. **Light nuclei** ($A \leq 40$): $n/p \approx 1$.  The Coulomb
   correction $c \cdot A^{2/3}$ is small; the curve lies near
   the diagonal $p = A/2$.

2. **Medium nuclei** ($40 < A \leq 120$): $n/p$ rises from
   $1.0$ to $1.4$.  The Coulomb term bends the curve below the
   diagonal, requiring extra neutrons.

3. **Heavy nuclei** ($A > 120$): $n/p \to 1.6$.  The $p^2$
   growth of the Coulomb penalty dominates; the curve flattens.

4. **Magic numbers** ($\diamond$, $\star$): Helium, calcium,
   tin, and lead have anomalously low Diophantine error *and*
   closed Skein shell structure.  The doubly-magic nuclei
   ($^4$He, $^{40}$Ca, $^{208}$Pb) have $\varepsilon < 0.8$
   combined with shell closure.

5. **Iron peak**: The maximum binding energy per nucleon
   $B/A \approx 8.79$ MeV occurs at $^{56}$Fe, where the
   competition between volume binding ($\propto A$) and
   Coulomb repulsion ($\propto p^2/A^{1/3}$) is optimally
   balanced.

The continuous curve $p^*(A)$ and the integer lattice points
$(p_{\mathrm{stab}}, n_{\mathrm{stab}})$ are illustrated in the
[valley of stability simulator](#sim:valley-stability).
