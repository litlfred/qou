The model takes the nucleon normal form (NF) to need no explicit gluon factors $L_\pm$ beyond the Borromean braid $B_3 = (\sigma_0\sigma_1^{-1})^3$. The reason is the double-counting argument in the Interpretation below. Five candidate models are compared here; the comparison does not test this choice, because the energy scale $E_0$ is fitted.

**Definition recall** ([Borromean baryon](#def:borromean-baryon)).
$B = \mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1}) \oplus \mathcal{L}_H$.
The three constituents are unknots; the Hopf link $\mathcal{L}_H$ binds them. Flavour is the crossing orientation of each unknot within $\mathcal{B}_3$: $\mathfrak{u} = \sigma$ (positive), $\mathfrak{d} = \sigma^{-1}$ (negative).

**Model definitions.**

| Model | Formula | Description |
|-------|---------|-------------|
| A | $B_3 \cdot \mathrm{cx}$ | Borromean only (no extra gluons) |
| B | $B_3 \cdot \prod [\sigma_i^2 \cdot \mathrm{cx}_{ij}]$ | Hopf gluon $\sigma_i^2$ per quark pair |
| C | $B_3 \cdot \sigma_0^2 \sigma_1^2 \cdot \mathrm{cx}$ | Global Hopf dressing |
| D | $B_3 \cdot L_+ \cdot \mathrm{cx}$ | Single $L_+$ element |
| E | $B_3 \cdot L_+ L_- \cdot \mathrm{cx}$ | $L_+L_-$ pair (both orientations) |

where $\mathrm{cx} = \mathrm{cx}(q_0,q_1) \cdot \mathrm{cx}(q_0,q_2) \cdot \mathrm{cx}(q_1,q_2)$ are the pairwise typed crossings ($\sigma$ for $\mathfrak{u}\mathfrak{u}$, $\sigma^{-1}$ for $\mathfrak{d}\mathfrak{d}$, $\tfrac{1}{2}(\sigma + \sigma^{-1})$ for $\mathfrak{u}\mathfrak{d}$).

**Table K.3: Nucleon NF comparison across gluon models.**

| Model | net$(\mathfrak{p})$ | net$(\mathfrak{n})$ | $\Delta$(n$-$p) | $\Delta \times E_0$ (MeV) | $E_0$ implied (MeV) |
|-------|:-------------------:|:-------------------:|:---------------:|:-------------------------:|:--------------------:|
| A | $+0.9991$ | $+0.8108$ | $-0.1883$ | $-0.7823$ | $4.155$ |
| B | $+1.8460$ | $+1.4939$ | $-0.3521$ | $-1.4628$ | $2.222$ |
| C | $+1.5116$ | $+1.2311$ | $-0.2805$ | $-1.1653$ | $2.789$ |
| D | $+1.2085$ | $+0.9993$ | $-0.2092$ | $-0.8693$ | $3.739$ |
| E | $+1.4704$ | $+1.1899$ | $-0.2805$ | $-1.1653$ | $2.789$ |

**CODATA reference:** $Q = m_{\mathfrak{n}} - m_{\mathfrak{p}} - m_e = -0.78233$ MeV.

The column $\Delta \times E_0$ uses $E_0 = 4.155$ MeV for every model, which is the value implied by Model A: $E_0 = Q/\Delta_A$ is fitted to the CODATA $Q$. Model A therefore reproduces CODATA by construction, and its row is not a test. $E_0$ is a fitted scale, not one of the calibrations CAL-1/2/3. With $E_0$ fixed this way the other models overshoot $|\Delta|$, giving $|Q| > 0.87$ MeV, so the table ranks the models only relative to Model A.

Quarks interact as single-crossing unknots, not as full three-crossing words (Definition 4.27.1): replacing each crossing with the electron word ($\sigma_0\sigma_1\sigma_0$ for $\mathfrak{u}$, $\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ for $\mathfrak{d}$) gives $\Delta \times E_0 = -2.51$ MeV at the same fitted $E_0$, about $3.2$ times Model A's value.

**Interpretation.**
The Borromean braid $B_3$ has NF:

$$
  B_3 = +0.998\,\mathbf{1} - 0.010\sigma_0 + 0.009\sigma_1 + 0.046L_+ - 0.044L_-
$$

The $L_+$ and $L_-$ terms constitute the Hopf link $\mathcal{L}_H$. The $\oplus$ operation in $B = \mathcal{B}_3 \oplus \mathcal{L}_H$ is intrinsic to the Borromean braid algebra, not an additional factor. Explicitly adding Hopf links (Models B–E) double-counts the gluon contribution. In Model A the braid $B_3 = (\sigma_0\sigma_1^{-1})^3$ carries both confinement ($\mathcal{B}_3$) and gluon binding ($\mathcal{L}_H$).

The model reads a zero signed gluon sum as baryon color neutrality; here the sum is $+0.046 - 0.044 = +0.002$, so $B_3$ does not meet it exactly at $q_0$, and no tolerance is fixed. The $\mathbf{1}$ term ($\approx +0.998$) places $B_3$ perturbatively close to the identity.

The Model A proton and neutron NF are:

$$
  \mathfrak{p} = B_3 \cdot \sigma(\mathfrak{u},\mathfrak{u})
  \cdot \tfrac{1}{2}(\sigma + \sigma^{-1})(\mathfrak{u},\mathfrak{d})
  \cdot \tfrac{1}{2}(\sigma + \sigma^{-1})(\mathfrak{u},\mathfrak{d})
$$

$$
  \mathrm{NF}(\mathfrak{p})
  = -0.100\,\mathbf{1} + 0.036\sigma_0 + 0.998\sigma_1 + 0.099L_+ + 0.009L_- - 0.043e^-
$$

$$
  \mathrm{NF}(\mathfrak{n})
  = -0.202\,\mathbf{1} + 0.048\sigma_0 + 1.009\sigma_1 - 0.010L_+ + 0.009L_- - 0.044e^-
$$

The proton has net $\approx +0.999$; the neutron has net $\approx +0.811$. Fitting the difference $\Delta \approx -0.188$ to the CODATA $Q$ gives the quark-level energy scale $E_0 = Q/\Delta \approx 4.155$ MeV. This is a fit.
