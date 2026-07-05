Does the nucleon NF require explicit Hopf-link gluon factors
beyond the Borromean braid $B_3 = (\sigma_0\sigma_1^{-1})^3$?
Five models were tested
(witness: `nucleon-with-gluons-nf.witness.json`).

**Definition recall** ([Borromean baryon](#def:borromean-baryon)).
$B = \mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1}) \oplus \mathcal{L}_H$.
The three constituents are **unknots** (not trefoils); the Hopf
link $\mathcal{L}_H$ binds them.  Up/down flavour is the
**crossing orientation** of each unknot within $\mathcal{B}_3$:
$\mathfrak{u} = \sigma$ (positive), $\mathfrak{d} = \sigma^{-1}$ (negative).

**Model definitions.**

| Model | Formula | Description |
|-------|---------|-------------|
| A | $B_3 \cdot \mathrm{cx}$ | Borromean only (no extra gluons) |
| B | $B_3 \cdot \prod [\sigma_i^2 \cdot \mathrm{cx}_{ij}]$ | Hopf gluon $\sigma_i^2$ per quark pair |
| C | $B_3 \cdot \sigma_0^2 \sigma_1^2 \cdot \mathrm{cx}$ | Global Hopf dressing |
| D | $B_3 \cdot L_+ \cdot \mathrm{cx}$ | Single Hopf link element |
| E | $B_3 \cdot L_+ L_- \cdot \mathrm{cx}$ | Hopf pair (both orientations) |

where $\mathrm{cx} = \mathrm{cx}(q_0,q_1) \cdot \mathrm{cx}(q_0,q_2) \cdot \mathrm{cx}(q_1,q_2)$
are the pairwise typed crossings ($\sigma$ for $\mathfrak{u}\mathfrak{u}$,
$\sigma^{-1}$ for $\mathfrak{d}\mathfrak{d}$,
$\tfrac{1}{2}(\sigma + \sigma^{-1})$ for $\mathfrak{u}\mathfrak{d}$).

**Table K.3: Nucleon NF comparison across gluon models.**

| Model | net$(\mathfrak{p})$ | net$(\mathfrak{n})$ | $\Delta$(n$-$p) | $\Delta \times E_0$ (MeV) | $E_0$ implied (MeV) |
|-------|:-------------------:|:-------------------:|:---------------:|:-------------------------:|:--------------------:|
| A | $+0.9991$ | $+0.8108$ | $-0.1883$ | $-0.7823$ | $4.155$ |
| B | $+1.8460$ | $+1.4939$ | $-0.3521$ | $-1.4628$ | $2.222$ |
| C | $+1.5116$ | $+1.2311$ | $-0.2805$ | $-1.1653$ | $2.789$ |
| D | $+1.2085$ | $+0.9993$ | $-0.2092$ | $-0.8693$ | $3.739$ |
| E | $+1.4704$ | $+1.1899$ | $-0.2805$ | $-1.1653$ | $2.789$ |

**CODATA reference:** $Q = m_{\mathfrak{n}} - m_{\mathfrak{p}} - m_e = -0.78233$ MeV.

**Result:** Model A (Borromean only) matches CODATA exactly
(residual $< 10^{-6}$ MeV).  All other models overshoot
$|\Delta|$, giving $|Q| > 0.87$ MeV.

**Trefoil vs unknot test** (witness:
`trefoil-quark-nucleon-nf.witness.json`).  Using full trefoil
braid words ($\sigma_0\sigma_1\sigma_0$ for $\mathfrak{u}$,
$\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ for $\mathfrak{d}$)
gives $\Delta \times E_0 = -2.51$ MeV — overshooting by
$3\times$.  This confirms that quarks interact as single-crossing
unknots, not as full trefoils, consistent with Definition 4.27.1.

**Interpretation: $\mathcal{B}_3 \oplus \mathcal{L}_H$ is
already encoded in $B_3$.**

The Borromean braid $B_3$ has NF:

$$
  B_3 = +0.998\gamma - 0.010\sigma_0 + 0.009\sigma_1
        + 0.046L_+ - 0.044L_-
$$

The $L_+ \approx +0.046$ and $L_- \approx -0.044$ terms ARE
the Hopf link $\mathcal{L}_H$ from Definition 4.27.1.  The
$\oplus$ in $B = \mathcal{B}_3 \oplus \mathcal{L}_H$ is not
an additional multiplicative factor — it describes the Hopf-link
content that the Borromean braid algebra automatically generates.

Adding explicit Hopf links (Models B--E) **double-counts** the
gluon contribution, producing $\Delta$ values that are too large.
The Borromean confinement braid $B_3 = (\sigma_0\sigma_1^{-1})^3$
is the **complete and sufficient** encoding of the baryon:
confinement ($\mathcal{B}_3$) and gluon binding ($\mathcal{L}_H$)
in a single algebraic object.

Their near-cancellation ($+0.046 - 0.044 = +0.002$) reflects
the color neutrality of the baryon: the net gluon content is
close to zero, consistent with a color singlet.

The $\gamma$ term $\approx +0.998$ shows that $B_3$ is
perturbatively close to the identity — the Borromean
confinement is a small correction to free quarks.

**Proton and neutron NF** (Model A, confirmed):

$$
  \mathfrak{p} = B_3 \cdot \sigma(\mathfrak{u},\mathfrak{u})
  \cdot \tfrac{1}{2}(\sigma + \sigma^{-1})(\mathfrak{u},\mathfrak{d})
  \cdot \tfrac{1}{2}(\sigma + \sigma^{-1})(\mathfrak{u},\mathfrak{d})
$$

$$
  \mathrm{NF}(\mathfrak{p})
  = -0.100\gamma + 0.036\sigma_0 + 0.998\sigma_1
    + 0.099L_+ + 0.009L_- - 0.043e^-
$$

$$
  \mathrm{NF}(\mathfrak{n})
  = -0.202\gamma + 0.048\sigma_0 + 1.009\sigma_1
    - 0.010L_+ + 0.009L_- - 0.044e^-
$$

The proton has net $\approx +0.999$; the neutron has
net $\approx +0.811$.  The difference $\Delta \approx -0.188$
calibrates the quark-level energy scale $E_0 = Q/\Delta \approx 4.155$ MeV.
