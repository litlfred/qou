<!-- FILE_START: intro-pair-production-knot-operators.md -->
Particle creation resolves at the categorical level as a Breit–Wheeler pair production. Two incoming photonic knot states ($0_1$ exceptional divisors) collide. The Frobenius Gram matrix on the categorical state space selects an emergent particle-antiparticle pair. 

We formalise the kinematics through the $Q$-value transition. We specialise to Breit-Wheeler kinematics ($\gamma\gamma \to e^+ e^-$) and quark-antiquark production. We formulate the knot-operator selection mechanism via the Frobenius Gram matrix. The mass spectrum construction resolves any residual ambiguity.
<!-- FILE_END: intro-pair-production-knot-operators.md -->

<!-- FILE_START: q-value-transition.md -->
We define the $Q$-value of a nuclear transition directly from the categorical action. This $q$-deformed transition energy replaces classical energy conservation.

**Definition (mass difference, primary).**
For a $\beta^-$ decay $\mathcal{N}(Z,N) \to \mathcal{N}(Z{+}1,N{-}1) + e^- + \bar{\nu}_e$, the $Q$-value is the mass difference of neutral atoms:

$$
  Q = M(Z, N) - M(Z{+}1, N{-}1),
$$

where $M(Z, N) = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e - B(Z, N)$ is the neutral atomic mass. The term $B(Z, N)$ is the BW binding energy at Hecke level $k$.
<!-- FILE_END: q-value-transition.md -->

<!-- FILE_START: q-value-transition-properties.md -->
We develop the $Q$-value of a nuclear transition. We analyse its precision behaviour, crossing-level decomposition, $q$-anomaly, and the non-conservation of $q$-momentum. The $q$-anomaly breaks classical energy conservation.

This definition is consistent with mass accuracy. If $|\Delta M/M| \approx 0.002\%$, then $Q$-values for transitions with $Q \gg \Delta M$ inherit the same precision. For transitions with small $Q$ (e.g. ${}^3\mathrm{H} \to {}^3\mathrm{He}$, $Q = 18.6$ keV), catastrophic cancellation amplifies the mass error: $\delta Q/Q \approx (M/Q) \times (\delta M/M)$.

At $k = 11$: $Q(n \to {}^1\mathrm{H}) = 0.782$ MeV ($0.00\%$), $Q({}^3\mathrm{H} \to {}^3\mathrm{He}) = 0.01823$ MeV ($-2.1\%$).

## Crossing-level decomposition

The parent normal form $\mathcal{N}(p,n)$ and daughter normal form $\mathcal{N}(p+1, n-1)$ differ at exactly $|\delta p|$ crossings. These are the quarks of the converting nucleon. At each changed crossing:

$$
  \Delta \mathfrak{E}_\times
  = 
  \mathfrak{E}_\times^{(\epsilon_{\mathrm{par}})}(q)
  - \mathfrak{E}_\times^{(\epsilon_{\mathrm{dau}})}(q).
$$

For a $\mathfrak{d} \to \mathfrak{u}$ change ($\sigma_k^{-1} \to \sigma_k$), we have $\Delta \mathfrak{E}_\times = q - q^{-1}$. The $Q$-value is:

$$
  Q
  = 
  \sum_{\text{changed crossings}} \Delta \mathfrak{E}_\times
  -  \mathfrak{S}_q(e).
$$

The unknot has trivial action. We drop $\mathfrak{S}_q(\nu^{\sigma}) = 0$.

## Classical limit and the $q$-anomaly

**Warning.** We do not assume classical energy conservation.

In classical physics, conservation of energy defines the $Q$-value:

$$
  Q_{\mathrm{classical}}
  = 
  T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}
  \stackrel{?}{=}
  M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e.
$$

This equality uses $E_{\mathrm{before}} = E_{\mathrm{after}}$. In the $q$-deformed framework, this conservation law fails because the $q$-differential does not satisfy $d_q^2 = 0$:

$$
  d_q f(x) =  \frac{f(qx) - f(x)}{(q-1)x}.
