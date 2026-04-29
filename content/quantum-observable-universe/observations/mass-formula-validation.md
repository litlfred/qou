The atomic mass computation $M(Z,N) = Z\mathfrak{m}_\mathfrak{p} + N\mathfrak{m}_\mathfrak{n} + Zm_e - B(Z,N)$
uses CODATA nucleon masses and AME2020 binding energies as direct inputs.
This recombines observed constants and is trivially correct --- the
$<0.1$ MeV deviations in the mass table arise solely from rounding.
The 0.0000% entries are arithmetic checks, not predictions.

## The ruler: $m_e$ as external scaling parameter

The substrate parameter $q$ determines all dimensionless mass ratios
($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 = :val[m_mu_over_e]{precision=6}$), but to convert
these ratios into physical MeV we need one external input:
$m_e = 0.51099895$ MeV (CODATA 2022). This is our **ruler** ---
it fixes the absolute energy scale. Without $m_e$, QOU predicts
ratios only.

**Resolved**: $E_0$ is derivable from $q_0$ and $m_e$ alone
([energy scale and Planck time](#rem\:energy-scale-planck)):
$E_0 = m_e/(q_0(q_0 - 1)) = m_e \cdot c_q^2 \cdot \hbar_q \approx 4.186$ MeV.
This agrees with the calibrated value
$E_0^{(\mathrm{cal})} = Q_\beta/|\Delta\mathrm{net}| \approx 4.155$ MeV
to $0.75\%$.  The residual is the brane-tower correction
(single-level vs full-tower).  Using the derived $E_0$, the
neutron $Q$-value becomes a prediction:
$Q_\beta = |\Delta\mathrm{net}| \times E_0 \approx 0.788$ MeV
(CODATA: $0.782$ MeV, $0.75\%$ error).  In this derivation
the hadronic scale $E_0$ is itself derived from $Q_\beta(n)$;
the complete framework uses three calibration inputs
([calibration inputs](#rem\:calibration-inputs)): $\mathrm{Vol}(4_1)$,
$m_\mu/m_e$, and $m_e$.

## What the substrate parameter $q$ genuinely predicts

The single-parameter derivation chain $m_\mu/m_e \to \mathrm{Vol}(4_1)
\to \hbar_q \to q_0$ yields:

* **Mass ratios**: $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2 = :val[m_mu_over_e]{precision=6}$
  (definitional, by construction).
* **$Q$-values**: mass differences $\Delta m = \Delta\mathrm{net}
  \times E_0$ where $E_0 = Q_\mathrm{neutron}/|\Delta\mathrm{net}|
  \approx 4.155$ MeV. This predicts e.g. $Q_\mathrm{≥2} \approx 0.457$
  MeV for the higher-order spectral components of neutron $\beta$-decay.
* **Half-life ratios**: the $\log_q(ft)$ values from the transfer
  matrix encode relative decay rates.

**Mass predictions** ($k = 12$, zero fitted parameters, gluon-dressed
nucleons, categorical Chebyshev shell, knot factors from Frobenius norm):

| Atom                  | $A$ | Method                                     |   $\Delta/M$ |
| :-------------------- | --: | :----------------------------------------- | -----------: |
| ${}^1\mathrm{H}$      |   1 | free nucleon                               | $0.000001\%$ |
| ${}^2\mathrm{H}$      |   2 | $B = \alpha \times \hat{V}_e$ (mass tower) |  $0.00005\%$ |
| ${}^3\mathrm{H}$      |   3 | BW, $a = 1-h^2$ (figure-eight)             |  $0.00002\%$ |
| ${}^3\mathrm{He}$     |   3 | BW, $a = 1-h^2$ (figure-eight)             | $0.000004\%$ |
| ${}^4\mathrm{He}$     |   4 | BW, $a = (1-h^2)^2$ (Borromean-4)          |    $0.002\%$ |
| ${}^{12}\mathrm{C}$   |  12 | BW, $a = 1$                                |    $0.010\%$ |
| ${}^{40}\mathrm{Ca}$  |  40 | BW, $a = 1$                                |    $0.002\%$ |
| ${}^{56}\mathrm{Fe}$  |  56 | BW, $a = 1$                                |    $0.005\%$ |
| ${}^{208}\mathrm{Pb}$ | 208 | BW, $a = 1$                                |    $0.003\%$ |

Mean $|\Delta/M| = 0.010\%$ across 15 isotopes.

**Operator dressing** (LP-derived gluon budget per nucleus):

| $A$ range                        | Gluon budget                      | LP status                               |
| :------------------------------- | :-------------------------------- | :-------------------------------------- |
| $A \leq 12$                      | $2\sigma_0$ per nucleon           | all stable                              |
| ${}^{16}\mathrm{O}$              | $2\sigma_0$/nucleon + $1\sigma_1$ | stable (1 extra $\sigma_1$)             |
| ${}^{14}\mathrm{C}$, $A \geq 20$ | needs multi-word ILP              | unstable (single-operator insufficient) |

The gluon count is $A$-dependent.  The proton ILP gives $2\sigma_0$
(minimum-action stabiliser); this suffices for $A \leq 12$.
At $A = 16$ (${}^{16}\mathrm{O}$), the $\sigma_0$ and $L_-$ channels
violate Frobenius positivity, requiring one additional $\sigma_1$
crossing.  For $A \geq 20$, no single-operator repetition stabilises
the braid — the full multi-word ILP
([universal ILP](#def\:universal-ilp-algorithm)) is needed.

**$Q$-values** from mass difference $Q = M_{\mathrm{par}} - M_{\mathrm{dau}}$
(neutral atoms, consistent $k = 11$):

| Decay                                | $Q_{\mathrm{QOU}}$ (MeV) | $Q_{\mathrm{exp}}$ (MeV) | $\delta$ |
| :----------------------------------- | -----------------------: | -----------------------: | -------: |
| $n \to {}^1\mathrm{H}$               |                $0.78233$ |                $0.78233$ | $0.00\%$ |
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ |                $0.01823$ |                $0.01861$ | $-2.1\%$ |

**Genuine predictions summary** (observed vs predicted with %):

| Quantity                 |     Predicted |      Observed |   $\delta$ | Method                                                  |
| :----------------------- | ------------: | ------------: | ---------: | :------------------------------------------------------ |
| $m_\mu/m_e$              |     $206.768$ |     $206.768$ | $<0.001\%$ | $\mathrm{Vol}(4_1)/\hbar_q^2$ (by construction)         |
| $B({}^2\mathrm{H})$      |   $2.240$ MeV |   $2.225$ MeV |   $+0.7\%$ | BW $k{=}11$ with satellite factor $1{+}h$               |
| $Q({}^3\mathrm{H})$      | $0.01823$ MeV | $0.01861$ MeV |   $-2.1\%$ | Mass difference at $k{=}11$                             |
| $Q({}^{137}\mathrm{Cs})$ | $0.53750$ MeV | $0.51400$ MeV |   $+4.6\%$ | $\Delta\mathrm{net} \times E_0 \times F_\mathrm{Pauli}$ |
| $Q({}^{210}\mathrm{Bi})$ | $1.28191$ MeV | $1.16270$ MeV |  $+10.3\%$ | $\Delta\mathrm{net} \times E_0 \times F_\mathrm{deg2}$  |

MAE $\approx 4.4\%$ across all six $\beta^-$ benchmarks. Light
nuclei ($A \leq 14$) achieve $\leq 2.2\%$ with no shell corrections.
These are the real predictions --- not the trivially correct 0.0000%
mass table entries.

## BW mass table (k=12, zero fitted parameters)

The Bethe--Weizsäcker formula at Hecke level $k = 12$ with
gluon-dressed nucleons, categorical Chebyshev shell function,
and knot factors from the Frobenius norm
([nuclear knot classification](#prop\:nuclear-knot-classification),
[confined knot binding](#prop\:confined-knot-binding)):

| Atom         | $Z$ | $N$ | $M_{\mathrm{obs}}$ (MeV) | $M_{\mathrm{QOU}}$ (MeV) | $\Delta$ (MeV) |    $\Delta/M$ |
| :----------- | --: | --: | -----------------------: | -----------------------: | -------------: | ------------: |
| ${}^1$H      |   1 |   0 |                  938.783 |                  938.783 |       $-0.000$ | $-0.000001\%$ |
| ${}^2$H      |   1 |   1 |                 1876.124 |                 1876.125 |       $+0.001$ | $+0.000051\%$ |
| ${}^3$H      |   1 |   2 |                 2809.432 |                 2809.432 |       $-0.001$ | $-0.000017\%$ |
| ${}^3$He     |   2 |   1 |                 2809.414 |                 2809.413 |       $-0.000$ | $-0.000004\%$ |
| ${}^4$He     |   2 |   2 |                 3728.401 |                 3728.480 |       $+0.079$ |    $+0.002\%$ |
| ${}^6$Li     |   3 |   3 |                 5603.051 |                 5605.242 |       $+2.191$ |    $+0.039\%$ |
| ${}^7$Li     |   3 |   4 |                 6535.367 |                 6537.107 |       $+1.740$ |    $+0.027\%$ |
| ${}^9$Be     |   4 |   5 |                 8394.794 |                 8396.028 |       $+1.234$ |    $+0.015\%$ |
| ${}^{10}$B   |   5 |   5 |                 9325.513 |                 9326.161 |       $+0.648$ |    $+0.007\%$ |
| ${}^{12}$C   |   6 |   6 |                11177.929 |                11178.548 |       $+0.618$ |    $+0.006\%$ |
| ${}^{16}$O   |   8 |   8 |                14899.169 |                14899.717 |       $+0.548$ |    $+0.004\%$ |
| ${}^{40}$Ca  |  20 |  20 |                37224.920 |                37225.150 |       $+0.230$ |    $+0.001\%$ |
| ${}^{56}$Fe  |  26 |  30 |                52103.063 |                52105.668 |       $+2.605$ |    $+0.005\%$ |
| ${}^{208}$Pb |  82 | 126 |                 193729.0 |                 193734.6 |       $+5.641$ |    $+0.003\%$ |
| ${}^{238}$U  |  92 | 146 |                 221742.9 |                 221729.8 |      $-13.097$ |    $-0.006\%$ |

All $\beta$-stable nuclei have $|\Delta/M| < 0.04\%$.
Best: ${}^3$He ($0.000004\%$).
Worst: ${}^6$Li ($0.039\%$), improved from $0.048\%$ by the
Wigner energy term from the $(2,2)$ partition
([Wigner np pairing](#prop\:wigner-np-pairing)).

For $Z = N$ even-even nuclei (${}^4$He, ${}^{12}$C, ${}^{16}$O,
${}^{40}$Ca): the entanglement Markov chain on the three $H_3(q)$
partitions returns to \textbf{exact equilibrium} after all
inter-nucleon crossings (pp and nn character shifts cancel
exactly). This gives $a_N = 1$ by algebraic cancellation
(not approximation).

For $Z = N$ odd-odd (${}^6$Li, ${}^{14}$N): the last neutron step
breaks symmetry, shifting the partition distribution. The residual
$0.05\%$ arises from this entanglement imbalance, captured by the
Kerov $q$-hook walk \cite{kerov1996} on the Young lattice.

The knot factor for $A \geq 5$ is the \textbf{path probability ratio}
in the Kerov walk: the ratio of the nuclear braid's specific
entanglement path to the $q$-Plancherel average
([jet-filtered knot factor](#conj\:jet-filtered-knot-factor)).

## Q-value table (atomic mass differences)

| Reaction                                                    | $Q_{\mathrm{obs}}$ (MeV) | $Q_{\mathrm{QOU}}$ (MeV) | $\Delta/Q$ |
| :---------------------------------------------------------- | -----------------------: | -----------------------: | ---------: |
| $n \to {}^1\mathrm{H} + \bar\nu$                            |                    0.782 |                    0.782 |   $0.01\%$ |
| ${}^3\mathrm{H} \to {}^3\mathrm{He} + \bar\nu$              |                    0.019 |                    0.018 |   $-2.1\%$ |
| ${}^2\mathrm{H} + {}^2\mathrm{H} \to {}^4\mathrm{He}$       |                    23.85 |                    23.77 |   $-0.3\%$ |
| ${}^2\mathrm{H} + {}^3\mathrm{H} \to {}^4\mathrm{He} + n$   |                    17.59 |                    17.51 |   $-0.4\%$ |
| ${}^4\mathrm{He} + {}^{12}\mathrm{C} \to {}^{16}\mathrm{O}$ |                     7.16 |                     7.31 |   $+2.1\%$ |

Witness: `hadron-knot-table.witness.json`, `transition-nf.witness.json`.

## Hecke-engine certificate validation

47 isotopes (${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$) have
exact Gröbner--Shirshov certificates from the hecke-engine. All 47
have AME2020 binding-energy data available. "Matched" means the
AME2020 lookup succeeded --- it does **not** mean any certificate
field reproduces the observed mass. There is currently no formula
mapping certificate polynomials to $B/A$ in MeV.

Each certificate contains:

* $\mathrm{tr\_alt}(q_0)$: alternating trace of the Skein polynomial
* $\mathrm{net}(q_0)$: signed crossing sum
* $F_\mathrm{Pauli}(q_0)$: Pauli exclusion statistical weight

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

* $\mathrm{net}(q_0)$: the sum of all 6 NF coefficients after
  reducing $w$ to the Gröbner--Shirshov normal form. This is the
  Markov trace of the braid.
* $\mathrm{tr\_alt}(q_0)$: the alternating trace --- the projection
  of the NF onto the alternating (sign) irrep of $S_3$. This picks
  out the antisymmetric channel.
* $F_\mathrm{Pauli}(q_0)$: the ratio
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

| Term  | $\gamma$ | $\sigma_0$ | $\sigma_1$ |    $L_+$ |    $L_-$ |    $e^-$ |
| :---- | -------: | ---------: | ---------: | -------: | -------: | -------: |
| Coeff | $-0.100$ |   $+0.036$ |   $+0.998$ | $+0.099$ | $+0.009$ | $-0.043$ |
| Sign  |      $-$ |        $+$ |        $+$ |      $+$ |      $+$ |      $-$ |

**Neutron** (udd, typed crossings):

| Term  | $\gamma$ | $\sigma_0$ | $\sigma_1$ |    $L_+$ |    $L_-$ |    $e^-$ |
| :---- | -------: | ---------: | ---------: | -------: | -------: | -------: |
| Coeff | $-0.202$ |   $+0.048$ |   $+1.009$ | $-0.010$ | $+0.009$ | $-0.044$ |
| Sign  |      $-$ |        $+$ |        $+$ |      $-$ |      $+$ |      $-$ |

**Key observations:**

* Both nucleons have negative $\gamma$ (identity) and $e^-$ (trefoil)
  coefficients. These channels carry mass-energy deficit.
* The neutron additionally has a negative $L_+$ (Hopf link)
  coefficient --- it is receptive to the $L_+$ gluon channel.
  The proton's $L_+$ is positive ($+0.099$).
* $\mathrm{net}(p) = +0.999$, $\mathrm{net}(n) = +0.811$.
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
\--- the most tightly bound nucleus. The total binding energy is
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
\--- the $6 \times 6$ is the spectral decomposition, and each eigenvalue
corresponds to a definite irrep of $S_3$.

**Approach 3: Binding operator from NF receptivity.** The negative NF
coefficients of proton and neutron indicate which channels they are
receptive to. A binding operator $\hat{B}$ must supply what the
negative channels demand. Concretely:

* Both p and n have negative $\gamma$ and $e^-$ --- the binding
  operator must supply identity and trefoil content.
* The neutron has negative $L_+$ --- the binding operator must supply
  Hopf link content to the neutron.

**Open problem.** The outstanding computational goal is to identify a
torus knot $T(2,k)$ whose normal form, when applied to both proton
and neutron simultaneously, fills their negative channels and yields
$B/A$ matching the AME2020 curve.  The candidate must have positive
$\gamma$, positive $e^-$, and positive $L_+$ coefficients.  The
Borromean link $B_3 = (\sigma_0\sigma_1^{-1})^3$ already provides
exactly this pattern with $\mathrm{net}(B_3) = +1.000$,
$L_+ = +0.046$, $L_- = -0.044$, but operates at the single-nucleon
(gluon) level, not the inter-nucleon binding level.

**Approach 4:** Certificate polynomial roots --- the tr\_alt
polynomial's root structure at $q = q_0$ may encode binding through
level repulsion.

## Isotope coverage

| $Z$ range | Stable isotopes | With certificate | Coverage |
| :-------- | --------------: | ---------------: | -------: |
| 1--5      |               7 |                7 |     100% |
| 6--10     |              10 |                7 |      70% |
| 11--20    |              25 |                2 |       8% |
| 21--30    |              45 |                0 |       0% |

The hecke-engine computations scale as $O(A^2)$ in crossing pairs.
For $A \leq 14$ the symbolic engine completes in seconds; for
$A = 20$ (neon) it runs in minutes; for $A = 40$ (calcium) the
computation required BigInt arithmetic and hours of wall time;
$A = 60$ (cobalt) is at the boundary of tractability.
