**Existing data sets.**

* **CODATA 2022** (NIST, current recommended): $\alpha^{-1} \approx 137.035999177(21)$ (relative uncertainty $1.5 \times 10^{-10}$). Derived from electron $g - 2$ and tenth-order QED. This is the value the comparison table below uses.
* **CODATA 2018** (NIST, superseded): $\alpha^{-1} \approx 137.035999084(21)$. Kept as the **comparison vintage** only: several superseded figures elsewhere in the corpus are recorded against it and stay legible that way. It is never the current value. The $2018 \to 2022$ shift is $9.3 \times 10^{-8}$, or $0.679\;\mathrm{ppb}$.
* **Cs-133 recoil** (Parker et al., 2018): $\alpha^{-1} \approx 137.035999046(27)$. Independent of $g - 2$.
* **Rb-87 recoil** (Morel et al., 2020): $\alpha^{-1} \approx 137.035999206(11)$. The most precise determination to date.

**Chern-Simons correction: :refterm[descent]{#descent} decomposition of the coupling.**

The bare coupling $q \cdot [9]_q \cdot [10]_q = 136.823$ captures the base holonomy of the electromagnetic endomorphism. The Chern-Simons invariants of the force-carrier torus knots provide the exceptional divisor correction:

| Force carrier      | CS invariant           | Value    |
| ------------------ | ---------------------- | -------- |
| $T_{2,9}$ (strong) | $\pi^2 \cdot 10/9$     | $10.966$ |
| $T_{3,5}$ (weak)   | $\pi^2 \cdot 16/15$    | $10.528$ |
| Sum                | $\pi^2 (10/9 + 16/15)$ | $21.494$ |

The correction enters as a geometric tower whose ratio carries the Gram-determinant factor $\kappa$, the $J^2$ self-dual damping of the Chern--Simons pairing $G_{\mathrm{CS}}$ (defined in [EM coupling Chern-Simons](#rem:em-coupling-chern-simons); see the disambiguation below for which matrix that is):

$$
  \alpha^{-1}_{\mathrm{CS}}
  =
  \alpha^{-1}_{\mathrm{bare}} \Bigl(1 + \delta_{\mathrm{CS}} + \delta_{\mathrm{CS}}^2 \kappa + \delta_{\mathrm{CS}}^3 \kappa^2 + \cdots\Bigr)
  =
  \alpha^{-1}_{\mathrm{bare}} \Bigl(1 + \frac{\delta_{\mathrm{CS}}}{1 - \delta_{\mathrm{CS}}\kappa}\Bigr)
  \approx 137.0359351
$$

where $\delta_{\mathrm{CS}} = (\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})) \cdot ([2]_q/2) \cdot \hbar_q^2 / \alpha^{-1}_{\mathrm{bare}} \approx 0.0015506$ and $\kappa = \det G^{\mathrm{cl}}_{\mathrm{CS}} / \det G^{q}_{\mathrm{CS}} \approx 1.7216$ is the ratio of the classical to the $q$-deformed Gram determinant **of the Chern--Simons pairing** ([Gram-determinant ratio](#def:cs-gram-determinant-ratio)). The structural closure of $\kappa$ is an open problem; the identification is unproved ([EM coupling Chern-Simons](#rem:em-coupling-chern-simons), [open problems](#rem:alpha-em-derivation-open-problems)).

**Distinction between the Chern–Simons pairing matrix $G_{\mathrm{CS}}$ and the Hecke Markov Gram matrix $G$.** To distinguish the Chern–Simons intersection pairing from the $6 \times 6$ Hecke Markov Gram matrix $G$ on $H_3(q)$, the Chern–Simons matrix is denoted throughout by $G_{\mathrm{CS}}$. $G_{\mathrm{CS}}$ is the $2 \times 2$ Chern--Simons pairing Gram of the force-carrier pair $(T_{2,9}, T_{3,5})$ on Bring's surface --- diagonal $\mathrm{CS}_i + \pi^2 s_i^2 / c_i^2$, off-diagonal $\pi^2 \ell^2 / (c_1 c_2)$, with the $q$-deformation replacing $m, n$ by $[m]_q, [n]_q$. It is **not** the $6 \times 6$ Markov--Gram matrix $G_{ij} = \mathrm{tr}_M(b_i b_j)$ of the $H_3(q)$ normal-form basis ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). At $q_0$:

| matrix | $\det$ at $q_0$ | carries the Markov parameter $z$? |
| ------ | --------------- | --------------------------------- |
| $G^{q}_{\mathrm{CS}}$ (this block) | $35.21703297433989011$ | no |
| $G^{\mathrm{cl}}_{\mathrm{CS}}$ (this block) | $60.630144110670241284$ | no |
| Markov--Gram, trace convention C (excised) | $-0.18920521914403668$ | yes |
| Markov--Gram, trace convention D (production) | $0$ exactly --- the form is **singular**, $G^{-1}$ does not exist | yes |

$G_{\mathrm{CS}}$ is built from $\pi$, the torus-knot data $(m_i, n_i)$ and the quantum integers $[2]_q, [3]_q, [5]_q, [9]_q$ alone; no Markov parameter $z$ enters it, and none enters $\hbar_q = 1 - q^{-1}$ either. **The $\alpha^{-1}$ figure above therefore does not sit downstream of the Markov--Gram determinant and is independent of the choice between trace conventions C and D.** At 60 digits: bare $136.82320885358258431$, $\delta_{\mathrm{CS}} = 0.0015506021328500969$, $\kappa = 1.721614201708788213$, resummed $\alpha^{-1} = 137.03593509397560466$, i.e. $-0.4676\;\mathrm{ppm}$ against CODATA 2022 --- matching every published digit in this block.

The tower is geometric with ratio $\delta_{\mathrm{CS}}\kappa \approx 2.7 \times 10^{-3}$, so it sums in closed form: there is no truncation order, and the closed form is exact to all orders.

| Formula                            | $\alpha^{-1}$   | Discrepancy             |
| ---------------------------------- | --------------- | ----------------------- |
| Bare: $q \cdot [9]_q \cdot [10]_q$ | $136.8232089$   | $-1553\;\mathrm{ppm}$   |
| CS-corrected (exact resummation)   | $137.0359351$   | $-0.468\;\mathrm{ppm}$  |
| CODATA 2022                        | $137.035999177$ | —                       |

The residual $-0.468\;\mathrm{ppm}$ survives exact resummation and is therefore structural: no further orders remain to be added.

**Sensitivity to $q$.**

The prediction $\alpha^{-1}(q) = [9]_q [10]_q / q^{-1}$ depends steeply on $q$. Matching the CODATA central value requires $q \approx 1.11023 \pm 0.00002$. Extract $q$ independently from two other observables:

* **Neutron-to-proton mass ratio**: $q \approx q_0$ (via the Skein mass formula).
* **Tritium half-life**: $q \approx 1.109$--$1.112$ (via the transfer matrix calculation).

The consistency window $q \in [1.109, 1.112]$ accommodates all three determinations.

**Running of $\alpha_{\mathrm{EM}}$ with energy.**

| Energy scale           | $\alpha^{-1}$ (experiment) | $q$ (inverted) |
| ---------------------- | -------------------------- | -------------- |
| $0$ (Thomson limit)    | $137.036$                  | $1.11023$      |
| $m_Z \approx 91.2$ GeV | $127.95 \pm 0.02$          | $1.1003$       |
| $m_W \approx 80.4$ GeV | $\sim 128.0$               | $\sim 1.1005$  |

The running of $\alpha^{-1}$ from $137$ to $128$ corresponds to a $\sim 1\%$ decrease in $q$. The Reeb flow on the Bring's surface drives this running. At higher energies (shorter distances), the effective $q$ decreases toward the classical limit $q = 1$.

**Planned observations.**

* **FNAL muon $g - 2$** (Run 4+5): Tightens the $\alpha$ extraction. Tests whether the muon couples to the same $q$ as the electron, probing generation-dependent substrate coupling.
* **PSI muonium spectroscopy**: Directly measures $\alpha_{\mathrm{EM}}$ at the muonic scale. Sensitive to $q$-corrections depending on lepton generation (Reeb degree).
* **Electron EDM** (ACME III, JILA): Constrains CP-violating phases in the crossing energy decomposition. Tests whether the symmetric/antisymmetric split of the Skein algebra holds exactly.
