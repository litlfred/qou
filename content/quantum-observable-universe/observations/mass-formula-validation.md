The atomic mass formula $M(Z,N) = Z\mathfrak{m}_\mathfrak{p} + N\mathfrak{m}_\mathfrak{n} + Zm_e - B(Z,N)$
inputs CODATA nucleon masses and AME2020 binding energies directly.
This recombination of observed constants is tautological. The
$<0.1$ MeV deviations in the mass table arise solely from rounding.
The 0.0000% entries are arithmetic checks, not predictions.

## The ruler: $m_e$ as external scaling parameter

The substrate parameter $q$ determines all dimensionless mass ratios
($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 = :val[m_mu_over_e]{precision=6}$). Converting
these ratios into physical units requires one external input:
$m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV (CODATA 2022). This ruler
fixes the absolute energy scale. Without $m_e$, the framework predicts
only mass ratios.

We derive the hadronic scale $E_0$ from $q_0$ and $m_e$
([energy scale and Planck time](#rem:energy-scale-planck)):
$E_0 = m_e/(q_0(q_0 - 1)) = m_e \cdot c_q^2 \cdot \hbar_q \approx 4.186$ MeV.
This value agrees with the calibrated scale
$E_0^{(\mathrm{cal})} = \mathfrak{Q}_\beta/|\Delta\mathrm{net}| \approx 4.155$ MeV
to $0.75\%$. The residual stems from the brane-tower correction
(single-level versus full-tower). With the derived $E_0$, the
neutron $Q$-value is a prediction:
$\mathfrak{Q}_\beta = |\Delta\mathrm{net}| \times E_0 \approx 0.788$ MeV
(CODATA: $0.782$ MeV). The complete framework relies on three calibration inputs
([calibration inputs](#rem:calibration-inputs)): $\mathrm{Vol}(4_1)$,
$m_\mu/m_e$, and $m_e$.

## Genuine predictions of the substrate parameter $q$

The derivation chain $m_\mu/m_e \to \mathrm{Vol}(4_1)
\to \hbar_q \to q_0$ yields:

- **Mass ratios**: $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 = :val[m_mu_over_e]{precision=6}$
 (definitional, by construction).
- **$Q$-values**: mass differences $\Delta m = \Delta\mathrm{net}
  \times E_0$ where $E_0 = Q_\mathrm{neutron}/|\Delta\mathrm{net}|
  \approx 4.155$ MeV. This predicts e.g. $Q_{\mathrm{n}\ge 2} \approx 0.457$
 MeV for the higher-order spectral components of neutron $\beta$-decay.
- **Half-life ratios**: the $\log_q(ft)$ values from the transfer
 matrix encode relative decay rates.

**Mass predictions** ($k = 12$, zero fitted parameters, gluon-dressed
nucleons, categorical Chebyshev shell, knot factors from Frobenius norm):

See [Table 1](#tbl:mass-formula-validation-table1-data).

Mean $|\Delta/M| = 0.010\%$ across 15 isotopes.

**Operator dressing** (LP-derived gluon budget per nucleus):

See [Table 2](#tbl:mass-formula-validation-table2-data).

The gluon count depends on $A$. The proton ILP yields $2\sigma_0$
(minimum-action stabiliser), sufficing for $A \leq 12$.
At $A = 16$ (${}^{16}\mathrm{O}$), the $\sigma_0$ and $L_-$ channels
violate Frobenius positivity, forcing one additional $\sigma_1$
crossing. For $A \geq 20$, no single-operator repetition stabilises
the braid; we require the full multi-word ILP
([universal ILP](#def:universal-ilp-algorithm)).

**$Q$-values** from mass difference $Q = M_{\mathrm{par}} - M_{\mathrm{dau}}$
(neutral atoms, consistent $k = 11$):

See [Table 3](#tbl:mass-formula-validation-table3-data).

**Genuine predictions summary** (observed vs predicted with %):

See [Table 4](#tbl:mass-formula-validation-table4-data).

MAE is approximately $4.4\%$ across all six $\beta^-$ benchmarks. Light
nuclei ($A \leq 14$) achieve $\leq 2.2\%$ without shell corrections.
These are genuine predictions, distinct from the tautological 0.0000%
mass table entries.

## BW mass table (k=12, zero fitted parameters)

The Bethe--Weizsäcker formula at Hecke level $k = 12$ with
gluon-dressed nucleons, categorical Chebyshev shell function,
and knot factors from the Frobenius norm
([nuclear knot classification](#prop:nuclear-knot-classification),
[confined knot binding](#prop:confined-knot-binding)):

See [Table 5](#tbl:mass-formula-validation-table5-data).

All $\beta$-stable nuclei satisfy $|\Delta/M| < 0.04\%$.
The ${}^3$He mass is most accurate ($0.000004\%$).
The ${}^6$Li mass is least accurate ($0.039\%$), though the
Wigner energy term from the $(2,2)$ partition improves this
from $0.048\%$ ([Wigner np pairing](#prop:wigner-np-pairing)).

For $Z = N$ even-even nuclei (${}^4$He, ${}^{12}$C, ${}^{16}$O,
${}^{40}$Ca), the entanglement Markov chain on the three $H_3(q)$
partitions returns to exact equilibrium after all
inter-nucleon crossings. Proton-proton and neutron-neutron character shifts cancel
exactly, yielding $a_N = 1$ by algebraic identity rather than approximation.

For $Z = N$ odd-odd nuclei (${}^6$Li, ${}^{14}$N), the final neutron step
breaks symmetry and shifts the partition distribution. The residual
$0.05\%$ error stems from this entanglement imbalance. The
Kerov $q$-hook walk \cite{kerov1996} on the Young lattice captures this effect.

For $A \geq 5$, the knot factor is the path probability ratio
in the Kerov walk: the ratio of the nuclear braid's specific
entanglement path to the $q$-Plancherel average
([jet-filtered knot factor](#conj:jet-filtered-knot-factor)).

## Q-value table (atomic mass differences)

See [Table 6](#tbl:mass-formula-validation-table6-data).

Witness: `hadron-knot-table.witness.json`, `transition-nf.witness.json`.

## Hecke-engine certificate validation

We compute exact Gröbner--Shirshov certificates for 47 isotopes
(${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$). All 47
have AME2020 binding-energy data. "Matched" indicates successful
AME2020 lookup, not mass reproduction. We lack a direct formula
mapping certificate polynomials to $B/A$ in MeV.

Each certificate contains:

- $\mathrm{tr\_alt}(q_0)$: the alternating trace of the Skein polynomial.
- $\mathrm{net}(q_0)$: the signed crossing sum.
- $F_\mathrm{Pauli}(q_0)$: the Pauli exclusion statistical weight.

The $\mathrm{net}$ values span 50 orders of magnitude
(from $10^{-8}$ for ${}^{11}\mathrm{B}$ to $10^{47}$ for
${}^{60}\mathrm{Co}$), while $B/A$ varies only between 0 and 9 MeV.
No simple linear mapping $\mathrm{net} \times E_0 = M$ exists across
all isotopes. The certificate fields encode combinatorial crossing
structure rather than direct mass.

## Certificate fields and the $6 \times 6$ transfer matrix

The three certificate fields evaluate polynomials derived
from the $6 \times 6$ transfer matrix of $H_3(q)$. This matrix acts
on the full normal form basis
$\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$.
These correspond to the six reduced words of $S_3$:
$\{1, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$.

**Certificate field origins.** For a nuclear braid word $w$ with
$A$ nucleons:

- $\mathrm{net}(q_0)$: the sum of all six normal form coefficients after
  Gröbner--Shirshov reduction. This evaluates the Markov trace of the braid.
- $\mathrm{tr\_alt}(q_0)$: the projection of the normal form onto the
  alternating irrep of $S_3$. This isolates the antisymmetric channel.
- $F_\mathrm{Pauli}(q_0)$: the ratio $\mathrm{tr\_alt}/\mathrm{tr\_sym}$.
  This measures the Pauli exclusion statistical weight, suppressing
  symmetric configurations for identical fermions.

**Irrep decomposition.** The regular representation of $H_3(q)$
decomposes as:

$$
H_3(q) \cong V_\mathrm{sym}(1) \oplus V_\mathrm{std}(2) \oplus V_\mathrm{alt}(1)
$$

The dimensions sum to $1 + 2^2 + 1 = 6$. The standard irrep
appears with multiplicity two. The $6 \times 6$ transfer matrix captures
all three irreps. Earlier computations used a $2 \times 2$ matrix,
capturing only the symmetric irrep and one copy of the standard irrep,
entirely missing the alternating channel.

**Necessity of the full $6 \times 6$.** The adjoint representation
of the strong force requires all three channels. The $L_+$ and $L_-$
terms (Hopf links) carry the gluon field content. The $e^-$ term
(the trefoil $\sigma_0\sigma_1\sigma_0$, or longest element $w_0$)
carries the alternating irrep. Without the $6 \times 6$ matrix,
we cannot compute $F_\mathrm{Pauli}$, rendering nuclear shell effects invisible.

## Nucleon NF structure and binding receptivity

Each nucleon normal form in $H_3(q)$ has six coefficients.
Negative coefficients indicate a deficit; the nucleon is
receptive to absorbing these channels from a binding partner.

**Proton** (uud, typed crossings):

See [Table 7](#tbl:mass-formula-validation-table7-data).

**Neutron** (udd, typed crossings):

See [Table 8](#tbl:mass-formula-validation-table8-data).

**Key observations:**

- Both nucleons have negative $\gamma$ (identity) and $e^-$ (trefoil)
  coefficients. These channels carry mass-energy deficits.
- The neutron has a negative $L_+$ (Hopf link) coefficient, making
  it receptive to the $L_+$ gluon channel. The proton $L_+$
  coefficient is positive ($+0.099$).
- We have $\mathrm{net}(p) = +0.999$ and $\mathrm{net}(n) = +0.811$.
  The difference $\Delta\mathrm{net} = -0.188$ drives the neutron
  $\beta$-decay $Q$-value.

**Beta decay minimality.** Free neutron decay
$n \to p + e^- + \bar{\nu}$ is the simplest $\beta^-$ process.
It involves a single nucleon, free of nuclear environment or
Coulomb corrections. This minimality calibrates $E_0$ directly.
The next simplest decay is tritium
${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar{\nu}$, where the
spectator deuteron adds only a small correction.

## The open problem: $B/A$ from $q$

**Physics of $B/A$.** The binding energy per nucleon $B/A$ measures
nuclear cohesion. For free nucleons
(${}^1\mathrm{H}$), $B/A = 0$. For iron-56, $B/A \approx 8.79$ MeV.
The total binding energy is
$B = Z m_\mathfrak{p} + N m_\mathfrak{n} - M_\mathrm{nucleus}$,
the mass deficit between free constituents and the bound
nucleus. The $B/A$ curve varies smoothly, encoding the entire nuclear
landscape.

**Significance.** Currently, $B/A$ enters the mass formula as an
external AME2020 input. This makes $M(Z,N)$ tautological. Deriving
$B/A$ from the certificate polynomial $P(q_0)$ would elevate
$M(Z,N) = Z m_\mathfrak{p}(q) + N m_\mathfrak{n}(q) + Z m_e - A \cdot (B/A)(q)$
to a one-parameter prediction, using $m_e$ as the sole ruler.
This remains the central open computation in the mass programme.

**Current status.** Computing $B/A$ from $q$ requires evaluating
the nuclear Skein volume integral from the transfer matrix chain.
The transfer matrix product $\prod_i \hat{V}_i(q)$ yields
the Skein polynomial $P(q)$. While $\ln|P(q_0)|$ grows monotonically
with $A$, the precise mapping $\ln|P| \to B/A$ is unknown.

**Approach 1: Volume integral.** For a single knot $K$, mass is
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$.
For an $A$-nucleon system, non-abelian Stokes expands the
composite braid volume as a sum over crossings:

$$
\mathrm{Vol}(K_A) = \sum_{i < j}^A V_{ij}(q)
$$

Here $V_{ij}$ is the crossing volume between strands $i$ and
$j$, computed via the $6 \times 6$ transfer matrix.
Binding energy is the deficit:

$$
B(Z,N) = \sum_\mathrm{free} \mathrm{Vol}(K_i) - \mathrm{Vol}(K_A)
$$

This reduces to a simple sum because Gröbner reduction makes each
crossing site contribute independently.

**Approach 2: Spectral decomposition.**
The $6 \times 6$ transfer matrix eigenvalues encode crossing energies in
each irrep channel. Binding energy may emerge from the difference
between eigenvalues of the interacting and free Skein polynomials.
This tracks cross-channel traffic on the jet bundle.

**Approach 3: Binding operator from normal form receptivity.**
A binding operator $\hat{B}$ must supply the channels where nucleons
exhibit deficits:

- Both nucleons demand identity ($\gamma$) and trefoil ($e^-$) content.
- The neutron demands Hopf link ($L_+$) content.

The outstanding goal is to identify a torus knot $T(2,k)$ whose normal form
fills these deficits and reproduces the AME2020 $B/A$ curve.
The candidate requires positive $\gamma$, $e^-$, and $L_+$ coefficients.
The Borromean link $B_3 = (\sigma_0\sigma_1^{-1})^3$ provides
this pattern ($\mathrm{net}(B_3) = +1.000$,
$L_+ = +0.046$, $L_- = -0.044$), but it operates at the intra-nucleon gluon level.

**Approach 4: Certificate polynomial roots.** The root structure
of the alternating trace polynomial at $q = q_0$ may encode binding
via level repulsion.

## Isotope coverage

See [Table 9](#tbl:mass-formula-validation-table9-data).

The symbolic Hecke engine scales as $O(A^2)$ in crossing pairs.
Computations for $A \leq 14$ complete in seconds. Neon ($A = 20$)
requires minutes. Calcium ($A = 40$) demands BigInt arithmetic and
hours of computation. Cobalt ($A = 60$) marks the current boundary of tractability.