$$

$$
  d_q(f \cdot g) =  (d_q f) \cdot g +  f(qx) \cdot (d_q g).
$$

The $q$-Leibniz rule has a shift $f(qx)$ rather than $f(x)$. The $q$-differential of a product is not the sum of differentials. Squaring gives:

$$
  d_q^2  \neq  0 \quad \text{for } q \neq 1.
$$

**Corollary:** The total $q$-energy of the products need not equal the total $q$-energy of the parent. We define the $q$-anomaly:

$$
  \delta_q
   := 
  Q
  - 
  (T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}).
$$

This anomaly is a genuine physical effect of the $q$-deformation. It does not vanish in general.

## Structure of the $q$-anomaly

The $q$-anomaly arises from the non-commutativity of the Iwahori--Hecke algebra. The Skein crossing change converts one quark. The re-reduction to Gröbner--Shirshov normal form introduces R2 moves $T^2 = (q - q^{-1})T + 1$. Each R2 move shifts the local $q$-environment:

$$
  q_{\mathrm{eff}} \mapsto q_{\mathrm{eff}} + \Delta q,
$$

where $\Delta q \propto \hbar_q^2 = (1 - q^{-1})^2$.

The self-deformation produces a net shift:

$$
  \Delta q_{\mathrm{eff}}
  = 
  \frac{A - 1}{A^2} \cdot \hbar_q^2.
$$

This shift modifies $Q$ at second order:

$$
  Q
  = 
  \underbrace{\Delta \mathfrak{S}_q - \mathfrak{S}_q(e)}_{\text{leading (crossing change)}}
  + 
  \underbrace{\frac{\partial \mathfrak{S}_q}{\partial q} \cdot \Delta q_{\mathrm{eff}}}_{\delta_q \text{ (q-anomaly)}}.
$$

**At $q = 1$:** $\delta_q = 0$ and $Q \to Q_{\mathrm{classical}}$. Classical conservation is restored.

**At the substrate parameter $q$:** $\delta_q \neq 0$. For tritium ($A = 3$), we have $\Delta q_{\mathrm{eff}} = 2/9 \cdot \hbar_q^2 \approx 0.0022$. This gives a correction $\delta_q / Q \sim 5\%$. This correction brings the tritium half-life prediction from 13 yr to 12.4 yr (observed 12.32 yr).

## $Q$ is not conserved

The $q$-anomaly $\delta_q$ implies that $Q$ is not the sum of kinetic energies. The $q$-deformation of the vacuum absorbs the missing energy. The effective substrate parameter shifts from $q$ to $q + \Delta q_{\mathrm{eff}}$.

This is the $q$-deformed quantum anomaly. The full categorical action $\mathfrak{S}_q$ of the entire system is the conserved quantity:

$$
  \mathfrak{S}_q(\mathrm{par})
  = 
  \mathfrak{S}_{q + \Delta q}(\mathrm{dau})
  + 
  \mathfrak{S}_q(e)
  + 
  \mathfrak{S}_q(\nu^{\sigma})
  + 
  \text{kinetic terms}.
$$

We evaluate the daughter at the shifted $q$. This is the $q$-analogue of energy conservation.

## Limits

| $q$ | Regime | $Q$ | $\delta_q$ |
|-----|--------|:---:|:---:|
| $q = 1$ | Classical | $0$ | $0$ |
| the substrate $q$ | Our universe | $\mathcal{Q}_{\exp} + \delta_q$ | $\neq 0$ |
| $q \to \infty$ | Deep-quantum | $\to \infty$ | $\to \infty$ |

## $q$-Momentum

The $q$-momentum satisfies a similar non-conservation. Classically:

$$
  \vec{p}_{\mathrm{par}} = \vec{p}_{\mathrm{dau}} + \vec{p}_e + \vec{p}_{\nu^{\sigma}}.
$$

In the $q$-deformed case, the Iwahori--Hecke algebra non-commutativity implies:

