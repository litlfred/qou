<!-- FILE_START: mass-predictions-intro.md -->
We apply the mass formula, calibrated by $q_0$ from the lepton sector,
to the hadron and nuclear spectrum and compare with CODATA and PDG values.
We first examine the lattice geometry. The stability cubic marks which
$(Z, N)$ coordinates lie on the stability surface. We tabulate
neutron-number predictions element by element for $p \leq 103$. We also
record how these predictions shift under local perturbations of the
substrate parameter $q$.

We next analyze mass ratios. We extract the dimensionless quotients
predicted by the mass identity and compare them directly with experimental
values. A full three-channel Hecke algebra calculation covers the first
ten elements. We compare framework mass contributions term-by-term against
corresponding Feynman-diagram amplitudes. We detail the channel-counting
reduction from four photon channels to three Wedderburn invariants, and
we classify the analyzed isotopes by data source.

The middle of this section addresses neutron-proton splitting and its
consequences. We derive this mass splitting from the single crossing-change
distinguishing the two nucleons. We establish the Borromean link topology
that supports the formula. A pair-skein mass formula provides the recursion
used for the deuteron and heavier states. We isolate the $u$--$d$ flavor split
from the dressed kinematics and record the numerical values at $q_0$.
We close the two-nucleon material by deriving the deuteron binding energy.

The section concludes with terminal-resolution results and the $W$-boson
anomaly. We prove the resolution-theoretic identity anchoring the closure.
Finally, we analyze the electroweak boson masses. This sets up the boson-mass
result used later to match weak-vertex amplitudes with $\beta$-decay
half-lives.

_(draft.)_
<!-- FILE_END: mass-predictions-intro.md -->

