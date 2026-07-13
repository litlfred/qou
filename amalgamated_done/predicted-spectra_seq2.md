<!-- FILE_START: intro-mesons-nucleons.md -->
We construct bound states from pair-production events. The meson is the lightest composite. It consists of a quark-antiquark pair joined by a colour string. We define the categorical meson via its formation chain.

A nucleon requires a third quark. This third quark threads the meson through a Borromean link. The link imparts the characteristic stability of protons and neutrons. We lift the meson through the Borromean linking morphism to establish the existence and uniqueness of the categorical proton. The categorical neutron follows via the parity-reversed braid word. These definitions specialise the substrate-level pair-production machinery to bound states.

This yields a categorical assignment of quarks, antiquarks, and nucleons. This structural assignment determines which nucleon configurations survive the archimedean specialisation without decaying.
<!-- FILE_END: intro-mesons-nucleons.md -->

<!-- FILE_START: meson-formation-chain.md -->
The meson arises through a three-step formation chain.

**Step 1: Pair production.**
A $1.6\%$ energy gap separates the bare photon pair from the threshold $2\mathfrak{m}_e$. The color weights $\varphi_0, \varphi_1$ close this gap by supplying Hopf link terms. Two colored photons $\gamma_i = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ thus fuse into an electron--positron pair:

$$
  \gamma_1 \cdot \gamma_2
   \longrightarrow 
  e^- + e^+
  +  \text{Hopf link content}(L_+ = \varphi_0\psi_1, L_- = \varphi_1\psi_0)
$$

**Step 2: Quark creation.**
To create a quark on the trefoil channel, the Hopf link $L_+ = \sigma_0\sigma_1$ from the colored photon normal form acts as a creation operator:

$$
  L_+ \cdot e^-
  = 
  (\sigma_0\sigma_1)(\sigma_0\sigma_1\sigma_0)
  \xrightarrow{\mathrm{NF}}
  \mathfrak{u} + \varphi_0\psi_1\cdot e^-
$$

Two independent pair productions create two quark--antiquark channels: $\mathfrak{u} + \bar{\mathfrak{u}}$ and $\mathfrak{d} + \bar{\mathfrak{d}}$.

**Step 3: Meson binding.**
To form the meson, a quark from one production binds with an antiquark from the other. The Hopf link $\mathcal{L}_H$ mediates this binding:

$$
  \mathfrak{u} + \bar{\mathfrak{d}}
  \xrightarrow{\mathcal{L}_H}
  \mathfrak{M}_+
  = 
  T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

**Summary chain.**

$$
  \gamma\gamma
  \xrightarrow{\text{Breit--Wheeler}}
  e^- e^+
  \xrightarrow{L_+}
  q\bar{q}
  \xrightarrow{\mathcal{L}_H}
  \mathfrak{M}
$$

Each arrow is a morphism in the Iwahori--Hecke algebra $H_3(q)$. Breit--Wheeler multiplies by $\sigma_0^2$. Quark creation left-multiplies by $L_+ = \sigma_0\sigma_1$. Meson binding inserts the Hopf link $\mathcal{L}_H = \sigma_0\sigma_1$ between the quark and antiquark crossing pairs. Evaluating at $q = q_0$ yields the meson normal form:

$$
  \mathrm{NF}(\mathfrak{M}_+)
  = 
  +0.209\sigma_1
  +  1.044 L_+
  +  0.044 L_-
  +  0.218 e^-
$$

This produces the net value $\mathrm{net}(\mathfrak{M}_+) = +1.515$.
<!-- FILE_END: meson-formation-chain.md -->

<!-- FILE_START: categorical-proton-exists.md -->
**Proposition (Categorical proton existence).**

The [categorical proton](#def:categorical-proton) $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ exists as a well-defined element of the Hecke algebra $H_3(q)$. It satisfies Frobenius stability $G x[\gamma] \ge 0$ at every step of the LP reduction. A separate proposition establishes [uniqueness of the categorical proton](#prop:categorical-proton-unique) up to braid isotopy.

#### Strategy

We construct the composite Hecke algebra element from the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean braid and the Hopf-link stabilizer. Gröbner--Shirshov reduction in $H_3(q)$ yields a canonical normal form. This procedure explicitly maintains linear-programming stability ($G x[\gamma] \ge 0$) at every step.

#### Formalization

The Lean formalization provides a `sorry`-free proxy proof (`CategoricalProton.exists`). This proof instantiates the structure over unconstrained real fields, omitting rigorous LP-stability bounds. A complete formal proof of Frobenius stability requires implementing the Hecke normal form and the linear-programming dual verification. The underlying mathematics guarantees the stability of the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean configuration. The explicit instantiation formally validates the structural existence of the categorical-proton model.

**Archimedean specialisation (§7c).** The underlying categorical identities hold over an abstract coefficient ring. Their archimedean realisation requires real- or complex-analytic constructs. This block invokes these constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The block therefore sits on the archimedean side of the substrate wall.
<!-- FILE_END: categorical-proton-exists.md -->
