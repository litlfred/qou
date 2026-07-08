<!-- FILE_START: intro-gravity-spacetime-lqg-comparison.md -->
Loop quantum gravity (LQG), the ADM canonical decomposition, and Ashtekar's connection-variable formulation are the three established programmes nearest to the QOU construction on the spacetime side. This section compares the QOU substrate against those programmes. We identify where each carries non-trivial categorical structure, where the QOU substrate supplies a structural extension, and where the assumptions diverge.
<!-- FILE_END: intro-gravity-spacetime-lqg-comparison.md -->

<!-- FILE_START: lqg-adm-ashtekar-comparison.md -->
**Remark (QOU as the categorical resolution of canonical quantum-gravity programmes).**
The contact-geometric machinery of the QOU framework aligns structurally with the canonical quantum-gravity programmes (ADM, Ashtekar, Smolin–Rovelli LQG). The ADM 3+1 foliation reappears as the contact affine chart $H = \ker \varTheta_A$ (the spatial slice), with the Reeb flow $\phi_t = \exp(t\xi)$ in the role of lapse-and-shift. The substantive differences are not which structures appear but where they live. We treat them as native categorical data, whereas canonical LQG bolts them onto a continuous background and recovers algebraic data as a regularisation patch.

## Dictionary

| Canonical programme | QOU realisation |
|---|---|
| **ADM 3+1 foliation** | contact affine chart $H = \ker \varTheta_A$ as spatial slice; Reeb flow $\phi_t = \exp(t\xi)$ as canonical lapse-and-shift |
| **Wheeler–DeWitt** | Variational minimum $\delta \mathfrak{S}_q / \delta \nabla = 0 \Rightarrow \star_q F_\nabla = F_\nabla$ on adelic states |
| **Ashtekar connection** | Categorical Dirac $\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \iota_\xi \nabla$; $\hbar_q \iota_\xi \nabla$ plays the role of $\gamma K$ |
| **Barbero–Immirzi parameter** | Substrate parameter $q_0 \approx 1.11$, derived from the substrate Reeb flow |
| **Horizon entropy** | Archimedean limit of the $q$-dimension partition function |
| **Horizon Hilbert subspaces** | Wedderburn blocks $M_{d_\lambda}(\mathbb{Q}(q))$ |
| **Densitised triad** | Bring-curve coordinates under the $S_5$ action |
| **Spin networks** | Knot operators as Reeb-$U(1)$ Wilson loops |
| **Spin foams** | Frobenius-pairing cobordism amplitudes via $\mathrm{tr}_M(\mathcal{B}_K)$ |
| **Kodama state** | $S_0$ saddle of the Faddeev WKB of $\Phi_q$ |
| **Reality conditions** | Adelic product selects the unique real archimedean realisation |
| **Relational QM** | Adelic product formula $\prod_v \lVert \psi \rVert_v = 1$ |
| **Area operator** | Archimedean limit of the $\mathrm{SU}_q(2)$ Casimir on each boundary rep |
| **Volume operator** | Bulk period face of the non-abelian Stokes |
| **Holonomy–flux algebra** | Non-abelian-Stokes holonomy plus Frobenius/Markov flux |
| **Diffeomorphism constraint** | Built in; $\mathrm{tr}_M(\mathcal{B}_K)$ is an ambient-isotopy invariant |
| **Hamiltonian constraint** | Categorical Dirac generator $\mathfrak{D}_\nabla$ |
| **Coherent states** | Archimedean limit of the categorical state |
| **LQC bounce & CCC** | Big Bang = $q\to1^+$; heat death = $q\to\infty$ |
| **Discrete geometry** | Algebraic discreteness (finite Wedderburn blocks plus finite GS-filtration slices) |

## Three structural advantages

The dictionary tightens around three points where QOU avoids known obstructions of the canonical programmes:

1. **No "problem of time".** ADM presupposes a continuous time coordinate. We have no inbuilt time. Macroscopic time emerges as the Reeb flow, driven by the $q$-anomaly $d_q^2 \neq 0$. Transition amplitudes between algebraic states are the Frobenius pairings, not Wheeler–DeWitt evolution operators.
2. **No Barbero–Immirzi fudge factor.** The continuous Ashtekar connection uses $\gamma$ as a free parameter to match black-hole entropy. The corresponding parameter in QOU is the substrate $q_0$, derived from the categorical Reeb flow and locked by the algebraic structure of Bring's surface.
3. **Native self-duality.** Ashtekar's original formulation made the Hamiltonian constraint polynomial via complex self-duality, but required intractable "reality conditions". QOU recovers exact self-duality $\star_q F_\nabla = F_\nabla$ directly. The adelic product and continuous deformation produce the real Lorentzian archimedean projection naturally.

## Limitations of the claim

We do not claim that QOU derives LQG from first principles. Canonical loop quantum gravity is a self-contained research programme. Every structural ingredient that the canonical programmes introduce as a separate assumption appears in QOU as a derived output of the categorical substrate plus Bring-curve constraint. The relevant QOU-side outputs depend on the OS reflection-positivity conjecture and the surreal mass-gap bound. Granting both, the comparison yields a structural equivalence at the level of the Hamiltonian-constraint reduction.
<!-- FILE_END: lqg-adm-ashtekar-comparison.md -->

<!-- FILE_START: lqg-entropy-qdim-partition-pole.md -->
The LQG horizon-entropy state count admits a QOU recasting. The analytic Laplace count becomes an algebraic partition-function pole.

**Conjecture.** Let the horizon be punctured by knot operators, each carrying an $\mathrm{SU}_q(2)$ boundary representation. Define the per-puncture $q$-dimension partition function

$$
  Z_1(s) \;=\; \sum_{j \in \frac12\mathbb{N}} [2j+1]_q \,
  e^{-s\,\tau\!\bigl(C_q(V_j)\bigr)},
$$

where $\tau(C_q(V_j))$ is the archimedean image of the $\mathrm{SU}_q(2)$ Casimir on $V_j$. Then:

1. **Entropy = pole.** The horizon-state generating function $\sum_{n\ge0} Z_1(s)^n = (1 - Z_1(s))^{-1}$ has a pole at the critical value $s_\star$ with $Z_1(s_\star) = 1$, and the entropy density is $s_\star$.
2. **Gauss constraint = trace closure.** The closed-horizon $U(1)$ Gauss constraint $\sum_p m_p = 0$ is the trace-closure condition. The closed-link evaluation is a morphism $\mathbf{1} \to \mathbf{1}$.
3. **Immirzi from criticality.** Matching to the Bekenstein–Hawking law $S = A/4\ell_p^2$ fixes the Barbero–Immirzi parameter as $\gamma = s_\star/2\pi$.

**Scope.** This is an algebraic recasting of an established analytic result, not a from-scratch derivation of black-hole entropy. The leading $\gamma$ is the $q \to 1$ value and is $q_0$-independent. True $q_0$-dependence enters only through the $q$-deformed degeneracy $[2j+1]_{q_0}$.
<!-- FILE_END: lqg-entropy-qdim-partition-pole.md -->

<!-- FILE_START: outro-gravity-spacetime.md -->
This closes the gravity-and-spacetime chapter. We position the QOU substrate against the canonical quantum-gravity programmes. Each carries non-trivial categorical structure, but the QOU substrate supplies the Reeb derivation and the substrate-parametrised differential to pin the classical-limit obstruction structurally. The geometric-Langlands chapter formalises the resulting categorical backbone.
<!-- FILE_END: outro-gravity-spacetime.md -->