<!-- FILE_START: stability-cubic-plot.md -->
At $q = q_0$, the stability cubic ([Diophantine valley](#rem:diophantine-valley))

$$
  t^3 =  2p(1 + ct^2),
  \qquad c = 0.01497, \quad A = t^3
$$

parametrises the valley of stability. The integer lattice points $(p, n) \in \mathbb{N}^2$ on this curve represent the stable nuclei.

See [Table](#tbl:stability-cubic-plot-table-data).

The predicted neutron number $N_{\mathrm{pred}}$ minimizes the convex quadratic $E(p, A)$ ([integer stability](#prop:integer-stability)) at each $p$. The discrepancy $\Delta N = |N_{\mathrm{pred}} - N_{\mathrm{obs}}|$ is zero up to iron, and at most $2$ across the periodic table.

The curve $p = t^3/(2 + 2ct^2)$ bends away from the diagonal $n = p$ as $A$ increases. The Coulomb term $a_C \cdot p^2/A^{1/3}$ penalizes proton-rich nuclei, demanding additional neutrons. Driven entirely by $q_0$, the neutron excess grows from $0\%$ at hydrogen ($p=1, n=0$) to $59\%$ at uranium ($p=92, n=146$).

See the [valley of stability simulator](#sim:valley-stability).
<!-- FILE_END: stability-cubic-plot.md -->

<!-- FILE_START: neutron-prediction-comparison.md -->
**Proposition.**
At $q = q_0$, the beta-stability formula
([beta-stability](#prop:beta-stability))

$$
  p^*(A) =  \frac{A}{2 + c \cdot A^{2/3}},
  \qquad c = \frac{a_C}{2a_A} = 0.01497,
$$

predicts a stable neutron number $n_{\mathrm{pred}}(p)$ for each proton
number $p$. We compare this prediction against the observed most stable
isotope (AME2020/NUBASE2020) across all 103 elements:

See [Table](#tbl:neutron-prediction-comparison-table-data).

The mean discrepancy is $\overline{|\Delta n|} = 1.7$ neutrons across all
103 elements. The maximum discrepancy $|\Delta n| = 8$ occurs at $p = 102$
(nobelium) and $p = 103$ (lawrencium). Both are transuranic elements whose
most stable isotopes are poorly determined.

**Formal witness.**
The predicted and observed neutron numbers for all 103 elements reside in
the Lean witness data `integer-stability.lean`. The theorem
`stable_neutron_max_error` formally verifies that $|\Delta n| \leq 8$
for every element.
<!-- FILE_END: neutron-prediction-comparison.md -->

<!-- FILE_START: neutron-prediction-comparison-interpretation.md -->
The beta-stability formula yields the smooth, shell-free prediction from
the stability cubic ([Diophantine valley](#rem:diophantine-valley)).
Discrepancies $|\Delta n| \geq 2$ concentrate at:

1. **Stability pair closures** ($n = 20, 28, 50, 82, 126$). The observed
   neutron count clusters at these values, while the smooth formula passes
   through them. This generates the $|\Delta n| = 4$ residuals at calcium
   ($n_{\mathrm{obs}} = 20$, $n_{\mathrm{pred}} = 24$) and barium
   ($n_{\mathrm{obs}} = 82$, $n_{\mathrm{pred}} = 78$).
2. **Transuranic elements** ($p > 92$). The observed isotopes possess
   half-lives too short to pinpoint the most stable $n$ precisely.

The smooth formula derives the overarching trend (neutron excess growing
from $0\%$ to $60\%$) entirely from the single parameter $q$. The residuals
encode the shell structure (stability pairs). Characterizing this structure
remains the open goal of the
[elliptic stability conjecture](#rem:elliptic-stability-locus).
<!-- FILE_END: neutron-prediction-comparison-interpretation.md -->

<!-- FILE_START: q-stability-ranges.md -->
The beta-stability formula ([integer stability](#prop:integer-stability)) predicts the stable neutron number $n_{\mathrm{pred}}(p)$. This is an integer-valued function of the substrate parameter $q$. For each element $p$, $n_{\mathrm{pred}}$ remains constant over a range $[q_{\min}, q_{\max}]$. The prediction is robust against local variations in $q$.

**$q$-Stability ranges for light elements.**

See [Table](#tbl:q-stability-ranges-table-data).

**Observations.**

1. **Helium** ($p = 2$). The value $n_{\mathrm{pred}} = 2$ is stable over $q \in [1.001, 1.828]$, yielding a width of $0.83$. The $\alpha$ particle is robust against nearly any $q > 1$.
2. **Light elements** ($p \leq 6$). The $q$-stability window extends from $q = 1$ to well above $q = q_0$. These nuclei exist for any $q > 1$.
3. **Medium elements** ($p = 10$--$26$). The window narrows to $\Delta q \approx 0.02$--$0.10$. The prediction becomes sensitive to the precise value of $q$.
4. **Heavy elements** ($p > 50$). The window shrinks to $\Delta q < 0.01$. A $1\%$ shift in $q$ alters the predicted stable isotope.

**Physical interpretation.**

The narrowing of the $q$-stability window with increasing $p$ reflects the growing Coulomb penalty. For heavy nuclei, the balance between Coulomb repulsion $a_C \cdot p^2/A^{1/3}$ and isospin asymmetry $a_A \cdot (n - p)^2/A$ is delicate. Small changes in $q$ tip this balance. Light nuclei carry a negligible Coulomb term and remain insensitive to $q$.

Consequently, the existence of crossing asymmetry ($q > 1$) determines the bulk of the periodic table, rather than the specific value $q_0$. The fine structure—identifying the stable isotope for each heavy element—depends on the precise value of $q$.
<!-- FILE_END: q-stability-ranges.md -->

<!-- FILE_START: mass-ratio-predictions.md -->
The [mass identity](#def:mass-identity) expresses inertial mass as the
norm of a nonabelian multiplicative integral of the connection-curvature
pair $(\nabla_A q, L \wedge F^+)$ over a surface bounding the vortex
filament. In the Descartes universe with $\chi(\mathcal{S}) = -6$, bundle
topology constrains the allowed vortex configurations and determines the
mass spectrum. The electron-muon mass ratio, for example, stems from the
ratio of vertical degrees in the Reeb decomposition
([Descartes leptons](#rem:archimedean-leptons)). Evaluating the mass
identity at successive levels of the brane tower
([recursive brane tower](#def:recursive-brane-tower)) yields theoretical
predictions for lepton and hadron mass ratios.
<!-- FILE_END: mass-ratio-predictions.md -->

<!-- FILE_START: atom-mass-full-hecke.md -->
The simple CODATA-recombination mass formula $M_q = Z\mathfrak{m}_{\mathfrak{p}} + N\mathfrak{m}_{\mathfrak{n}} + Z\mathfrak{m}_e - (Z+N)\,B/A$ uses only the 2$\times$2 **standard** irrep of $H_3(q)$ for the transfer matrix chain. Per-atom knot identifications are collected in the recursive knot$\to$particle dictionary ([recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas)). This projects the Hecke element onto the $(2,1)$-seminormal representation and discards the symmetric (trivial) and alternating (sign) channels. For multi-nucleon systems, this projection throws away the dominant contribution. The standard channel trace $\mathrm{tr}_{\mathrm{std}}$ decays exponentially with $A$, while $\mathrm{tr}_{\mathrm{sym}}$ and $\mathrm{tr}_{\mathrm{alt}}$ remain $O(1)$.

We compute the atomic mass for $Z = 1$ through $Z = 10$ using the full regular representation of $H_3(q)$. We track all three irreducible channels independently.

## Three-channel decomposition

See [Table: Three-channel $H_3(q)$ decomposition](#tbl:atom-mass-full-hecke-table-data).

The full Markov trace decomposes over the three Wedderburn blocks of $H_3(q)$ as

$$
  \mathrm{tr}_M^{\mathrm{full}}
  = \hat y_{\mathrm{sym}}\,\mathrm{tr}_{\mathrm{sym}}
  + \hat y_{\mathrm{std}}\,\mathrm{tr}_{\mathrm{std}}
  + \hat y_{\mathrm{alt}}\,\mathrm{tr}_{\mathrm{alt}},
$$

where $\hat y_\lambda = y_\lambda(q)\,d_\lambda$ are the $q$-deformed Jones--Markov weights. These weights are the Wenzl Schur principal specialisation of the canonical $y_\lambda$ ([Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge)), normalised by $\sum_\lambda \hat y_\lambda = 1$. The production Markov-trace uses these weights throughout. The classical Wedderburn--Artin values $d_\lambda^2 / |S_3| = \{\tfrac16, \tfrac23, \tfrac16\}$ are only their $q \to 1$ limit. At the substrate scale, this deformation is large. From the cached weights, $\hat y_{\mathrm{sym}} \approx 0.42$, $\hat y_{\mathrm{std}} \approx 0.56$, and $\hat y_{\mathrm{alt}} \approx 0.02$. The symmetric weight rises by roughly $2.5\times$ and the alternating weight falls by roughly $7\times$ relative to the classical equal-weighting.

For a single nucleon ($A = 1$), this three-channel sum equals the full $H_3(q)$ Markov trace. For $A > 1$, it acts as a three-channel $H_3$ projection of the multi-nucleon state, not the full $H_{3A}(q)$ Markov trace. The two coincide only at $A = 1$. The columns below model this projection rather than the canonical $H_{3A}$ trace.

## Mass decomposition (fibre / horizontal / mixed)

For each nucleus, the mass integrand ([Hecke mass element](#def:hecke-mass-element)) splits along the charge--mass duality ([charge--mass duality](#rem:hecke-charge-mass-duality)):

1. **Horizontal** (crossing energy):
   $\mathfrak{E}_{\mathrm{cross}} = n_+ q - n_- q^{-1}$,
   where $n_+$ counts proton--proton pairs and $n_-$ counts neutron--neutron pairs.

2. **Vertical / fibre** (Markov trace mass):
   $\mathfrak{m}_{\mathrm{vert}} = \mathrm{tr}_M^{\mathrm{full}}(\Phi_{\mathrm{mass}})$.

3. **Mixed** (vertex operator coupling):
   $\mathfrak{m}_{\mathrm{mix}} = \mathfrak{E}_{\mathrm{cross}} \cdot (q - 1)^2$.

## Results for $Z = 1$--$10$

We evaluate the per-channel traces $\mathrm{tr}_{\mathrm{sym}}, \mathrm{tr}_{\mathrm{std}}, \mathrm{tr}_{\mathrm{alt}}$ below at $q = 111/100$. This is a convenient rational near the substrate $q_0 \approx 1.10998$, allowing exact arithmetic. Binding energy comes from the Skein binding Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) with $q$-derived Bethe--Weizsäcker coefficients.

See [Table](#tbl:atom-mass-full-hecke-table-data).

**Note (weighting convention).** The $\mathrm{tr}_{\mathrm{full}}$ column of the table uses the canonical $q$-deformed weights $\hat y_\lambda$ above (witness `atom-mass-full-hecke.witness.json`). The $q \to 1$ classical weighting gives materially different values (for ${}^4\mathrm{He}$, $\mathrm{tr}_{\mathrm{full}} = 0.516$ q-deformed vs $0.422$ classical). The $B/A$ and $\Delta$ columns are independent of this weighting. They derive from the Skein binding Lagrangian (Bethe--Weizsäcker form), not from $\mathrm{tr}_{\mathrm{full}}$. The per-channel traces are inherited from the published table. An independent witness for the high-$A$ $\chi^\lambda$ remains a separate open item, as the Gröbner--Shirshov reducer is infeasible past the light nuclei.

## Key observations

1. **Standard channel suppression.** The standard (2$\times$2) trace shrinks rapidly with $A$ for odd-$A$ and neutron-excess nuclei: from $1.0$ at $A = 1$ to $\sim 10^{-7}$ at $A = 19$ (${}^{19}\mathrm{F}$). For even-even nuclei (${}^{16}\mathrm{O}$, ${}^{20}\mathrm{Ne}$), the standard trace remains $O(10^{-1})$ due to the symmetric ground-state ordering. In all cases, the symmetric and alternating channels remain $O(1)$. The full Wedderburn trace recovers the physically correct mass scale.

2. **Alternating channel sign flips.** The alternating trace changes sign according to the parity of the total crossing count (the exponent of $(-q^{-1})$ in the alternating eigenvalue product). This parity depends on the ground-state ordering rather than directly on even/odd $A$. Under classical equal weighting, this sign variation propagates to $\mathrm{tr}_{\mathrm{full}}$, producing negative entries at ${}^7\mathrm{Li}$, ${}^{11}\mathrm{B}$, and ${}^{19}\mathrm{F}$. Under canonical $q$-deformed weights, the alternating block is suppressed $\sim 7\times$. Consequently, $\mathrm{tr}_{\mathrm{full}}$ stays positive and $O(0.2$--$1)$ across the table. The apparent sign variation was a classical-weighting artifact.

3. **${}^{14}\mathrm{N}$ cancellation.** For the symmetric nucleus $Z = N = 7$, the symmetric and alternating traces nearly cancel: $\mathrm{tr}_{\mathrm{sym}} \approx -\mathrm{tr}_{\mathrm{alt}}$, giving $\mathrm{tr}_{\mathrm{full}} \approx 0$ under classical weights. The equal proton--neutron composition produces equal-and-opposite contributions in the trivial and sign representations. This near-cancellation depends entirely on the classical weighting $\hat y_{\mathrm{sym}} = \hat y_{\mathrm{alt}}$. Under the canonical $q$-deformed weights, the symmetric block outweighs the alternating one by $\sim 18\times$, giving $\mathrm{tr}_{\mathrm{full}} = 0.512$ at ${}^{14}\mathrm{N}$. The near-cancellation vanishes.

4. **Binding energy deviations.** The Skein Lagrangian with $q$-derived Bethe--Weizsäcker coefficients reproduces $B/A$ to within $\sim 1$ MeV of AME2020 for most atoms. The largest deviation occurs at ${}^4\mathrm{He}$ ($+1.1$ MeV/$A$), where the semi-empirical formula undercounts the doubly-magic shell closure.

**Witness**: `atom-mass-full-hecke.witness.json` (producer `computations/atom_mass_full_hecke_qdeformed.py`). We apply the canonical $q$-deformed weights $\hat y_\lambda$ (from [Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge), `y-lambda-at-q0.witness.json`) to the inherited per-atom channel traces. The high-$A$ $\chi^\lambda$ are not yet independently witnessed (GS reducer infeasible past light nuclei).
<!-- FILE_END: atom-mass-full-hecke.md -->

