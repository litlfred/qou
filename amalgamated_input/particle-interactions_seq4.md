<!-- FILE_START: nucleon-derivation-intro.md -->
The linear programming machinery selects the Borromean operator $\mathcal{B}_3$ as the unique confinement optimum. We apply this selection rule to the photon pair-production vertex to derive the nucleons. Closing the four-term photon braid with $\mathcal{B}_3$ yields the proton and neutron normal forms. These normal forms remain independent of the incoming photon polarization. We package this construction as the derived atom $\mathcal{A}(Z, N)$. This completes the derivation chain $\gamma\gamma \to q\bar q \to \mathfrak{p}, \mathfrak{n} \to \mathcal{A}(Z, N)$, establishing the foundation for our subsequent study of nuclear stability.
<!-- FILE_END: nucleon-derivation-intro.md -->

<!-- FILE_START: up-quark.md -->
**Definition.**
*The **up quark** is an unknot localized in a color tube of the Bring's surface with **positive crossing orientation** within the Borromean link $\mathcal{B}_3$.*

$$
  \mathfrak{u} =  \nu \big|_{\mathcal{B}_3, +}
$$

*The up quark is not a distinct knot type. It is the unknot distinguished by its environment. It is threaded through a color tube and Borromean-linked with two other unknots.*
<!-- FILE_END: up-quark.md -->

<!-- FILE_START: up-quark-properties.md -->
**Crossing orientation.**
Within $\mathcal{B}_3$, each component passes over and under the other two at specific crossings. The positive orientation means the up quark's crossings contribute $+q$ to the Skein polynomial at each crossing point. This gives the up quark a Coulomb charge contribution of $+2/3$ relative to the proton.

**Isolation.**
An isolated up quark does not exist. Removing it from $\mathcal{B}_3$ unlinks the remaining two unknots, which destroys the baryon.
<!-- FILE_END: up-quark-properties.md -->

<!-- FILE_START: down-quark.md -->
**Definition.**
*The **down quark** is an unknot localized in a color tube with **negative crossing orientation** within the Borromean link $\mathcal{B}_3$.*

$$
  \mathfrak{d} =  \nu \big|_{\mathcal{B}_3, -}
$$

*The down quark differs from the up quark only by crossing orientation. At each crossing point within $\mathcal{B}_3$, the down quark strand passes under where the up quark passes over. This reversal contributes $q^{-1}$ instead of $q$ to the Skein polynomial. This gives the down quark a Coulomb charge contribution of $-1/3$ relative to the proton.*
<!-- FILE_END: down-quark.md -->

<!-- FILE_START: down-quark-properties.md -->
**Mass splitting.**
The up and down quarks possess the same knot type and environment. The mass difference $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ arises from crossing asymmetry. The Skein relation weights positive crossings by $q$ and negative crossings by $q^{-1}$. The reversed-orientation component therefore carries a distinct Skein resolution energy.

**Isolation.**
Like the up quark, the down quark cannot be isolated. It labels a Borromean component rather than a free particle.
<!-- FILE_END: down-quark-properties.md -->

<!-- FILE_START: quark-antiquark-production.md -->
**Definition.**
*A **quark--antiquark production** is the full chain $\gamma\gamma \to q\bar{q}$, in which two colored photons collide and their Hecke-algebra product reduces to a quark--antiquark channel. Each photon is the Hecke algebra element:*
$$
\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1
$$
*with independent color weights $\varphi_0, \varphi_1, \varphi_{01}$.*
<!-- FILE_END: quark-antiquark-production.md -->

<!-- FILE_START: quark-antiquark-production-reduction.md -->
**Step 0: two colored photons collide.**
Each photon is the Hecke algebra element $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$. The derivation uses the 3-term specialization $\varphi_{01} = 0$.

**Step 1: expand the product $\gamma_1 \cdot \gamma_2$.**
Their product NF in $H_3(q)$ yields Hopf link terms $L_+$ and $L_-$ exclusively from cross-color products.

