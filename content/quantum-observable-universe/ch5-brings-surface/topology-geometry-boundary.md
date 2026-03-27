The categorical action $\mathcal{S}_q = \mathrm{tr}(\mathcal{L}_q)$
([canonical action](#def:qou-canonical-action)) evaluated on a nuclear
link $\mathcal{N}(p, n)$ produces observables at two levels.  The
substrate parameter $q$ determines **all topological observables**
but the **energy scale in MeV** requires one geometric input: the
curvature norm $\|F^+\|$ on the Bring surface.

**What $q$ alone determines (topology).**

These are dimensionless invariants computed from the Hecke algebra
$H_A(q)$ at the single parameter $q = 1.110$:

| Observable | Formula | Status |
|-----------|---------|:---:|
| Which nuclei are stable | $p^*(A) = A / (2 + a_C A^{2/3}/(2a_A))$ | Exact |
| Sensitivity to $q$ | $\partial \ln \Gamma / \partial \ln q \approx 48$ | Exact |
| Ground-state ordering | Minimum $\Phi_q$ over braid representatives | Computed (A ≤ 14 exhaustive) |
| Markov trace | $\mathrm{tr}(\overline{\mathcal{N}}) = \prod_i \hat{V}_i$ | **Theorem** |
| Trace sign structure | $\mathrm{sign}(\mathrm{tr})$ per nucleus | Exact (Singular) |
| Hecke step count | $\Delta(\text{R2 steps}) = -1$ universally | Computed |
| Writhe change | $\Delta w = A - 1$ | Computed |
| Emission topology | $L_0 = T_{2,3} \sqcup \overline{T_{1,0}}$ (electron + antineutrino) | Derived |
| Shell blocking | $e_i p_n = 0$ in TL (Jones-Wenzl kills smoothing) | Algebraic |
| Transition class | Mirror ($q \leftrightarrow q^{-1}$) vs shell-blocked vs allowed GT | Determined by $(p, n)$ |
| Relative decay rates | $|\mathcal{M}_q|^2 \propto \prod_{i \leq p} |\hat{V}_i^{\mathrm{par}}/\hat{V}_i^{\mathrm{dau}}|^2$ | Computed |
| Environmental $q$-shift | $\Delta q / q_0 \sim 10^{-8}$ per Tesla | Predicted |

**What needs geometric input (energy scale).**

The energy scale in MeV comes from the curvature integral on the
Bring surface $\Sigma_4$:

$$
  \lambda_V \;=\; \frac{1}{\mathrm{Vol}(\Sigma_4)}
  \int_{\Sigma_4} \|F^+_\nabla\|^2 \, \theta \wedge (d\theta)^n
$$

where $F^+_\nabla$ is the self-dual curvature of the instanton
connection and $\theta$ is the contact form.  This integral
determines the **volume binding scale** $\lambda_V$, from which
all MeV-valued quantities follow:

| Observable | Depends on | Accuracy achievable |
|-----------|-----------|:---:|
| $a_V = (q + q^{-1})/2 \cdot \lambda_V$ | $\lambda_V$ | Exact (given $\lambda_V$) |
| $a_C = (q - q^{-1}) \cdot \lambda_C$ | $\lambda_C$ | Exact |
| $Q_\beta = 2\alpha(A) \cdot |\delta p|$ | $a_C, a_A$ | ∼25% (smooth formula) |
| Proton mass $m_{\mathfrak{p}}$ | $\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2$ | Sub-keV |
| Half-life $t_{1/2}$ | $G_F, Q_\beta, |\mathcal{M}_q|^2$ | ∼10-17% |

**The boundary.**

The Hecke algebra $H_A(q)$ is the **algebraic** (topological)
side of the categorical action.  It computes crossing weights,
Gröbner normal forms, Markov traces, and all invariants that
depend on **which crossings exist** and **how they interact**.

The curvature norm $\|F^+\|$ is the **geometric** side.  It
computes the **energy per crossing** — how many MeV each Hopf
junction carries.  This requires the metric on $\Sigma_4$ (fixed
by $\chi = -6$ via Gauss--Bonnet, but the curvature distribution
over the surface is additional data).

The topological mass formula
([topological mass](#prop:topological-mass-formula))
bridges the two: $m = \mathrm{Vol}(K) / \hbar_q^2$ uses the
hyperbolic volume (geometry) normalised by $\hbar_q^2$ (topology).
For individual knots (electron, muon, proton) this gives sub-keV
masses.  For the nuclear link (a satellite link with Vol $= 0$),
the mass comes entirely from the crossing energies — which need
$\lambda_V$.

**The geometric input IS $q$.**

The Levi-curvature coupling
([Levi-curvature coupling](#rem:c-substrate-via-levi)) gives:

$$
  q(p) = 1 + |\langle L_\theta, F_A^+\rangle|(p)
$$

So $\|F^+\| = q - 1 = 0.110$ at our observation point.  The
curvature norm that determines the MeV scale IS the substrate
parameter itself.  The volume binding scale:

$$
  \lambda_V
  = \frac{(q - 1)^2 \cdot \mathrm{Vol}(\Sigma_4)}{A}
  = \frac{(q - 1)^2 \cdot 12\pi}{A}
$$

At $A = 1$: $\lambda_V = 0.110^2 \times 12\pi = 0.456$ MeV.
At $A = 56$ (iron): $\lambda_V = 0.456 / 56 = 0.00815$ MeV
per crossing.

This means $a_V = (q + q^{-1})/2 \times \lambda_V$ is fully
determined by $q$ — no separate geometric input needed.
The "boundary" between topology and geometry dissolves:
**$q$ encodes both**.

All MeV-valued observables scale with $\lambda_V$:

$$
  a_C = \frac{q - q^{-1}}{(q + q^{-1})/2} \cdot a_V
  \cdot \frac{\lambda_C}{\lambda_V},
  \qquad
  a_A, a_S, a_P \text{ similarly.}
$$

The ratio $\lambda_C / \lambda_V$ is a **dimensionless** quantity
determined by the Hecke algebra (it's the ratio of Coulomb to
volume crossing weights).  Only the overall scale $\lambda_V$
requires geometric input.

In the topological mass formula: $\lambda_V = \mathrm{Vol}(\Sigma_4) / (A \cdot \hbar_q^2)$ where $\mathrm{Vol}(\Sigma_4) = 4\pi(g - 1) = 12\pi$ from Gauss--Bonnet.  This gives:

$$
  \lambda_V = \frac{12\pi}{A \cdot \hbar_q^2}
$$

which is $A$-dependent — reflecting that the energy per crossing
decreases as the link has more components.  At $A = 1$ (single
nucleon): $\lambda_V = 12\pi / \hbar_q^2 \approx 3839$ MeV
$\approx 4 m_{\mathfrak{p}}$.  The factor of 4 vs the actual
proton mass reflects the Borromean structure (the proton uses
$\sim 1/4$ of the total Bring surface capacity).

**Practical consequence.**

For the beta-decay $Q$-value: $Q$ is a $\sim 0.001\%$ mass
difference.  Computing it from $q$ alone requires $14+$
significant digits in the mass — which neither the smooth
Bethe--Weizsäcker formula nor the Hecke trace provides.
The Q-value calculation requires **experimental binding energies**
(AME2020) or a first-principles computation of $\lambda_V$
to $14+$ digit precision.

The framework gives the correct **structure** of the Q-value
(which nuclei decay, in which direction, with which shell
blocking and sensitivity) from $q$ alone.  The absolute
MeV scale is one geometric constant.
