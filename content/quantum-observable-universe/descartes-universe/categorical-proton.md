The **proton** is the baryon with $2 + 1$ crossing partition:
two up quarks (positive orientation) and one down quark (negative
orientation) in the Borromean braid $\mathcal{B}_3$
([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{p}
  \;=\;
  \mathcal{B}_3(\mathfrak{u},\, \mathfrak{u},\, \mathfrak{d})
$$

where:

- $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the Borromean
  braid of three unknots threaded through coral tubes $(r, g, b)$
  ([color tube coordinates](#def:color-tube-coordinates)):
  two with positive crossing orientation ($\mathfrak{u}$,
  [up quark](#def:up-quark)) and one with negative orientation
  ($\mathfrak{d}$, [down quark](#def:down-quark)),

- $\mathcal{B}_3$ intrinsically contains Hopf link content
  ($L_+ \approx +0.046$, $L_- \approx -0.044$ in its NF) —
  this is the gluon field binding the three constituents
  (no separate Hopf link factor is needed),

- the $S_3$ permutation symmetry of the coral tubes ensures
  the definition is independent of the color assignment.

**Step 1: Borromean braid NF.**
The inverse $\sigma_1^{-1} = \sigma_1 - H_A \cdot \mathbf{1}$
(from the Hecke relation $\sigma_i^2 = H_A\,\sigma_i + \mathbf{1}$,
where $H_A = q - q^{-1}$) gives
$\mathcal{B}_3 = (\sigma_0(\sigma_1 - H_A))^3$.
Expanding and reducing in $H_3(q)$ at $q_0 \approx 1.1100$:

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\mathbf{1}$ | $\nu$ | $+0.9981$ |
| $\sigma_0$ | $H^0$ | $-0.0095$ |
| $\sigma_1$ | $H^1$ | $+0.0091$ |
| $\sigma_0\sigma_1$ | $L_+$ | $+0.0456$ |
| $\sigma_1\sigma_0$ | $L_-$ | $-0.0437$ |

$$
  \mathrm{net}(\mathcal{B}_3) \;=\; +1.0000
$$

The Hopf link terms $L_\pm$ are the gluon field:
$\mathcal{B}_3$ produces binding without any external
Hopf link factor.

**Step 2: typed crossings.**
The quark flavor determines the crossing eigenvalue in $H_3(q)$.
Each pair of quarks contributes a crossing on the generator
connecting their strands:

| Pair | Type | Crossing element |
|:---|:---|:---|
| $(0,1)$ | $\mathfrak{u}$-$\mathfrak{u}$ | $\sigma_0$ |
| $(0,2)$ | $\mathfrak{u}$-$\mathfrak{d}$ | $\sigma_0 - \tfrac{1}{2}H_A\cdot\mathbf{1}$ |
| $(1,2)$ | $\mathfrak{u}$-$\mathfrak{d}$ | $\sigma_1 - \tfrac{1}{2}H_A\cdot\mathbf{1}$ |

The $\mathfrak{u}$-$\mathfrak{u}$ crossing keeps eigenvalue $+q$;
$\mathfrak{d}$-type crossings carry a $-H_A$ shift
(eigenvalue $-q^{-1}$); mixed $\mathfrak{u}$-$\mathfrak{d}$
crossings get a half-shift $-\tfrac{1}{2}H_A$.

The proton is
$\mathfrak{p} = \mathcal{B}_3 \times \sigma_0
\times (\sigma_0 - \tfrac{1}{2}H_A)
\times (\sigma_1 - \tfrac{1}{2}H_A)$,
reduced at each step by Gröbner–Shirshov.

**Step 3: proton NF.**
After all three typed crossings at $q_0 \approx 1.1100$:

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\mathbf{1}$ | $\nu$ | $-0.0997$ |
| $\sigma_0$ | $H^0$ | $+0.0357$ |
| $\sigma_1$ | $H^1$ | $+0.9976$ |
| $\sigma_0\sigma_1$ | $L_+$ | $+0.0994$ |
| $\sigma_1\sigma_0$ | $L_-$ | $+0.0093$ |
| $\sigma_0\sigma_1\sigma_0$ | $e^-$ | $-0.0432$ |

$$
  \mathrm{net}(\mathfrak{p}) \;=\; +0.9991
$$

The dominant term is $H^1 \approx +0.998$, reflecting
the up-quark crossing on strand 1.  The two mixed
$\mathfrak{u}$-$\mathfrak{d}$ half-shifts drive $\nu$ negative
($+0.998 \to -0.100$) and produce a trefoil component
$e^- \approx -0.043$.  The $L_+$ and $L_-$ coefficients
change sign pattern relative to B₃, encoding the interplay
of flavor and color confinement.

**Mass.**
The proton mass comes from the hyperbolic volume of the
Borromean link:

$$
  m_{\mathfrak{p}}
  \;=\;
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  \;+\; \text{Skein corrections}
$$

The Skein corrections arise from the crossing asymmetry between
the $\mathfrak{u}$ and $\mathfrak{d}$ components.  The pair Skein formula gives:

$$
  m_{\mathfrak{p}}
  \;=\;
  \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$: $m_{\mathfrak{p}}(q_0) \approx 938.272$ MeV, derived from the substrate parameter ([local substrate](#prop:local-substrate-q)).

**Coulomb charge.**
The proton carries net **positive crossing chirality**: two
positive-orientation unknots ($\mathfrak{u}$) outweigh one negative ($\mathfrak{d}$),
giving a net Coulomb charge

$$
  Q(\mathfrak{p}) \;=\; 2 \cdot (+\tfrac{2}{3}) + 1 \cdot (-\tfrac{1}{3}) \;=\; +1.
$$
