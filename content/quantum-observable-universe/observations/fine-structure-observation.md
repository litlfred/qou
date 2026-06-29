The electromagnetic coupling
([EM coupling projection](#prop:em-coupling-projection)) predicts
$\alpha_{\mathrm{EM}}$ as a function of the substrate parameter $q$
alone, with no free parameters.

**Bare formula (base holonomy):**

$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = 
  q \cdot [9]_q \cdot [10]_q
  = 136.823.
$$

**Chern-Simons corrected formula (:refterm[descent]{#descent} decomposition):**

$$
  \alpha_{\mathrm{EM}}^{-1}(q)
  = 
  \frac{q \cdot [9]_q \cdot [10]_q}{1 - \delta_{\mathrm{CS}}}
$$

where $\delta_{\mathrm{CS}} = (\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})) \cdot ([2]_q/2) \cdot \hbar_q^2 / (q \cdot [9]_q \cdot [10]_q)$ incorporates the Chern-Simons invariants of the two force-carrier torus knots.

The crossing numbers $9$ and $10$ are determined by the force-carrier
generators $T_{2,9}$ and $T_{3,5}$
([force identification](#rem:force-knot-identification)); the
$q$-integers are fixed by the Descartes substrate parameter.

**Numerical comparison with CODATA.**

See [Table 1](#tbl:fine-structure-observation-table1-data).

The Chern-Simons correction reduces the discrepancy by a factor of
$120$, from $0.155\%$ to $2.1\;\mathrm{ppm}$, with zero additional
parameters.  All ingredients — the bare coupling, the torus knot
Chern-Simons invariants, and $\hbar_q$ — are determined by $q$ alone.

**Inversion: $q$ from $\alpha_{\mathrm{EM}}$.**
Conversely, fixing $\alpha^{-1} \approx 137.036$ and solving for $q$
gives

$$
  q_{\mathrm{CODATA}} = 1.11023.
$$

This is consistent with the substrate parameter determined
independently from mass ratios
(mass predictions) and half-life
calculations ([half-life as $q$-probe](#rem:half-life-as-q-probe)),
providing a cross-check between the electromagnetic and strong
sectors.

**Sensitivity.**
The coupling is sensitive to $q$:

$$
  \frac{\partial \ln \alpha_{\mathrm{EM}}}{\partial \ln q}
  =  -1 - 
  \frac{9  q^9 [10]_q + 10  q^{10} [9]_q}
       {[9]_q [10]_q (q - q^{-1})}.
$$

At $q = q_0$ this evaluates to approximately $-20$: a $1\%$ shift
in $q$ produces a $\sim 20\%$ shift in $\alpha_{\mathrm{EM}}$.  The
tight agreement with experiment therefore constrains $q$ to a narrow
window around $q_0$.

**Comparison with other $q$-predictions.**

See [Table 2](#tbl:fine-structure-observation-table2-data).

The substrate parameter $q_0$ is overdetermined: three
independent classes of observables (electromagnetic coupling, mass
ratios, decay rates) all point to the same value.