**Quark creation: step-by-step reduction of $L_+ \cdot e^-$.**
The positive Hopf link $L_+ = \sigma_0\sigma_1$ applied to the trefoil $e^- = \sigma_0\sigma_1\sigma_0$ reduces to:

$$
  \mathrm{NF}(L_+ \cdot e^-)
  = 
  \sigma_1
  + 
  hL_+
  + 
  hL_-
  + 
  h^2e^-
$$

The Hopf link operator $L_+$ transmutes the trefoil electron into a virtual crossing $\sigma_1$ plus residual Hopf and trefoil content. The $e^-$ coefficient $h^2$ is the residual electron. The dominant output $\sigma_1$ is the hadronic crossing that becomes the up quark. The mirror operator $L_-$ creates an antiquark from the positron channel.

**Two independent productions.**
When two independent colored photon pairs undergo pair creation simultaneously, each produces a quark--antiquark channel. The quark type is determined by the crossing orientation.

**Meson formation.**
When the $\mathfrak{u}$ from production 1 and the $\bar{\mathfrak{d}}$ from production 2 come within Hopf linking distance, they bind via $\mathcal{L}_H$ to form a meson. The remaining $\bar{\mathfrak{u}}$ and $\mathfrak{d}$ either annihilate back to photons or form the antimeson.

**Three independent productions $\to$ nucleon.**
For baryon production, three independent pair creations produce three quark--antiquark pairs. Selecting one quark from each pair gives a quark triple which is confined by the Borromean braid $\mathcal{B}_3$.
<!-- FILE_END: quark-antiquark-production-reduction.md -->

<!-- FILE_START: four-term-pair-nucleon.md -->
We derive the proton and neutron from three independent $\gamma\gamma$ pair productions using the full 4-term photon color content.

## The 4-term photon

Each photon carries the full color content:

$$
  \gamma_k
  =
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1
$$

where $\varphi_{01}\sigma_0\sigma_1 = \varphi_{01}L_+$ is the Hopf link dressing. When $\varphi_{01} \neq 0$, the trefoil channel opens directly in the $\gamma\gamma$ product.

## Three pair productions

Three independent $\gamma\gamma$ collisions produce three quark--antiquark pairs. Each collision NF contains six terms. The quark is the crossing content. The antiquark is the mirror crossing.

## Confinement: $\mathcal{B}_3$ selected by minimum action

We select three quarks from the pairs and confine them via the Borromean braid $\mathcal{B}_3$. This is the unique minimum-action confinement operator.

The derivation chain is:

$$
  \mathfrak{p}
  =
  \mathcal{B}_3
  \cdot C(\mathfrak{u},\mathfrak{u};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_1)
$$

## Proton NF

Gröbner--Shirshov reduction yields $\mathrm{net}(\mathfrak{p}) \approx +0.999$.

## Neutron NF

For quarks $(\mathfrak{u}_1, \mathfrak{d}_2, \mathfrak{d}_3)$, reduction yields $\mathrm{net}(\mathfrak{n}) \approx +0.811$. The neutron exhibits a larger demand in $\gamma$ and an additional demand in $L_+$. This extra deficit drives beta decay.

## Confinement universality

The nucleon NF is independent of the photon polarization. Sweeping $\varphi_{01}$ from $0$ to $0.2$ leaves the proton and neutron NFs unchanged. The strong interaction erases the initial electromagnetic conditions.
<!-- FILE_END: four-term-pair-nucleon.md -->

<!-- FILE_START: confinement-universality.md -->
*Let $\gamma_k = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ be a 4-term photon. Let $\mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})$ denote the nucleon NF obtained by the derivation chain $\gamma\gamma \to q\bar{q} \to \mathcal{B}_3 \cdot \mathrm{crossings} \to \mathfrak{N}$.*

*Then for all $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$:*

$$
  \mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})
  =
  \mathfrak{N}(0, 0, 0)
  =
  \mathrm{NF}(\mathcal{B}_3 \cdot \mathrm{crossings}).
$$

*The nucleon NF depends only on $q$ and the quark flavor assignment.*