$$
  p_q(\mathrm{par})
  = 
  p_q(\mathrm{dau}) + p_q(e) + p_q(\nu^{\sigma})
  + 
  \delta p_q,
$$

where $\delta p_q \propto \hbar_q$ is a $q$-anomaly in momentum. This is the braid-group analogue of the quantum anomaly in gauge theories.
<!-- FILE_END: q-value-transition-properties.md -->

<!-- FILE_START: breit-wheeler-pair-production.md -->
**Definition (Breit--Wheeler pair production).**

The Breit--Wheeler process models categorical pair production, $\gamma\gamma \to e^- e^+$. The fusion of two photons into an electron--positron pair corresponds to an identity in the Iwahori--Hecke algebra $H_3(q)$:

$$
  \gamma_1 \cdot \gamma_2
  = 
  \mathrm{NF}(e^-) + \mathrm{NF}(e^+)
  +  \text{binding energy}.
$$

Braid words represent the photon, electron, and positron:

$$
  \gamma = \sigma_0, \qquad
  e^- = \sigma_0\sigma_1\sigma_0  \text{ (trefoil)}, \qquad
  e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}  \text{ (mirror trefoil)}.
$$

**Archimedean specialisation.** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The underlying categorical identities hold over an abstract coefficient ring. We specialise only their archimedean realisation.
<!-- FILE_END: breit-wheeler-pair-production.md -->

<!-- FILE_START: breit-wheeler-pair-production-derivation.md -->
**Derivation (Breit--Wheeler categorical pair production).**

We derive the Breit--Wheeler categorical pair production. We define the bare and colored photon. We compute the normal-form reduction of the pair product. We evaluate linear and circular polarization limits. We identify the four-term extension.

#### Bare photon pair

Two identical bare photons yield the product $\gamma\gamma = \sigma_0^2$. We apply the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$:

$$
  \mathrm{NF}(\gamma\gamma)
  =  (q - q^{-1})\sigma_0 + \mathbf{1}.
$$

The net valuation is $\mathrm{net}(\gamma\gamma) = 1 + (q - q^{-1}) \approx 1.209$. This corresponds to a bare pair energy $E_{\mathrm{pair}} \approx 1.006$ MeV. This falls $1.6\%$ short of the physical $2m_e = 1.022$ MeV threshold.

#### Colored photon

Matching the $2m_e$ threshold requires color dressing. The photon incorporates an admixture of the Hecke generators $\sigma_0$ and $\sigma_1$. A color parameter weights each generator:

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1,
$$

where $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$. The generator $\sigma_0$ acts on the $(\sigma, r)$ plane. The generator $\sigma_1$ acts on the $(r, g)$ plane. The product $\sigma_0\sigma_1 = L_+$ provides Hopf-link dressing. 

This derivation treats the 3-term specialization $\varphi_{01} = 0$.

#### Normal-form pair product

We expand the product $\gamma_1 \cdot \gamma_2$ for two 3-term colored photons $\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$ and $\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$. We reduce via $\sigma_i^2 = h\sigma_i + \mathbf{1}$, where $h = q - q^{-1}$.

Collecting by basis element yields:

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  \underbrace{(1 + \varphi_0\psi_0 + \varphi_1\psi_1)}_{\gamma}
  \mathbf{1}
  + 
  \underbrace{(\varphi_0 + \psi_0 + \varphi_0\psi_0h)}_{\sigma_0}
  \sigma_0
  + 
  \underbrace{(\varphi_1 + \psi_1 + \varphi_1\psi_1h)}_{\sigma_1}
  \sigma_1
  + 
  \underbrace{\varphi_0\psi_1}_{L_+}
  \sigma_0\sigma_1
  + 
  \underbrace{\varphi_1\psi_0}_{L_-}
  \sigma_1\sigma_0.
$$

The Hecke self-energy terms $\varphi_0\psi_0$ and $\varphi_1\psi_1$ contribute to the $\mathbf{1}$ coefficient. The Hopf link terms $L_\pm$ arise strictly from cross-color products $\varphi_0\psi_1$ and $\varphi_1\psi_0$.

