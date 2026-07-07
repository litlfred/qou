<!-- FILE_START: nucleon-derivation-intro.md -->
The linear programming machinery selects the Borromean operator $\mathcal{B}_3$ as the unique confinement optimum. We apply this selection rule to the photon pair-production vertex to derive the nucleons. Closing the four-term photon braid with $\mathcal{B}_3$ yields the proton and neutron normal forms. These normal forms remain independent of the incoming photon polarization. We package this construction as the derived atom $\mathcal{A}(Z, N)$. This completes the derivation chain $\gamma\gamma \to q\bar q \to \mathfrak{p}, \mathfrak{n} \to \mathcal{A}(Z, N)$, establishing the foundation for our subsequent study of nuclear stability.
<!-- FILE_END: nucleon-derivation-intro.md -->

<!-- FILE_START: up-quark.md -->
The **up quark** is an unknot (neutrino) localized in a color tube of the Bring's surface with **positive crossing orientation** within the Borromean link $\mathcal{B}_3$ ([Borromean quark conjecture](#conj:borromean-quark)).

$$
  \mathfrak{u} =  \nu \big|_{\mathcal{B}_3, +}
  \qquad\text{(unknot, positive orientation in } \mathcal{B}_3\text{)}
$$

The up quark is not a distinct knot type. It is the unknot $K_{0_1}$ ([neutrino](#def:neutrino-knot)) distinguished by its **environment**. It is threaded through a color tube ([color tube coordinates](#def:color-tube-coordinates)) and Borromean-linked with two other unknots.
<!-- FILE_END: up-quark.md -->

<!-- FILE_START: up-quark-properties.md -->
**Crossing orientation.**
Within $\mathcal{B}_3$, each component passes over and under the other two at specific crossings. The **positive orientation** means the up quark's crossings contribute $+q$ to the Skein polynomial at each crossing point. This gives the up quark a Coulomb charge contribution of $+2/3$ relative to the proton.

**Isolation.**
An isolated up quark does not exist. Removing it from $\mathcal{B}_3$ unlinks the remaining two unknots, which destroys the baryon. The "up quark" is a label for a component of the Borromean structure, not a free particle.
<!-- FILE_END: up-quark-properties.md -->

<!-- FILE_START: down-quark.md -->
The **down quark** is an unknot (neutrino) localized in a color tube with **negative crossing orientation** within the Borromean link $\mathcal{B}_3$ ([Borromean quark conjecture](#conj:borromean-quark)).

$$
  \mathfrak{d} =  \nu \big|_{\mathcal{B}_3, -}
  \qquad\text{(unknot, negative orientation in } \mathcal{B}_3\text{)}
$$

The down quark differs from the up quark ([up quark](#def:up-quark)) only by **crossing orientation**. At each crossing point within $\mathcal{B}_3$, the down quark strand passes under where the up quark passes over. This reversal contributes $q^{-1}$ instead of $q$ to the Skein polynomial. This gives the down quark a Coulomb charge contribution of $-1/3$ relative to the proton.
<!-- FILE_END: down-quark.md -->

<!-- FILE_START: down-quark-properties.md -->
**Mass splitting.**
The up and down quarks possess the same knot type (unknot) and environment (Borromean-linked in a color tube). The mass difference $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$ arises from **crossing asymmetry** ([crossing asymmetry](#rem:skein-crossing-asymmetry)). The Skein relation weights positive crossings by $q$ and negative crossings by $q^{-1}$. The reversed-orientation component therefore carries a distinct Skein resolution energy.

**Isolation.**
Like the up quark, the down quark cannot be isolated. It labels a Borromean component rather than a free particle.
<!-- FILE_END: down-quark-properties.md -->

<!-- FILE_START: quark-antiquark-production.md -->
A **quark--antiquark production** is the full chain $\gamma\gamma \to q\bar{q}$, in which two colored photons collide and their Hecke-algebra product reduces to a quark--antiquark channel. Each photon is the Hecke algebra element:
$$
\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1
$$
with independent color weights $\varphi_0, \varphi_1, \varphi_{01}$ ([pair production](#def:breit-wheeler-pair-production)).

The [reduction remark](#rem:quark-antiquark-production-reduction) develops the step-by-step Hecke reduction realizing this chain, from the photon product through quark creation, independent productions, and meson or nucleon formation.
<!-- FILE_END: quark-antiquark-production.md -->

<!-- FILE_START: quark-antiquark-production-reduction.md -->
The [quark--antiquark production definition](#def:quark-antiquark-production)
names the chain $\gamma\gamma \to q\bar{q}$; here is the mechanism, step
by step, with no gap between photon pair and quark output.

**Step 0: two colored photons collide.**
Each photon is the Hecke algebra element
$\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$
with independent color weights $\varphi_0, \varphi_1, \varphi_{01}$
([pair production](#def:breit-wheeler-pair-production)).
The derivation below uses the 3-term specialization $\varphi_{01} = 0$.

**Step 1: expand the product $\gamma_1 \cdot \gamma_2$.**
Given two colored photons (3-term specialization)
$\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$
and
$\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$,
their product NF in $H_3(q)$ is
([color content](#rem:knot-basis-color-content)):

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  (1 + \varphi_0\psi_0 + \varphi_1\psi_1)\gamma
  + 
  (\varphi_0 + \psi_0 + \varphi_0\psi_0h)\sigma_0
  + 
  (\varphi_1 + \psi_1 + \varphi_1\psi_1h)\sigma_1
  + 
  \varphi_0\psi_1L_+
  + 
  \varphi_1\psi_0L_-
$$

where $h = q - q^{-1}$.  The Hopf link terms
$L_+ = \sigma_0\sigma_1$ and $L_- = \sigma_1\sigma_0$ arise
exclusively from **cross-color** products: $\varphi_0\psi_1$
and $\varphi_1\psi_0$.

**Quark creation: step-by-step reduction of $L_+ \cdot e^-$.**
The positive Hopf link $L_+ = \sigma_0\sigma_1$ applied to the
trefoil $e^- = \sigma_0\sigma_1\sigma_0$ gives the five-letter
word $\sigma_0\sigma_1\sigma_0\sigma_1\sigma_0$.  Reduce using
the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$
and the Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$
(where $h = q - q^{-1}$):

$$
  \sigma_0\sigma_1 \cdot \sigma_0\sigma_1\sigma_0
  = 
  \sigma_0 \cdot (\sigma_1 \cdot \sigma_0\sigma_1\sigma_0)
$$

**Inner product** $\sigma_1 \cdot \sigma_0\sigma_1\sigma_0$:
apply the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$:

$$
  \sigma_1 \cdot \sigma_1\sigma_0\sigma_1
  = 
  \sigma_1^2 \cdot \sigma_0\sigma_1
  = 
  (h\sigma_1 + \mathbf{1}) \cdot \sigma_0\sigma_1
  = 
  h\sigma_1\sigma_0\sigma_1 + \sigma_0\sigma_1
$$

Apply the braid relation again ($\sigma_1\sigma_0\sigma_1 = \sigma_0\sigma_1\sigma_0$):

$$
  = 
  h\sigma_0\sigma_1\sigma_0 + \sigma_0\sigma_1
$$

**Outer product** $\sigma_0 \cdot (h\sigma_0\sigma_1\sigma_0 + \sigma_0\sigma_1)$:

$$
  h\sigma_0^2\sigma_1\sigma_0
  + 
  \sigma_0^2\sigma_1
$$

Apply $\sigma_0^2 = h\sigma_0 + \mathbf{1}$ to each:

$$
  h(h\sigma_0 + \mathbf{1})\sigma_1\sigma_0
  + 
  (h\sigma_0 + \mathbf{1})\sigma_1
$$

Distribute:

$$
  h^2\sigma_0\sigma_1\sigma_0
  + 
  h\sigma_1\sigma_0
  + 
  h\sigma_0\sigma_1
  + 
  \sigma_1
$$

**Result in the NF basis** $\{\mathbf{1}, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:

$$
  \mathrm{NF}(L_+ \cdot e^-)
  = 
  \sigma_1
  + 
  h\sigma_0\sigma_1
  + 
  h\sigma_1\sigma_0
  + 
  h^2\sigma_0\sigma_1\sigma_0
$$

$$
  = 
  \sigma_1
  + 
  hL_+
  + 
  hL_-
  + 
  h^2e^-
$$

At $q_0 \approx 1.110$ ($h \approx 0.209$):

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\sigma_1$ | $\sigma_1$ | $1.000$ |
| $\sigma_0\sigma_1$ | $L_+$ | $h \approx 0.209$ |
| $\sigma_1\sigma_0$ | $L_-$ | $h \approx 0.209$ |
| $\sigma_0\sigma_1\sigma_0$ | $e^-$ | $h^2 \approx 0.044$ |

The Hopf link operator $L_+$ transmutes the trefoil electron into
a virtual crossing $\sigma_1$ plus residual Hopf and trefoil content.
The $e^-$ coefficient $h^2$ is the **residual electron** —
physically, the fraction of the original lepton that survives the
quark creation. The dominant output $\sigma_1$ is the
hadronic crossing that becomes the quark
([up quark](#def:up-quark)).  The mirror operator $L_-$ creates
an antiquark ($\bar{\mathfrak{d}}$) from the positron channel.

**Two independent productions.**
When two independent colored photon pairs undergo pair creation
simultaneously, each produces a quark--antiquark channel:

$$
  \gamma_1 \cdot \gamma_2  \to 
  \mathfrak{u} + \bar{\mathfrak{u}}
  \qquad\text{(production 1: up-type)}
$$

$$
  \gamma_3 \cdot \gamma_4  \to 
  \mathfrak{d} + \bar{\mathfrak{d}}
  \qquad\text{(production 2: down-type)}
$$

The quark type (up vs down) is determined by the crossing
orientation: $\sigma$ gives $\mathfrak{u}$ (positive), while
$\sigma^{-1}$ gives $\mathfrak{d}$ (negative)
([down quark](#def:down-quark)).

**Meson formation.**
When the $\mathfrak{u}$ from production 1 and the
$\bar{\mathfrak{d}}$ from production 2 come within Hopf linking
distance, they bind via $\mathcal{L}_H$ to form a meson
([categorical meson](#def:categorical-meson)):

$$
  \mathfrak{u} + \bar{\mathfrak{d}}
  \xrightarrow{\mathcal{L}_H}
  \mathfrak{M}_+
  =  T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

The remaining $\bar{\mathfrak{u}}$ and $\mathfrak{d}$ either
annihilate back to photons or form the antimeson $\mathfrak{M}_-$.
This is the categorical expression of $\gamma\gamma \to
q\bar{q} + q\bar{q} \to \mathfrak{M} + \mathfrak{M}$.

**Three independent productions $\to$ nucleon.**
For baryon production, three independent pair creations produce
three quark--antiquark pairs.  Selecting one quark from each pair
gives a quark triple ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$ for
proton, $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ for neutron)
which is confined by the Borromean braid $\mathcal{B}_3$
([4-term pair nucleon](#prop:four-term-pair-nucleon)).
The confinement operator is derived, not asserted — see
[confinement selection](#prop:confinement-operator-selection).

**Witness**: `breit-wheeler-nucleon-nf.witness.json`, `meson-nucleon-nf.witness.json`, `four-term-photon-to-atoms.witness.json`.
<!-- FILE_END: quark-antiquark-production-reduction.md -->

<!-- FILE_START: four-term-pair-nucleon.md -->
We derive the proton and neutron from three independent $\gamma\gamma$ pair productions using the full 4-term photon color content.

## The 4-term photon

Each photon carries the full color content ([color content](#rem:knot-basis-color-content)):

$$
  \gamma_k
  =
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1
$$

where $\varphi_{01}\sigma_0\sigma_1 = \varphi_{01}L_+$ is the Hopf link dressing ([photon knot operations](#rem:physics-names-knot-operations)). When $\varphi_{01} = 0$, the $e^-$ channel closes. When $\varphi_{01} \neq 0$, the trefoil channel opens directly in the $\gamma\gamma$ product.

## Three pair productions

Three independent $\gamma\gamma$ collisions produce three quark--antiquark pairs ([quark--antiquark production](#def:quark-antiquark-production)):

$$
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_1 + \bar{\mathfrak{u}}_1,
  \qquad
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_2 + \bar{\mathfrak{u}}_2,
  \qquad
  \gamma\gamma \xrightarrow{L_-}
  \mathfrak{d}_3 + \bar{\mathfrak{d}}_3.
$$

Each collision NF contains six terms (at $\varphi_{01} = 0.02$):

See [Table 1](#tbl:four-term-pair-nucleon-table1-data).

The quark is the crossing content ($\sigma_0$ or $\sigma_1$). The antiquark is the mirror crossing ($\sigma_0^{-1}$ or $\sigma_1^{-1}$).

## Confinement: $\mathcal{B}_3$ selected by minimum action

We select three quarks ($\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3$ for the proton) from the pairs and confine them via the Borromean braid $\mathcal{B}_3$. This is the unique minimum-action confinement operator ([confinement selection](#prop:confinement-operator-selection)).

The derivation chain is:

$$
  \mathfrak{p}
  =
  \mathcal{B}_3
  \cdot C(\mathfrak{u},\mathfrak{u};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_1)
$$

where $C(f_i, f_j; \sigma_k)$ is the typed crossing ([categorical proton](#def:categorical-proton)).

## Proton NF

Gröbner--Shirshov reduction at $q_0 \approx 1.1100$ yields:

See [Table 2](#tbl:four-term-pair-nucleon-table2-data).

$$
  \mathrm{net}(\mathfrak{p}) \approx +0.999
$$

## Neutron NF

For quarks $(\mathfrak{u}_1, \mathfrak{d}_2, \mathfrak{d}_3)$:

See [Table 3](#tbl:four-term-pair-nucleon-table3-data).

$$
  \mathrm{net}(\mathfrak{n}) \approx +0.811
$$

The neutron exhibits a larger demand in $\gamma$ ($-0.202$ versus $-0.100$) and an additional demand in $L_+$ ($-0.010$). This extra deficit drives beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$.

## Confinement universality

The nucleon NF is independent of the photon polarization $(\varphi_0, \varphi_1, \varphi_{01})$. Sweeping $\varphi_{01}$ from $0$ to $0.2$ leaves the proton and neutron NFs unchanged. The photon initial conditions determine which quark pairs are created. Once we select and confine the quarks by $\mathcal{B}_3$, the NF depends only on $q_0$ and the quark flavors.

**Witness**: `four-term-photon-to-atoms.witness.json`.
<!-- FILE_END: four-term-pair-nucleon.md -->

<!-- FILE_START: confinement-universality.md -->
The nucleon normal form is independent of the photon polarization parameters $(\varphi_0, \varphi_1, \varphi_{01})$ that created the constituent quarks.

## Statement

**Proposition.** Let $\gamma_k = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ be a 4-term photon ([Breit--Wheeler](#def:breit-wheeler-pair-production)). Let $\mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})$ denote the nucleon NF obtained by the derivation chain ([4-term pair nucleon](#prop:four-term-pair-nucleon)): $\gamma\gamma \to q\bar{q} \to \mathcal{B}_3 \cdot \mathrm{crossings} \to \mathfrak{N}$.

Then for all $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$:

$$
  \mathfrak{N}(\varphi_0, \varphi_1, \varphi_{01})
  =
  \mathfrak{N}(0, 0, 0)
  =
  \mathrm{NF}(\mathcal{B}_3 \cdot \mathrm{crossings}).
$$

The nucleon NF depends only on $q$ and the quark flavor assignment.

## Physical interpretation

This is the categorical expression of asymptotic freedom: the strong interaction ($\mathcal{B}_3$ confinement) washes out the electromagnetic initial conditions ($\varphi$ parameters). At short distances (inside the Borromean braid), only the quark flavor matters. The photon polarization is a long-distance electromagnetic property that decouples under confinement.

**Witness:** `four-term-photon-to-atoms.witness.json` (Phase 5: $\varphi_{01}$ sweep with constant nucleon NF).
<!-- FILE_END: confinement-universality.md -->

<!-- FILE_START: derived-atom.md -->
A **derived atom** $\mathcal{A}(Z, N)$ with atomic number $Z$ and neutron number $N$ is the endpoint of a categorical construction. No component is asserted. Each step is derived from the previous one via operations in $H_A(q)$ where $A = Z + N$.

## Construction

**Definition.** Let $q$ be the braiding eigenvalue of $(\mathbf{C}, A, \tau)$. The **derived atom** $\mathcal{A}(Z, N)$ is the element of $H_A(q)$ obtained by the following five steps:

1. **Pair production.** For each nucleon $k \in \{1, \ldots, Z + N\}$, three independent 4-term photon collisions $\gamma_{k,i} \cdot \gamma_{k,i}' \in H_3(q)$ ($i = 1,2,3$) produce three quark--antiquark pairs via the Hecke relation ([Breit--Wheeler](#def:breit-wheeler-pair-production)).
2. **Quark selection.** Select one quark from each pair:
   - Proton ($k \leq Z$): select $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$.
   - Neutron ($k > Z$): select $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$.
   
   The remaining antiquarks either annihilate or form antinucleons. Baryon number is conserved: $3 \times 0 = 1 + (-1)$.
3. **Borromean confinement.** The minimum-action operator $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ confines each triple of quarks ([confinement selection](#prop:confinement-operator-selection)). This yields pre-gluon NF elements in $H_3(q)$.
4. **Gluon stabilisation.** The confined nucleon $\mathcal{B}_3 \times \Delta_3$ is LP-unstable ([integer LP gluon](#prop:mass-endomorphism-tower)): the $\gamma$ Frobenius channel violates positivity. The integer LP dual selects the minimum gluon:
   - Proton: $\sigma_0 \to \sigma_0$ ($2$ bare crossings, $11$ total).
   - Neutron: $L_+ \to L_-$ ($4$ Hopf link crossings, $13$ total).
   
   The gluon is required by LP stability at $q_0 \approx 1.110$ (the proton is stable without a gluon only for $q < 1.104$). The stabilised nucleon NF elements are $\mathfrak{N}_k \in H_3(q)$.
5. **Nuclear assembly.** Inter-nucleon typed crossings in $H_A(q)$ link the $A = Z + N$ nucleons:

$$
  \mathcal{N}(Z, N)
  \;=\;
  \mathrm{NF}\!\left(
    \prod_{k=1}^{A} \mathfrak{N}_k
    \cdot
    \prod_{1 \leq i < j \leq A}
    C(\mathfrak{N}_i, \mathfrak{N}_j; \sigma_{\min(i-1, A-2)})
  \right)
$$

where $C(\mathfrak{N}_i, \mathfrak{N}_j; \sigma_g)$ is the inter-nucleon typed crossing:
   - $p$-$p$: $\sigma_g$ (positive, eigenvalue $+q$).
   - $n$-$n$: $\sigma_g - H_A$ (negative, eigenvalue $-q^{-1}$).
   - $p$-$n$: $\sigma_g - \tfrac{1}{2}H_A$ (mixed).

6. **Electron cloud.** Electromagnetic crossings $\sigma_{g_e}$ link $Z$ electrons (trefoils $T_{2,3} = \sigma_0\sigma_1\sigma_0$) to the nucleus via Hopf links:

$$
  \mathcal{A}(Z, N)
  \;=\;
  \mathrm{NF}\!\left(
    \mathcal{N}(Z, N)
    \cdot
    \prod_{e=1}^{Z}
    \sigma_{g_e} \cdot T_{2,3}
  \right)
$$

where $g_e = (e - 1) \bmod 2$ alternates the generator to distribute electrons across crossing planes.

## Inductive Gröbner--Shirshov reduction

For large $A$, the unreduced braid word has exponentially many terms. The Gröbner--Shirshov normal form is computed inductively. We reduce after each multiplication step, not at the end:

$$
  \mathcal{N}_{\leq k+1}
  \;=\;
  \mathrm{NF}\bigl(
    \mathcal{N}_{\leq k}
    \cdot C(\mathfrak{N}_k, \mathfrak{N}_{k+1}; \sigma_g)
    \cdot \mathfrak{N}_{k+1}
  \bigr).
$$

Each intermediate result is in normal form (at most $\binom{A-1}{k}$ terms of length $\leq A - 1$). The total computation is polynomial in $A$ ([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).

## NF characterization

The derived atom $\mathcal{A}(Z, N)$ is a unique element of $H_A(q)$ in Gröbner--Shirshov normal form:

$$
  \mathcal{A}(Z, N)
  \;=\;
  \sum_{w \in \mathrm{NF}(B_A)}
  c_w(q, Z, N) \cdot w
$$

where $c_w \in \mathbb{Z}[q, q^{-1}]$ are Laurent polynomial coefficients determined by $q$, $Z$, and $N$.

**Witness:** `four-term-photon-to-atoms.witness.json`.
<!-- FILE_END: derived-atom.md -->

<!-- FILE_START: nucleon-from-photons-summary.md -->
This is the complete derivation chain from photons to atoms, verifying conservation laws at each step.

## Chain

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
| $\mathcal{B}_3$ confinement | 3 quarks | nucleon ($\mathfrak{p}$ or $\mathfrak{n}$) | $+1$ | $0$ | $0,+1$ |
| Hopf link $\oplus e^-$ | nucleon + electron | atom | $+1$ | $+1$ | $0$ |

Baryon number ($B$), lepton number ($L$), and electric charge ($Q$) remain conserved at every step. The antiquarks either annihilate back to photons or form an antinucleon.

## Key results

1. **Confinement is derived**: Minimum action selects $\mathcal{B}_3$ among operators matching the physical nucleon net ([confinement selection](#prop:confinement-operator-selection)).
2. **Beta decay channel**: The $e^- < 0$ coefficient in the confined nucleon normal form defines the categorical beta decay channel. This emerges directly from $\mathcal{B}_3$ confinement rather than being imposed.
3. **Confinement universality**: The nucleon normal form depends solely on $q_0$ and quark flavors, independent of photon polarization. The strong force erases electromagnetic initial conditions.
4. **Shell closure**: Hydrogen carries $\sigma_1 < 0$ demand (open shell). ${}^{3}\mathrm{He}$ achieves zero demand (closed shell). ${}^{4}\mathrm{He}$ yields a lower Markov trace, indicating tighter binding (doubly magic).

**Witness**: `confinement-operator-selection.witness.json`, `four-term-photon-to-atoms.witness.json`.
<!-- FILE_END: nucleon-from-photons-summary.md -->

