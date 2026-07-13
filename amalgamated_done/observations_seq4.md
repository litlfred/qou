<!-- FILE_START: mass-predictions-intro.md -->
We apply the mass formula, calibrated by $q_0$, to the hadron and nuclear spectrum. We compare these values against CODATA and PDG.

We examine the lattice geometry. The stability cubic bounds the stability surface. We tabulate neutron-number predictions for $p \leq 103$. We record prediction shifts under local perturbations of $q$.

We analyze mass ratios. A full three-channel Hecke algebra calculation covers the first ten elements. We compare mass contributions against Feynman-diagram amplitudes. We detail the channel-counting reduction from four photon channels to three Wedderburn invariants. 

We address neutron-proton splitting. We derive this mass splitting from the single crossing-change distinguishing the nucleons. We establish the Borromean link topology. A pair-skein mass formula provides the recursion for heavier states. We isolate the $u$--$d$ flavor split. We derive the deuteron binding energy.

We conclude with terminal-resolution results and the $W$-boson anomaly. We analyze electroweak boson masses, establishing the boson-mass result used to match weak-vertex amplitudes with $\beta$-decay half-lives.
<!-- FILE_END: mass-predictions-intro.md -->

<!-- FILE_START: stability-cubic-plot.md -->
At $q = q_0$, the stability cubic ([Diophantine valley](#rem:diophantine-valley)) parametrises the valley of stability:

$$
  t^3 =  2p(1 + ct^2),
  \qquad c = 0.01497, \quad A = t^3
$$

See [Table](#tbl:stability-cubic-plot-table-data).

The predicted neutron number $N_{\mathrm{pred}}$ minimizes the convex quadratic $E(p, A)$ ([integer stability](#prop:integer-stability)). The discrepancy $\Delta N = |N_{\mathrm{pred}} - N_{\mathrm{obs}}|$ is zero up to iron, and at most $2$ everywhere.

The Coulomb term $a_C \cdot p^2/A^{1/3}$ penalizes proton-rich nuclei. Driven entirely by $q_0$, the neutron excess grows from $0\%$ at hydrogen to $59\%$ at uranium.
<!-- FILE_END: stability-cubic-plot.md -->

<!-- FILE_START: neutron-prediction-comparison.md -->
**Proposition.**
At $q = q_0$, the beta-stability formula ([beta-stability](#prop:beta-stability)) predicts a stable neutron number $n_{\mathrm{pred}}(p)$:

$$
  p^*(A) =  \frac{A}{2 + c \cdot A^{2/3}},
  \qquad c = \frac{a_C}{2a_A} = 0.01497.
$$

We compare this against observed isotopes across 103 elements:

See [Table](#tbl:neutron-prediction-comparison-table-data).

The mean discrepancy is $\overline{|\Delta n|} = 1.7$. The maximum discrepancy $|\Delta n| = 8$ occurs at $p = 102$ and $p = 103$.

**Formal witness.**
The Lean theorem `stable_neutron_max_error` verifies $|\Delta n| \leq 8$.
<!-- FILE_END: neutron-prediction-comparison.md -->

<!-- FILE_START: neutron-prediction-comparison-interpretation.md -->
The beta-stability formula yields a smooth prediction. Discrepancies $|\Delta n| \geq 2$ cluster at:

1. **Stability pair closures** ($n = 20, 28, 50, 82, 126$). The formula passes smoothly through these points.
2. **Transuranic elements** ($p > 92$). Observed isotopes possess half-lives too short to pinpoint stability.

The smooth formula derives the neutron excess from $q$. The residuals encode shell structure. Characterizing this structure remains the goal of the [elliptic stability conjecture](#rem:elliptic-stability-locus).
<!-- FILE_END: neutron-prediction-comparison-interpretation.md -->

<!-- FILE_START: q-stability-ranges.md -->
The beta-stability formula ([integer stability](#prop:integer-stability)) yields $n_{\mathrm{pred}}(p)$. For each element $p$, $n_{\mathrm{pred}}$ remains constant over a range $[q_{\min}, q_{\max}]$.

**$q$-Stability ranges for light elements.**

See [Table](#tbl:q-stability-ranges-table-data).

**Observations.**

1. **Helium** ($p = 2$). $n_{\mathrm{pred}} = 2$ is stable over $q \in [1.001, 1.828]$.
2. **Light elements** ($p \leq 6$). The window extends from $q = 1$ to above $q_0$.
3. **Medium elements** ($p = 10$--$26$). The window narrows to $\Delta q \approx 0.02$--$0.10$.
4. **Heavy elements** ($p > 50$). The window shrinks to $\Delta q < 0.01$.

**Physical interpretation.**

The narrowing reflects the Coulomb penalty. For heavy nuclei, the balance between Coulomb repulsion and isospin asymmetry is sensitive to $q$. Crossing asymmetry ($q > 1$) determines the bulk of the periodic table. Fine structure depends precisely on $q$.
<!-- FILE_END: q-stability-ranges.md -->

<!-- FILE_START: mass-ratio-predictions.md -->
The [mass identity](#def:mass-identity) expresses inertial mass as the norm of a nonabelian multiplicative integral over a surface bounding the vortex filament. In the Descartes universe ($\chi(\mathcal{S}) = -6$), bundle topology constrains vortex configurations and determines the mass spectrum. Evaluating the mass identity at successive levels of the brane tower ([recursive brane tower](#def:recursive-brane-tower)) yields mass ratio predictions.
<!-- FILE_END: mass-ratio-predictions.md -->

<!-- FILE_START: atom-mass-full-hecke.md -->
The semi-empirical mass formula $M_q$ uses the 2$\times$2 **standard** irrep of $H_3(q)$. This discards the symmetric and alternating channels, missing the dominant contribution for multi-nucleon systems.

We compute the atomic mass for $Z = 1$--$10$ using the full regular representation of $H_3(q)$.

## Three-channel decomposition

See [Table: Three-channel $H_3(q)$ decomposition](#tbl:atom-mass-full-hecke-table-data).

The full Markov trace decomposes as:

$$
  \mathrm{tr}_M^{\mathrm{full}}
  = \hat y_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}}
  + \hat y_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}}
  + \hat y_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}},
$$

where $\hat y_\lambda$ are the $q$-deformed Jones--Markov weights. At $q \approx 1.11$, $\hat y_{\mathrm{sym}} \approx 0.42$, $\hat y_{\mathrm{std}} \approx 0.56$, and $\hat y_{\mathrm{alt}} \approx 0.02$. The classical Wedderburn--Artin values are heavily deformed.

## Mass decomposition

The mass integrand splits into:

1. **Horizontal**: $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$.
2. **Vertical**: $\mathfrak{m}_{\mathrm{vert}} = \mathrm{tr}_M^{\mathrm{full}}(\Phi_{\mathrm{mass}})$.
3. **Mixed**: $\mathfrak{m}_{\mathrm{mix}} = \mathfrak{E}_{\mathrm{cross}} \cdot (q - 1)^2$.

## Results for $Z = 1$--$10$

We evaluate the traces at $q = 111/100$.

See [Table](#tbl:atom-mass-full-hecke-table-data).

## Key observations

1. **Standard channel suppression.** The standard trace shrinks rapidly with $A$. The symmetric and alternating channels remain $O(1)$.
2. **Alternating channel sign flips.** Under canonical $q$-deformed weights, the alternating block is suppressed. The apparent sign variation was a classical-weighting artifact.
3. **${}^{14}\mathrm{N}$ cancellation.** The near-cancellation between symmetric and alternating traces depends entirely on classical weighting. It vanishes under canonical $q$-deformed weights.
4. **Binding energy deviations.** The semi-empirical formula undercounts the doubly-magic shell closure at ${}^4\mathrm{He}$.

**Witness**: `atom-mass-full-hecke.witness.json`. We lack independent witnesses for high-$A$ traces.
<!-- FILE_END: atom-mass-full-hecke.md -->
