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
