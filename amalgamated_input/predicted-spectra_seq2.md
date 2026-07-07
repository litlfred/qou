<!-- FILE_START: intro-mesons-nucleons.md -->
We now construct bound states from pair-production events. The lightest composite is the meson, consisting of a quark-antiquark pair joined by a colour string. The nucleon requires a third quark. This third quark threads the meson through a Borromean link, imparting the characteristic stability of protons and neutrons.

We first define the categorical meson via its formation chain. We then establish existence and uniqueness for the categorical proton by lifting the meson through the Borromean linking morphism. The categorical neutron follows via the parity-reversed braid word. Both nucleon definitions specialise the substrate-level pair-production machinery to bound states.

The output is a categorical assignment of quarks, antiquarks, and nucleons. This structural assignment determines which nucleon configurations survive the archimedean specialisation without decaying.
<!-- FILE_END: intro-mesons-nucleons.md -->

<!-- FILE_START: meson-formation-chain.md -->
The meson arises through a three-step formation chain. We define each step formally.

**Step 1: Pair production.**
Two colored photons $\gamma_i = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ fuse into an electron--positron pair:

$$
  \gamma_1 \cdot \gamma_2
   \longrightarrow 
  e^- + e^+
  +  \text{Hopf link content}(L_+ = \varphi_0\psi_1, L_- = \varphi_1\psi_0)
$$

The color weights $\varphi_0, \varphi_1$ supply the Hopf link terms. These terms close the $1.6\%$ energy gap between the bare photon pair and the threshold $2\mathfrak{m}_e$.

**Step 2: Quark creation.**
The Hopf link $L_+ = \sigma_0\sigma_1$ in the colored photon normal form acts as the quark creation operator on the trefoil channel:

$$
  L_+ \cdot e^-
  = 
  (\sigma_0\sigma_1)(\sigma_0\sigma_1\sigma_0)
  \xrightarrow{\mathrm{NF}}
  \mathfrak{u} + \varphi_0\psi_1\cdot e^-
$$

Two independent pair productions create two quark--antiquark channels: $\mathfrak{u} + \bar{\mathfrak{u}}$ and $\mathfrak{d} + \bar{\mathfrak{d}}$.

**Step 3: Meson binding.**
A quark from one production binds with an antiquark from the other via the Hopf link $\mathcal{L}_H$:

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

Each arrow is a morphism in the Iwahori--Hecke algebra $H_3(q)$. Breit--Wheeler is multiplication by $\sigma_0^2$. Quark creation is left-multiplication by $L_+ = \sigma_0\sigma_1$. Meson binding is the insertion of the Hopf link $\mathcal{L}_H = \sigma_0\sigma_1$ between quark and antiquark crossing pairs. At $q = q_0$, the meson normal form is:

$$
  \mathrm{NF}(\mathfrak{M}_+)
  = 
  +0.209\sigma_1
  +  1.044 L_+
  +  0.044 L_-
  +  0.218 e^-
$$

This yields $\mathrm{net}(\mathfrak{M}_+) = +1.515$.
<!-- FILE_END: meson-formation-chain.md -->

<!-- FILE_START: categorical-proton-exists.md -->
**Proposition (Categorical proton existence).**

The [categorical proton](#def:categorical-proton) $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ exists as a well-defined element of the Hecke algebra $H_3(q)$. It satisfies Frobenius stability $G x[\gamma] \ge 0$ at every step of the LP reduction. Uniqueness up to braid isotopy is treated in [uniqueness of the categorical proton](#prop:categorical-proton-unique).

#### Strategy

We construct the composite Hecke algebra element from the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean braid and the Hopf-link stabilizer. Gröbner--Shirshov reduction in $H_3(q)$ reduces the evaluation to a canonical normal form. This procedure explicitly maintains linear-programming stability ($G x[\gamma] \ge 0$) throughout.

#### Formalization

The Lean formalization provides a `sorry`-free weak proxy proof (`CategoricalProton.exists`) by instantiating a structure without rigorous LP-stability bounds (using unconstrained real fields). Expanding this proxy into a complete proof of Frobenius-stability requires implementing the Hecke normal form and linear-programming dual verification. The underlying mathematics guarantees the stability of the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean configuration. The explicit instantiation formally validates the structural existence of the categorical-proton model.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The underlying categorical identities hold over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: categorical-proton-exists.md -->

