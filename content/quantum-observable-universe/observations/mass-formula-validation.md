The atomic mass computation $M(Z,N) = Z\mathfrak{m}_\mathfrak{p} + N\mathfrak{m}_\mathfrak{n} + Zm_e - B(Z,N)$
uses CODATA nucleon masses and AME2020 binding energies as direct inputs.
This recombines observed constants and is trivially correct --- the
$<0.1$ MeV deviations in the mass table arise solely from rounding.
The 0.0000% entries are arithmetic checks, not predictions.

## The ruler: $m_e$ as external scaling parameter

The substrate parameter $q$ determines all dimensionless mass ratios
($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 = 206.768$), but to convert
these ratios into physical MeV we need one external input:
$m_e = 0.51099895$ MeV (CODATA 2022). This is our **ruler** ---
it fixes the absolute energy scale. Without $m_e$, QOU predicts
ratios only.

**Resolved**: $E_0$ is derivable from $q_0$ and $m_e$ alone
([energy scale and Planck time](#rem:energy-scale-planck)):
$E_0 = m_e/(q_0(q_0 - 1)) = m_e \cdot c_q^2 \cdot \hbar_q \approx 4.186$ MeV.
This agrees with the calibrated value
$E_0^{(\mathrm{cal})} = Q_\beta/|\Delta\mathrm{net}| \approx 4.155$ MeV
to $0.75\%$.  The residual is the brane-tower correction
(single-level vs full-tower).  Using the derived $E_0$, the
neutron $Q$-value becomes a prediction:
$Q_\beta = |\Delta\mathrm{net}| \times E_0 \approx 0.788$ MeV
(CODATA: $0.782$ MeV, $0.75\%$ error).  No third calibration
input is needed.

## What the substrate parameter $q$ genuinely predicts

The single-parameter derivation chain $m_\mu/m_e \to \mathrm{Vol}(4_1)
\to \hbar_q \to q_0$ yields:

- **Mass ratios**: $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 = 206.768$
  (definitional, by construction).
- **$Q$-values**: mass differences $\Delta m = \Delta\mathrm{net}
  \times E_0$ where $E_0 = Q_\mathrm{neutron}/|\Delta\mathrm{net}|
  \approx 4.155$ MeV. This predicts e.g. $Q_\mathrm{≥2} \approx 0.457$
  MeV for the higher-order spectral components of neutron $\beta$-decay.
- **Half-life ratios**: the $\log_q(ft)$ values from the transfer
  matrix encode relative decay rates.

**Genuine predictions summary** (observed vs predicted with %):

| Quantity | Predicted | Observed | $\delta$ | Method |
|:---------|----------:|---------:|---------:|:-------|
| $m_\mu/m_e$ | $206.768$ | $206.768$ | $<0.001\%$ | $\mathrm{Vol}(4_1)/\hbar_q^2$ (by construction) |
| $Q({}^3\mathrm{H})$ | $0.01849$ MeV | $0.01861$ MeV | $-0.6\%$ | $\Delta\mathrm{net} \times E_0$ |
| $Q({}^{14}\mathrm{C})$ | $0.15300$ MeV | $0.15648$ MeV | $-2.2\%$ | $\Delta\mathrm{net} \times E_0$ |
| $Q({}^{90}\mathrm{Sr})$ | $0.55740$ MeV | $0.54590$ MeV | $+2.1\%$ | $\Delta\mathrm{net} \times E_0 \times F_\mathrm{deg2}$ |
| $Q({}^{60}\mathrm{Co})$ | $0.33856$ MeV | $0.31817$ MeV | $+6.4\%$ | $\Delta\mathrm{net} \times E_0 \times F_\mathrm{deg2}$ |
| $Q({}^{137}\mathrm{Cs})$ | $0.53750$ MeV | $0.51400$ MeV | $+4.6\%$ | $\Delta\mathrm{net} \times E_0 \times F_\mathrm{Pauli}$ |
| $Q({}^{210}\mathrm{Bi})$ | $1.28191$ MeV | $1.16270$ MeV | $+10.3\%$ | $\Delta\mathrm{net} \times E_0 \times F_\mathrm{deg2}$ |

MAE $\approx 4.4\%$ across all six $\beta^-$ benchmarks. Light
nuclei ($A \leq 14$) achieve $\leq 2.2\%$ with no shell corrections.
These are the real predictions --- not the trivially correct 0.0000%
mass table entries.

## Hecke-engine certificate validation

47 isotopes (${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$) have
exact Gröbner--Shirshov certificates from the hecke-engine. All 47
have AME2020 binding-energy data available. "Matched" means the
AME2020 lookup succeeded --- it does **not** mean any certificate
field reproduces the observed mass. There is currently no formula
mapping certificate polynomials to $B/A$ in MeV.

Each certificate contains:

- $\mathrm{tr\_alt}(q_0)$: alternating trace of the Skein polynomial
- $\mathrm{net}(q_0)$: signed crossing sum
- $F_\mathrm{Pauli}(q_0)$: Pauli exclusion statistical weight

Key finding: the net values span $\sim$50 orders of magnitude
($\sim10^{-8}$ for ${}^{11}\mathrm{B}$ to $\sim10^{47}$ for
${}^{60}\mathrm{Co}$) while $B/A$ varies only between 0 and 9 MeV.
No simple linear mapping $\mathrm{net} \times E_0 = M$ exists across
all isotopes. The certificate fields encode *combinatorial crossing
structure*, not mass directly.

## Certificate fields and the $6 \times 6$ transfer matrix

The three certificate fields are evaluations of polynomials derived
from the $6 \times 6$ transfer matrix of $H_3(q)$. The transfer
matrix acts on the full NF basis
$\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ (the 6 reduced
words of $S_3$, i.e. $\{1, \sigma_0, \sigma_1, \sigma_0\sigma_1,
\sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$).

**Certificate field origins.** For a nuclear braid word $w$ with
$A$ nucleons:

- $\mathrm{net}(q_0)$: the sum of all 6 NF coefficients after
  reducing $w$ to the Gröbner--Shirshov normal form. This is the
  Markov trace of the braid.
- $\mathrm{tr\_alt}(q_0)$: the alternating trace --- the projection
  of the NF onto the alternating (sign) irrep of $S_3$. This picks
  out the antisymmetric channel.
- $F_\mathrm{Pauli}(q_0)$: the ratio
  $\mathrm{tr\_alt}/\mathrm{tr\_sym}$, measuring the Pauli exclusion
  statistical weight. For identical fermions, $F_\mathrm{Pauli}$
  suppresses symmetric configurations.

**Irrep decomposition.** The regular representation of $H_3(q)$
decomposes into three irreps:

$$
H_3(q) \cong V_\mathrm{sym}(1) \oplus V_\mathrm{std}(2) \oplus V_\mathrm{alt}(1)
$$

where dimensions are $1 + 2^2 + 1 = 6$ (the standard irrep
appears with multiplicity 2 in the regular representation). The
$6 \times 6$ transfer matrix captures all three irreps simultaneously.
The $2 \times 2$ transfer matrix (used in earlier computations) only
captures the symmetric and one copy of the standard irrep, missing
the alternating channel entirely.

**Why the full $6 \times 6$ matters.** The adjoint representation
of the strong force requires all three channels. The $L_+$ and $L_-$
terms (Hopf links) carry the gluon field content. The $e^-$ term
(trefoil = $\sigma_0\sigma_1\sigma_0$, the longest element $w_0$)
carries the alternating irrep. Without the full $6 \times 6$, the
Pauli exclusion factor $F_\mathrm{Pauli}$ cannot be computed and
nuclear shell effects are invisible.

## Nucleon NF structure and binding receptivity

Each nucleon's NF in $H_3(q)$ has 6 coefficients with a characteristic
sign pattern. Negative coefficients indicate channels where the
nucleon has a *deficit* --- these are the channels it is receptive to
(can absorb from a binding partner).

**Proton** (uud, typed crossings):

| Term | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|:-----|-------:|--------:|--------:|------:|------:|------:|
| Coeff | $-0.100$ | $+0.036$ | $+0.998$ | $+0.099$ | $+0.009$ | $-0.043$ |
| Sign | $-$ | $+$ | $+$ | $+$ | $+$ | $-$ |

**Neutron** (udd, typed crossings):

| Term | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ |
|:-----|-------:|--------:|--------:|------:|------:|------:|
| Coeff | $-0.202$ | $+0.048$ | $+1.009$ | $-0.010$ | $+0.009$ | $-0.044$ |
| Sign | $-$ | $+$ | $+$ | $-$ | $+$ | $-$ |

**Key observations:**

- Both nucleons have negative $\gamma$ (identity) and $e^-$ (trefoil)
  coefficients. These channels carry mass-energy deficit.
- The neutron additionally has a negative $L_+$ (Hopf link)
  coefficient --- it is receptive to the $L_+$ gluon channel.
  The proton's $L_+$ is positive ($+0.099$).
- $\mathrm{net}(p) = +0.999$, $\mathrm{net}(n) = +0.811$.
  The $\Delta\mathrm{net} = -0.188$ drives the neutron $\beta$-decay
  $Q$-value.

**Beta decay: why free neutron is the simplest.** Free neutron decay
$n \to p + e^- + \bar{\nu}$ is the simplest possible $\beta^-$ decay:
a single nucleon, no nuclear environment, no Coulomb corrections.
This is why it calibrates $E_0$ directly. The next simplest is tritium
${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar{\nu}$, where the
spectator deuteron core adds only a small nuclear correction.

## The open problem: $B/A$ from $q$

**Physics of $B/A$.** The binding energy per nucleon $B/A$ measures
how tightly nucleons are bound inside a nucleus. For free nucleons
(${}^1\mathrm{H}$), $B/A = 0$. For iron-56, $B/A \approx 8.79$ MeV
--- the most tightly bound nucleus. The total binding energy is
$B = Z m_\mathfrak{p} + N m_\mathfrak{n} - M_\mathrm{nucleus}$,
i.e. the mass deficit between free constituents and the actual
nucleus. $B/A$ varies smoothly from 0 (hydrogen) through a peak
near iron to $\sim$7.6 (uranium), encoding the entire nuclear
landscape.

**Why this matters.** Currently, $B/A$ enters our mass formula as an
external AME2020 input, making $M(Z,N)$ a tautology. If $B/A$ could
be derived from the certificate polynomial $P(q_0)$, then
$M(Z,N) = Z m_\mathfrak{p}(q) + N m_\mathfrak{n}(q) + Z m_e - A \cdot (B/A)(q)$
would be a genuine one-parameter prediction (with $m_e$ as ruler).
This is the single most important open computation in the QOU mass
programme.

**Current status.** Computing $B/A$ purely from $q$ requires deriving
the nuclear Skein polynomial volume integral from the transfer matrix
chain, without importing AME2020 values. The transfer matrix product
$\prod_i \hat{V}_i(q)$ gives the Skein polynomial $P(q)$ whose
logarithm $\ln|P(q_0)|$ grows monotonically with $A$, but the
mapping $\ln|P| \to B/A$ is not yet established.

**Approach 1: Volume integral (non-abelian Stokes).** For a single
knot $K$, mass is $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$.
For a multi-nucleon system with $A$ nucleons, the non-abelian Stokes
theorem expands the volume integral over the composite braid as a sum
of crossing contributions:

$$
\mathrm{Vol}(K_A) = \sum_{i < j}^A V_{ij}(q)
$$

where $V_{ij}$ is the crossing volume between nucleon strands $i$ and
$j$. Each $V_{ij}$ is computed from the $6 \times 6$ transfer matrix
at the $(i,j)$ crossing site. The binding energy is the difference
between the interacting and free volumes:

$$
B(Z,N) = \sum_\mathrm{free} \mathrm{Vol}(K_i) - \mathrm{Vol}(K_A)
$$

This is a simple sum (not a path-ordered integral) because each
crossing site contributes independently to the total volume after
Gröbner reduction.

**Approach 2: Spectral decomposition (eigenvalues of $6 \times 6$).**
The eigenvalues of the transfer matrix encode crossing energies in
each irrep channel. The binding energy may emerge as the difference
between eigenvalues of the interacting vs free Skein polynomials.
This is the same as tracking cross-channel traffic on the jet bundle
--- the $6 \times 6$ is the spectral decomposition, and each eigenvalue
corresponds to a definite irrep of $S_3$.

**Approach 3: Binding operator from NF receptivity.** The negative NF
coefficients of proton and neutron indicate which channels they are
receptive to. A binding operator $\hat{B}$ must supply what the
negative channels demand. Concretely:

- Both p and n have negative $\gamma$ and $e^-$ --- the binding
  operator must supply identity and trefoil content.
- The neutron has negative $L_+$ --- the binding operator must supply
  Hopf link content to the neutron.

**TODO**: Find a torus knot $T(2,k)$ whose NF, when applied to
both proton and neutron simultaneously, fills their negative
channels and yields $B/A$ matching the AME2020 curve. The candidate
must have positive $\gamma$, positive $e^-$, and positive $L_+$
coefficients. The Borromean link $B_3 = (\sigma_0\sigma_1^{-1})^3$
already provides exactly this pattern with
$\mathrm{net}(B_3) = +1.000$, $L_+ = +0.046$, $L_- = -0.044$,
but operates at the single-nucleon (gluon) level, not the
inter-nucleon binding level.

**Approach 4:** Certificate polynomial roots --- the tr\_alt
polynomial's root structure at $q = q_0$ may encode binding through
level repulsion.

## Isotope coverage

| $Z$ range | Stable isotopes | With certificate | Coverage |
|:----------|----------------:|-----------------:|---------:|
| 1--5 | 7 | 7 | 100% |
| 6--10 | 10 | 7 | 70% |
| 11--20 | 25 | 2 | 8% |
| 21--30 | 45 | 0 | 0% |

The hecke-engine computations scale as $O(A^2)$ in crossing pairs.
For $A \leq 14$ the symbolic engine completes in seconds; for
$A = 20$ (neon) it runs in minutes; for $A = 40$ (calcium) the
computation required BigInt arithmetic and hours of wall time;
$A = 60$ (cobalt) is at the boundary of tractability.
