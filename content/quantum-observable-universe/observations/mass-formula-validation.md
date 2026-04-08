The atomic mass computation $M(Z,N) = Z\mathfrak{m}_\mathfrak{p} + N\mathfrak{m}_\mathfrak{n} + Zm_e - B(Z,N)$
uses CODATA nucleon masses and AME2020 binding energies as direct inputs.
This recombines observed constants and is trivially correct --- the
$<0.1$ MeV deviations in the mass table arise solely from rounding.

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

## Hecke-engine certificate validation

47 isotopes (${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$) have
exact Gröbner--Shirshov certificates from the hecke-engine. Each
certificate contains:

- $\mathrm{tr\_alt}(q_0)$: alternating trace of the Skein polynomial
- $\mathrm{net}(q_0)$: signed crossing sum
- $F_\mathrm{Pauli}(q_0)$: Pauli exclusion statistical weight

Key finding: the net values span $\sim$50 orders of magnitude
($\sim10^{-8}$ for ${}^{11}\mathrm{B}$ to $\sim10^{47}$ for
${}^{60}\mathrm{Co}$) while $B/A$ varies only between 0 and 9 MeV.
No simple linear mapping $\mathrm{net} \times E_0 = M$ exists across
all isotopes. The certificate fields encode *combinatorial crossing
structure*, not mass directly.

## The open problem: $B/A$ from $q$

Computing binding energy per nucleon purely from $q$ requires deriving
the nuclear Skein polynomial volume integral from the transfer matrix
chain, without importing AME2020 values. The transfer matrix product
$\prod_i \hat{V}_i(q)$ gives the Skein polynomial $P(q)$ whose
logarithm $\ln|P(q_0)|$ grows monotonically with $A$, but the
mapping $\ln|P| \to B/A$ is not yet established.

Potential approaches:
1. Volume integral: $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$
   works for individual knots (electron, muon). Extending to nuclear
   multi-body Skein polynomials requires integrating the
   $A$-nucleon crossing polynomial.
2. Spectral decomposition: the eigenvalues of the transfer matrix
   encode crossing energies. The binding energy may emerge as the
   difference between the interacting and free Skein polynomials.
3. Certificate polynomial roots: the tr\_alt polynomial's root
   structure at $q = q_0$ may encode binding through level repulsion.

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
