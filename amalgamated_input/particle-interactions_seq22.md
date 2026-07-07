<!-- FILE_START: intro-beta-stability-closure.md -->
Beta stability—the condition that an isotope avoids $\beta^-$ and $\beta^+$ emission—is the categorical closure condition preserved by the substrate flow. This section identifies the substrate-level beta-stable subset. We use the deuteron as a first-principles anchor.

We begin with the deuteron calculation. We then extend to the symbolic and operator-valued mass towers, recording closure properties under the substrate flow. We link the closure rule to the Mark-up rule. Finally, we supply the categorical version of the empirical valley of stability, which the next section refines into a Diophantine valley.
<!-- FILE_END: intro-beta-stability-closure.md -->

<!-- FILE_START: energy-scale-planck.md -->
The energy scale $E_0$ is **derived** from CAL-1 ($m_e$) and CAL-2 ($q_0$) alone. It consumes no β-decay calibration. It holds a natural interpretation in terms of the $q$-deformed Planck scale: it represents the energy of one Hecke reduction step. This is the physical cost of resolving a single $\sigma_i^2 \to h\sigma_i + \mathbf{1}$.

## Derived form

$$
  \boxed{
  E_0
  =
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \frac{m_e}{(q-1)^2} \cdot \frac{q-1}{q}
  =
  \frac{m_e}{q(q-1)}
  }
$$

At $q_0 \approx 1.110$, $E_0 \approx 4.186$ MeV.

**Input-error propagation**
The input errors are CAL-1 $\sigma_{m_e}/m_e \approx 0.3$ ppb and CAL-2 $\sigma_{q_0}/q_0 \approx 1.22$ ppb. The $q_0$ amplification factor is $\partial \ln E_0 / \partial \ln q_0 = (1 - 2q_0)/(q_0 - 1) \approx -11.09$ at $q_0 = 1.110$.

$$
  \sigma_{E_0} / E_0
  \approx
  \sqrt{(0.3\,\mathrm{ppb})^2 + (11.09 \times 1.22\,\mathrm{ppb})^2}
  \approx 13.5\,\mathrm{ppb}.
$$

This yields $\sigma_{E_0} \approx 5.7 \times 10^{-8}$ MeV. This error is entirely negligible at the keV scale of β-decay observables.

## Calibration-cross-check

A historical "calibrated $E_0$" definition used CAL-3 ($\mathfrak{Q}_\beta$) as input via $E_0^{(\text{cal})} = \mathfrak{Q}_\beta^{\text{CODATA}} / \lvert\Delta(\mathrm{net})\rvert \approx 4.155$ MeV. **This form is no longer used** in the prediction pipeline. It consumes CAL-3 as input rather than treating it as a prediction ([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)).