The net evaluation is the sum of all coefficients:

$$
  \mathrm{net}
  = 
  (1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)
  + 
  (\varphi_0\psi_0 + \varphi_1\psi_1)h.
$$

#### Polarization limits

**Linear (symmetric) polarization:** 
We set equal color in both generators, $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = \phi$.
- $\gamma$: $1 + 2\phi^2$
- $\sigma_0$: $2\phi + \phi^2 h$
- $\sigma_1$: $2\phi + \phi^2 h$
- $L_+$: $\phi^2$
- $L_-$: $\phi^2$

The equal Hopf link content ($L_+ = L_- = \phi^2$) implies zero chirality. The net valuation is $(1 + 2\phi)^2 + 2\phi^2 h$. Setting $E_{\mathrm{pair}} = 2m_e$ fixes $\phi = 0.0487$.

**Circular (orthogonal) polarization:**
We set orthogonal polarization, $\varphi_0 = s$, $\varphi_1 = 0$, $\psi_0 = 0$, $\psi_1 = s$.
- $\gamma$: $1$
- $\sigma_0$: $s$
- $\sigma_1$: $s$
- $L_+$: $s^2$
- $L_-$: $0$

Only $L_+$ appears ($L_- = 0$). This produces maximally chiral Hopf content. The Hecke self-energy vanishes ($\varphi_0\psi_0 = \varphi_1\psi_1 = 0$). The net valuation is $(1 + s)^2$. Setting $E_{\mathrm{pair}} = 2m_e$ fixes $s = 0.0978$.

Both models close the $1.6\%$ energy gap. The color weight generates Hopf link content $L_\pm$ that supplies the missing pair production energy. The asymmetry $L_+ \neq L_-$ in the circular model acts as the categorical expression of photon helicity.

#### Four-term extension

Activating $\varphi_{01} \neq 0$ recovers the general 4-term photon. The $\gamma\gamma$ product directly opens the $e^-$ (trefoil) channel. The 6-term normal form and the derivation of nucleons from pair production follow from these operations.

**Witness:** `breit-wheeler-nucleon-nf.witness.json`
<!-- FILE_END: breit-wheeler-pair-production-derivation.md -->

<!-- FILE_START: gamma-gamma-generates-particles.md -->
*Two independent photons multiplied in the Iwahori--Hecke algebra $H_3(q)$ reach every operator of the six-element basis $\{\mathbf{1}, \sigma_0, \sigma_1, L_+, L_-, e^-\}$. The photon and the elementary crossings generate the whole particle catalogue through pair production.*

We write two colored photons with independent color weights:

$$
  \gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
             + \varphi_{01}\sigma_0\sigma_1,
  \qquad
  \gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1
             + \psi_{01}\sigma_0\sigma_1.
$$

We reduce $\gamma_1\cdot\gamma_2$ with the Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + \mathbf{1}$. This places five of the six basis operators in the three-term product (where $\varphi_{01}=\psi_{01}=0$):

$$
  \operatorname{NF}(\gamma_1\gamma_2)
  = \underbrace{(1+\varphi_0\psi_0+\varphi_1\psi_1)}_{\mathbf{1}}
  + \underbrace{(\varphi_0+\psi_0+\varphi_0\psi_0\,h)}_{\sigma_0}\sigma_0
  + \underbrace{(\varphi_1+\psi_1+\varphi_1\psi_1\,h)}_{\sigma_1}\sigma_1
  + \underbrace{\varphi_0\psi_1}_{L_+}\sigma_0\sigma_1
  + \underbrace{\varphi_1\psi_0}_{L_-}\sigma_1\sigma_0 ,
  \qquad h = q-q^{-1}.
$$

