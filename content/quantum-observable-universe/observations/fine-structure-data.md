**Existing data sets.**

* **CODATA 2018** (NIST): $\alpha^{-1} \approx 137.035999084(21)$ (relative uncertainty $1.5 \times 10^{-10}$). Derived from electron $g - 2$ and tenth-order QED.
* **Cs-133 recoil** (Parker et al., 2018): $\alpha^{-1} \approx 137.035999046(27)$. Independent of $g - 2$.
* **Rb-87 recoil** (Morel et al., 2020): $\alpha^{-1} \approx 137.035999206(11)$. The most precise determination to date.

**Chern-Simons correction: :refterm[descent]{#descent} decomposition of the coupling.**

The bare coupling $q \cdot [9]_q \cdot [10]_q = 136.823$ captures the base holonomy of the electromagnetic endomorphism. The Chern-Simons invariants of the force-carrier torus knots provide the exceptional divisor correction:

| Force carrier      | CS invariant           | Value    |
| ------------------ | ---------------------- | -------- |
| $T_{2,9}$ (strong) | $\pi^2 \cdot 10/9$     | $10.966$ |
| $T_{3,5}$ (weak)   | $\pi^2 \cdot 16/15$    | $10.528$ |
| Sum                | $\pi^2 (10/9 + 16/15)$ | $21.494$ |

The correction enters as a geometric tower whose ratio carries the Gram-determinant factor $\kappa$, the $J^2$ self-dual damping of the Chern--Simons pairing:

$$
  \alpha^{-1}_{\mathrm{CS}}
  =
  \alpha^{-1}_{\mathrm{bare}} \Bigl(1 + \delta_{\mathrm{CS}} + \delta_{\mathrm{CS}}^2 \kappa + \delta_{\mathrm{CS}}^3 \kappa^2 + \cdots\Bigr)
  =
  \alpha^{-1}_{\mathrm{bare}} \Bigl(1 + \frac{\delta_{\mathrm{CS}}}{1 - \delta_{\mathrm{CS}}\kappa}\Bigr)
  \approx 137.0359351
$$

where $\delta_{\mathrm{CS}} = (\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})) \cdot ([2]_q/2) \cdot \hbar_q^2 / \alpha^{-1}_{\mathrm{bare}} \approx 0.0015506$ and $\kappa = \det G_{\mathrm{cl}} / \det G_q \approx 1.7216$ is the ratio of the classical to the $q$-deformed Gram determinant of that pairing.

The tower is geometric with ratio $\delta_{\mathrm{CS}}\kappa \approx 2.7 \times 10^{-3}$, so it sums in closed form: there is no truncation order, and the closed form is exact to all orders.

| Formula                            | $\alpha^{-1}$   | Discrepancy             |
| ---------------------------------- | --------------- | ----------------------- |
| Bare: $q \cdot [9]_q \cdot [10]_q$ | $136.8232089$   | $-1553\;\mathrm{ppm}$   |
| CS-corrected (exact resummation)   | $137.0359351$   | $-0.468\;\mathrm{ppm}$  |
| CODATA 2022                        | $137.035999177$ | —                       |

The residual $-0.468\;\mathrm{ppm}$ survives exact resummation and is therefore structural: no further orders remain to be added.

**Sensitivity to $q$.**

The prediction $\alpha^{-1}(q) = [9]_q [10]_q / q^{-1}$ depends steeply on $q$. Matching the CODATA central value requires $q \approx 1.11023 ± 0.00002$. We extract $q$ independently from two other observables:

* **Neutron-to-proton mass ratio**: $q \approx q_0$ (via the Skein mass formula).
* **Tritium half-life**: $q \approx 1.109$--$1.112$ (via the transfer matrix calculation).

The consistency window $q \in [1.109, 1.112]$ accommodates all three determinations.

**Running of $\alpha_{\mathrm{EM}}$ with energy.**

| Energy scale           | $\alpha^{-1}$ (experiment) | $q$ (inverted) |
| ---------------------- | -------------------------- | -------------- |
| $0$ (Thomson limit)    | $137.036$                  | $1.11023$      |
| $m_Z \approx 91.2$ GeV | $127.95 ± 0.02$          | $1.1003$       |
| $m_W \approx 80.4$ GeV | $\sim 128.0$               | $\sim 1.1005$  |

The running of $\alpha^{-1}$ from $137$ to $128$ corresponds to a $\sim 1\%$ decrease in $q$. The Reeb flow on the Bring's surface drives this running. At higher energies (shorter distances), the effective $q$ decreases toward the classical limit $q = 1$.

**Planned observations.**

* **FNAL muon $g - 2$** (Run 4+5): Tightens the $\alpha$ extraction. Tests whether the muon couples to the same $q$ as the electron, probing generation-dependent substrate coupling.
* **PSI muonium spectroscopy**: Directly measures $\alpha_{\mathrm{EM}}$ at the muonic scale. Sensitive to $q$-corrections depending on lepton generation (Reeb degree).
* **Electron EDM** (ACME III, JILA): Constrains CP-violating phases in the crossing energy decomposition. Tests whether the symmetric/antisymmetric split of the Skein algebra holds exactly.
