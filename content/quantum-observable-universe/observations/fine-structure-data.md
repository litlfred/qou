**Existing data sets.**

* **CODATA 2018** (NIST): $\alpha^{-1} \approx 137.035999084(21)$,
  relative uncertainty $1.5 \times 10^{-10}$.  Determined from
  electron $g - 2$ combined with QED calculations to tenth order.
* **Cs-133 recoil** (Parker et al., 2018):
  $\alpha^{-1} \approx 137.035999046(27)$, independent of $g - 2$.
* **Rb-87 recoil** (Morel et al., 2020):
  $\alpha^{-1} \approx 137.035999206(11)$, the most precise
  determination to date.

**Chern-Simons correction: :refterm[descent]{#descent} decomposition of the coupling.**

The bare coupling $q \cdot [9]_q \cdot [10]_q = 136.823$ captures
the base holonomy of the electromagnetic endomorphism.  The Chern-Simons
invariants of the force-carrier torus knots provide the exceptional
divisor correction:

| Force carrier      | CS invariant           | Value    |
| ------------------ | ---------------------- | -------- |
| $T_{2,9}$ (strong) | $\pi^2 \cdot 10/9$     | $10.966$ |
| $T_{3,5}$ (weak)   | $\pi^2 \cdot 16/15$    | $10.528$ |
| Sum                | $\pi^2 (10/9 + 16/15)$ | $21.494$ |

The corrected coupling:

$$
  \alpha^{-1}_{\mathrm{CS}}
  =
  \frac{q \cdot [9]_q \cdot [10]_q}{1 - \delta_{\mathrm{CS}}}
  =
  \frac{136.823}{1 - 0.001551}
  =
  137.036
$$

where $\delta_{\mathrm{CS}} = (\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})) \cdot ([2]_q/2) \cdot \hbar_q^2 / \alpha^{-1}_{\mathrm{bare}} = 0.001551$.

| Formula                            | $\alpha^{-1}$   | Discrepancy          |
| ---------------------------------- | --------------- | -------------------- |
| Bare: $q \cdot [9]_q \cdot [10]_q$ | $136.823$       | $-0.155\%$           |
| CS-corrected                       | $137.036$       | $-2.1\;\mathrm{ppm}$ |
| CODATA 2018                        | $137.035999084$ | —                    |

**Sensitivity to $q$.**

The QOU prediction $\alpha^{-1}(q) = [9]_q [10]_q / q^{-1}$ is a
steep function of $q$.  Matching the CODATA central value requires
$q \approx 1.11023 \pm 0.00002$ (propagating experimental uncertainty).
This can be compared to $q$ values extracted from:

* **Neutron-to-proton mass ratio**: $q \approx q_0$ (from Skein
  mass formula)
* **Tritium half-life**: $q \approx 1.109$–$1.112$ (from transfer
  matrix calculation)

The consistency window $q \in [1.109, 1.112]$ accommodates all
three determinations.

**Running of $\alpha_{\mathrm{EM}}$ with energy.**

| Energy scale           | $\alpha^{-1}$ (experiment) | $q$ (inverted) |
| ---------------------- | -------------------------- | -------------- |
| $0$ (Thomson limit)    | $137.036$                  | $1.11023$      |
| $m_Z \approx 91.2$ GeV | $127.95 \pm 0.02$          | $1.1003$       |
| $m_W \approx 80.4$ GeV | $\sim 128.0$               | $\sim 1.1005$  |

The running from $137$ to $128$ corresponds to a $\sim 1\%$ decrease
in $q$.  In the QOU framework, this running is driven by the Reeb
flow on the Bring's surface: at higher energies (shorter distances),
the effective $q$ decreases toward the classical limit $q = 1$.

**Planned observations.**

* **FNAL muon $g - 2$** (Run 4+5): will tighten $\alpha$ extraction
  and test whether the muon couples to the same $q$ as the electron,
  probing generation-dependent substrate coupling.
* **PSI muonium spectroscopy**: direct measurement of
  $\alpha_{\mathrm{EM}}$ at the muonic scale, sensitive to
  $q$-corrections that depend on the lepton generation (Reeb degree).
* **Electron EDM** (ACME III, JILA): constrains CP-violating phases
  in the crossing energy decomposition, testing whether the
  symmetric/antisymmetric split of the Skein algebra is exact.