The two chiral operators are generated independently. The $L_+$ coefficient is the cross-color product $\varphi_0\psi_1$. The $L_-$ coefficient is $\varphi_1\psi_0$. For any target pair $(a,b)$, the weights $(\varphi_0,\varphi_1,\psi_0,\psi_1)=(a,b,1,1)$ realise $L_+=a$ and $L_-=b$. The operator $L_-=\sigma_1\sigma_0$ is absent from any single photon. The single photon support is $\{\mathbf{1},\sigma_0,\sigma_1,\sigma_0\sigma_1\}$. The two-photon cross term produces $L_-$. Restoring the four-term coupling $\varphi_{01}\neq 0$ opens the remaining basis operator $e^-=\sigma_0\sigma_1\sigma_0$. This completes the basis.

The span of the two-photon products is all of $H_3(q)$. The photon and the elementary crossings generate the full operator catalogue. Pair production ($\gamma\gamma$) is the categorical mechanism by which light assembles matter.

### Lean structure
The generative core is formalised over a generic commutative ring. The cross-color coefficients are purely algebraic, with no $q_0$ specialization. The theorem `gamma_gamma_chirality_surjective` proves that the chiral pair $(L_+, L_-)$ is jointly surjective in the photon color weights. The theorem `gamma_gamma_reaches_Lminus` exhibits a two-photon product carrying the $L_-=\sigma_1\sigma_0$ operator that no single photon holds.
<!-- FILE_END: gamma-gamma-generates-particles.md -->

<!-- FILE_START: knot-operator-selection.md -->
The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ of the categorical action decomposes over the irreducible representations of $H_n(q)$. This decomposition and the Frobenius self-duality $A \cong A^\vee$ determine the specific knot operators that mediate any interaction. They also determine their corresponding weights.

## Statement

**Proposition (knot operator selection).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with archimedean realisation $H_r(q)$. Let $\{\tau(r_i, s_i)\}_{i=1}^{6}$ be the embeddable torus knots on $\Sigma_4$. Let $\gamma_1, \gamma_2 \in H_3(q)$ be two incoming particle states.*

**(i) Spectral decomposition of the mediating endomorphism.**
*The physics endomorphism $\Phi$ decomposes via Schur orthogonality:*

$$
  \Phi
  =
  \sum_{\lambda \vdash r}
  d_\lambda(q) \cdot \Phi_\lambda,
$$

*where $d_\lambda(q)$ is the quantum dimension of irrep $\lambda$. The operator $\Phi_\lambda = e_\lambda \Phi e_\lambda$ is the projection of $\Phi$ onto the $\lambda$-isotypic component. Each irrep $\lambda$ corresponds to a torus knot $\tau(r,s)$ via the knot eigenbasis.*

**(ii) Multi-channel pair production.**
*The categorical action of two photons $\gamma_1, \gamma_2$ through the mediating endomorphism is:*

$$
  \mathcal{S}(\gamma_1, \gamma_2)
  =
  \mathrm{tr}\!\left(
    \Phi \cdot (\gamma_1 \otimes \gamma_2)
  \right)
  =
  \sum_{\lambda}
  d_\lambda(q) \cdot
  \mathrm{tr}_\lambda\!\bigl(
    \gamma_1 \cdot \beta(\tau_\lambda) \cdot \gamma_2
  \bigr).
$$

*Multiple knot operators act simultaneously. The quantum dimension weights each operator. The interaction is a superposition of channels.*

