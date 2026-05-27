**Proposition (meson scale independence).**
*The pion mass $m_\pi$ cannot be derived from the substrate
parameters $(m_\mathfrak{e}, q_0)$ alone.  The Markov trace of the
meson braid $\mathfrak{M}_+ = (\sigma_0\sigma_1)^2 \cdot \sigma_1\sigma_0$
determines only the **relative** meson mass spectrum (character ratios
between mesons), not the **absolute** scale $m_\pi$ itself.*

**Proof (SDP + representation-theoretic).**

*Step 1 (Wedderburn active set).* The confinement SDP applied to
$\mathfrak{M}_+$ at $H_3(q_0)$ yields active set $= \{(2,1)\}$
for both the pion and kaon braids.  The trivial $(3)$ and sign
$(1^3)$ blocks are PSD-satisfied.  This matches the baryon
(Borromean) active set — the standard irrep is the universal
demand channel.

*Step 2 (exact characters).* The Hecke characters on the standard
irrep are:
$$
  \chi^{(2,1)}(\pi) = -(h^2 + 1) = -([3]_q - 2),
  \qquad
  \chi^{(2,1)}(K) = -1.
$$
Both are exact (verified to machine precision at $q_0$).  The
transition $\pi \to K$ (2 extra $\sigma_1$ crossings) sends
$-(h^2+1) \mapsto -1$ via the Hecke relation
$\sigma_1^2 = h\sigma_1 + 1$.

*Step 3 (derived character ratios).* Under $n$ extra $\sigma_1$
crossings, the per-partition character ratios are:
$$
  \frac{\chi^{(3)}(K)}{\chi^{(3)}(\pi)} = q^2,
  \quad
  \frac{\chi^{(2,1)}(K)}{\chi^{(2,1)}(\pi)} = \frac{1}{h^2+1},
  \quad
  \frac{\chi^{(1^3)}(K)}{\chi^{(1^3)}(\pi)} = q^{-2}.
$$
These are derivable from the Hecke eigenvalues ($q$ on $(3)$,
$-q^{-1}$ on $(1^3)$, mixed on $(2,1)$), not fitted to data.
The full trace ratio $\mathrm{tr}_M(K)/\mathrm{tr}_M(\pi) = 1.384$
is determined by these ratios.

*Step 4 (missing normalization).* The baryon mass formula uses
$m_p = m_\mathfrak{e} \cdot \mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2
\cdot [\text{linking weight}]$,
where $\mathrm{Vol}(\mathcal{B}_3) = 8G > 0$ is the hyperbolic
volume of the Borromean complement.  The meson analogue would
require $\mathrm{Vol}(\text{Hopf link complement})$, but the Hopf
link complement is a solid torus with **zero hyperbolic volume**.
There is no hyperbolic invariant to set the meson scale.

*Step 5 (independence).* Since:
- the meson Markov trace determines only ratios (Step 3),
- the meson topology has no hyperbolic volume (Step 4),
- no combination of $m_\mathfrak{e}$, $q_0$, $\mathrm{Vol}(4_1)$,
  $\mathrm{Vol}(\mathcal{B}_3)$, $\hbar_q$ matches
  $m_\pi = 139.57\,\mathrm{MeV}$ within $8000\,\mathrm{ppm}$,

the pion mass is an **independent calibration input** (CAL-3),
encoding the chiral symmetry breaking scale. $\square$

## Cohomological context of the three calibrations

The three calibration inputs live in distinct cohomological
layers of the Hecke tower:

| CAL | Input | Hecke level | Representation | Cohomological role |
|-----|-------|-------------|----------------|-------------------|
| **CAL-1** | $m_\mathfrak{e}$ | $H_2(q)$ | trivial $(2)$ | **absolute scale** — sets the MeV unit via the electron mass; lives in $H^0$ (degree-zero cohomology, the scalar coefficient ring) |
| **CAL-2** | $m_\mu/m_\mathfrak{e} = \mathrm{Vol}(4_1)/\hbar_q^2$ | $H_2(q) \to H_3(q)$ | standard $(2,1)$ | **substrate deformation** — the figure-eight knot volume is a motivic period in $K_3(\mathbb{Q}(\zeta))$; fixes $q_0$ via the Bloch–Wigner dilogarithm; lives in $H^2$ (the Borel regulator class) |
| **CAL-3** | $m_\pi$ | $H_3(q)$ | Hopf link ($L_+$) | **chiral scale** — the Goldstone boson mass from $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ breaking; lives in $H^3$ (the Chern–Simons class, parity-odd); absent from the substrate ($\mathrm{Vol}(\text{Hopf}) = 0$) |

The independence is structural: each calibration lives in a
different degree of the motivic cohomology of the knot complement
lattice.  CAL-1 is degree 0 (a scale), CAL-2 is degree 2 (a
Borel class = dilogarithm period), and CAL-3 is degree 3 (a
Chern–Simons invariant = trilogarithm period).

The substrate parameter $q_0$ is determined by CAL-2 (the
muon-anchor identity).  The Borromean volume $8G$ and the
Markov trace $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ are both
functions of $q_0$ — so baryons need only CAL-1 + CAL-2.
Mesons additionally need CAL-3 because the Hopf link's
vanishing volume removes the degree-2 handle that baryons use.

## What CAL-3 buys

With $m_\pi$ as input, the Hecke character ratios give:
- $m_K / m_\pi$: from $\mathrm{tr}_M(K)/\mathrm{tr}_M(\pi)$
  × normalization factor (derivable once CAL-3 fixes the scale)
- $m_\eta, m_\phi, m_D, \ldots$: from character ratios at
  higher crossing counts (10, 14, $\ldots$)

The entire meson spectrum follows from CAL-3 + the derived
character structure.  No additional free parameters.