The 0.74% gap between the derived $E_0 \approx 4.186$ MeV and the cross-check $\approx 4.155$ MeV stems from the brane-tower truncation residual at $N=0$. This is identical to the +0.17% / +1.31 keV residual in the $\mathfrak{Q}_\beta$ prediction. By the structural bound ([`per-braid-mass-tower.md`](#prop:per-braid-mass-tower)), this residual is $O(\hbar_q^2/(1 - \hbar_q^2)) \approx 1\%$ at $N=0$.

## Physical meaning

$$
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \underbrace{m_e \cdot c_q^2}_{\text{electron rest energy}}
  \times
  \underbrace{\hbar_q}_{\text{action per Planck tick}}
  =
  \frac{m_e \cdot c_q^2}{t_P}
$$

This quantity is the **electron's rest energy per Planck time**. It serves as the natural energy quantum for a single interaction step in a universe where:
- the lightest charged particle has mass $m_e$,
- the speed of information is $c_q = 1/(q-1)$,
- one Planck time is $t_P = 1/\hbar_q \approx 10.1$ Reeb operations.

Each Hecke reduction step $\sigma_i^2 \to h\sigma_i + \mathbf{1}$ corresponds to one Planck tick of interaction. The double crossing resolves into a weighted single crossing (energy cost $h = q - q^{-1}$ in Skein units) plus an identity strand (photon release). The physical energy cost of this step is $E_0$.

## Calibration by free neutron decay

The free neutron decay $n \to p + e^- + \bar\nu_e$ provides the simplest hadronic process exercising a single Hecke step. It involves one crossing change $\mathfrak{d} \to \mathfrak{u}$ inside one nucleon, free of nuclear environment corrections. The Q-value $\mathfrak{Q}_\beta = 0.782$ MeV is the energy released by this crossing change. Dividing by the dimensionless Hecke NF difference $\lvert\Delta\mathrm{net}\rvert \approx 0.188$ gives $E_0 = \mathfrak{Q}_\beta / \lvert\Delta\mathrm{net}\rvert \approx 4.179$ MeV.

This procedure parallels measuring the speed of light by timing the simplest electromagnetic process. One clean measurement sets the scale, and every other scale follows.

## Calibration inputs in Planck units

Using the three $q$-constants $c_q, \hbar_q, t_P$ (all determined by $q_0$), the categorical three-calibration inputs ([three-calibration discipline](#prop:three-calibration-discipline)) become:

| Input | $H^k$ degree | What it fixes | In $q$-Planck units |
|-------|:-----------:|--------------|---------------------|
| $m_e$ | $H^0$ | The mass unit | $E_0/(c_q^2 \hbar_q)$ (the size) |
| $m_\mu/m_e$ | $H^1$ | $q_0$ | The shape (dimensionless) |
| $\mathfrak{Q}_\beta(n)$ | $H^2$ | The $\beta$-decay scale | $E_0$ in MeV |

Once $q_0$ is fixed, $c_q$, $\hbar_q$, $t_P$, and $G_q$ are determined. The mass scale $E_0$ then sets the correspondence between the $q$-Planck system and SI units. The $1\%$ residual between $E_0$ and $m_e c_q^2 \hbar_q$ represents the brane tower contribution. This is the difference between the single-level and full-tower mass.
<!-- FILE_END: energy-scale-planck.md -->

<!-- FILE_START: skein-binding-lagrangian.md -->
**Definition.**
Let $L = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a multi-nucleon Hopf link with $Z$ protons, $N$ neutrons, and $A = Z + N$. The **Skein binding Lagrangian** is the categorical action $\mathfrak{S}_q$ ([canonical action](#prop:qou-canonical-action)) evaluated on $L$:
$$
  \mathcal{L}_{\mathrm{bind}}[L]
  = 
  \mathcal{L}_{\mathrm{vol}}
  - \mathcal{L}_{\mathrm{surf}}
  - \mathcal{L}_{\mathrm{Coul}}
  - \mathcal{L}_{\mathrm{Pauli}}
  + \mathcal{L}_{\mathrm{pair}}.
$$
Each term arises from the Skein polynomial structure of $L$:

1. **Volume binding.** Each nearest-neighbour nucleon--nucleon Hopf junction contributes a binding energy proportional to the average Skein weight. There are roughly $A$ such junctions, yielding
   $$
     \mathcal{L}_{\mathrm{vol}}
     =  \frac{q + q^{-1}}{2} \cdot \lambda_V \cdot A
   $$
   where $\lambda_V$ is the per-junction energy scale.

2. **Surface correction.** Nucleons on the boundary of the link have fewer Hopf junctions. The boundary count scales as $A^{2/3}$:
   $$
     \mathcal{L}_{\mathrm{surf}}
     =  \frac{q + q^{-1}}{2} \cdot \lambda_S \cdot A^{2/3}.
   $$

3. **Coulomb repulsion.** Each proton--proton Hopf crossing takes the positive-crossing coefficient $q$ instead of the baseline $(q + q^{-1})/2$, producing a repulsive excess $\delta = \tfrac{1}{2}(q - q^{-1})$ per pair. The $\binom{p}{2}$ pairs are distributed over a link of radius $A^{1/3}$:
   $$
     \mathcal{L}_{\mathrm{Coul}}
     =  (q - q^{-1}) \cdot \lambda_C
     \cdot \frac{p(p-1)}{A^{1/3}}.
   $$

4. **Pauli asymmetry.** The [hadron definition](#def:hadron) uses the antisymmetric product $\mathrm{Sym}^n(-)$ for fermionic constituents. When $N \neq Z$, the species asymmetry costs energy from the exclusion constraint:
   $$
     \mathcal{L}_{\mathrm{Pauli}}
     =  \lambda_A \cdot \frac{(N - Z)^2}{4A}.
   $$

5. **Pairing.** Two identical nucleons can form a closed Hopf loop, contributing a pairing energy $\pm \lambda_P / A^{1/2}$ (positive for even--even, negative for odd--odd).
<!-- FILE_END: skein-binding-lagrangian.md -->

<!-- FILE_START: skein-binding-lagrangian-derivation.md -->
The [Skein binding Lagrangian](#def:skein-binding-lagrangian) is the categorical action $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ ([canonical action](#prop:qou-canonical-action)) evaluated on the field configuration $\psi = Z\mathfrak{p} \oplus N\mathfrak{n}$.

The [categorical Lagrangian](#def:categorical-lagrangian) $\mathcal{L}_q = \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla\psi$ decomposes via the Frobenius--Hopf structure into gravity, gauge, and matter sectors. When the state $\psi$ is a multi-nucleon Hopf link, the [Skein crossing asymmetry](#rem:skein-crossing-asymmetry) further splits the gauge sector by crossing chirality, producing the nuclear binding terms.

**1. Notation and classical limits.**
The Bethe--Weizsäcker coefficients are related to the Skein scales by:
$$
  a_V = \tfrac{1}{2}(q + q^{-1}) \cdot \lambda_V,
  \qquad
  a_C = (q - q^{-1}) \cdot \lambda_C,
  \qquad
  a_S = \tfrac{1}{2}(q + q^{-1}) \cdot \lambda_S.
$$
At $q = q_0$: $a_V \approx 15.56$ MeV, $a_C = (q - q^{-1}) \times 3.334 \approx 0.697$ MeV, $a_S \approx 17.23$ MeV, $a_A \approx 23.29$ MeV.

The Coulomb coefficient $a_C$ vanishes at $q = 1$ (no crossing asymmetry, no electromagnetic repulsion) and grows with $q$. The strong binding $a_V$ is nearly $q$-independent. The ratio
$$
  \frac{a_C}{a_V}
  =  \frac{q - q^{-1}}{q + q^{-1}}
  \cdot \frac{\lambda_C}{\lambda_V}
  =  \tanh(\ln q) \cdot \frac{\lambda_C}{\lambda_V}
$$
controls the balance between the strong and electromagnetic interactions.

**2. Derivation from the canonical action.**
The five terms arise from the three sectors of $\mathfrak{S}_q$ ([canonical action](#prop:qou-canonical-action)):

| Canonical sector | Evaluation on $L$ | Nuclear term |
|-----------------|-------------------|--------------|
| Gauge: $\int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$ | Hopf junction curvature, bulk | $\mathcal{L}_{\mathrm{vol}}$ |
| Gauge: same, boundary | Surface deficit in linking number | $\mathcal{L}_{\mathrm{surf}}$ |
| Gauge: $q$-weighting of $\wedge_q$ on $\mathfrak{p}$--$\mathfrak{p}$ crossings | Crossing asymmetry $q$ vs $q^{-1}$ | $\mathcal{L}_{\mathrm{Coul}}$ |
| Matter: $\int_A(\psi^* \cdot \mathcal{D}_\nabla\psi)$ | Fermionic exclusion cost | $\mathcal{L}_{\mathrm{Pauli}}$ |
| Matter: same, even--even pairing | Closed Hopf loops | $\mathcal{L}_{\mathrm{pair}}$ |

The gravity sector $\mathrm{tr}(q \cdot R_{\int})$ contributes a constant background that does not depend on $(p, n)$ and drops out of the beta-stability variation. The $q$-deformed wedge product $\wedge_q$ in the gauge sector automatically distinguishes same-chirality crossings (proton--proton, coefficient $q$) from mixed crossings (coefficient $(q + q^{-1})/2$), producing Coulomb repulsion directly from the geometry. The [mass identity](#def:mass-identity) then evaluates $\|\mathrm{tr}(\cdots)\|$ to give the nuclear mass.
<!-- FILE_END: skein-binding-lagrangian-derivation.md -->

<!-- FILE_START: beta-stability.md -->
The stable neutron number $n^*(p)$ for each element is determined by extremizing the Skein binding Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) over $n$ at fixed $p$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$. For a multi-nucleon Hopf link $L = Z\mathfrak{p} \oplus N\mathfrak{n}$ with $A = Z + N$, the beta-stable configuration satisfies $\partial \mathcal{L}_{\mathrm{bind}} / \partial n = 0$. This gives the beta-stability line:

$$
  p^*(A)
  = 
  \frac{A}{2 + a_C  A^{2/3} / (2a_A)}
$$

where $a_C = (q - q^{-1}) \cdot \lambda_C$ is the Coulomb coefficient from the crossing asymmetry, and $a_A$ is the Pauli asymmetry coefficient.

Equivalently, for a given $p$, the stable mass number is the fixed point of:

$$
  A^*(p) = p \left(2 + \frac{a_C}{2a_A} {A^*}^{2/3}\right)
$$

and $n^*(p) = A^*(p) - p$.

<!-- FILE_END: beta-stability.md -->

<!-- FILE_START: beta-stability-interpretation.md -->
**Derivation.**
At fixed $A$, beta decay converts $\mathfrak{n} \to \mathfrak{p}$ (or vice versa) while preserving $A$. We minimize the mass $M(p, A) = p \cdot m_{\mathfrak{p}} + (A-p) \cdot m_{\mathfrak{n}} - \mathcal{L}_{\mathrm{bind}}(p, A-p)$ by setting $\partial M / \partial p \big|_A = 0$:

$$
  (m_{\mathfrak{p}} - m_{\mathfrak{n}})
  + \frac{a_C  (2p - 1)}{A^{1/3}}
  - \frac{a_A  (A - 2p)}{A}
  = 0.
$$

Solving for $p$ (dropping the $-1$ and the small mass-difference correction):

$$
  a_A  \frac{A - 2p}{A}
  = a_C  \frac{2p}{A^{1/3}},
  \qquad
  p = \frac{A}{2 + a_C  A^{2/3} / (2a_A)}.
$$

**Verification.**
At $q = q_0$, with $a_C = (q - q^{-1}) \times 3.334 \approx 0.697$ MeV and $a_A \approx 23.29$ MeV, the formula reproduces the observed stable neutron numbers across the periodic table. The mean error is $|\Delta n| \approx 1.4$ neutrons (see [knot-periodic table](#prose:knot-periodic-table)).

**Limiting behaviour.**

| Regime | $q$ | $a_C$ | $n^*/p$ | Physics |
|--------|-----|-------|---------|---------|
| Classical | $q \to 1$ | $0$ | $1.00$ | No Coulomb; all nuclei symmetric |
| Our universe | $q = q_0$ | $0.70$ | $1.0$--$1.6$ | Valley of stability |
| Deep quantum | $q \to \infty$ | $\to \infty$ | $\to \infty$ | Coulomb overwhelms; no heavy nuclei |

The entire nuclear chart --- dictating which isotope is stable for each element --- follows from the single parameter $q$.
<!-- FILE_END: beta-stability-interpretation.md -->