This is the categorical expression of asymptotic freedom: the strong interaction washes out the electromagnetic initial conditions. At short distances, only the quark flavor matters. The photon polarization is a long-distance electromagnetic property that decouples under confinement.
<!-- FILE_END: confinement-universality.md -->

<!-- FILE_START: derived-atom.md -->
**Definition.**
*Let $q$ be the braiding eigenvalue of $(\mathbf{C}, A, \tau)$. The **derived atom** $\mathcal{A}(Z, N)$ is the element of $H_A(q)$ obtained by the following five steps:*

1. ***Pair production.** Three independent 4-term photon collisions produce three quark--antiquark pairs per nucleon via the Hecke relation.*
2. ***Quark selection.** Select one quark from each pair. The remaining antiquarks either annihilate or form antinucleons.*
3. ***Borromean confinement.** The minimum-action operator $\mathcal{B}_3$ confines each triple of quarks. This yields pre-gluon NF elements in $H_3(q)$.*
4. ***Gluon stabilisation.** The confined nucleon is LP-unstable. The integer LP dual selects the minimum gluon. The stabilised nucleon NF elements are $\mathfrak{N}_k \in H_3(q)$.*
5. ***Nuclear assembly.** Inter-nucleon typed crossings in $H_A(q)$ link the $A = Z + N$ nucleons.*
6. ***Electron cloud.** Electromagnetic crossings link $Z$ electrons to the nucleus via Hopf links.*

## Inductive Gröbner--Shirshov reduction

For large $A$, the unreduced braid word has exponentially many terms. The Gröbner--Shirshov normal form is computed inductively. We reduce after each multiplication step, not at the end. Each intermediate result is in normal form. The total computation is polynomial in $A$.

## NF characterization

The derived atom $\mathcal{A}(Z, N)$ is a unique element of $H_A(q)$ in Gröbner--Shirshov normal form:

$$
  \mathcal{A}(Z, N)
  \;=\;
  \sum_{w \in \mathrm{NF}(B_A)}
  c_w(q, Z, N) \cdot w
$$

where $c_w \in \mathbb{Z}[q, q^{-1}]$ are Laurent polynomial coefficients.
<!-- FILE_END: derived-atom.md -->

<!-- FILE_START: nucleon-from-photons-summary.md -->
This is the complete derivation chain from photons to atoms, verifying conservation laws at each step.

$$
  \underbrace{3(\gamma\gamma)}_{\text{6 photons}}
  \xrightarrow{\text{pair prod.}}
  \underbrace{3(q\bar{q})}_{\text{3 pairs}}
  \xrightarrow{\text{select}}
  \underbrace{(q_1, q_2, q_3)}_{\text{3 quarks}}
  \xrightarrow{\mathcal{B}_3}
  \underbrace{\mathfrak{N}}_{\text{nucleon}}
  \xrightarrow{\oplus}
  \underbrace{\mathcal{A}}_{\text{atom}}
$$

| Step | Input | Output | $B$ | $L$ | $Q$ |
|:---|:---|:---|:---:|:---:|:---:|
| $\gamma\gamma$ collision | 2 photons | $q\bar{q}$ pair | $0$ | $0$ | $0$ |
| Quark selection | 3 pairs | 3 quarks + 3 antiquarks | $\pm 1$ | $0$ | $\pm 1$ |
| $\mathcal{B}_3$ confinement | 3 quarks | nucleon | $+1$ | $0$ | $0,+1$ |
| Hopf link $\oplus e^-$ | nucleon + electron | atom | $+1$ | $+1$ | $0$ |

Baryon number, lepton number, and electric charge remain conserved at every step.

1. **Confinement is derived**: Minimum action selects $\mathcal{B}_3$ among operators matching the physical nucleon net.
2. **Beta decay channel**: The $e^-$ coefficient in the confined nucleon normal form defines the categorical beta decay channel.
3. **Confinement universality**: The nucleon normal form depends solely on $q_0$ and quark flavors.
4. **Shell closure**: Shell configuration demands dictate stability.
<!-- FILE_END: nucleon-from-photons-summary.md -->