**(iii) Frobenius demand--supply pairing.**
*The Frobenius self-duality $A \xrightarrow{\sim} A^\vee$ via $\int_A \circ \mu$ identifies the normal form decomposition of each state with its dual. For a state $K = \sum_i c_i b_i$ in the basis $\{b_i\} = \{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:*

* *Positive coefficients $c_i > 0$ are supply. These are channels the state provides.*
* *Negative coefficients $c_i < 0$ are demand. These are channels the state requires from its interaction partner.*

*The Frobenius pairing $\langle K_1, K_2 \rangle_F = \mathrm{tr}_M(K_1 \cdot K_2)$ is non-degenerate (QUO-1). For every nonzero demand profile, a unique minimal-norm supply satisfies it.*

**(iv) Minimum-action selection.**
*The physical interaction selects the $\Phi \in \mathrm{End}(A)$ minimizing the categorical action $|\mathfrak{S}| = |\mathrm{tr}(\Phi)|$ among those compatible with the on-shell condition $\star_q F_\nabla = F_\nabla$. The dominant channel is the irrep $\lambda_*$ with the largest $|d_{\lambda_*}(q) \cdot \mathrm{tr}_{\lambda_*}(\gamma_1 \cdot \beta(\tau_{\lambda_*}) \cdot \gamma_2)|$.*

## Multi-channel interpretation

For Breit--Wheeler pair production $\gamma\gamma \to e^-e^+$, the full interaction is:

$$
  \mathcal{S}(\gamma_1, \gamma_2)
  =
  \underbrace{d_{\mathrm{triv}}(q) \cdot P_{T_{1,0}}}_{\text{elastic: polarisation change}}
  +
  \underbrace{d_{\Box}(q) \cdot P_{T_{2,1}}}_{\text{single crossing}}
  +
  \underbrace{d_{\Box\Box}(q) \cdot P_{T_{2,2}}}_{\text{Hopf link (gluon)}}
  +
  \underbrace{d_{\yng(2,1)}(q) \cdot P_{T_{2,3}}}_{\text{trefoil (electron)}}
  +  \cdots
$$

All channels fire simultaneously. Two incoming photons can:

* change polarisation (trivial operator, no pair created),
* exchange a gluon ($T_{2,2}$, Hopf link),
* create $e^-e^+$ ($T_{2,3}$, trefoil),
* create $\mu^-\mu^+$ ($T_{2,5}$, cinquefoil, suppressed by higher crossing energy).

These events occur in a single interaction. The quantum dimension $d_\lambda(q)$ weights each channel. The branching ratios depend entirely on $q$ and the incoming photon polarisation content $\varphi_0, \varphi_1$.

Experiments detect the dominant channel. This channel carries the largest weight. The subdominant channels contribute to radiative corrections, vacuum polarisation, and the running of coupling constants. The elastic channel ($T_{1,0}$) is always present. Photon--photon scattering without pair creation is the leading process. Pair creation is a threshold-activated subdominant channel.

## Explicit dual construction

We consider a state $K \in H_3(q)$ with decomposition $K = \sum_i c_i b_i$. The Frobenius dual $K^\vee$ is the unique element satisfying:

$$
  \langle K^\vee, b_i \rangle_F = c_i
  \quad \forall i.
$$

By non-degeneracy, $K^\vee$ exists and is unique. In the basis, $K^\vee = \sum_i c_i (G^{-1})_{ij} b_j$. The term $G_{ij} = \langle b_i, b_j \rangle_F = \mathrm{tr}_M(b_i \cdot b_j)$ is the $6 \times 6$ Gram matrix of $H_3(q)$.

The demand vector of $K$ is the negative part:

$$
  \mathrm{dem}(K) = \sum_{i : c_i < 0} |c_i| \, b_i^\vee.
$$

The operator that fills the demand at minimum crossing energy is:

$$
  \Phi_{\mathrm{min}}
  =
  \arg\min_{\Phi \in \mathrm{End}(A)_{\mathrm{on-shell}}}
  \left\{
    \mathfrak{E}_{\mathrm{cross}}(\Phi)
    \ \Big|\ 
    \langle \Phi, \mathrm{dem}(K) \rangle_F \geq
    \|\mathrm{dem}(K)\|_F
  \right\}.
$$

For the positron ($e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$), the demand profile is $\{-0.218\gamma, -0.209 L_+, -0.209 L_-\}$. The mirror trefoil demands vacuum energy and Hopf content. The minimum-energy supply is the coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$. This morphism provides exactly the identity and Hopf content from the rigid structure. Its cost is $\mathrm{tr}(\mathrm{id}_A) = [2]_q = q + q^{-1} \approx 2.011$.
<!-- FILE_END: knot-operator-selection.md -->

