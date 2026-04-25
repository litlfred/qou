The **proton** is the baryon with $2 + 1$ crossing partition:
two up quarks (positive orientation) and one down quark (negative
orientation) in the Borromean braid $\mathcal{B}_3$
([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{p} = \mathcal{B}_3(\mathfrak{u},\mathfrak{u},\mathfrak{d})
$$

where:

- $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the Borromean
  braid of three unknots threaded through coral tubes $(r,g,b)$
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
The inverse $\sigma_1^{-1} = \sigma_1 - H_A \mathbf{1}$
(from the Hecke relation $\sigma_i^2 = H_A \sigma_i + \mathbf{1}$,
where $H_A = q - q^{-1}$) gives
$\mathcal{B}_3 = (\sigma_0(\sigma_1 - H_A))^3$.
Expanding and reducing in $H_3(q)$ at $q_0 \approx 1.1100$:

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\mathbf{1}$ | $\gamma$ | $+0.9981$ |
| $\sigma_0$ | $\sigma_0$ | $-0.0095$ |
| $\sigma_1$ | $\sigma_1$ | $+0.0091$ |
| $\sigma_0\sigma_1$ | $L_+$ | $+0.0456$ |
| $\sigma_1\sigma_0$ | $L_-$ | $-0.0437$ |

$$
  \mathrm{net}(\mathcal{B}_3) = +1.0000
$$

The Hopf link terms $L_\pm$ are the gluon field:
$\mathcal{B}_3$ produces binding without any external
Hopf link factor.
Witness: `breit-wheeler-nucleon-nf.witness.json`.

**Step 2: typed crossings.**
The quark flavor determines the crossing eigenvalue in $H_3(q)$.
Each pair of quarks contributes a crossing on the generator
connecting their strands:

| Pair | Type | Crossing element |
|:---|:---|:---|
| $(0,1)$ | $\mathfrak{u}$-$\mathfrak{u}$ | $\sigma_0$ |
| $(0,2)$ | $\mathfrak{u}$-$\mathfrak{d}$ | $\sigma_0 - \tfrac{1}{2}H_A \mathbf{1}$ |
| $(1,2)$ | $\mathfrak{u}$-$\mathfrak{d}$ | $\sigma_1 - \tfrac{1}{2}H_A \mathbf{1}$ |

The $\mathfrak{u}$-$\mathfrak{u}$ crossing keeps eigenvalue $+q$;
$\mathfrak{d}$-type crossings carry a $-H_A$ shift
(eigenvalue $-q^{-1}$); mixed $\mathfrak{u}$-$\mathfrak{d}$
crossings get a half-shift $-\tfrac{1}{2}H_A$.

The proton is
$\mathfrak{p} = \mathcal{B}_3 \times \sigma_0
\times (\sigma_0 - \tfrac{1}{2}H_A)
\times (\sigma_1 - \tfrac{1}{2}H_A)
\times L_-$,
reduced at each step by Gröbner–Shirshov.

**LP stability constraint.**
The 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$
(without the gluon) violates Frobenius positivity:
$G x[\gamma] < 0$.  A single Hopf link $L_- = \sigma_1\sigma_0$
is the **minimum** additional structure that restores stability.
The gluon is not assumed — it is **required** by the LP dual.

The **integer LP dual** enumerates all feasible gluon
combinations (up to $3$ operations from
$\{\sigma_0, \sigma_1, L_+, L_-\}$, requiring Frobenius
stability at every intermediate step) and selects the one
with minimum $|\mathrm{tr}_M|$.  Among $40$ feasible
solutions, the optimum is $\sigma_0 \to \sigma_0$: two
bare $\sigma_0$ crossings, giving $11$ crossings total
($6$ B₃ + $3$ quarks + $2$ gluon) with
$|\mathrm{tr}_M| = 0.027$.

**Step 3: proton NF (with Hopf gluon).**
After typed crossings and Hopf link stabilisation at
$q_0 \approx 1.1100$:

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\mathbf{1}$ | $\gamma$ | $-0.0095$ |
| $\sigma_0$ | $\sigma_0$ | $-0.0472$ |
| $\sigma_1$ | $\sigma_1$ | $+0.0337$ |
| $\sigma_0\sigma_1$ | $L_+$ | $-0.1114$ |
| $\sigma_1\sigma_0$ | $L_-$ | $+0.1185$ |
| $\sigma_0\sigma_1\sigma_0$ | $e^-$ | $+1.0224$ |

$$
  \mathrm{net}(\mathfrak{p}) = +1.0065
$$

The dominant term is $e^- \approx +1.022$ — the Hopf
gluon link redistributes the NF weight from $\sigma_1$
to the trefoil channel.  The Hopf link content
$L_\pm \approx \pm 0.11$ is larger than the B₃-only
value ($\pm 0.045$), reflecting the additional gluon
binding.  The construction is LP stable at every
intermediate step.

**Mass.**
The proton mass comes from the hyperbolic volume of the
Borromean link:

$$
  \mathfrak{m}_{\mathfrak{p}} =
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  + \text{Skein corrections}
$$

The Skein corrections arise from the crossing asymmetry between
the $\mathfrak{u}$ and $\mathfrak{d}$ components.  The pair Skein formula gives:

$$
  \mathfrak{m}_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$: $\mathfrak{m}_{\mathfrak{p}}(q_0) \approx 938.272$ MeV, derived from the substrate parameter ([local substrate](#prop:local-substrate-q)).

**Coulomb charge.**
The proton carries net **positive crossing chirality**: two
positive-orientation unknots ($\mathfrak{u}$) outweigh one negative ($\mathfrak{d}$),
giving a net Coulomb charge

$$
  Q(\mathfrak{p}) = 2 \cdot (+\tfrac{2}{3}) + 1 \cdot (-\tfrac{1}{3}) = +1.
$$

**Computational backing.** The Borromean construction underlying
this definition is supported by witness data committed alongside
the paper: `folio-assistant/computations/borromean-axial-coupling.witness.json`
(the axial-coupling $g_A$ from $H_3(q_0)$ matches PDG 2024
$g_A = 1.2754$), `proton-braid-sweep-gg.witness.json` (proton
braid coefficients in the NF basis at $q_0$), and
`borromean-qvalue.py` (derivation of $q_0 \approx 1.10998$ from
Borromean topology). These are numerical witnesses, not formal
proofs — see also
[Borromean-quark conjecture](#conj:borromean-quark) and the
ground-ring annotation in `borromean-quark.lean`.
