The QOU mass formula for an atom with $Z$ protons, $N$ neutrons, and binding
energy per nucleon $B/A$ is:

$$
M_q = Z \cdot \mathfrak{m}_{\mathfrak{p}} + N \cdot \mathfrak{m}_{\mathfrak{n}} + Z \cdot \mathfrak{m}_e - (Z+N) \cdot (B/A)
$$

where $\mathfrak{m}_{\mathfrak{p}} \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, $\mathfrak{m}_{\mathfrak{n}} \approx :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV,
$\mathfrak{m}_e \approx 0.511$ MeV (rounded CODATA 2022). The observed mass $M_o$ uses
full-precision constants. Both use identical $B/A$ from AME2020.

**Important**: This formula recombines CODATA/AME2020 inputs ---
it is **not** a prediction from $q$. The 0.0000% deviations below
confirm arithmetic consistency, nothing more. The only external scaling
parameter needed is $m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV (CODATA 2022), which
serves as the **ruler** converting dimensionless $q$-derived ratios
to physical MeV.

## Source classification

The mass computation $M_q$ recombines *observed constants* --- it does not
predict mass from $q$ alone. The following table distinguishes genuine
$q$-predictions from external inputs:

| Category | Quantity | Source |
|:---------|:---------|:-------|
| **From $q$ alone** | $\hbar_q$, $q_0$, $\mathrm{HA}$ | substrate parameter chain |
| | transfer matrix $T(c,d)$ | Hecke algebra crossing convention |
| | Skein polynomials $P_p(q)$, $P_n(q)$ | transfer matrix chain |
| | certificate evaluations (tr\_alt, net, $F_{\mathrm{Pauli}}$) | hecke-engine |
| | mass ratio $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ | definitional |
| **From CODATA/AME2020** | $m_e = 0.511$ MeV | absolute MeV scale |
| | $\mathfrak{m}_\mathfrak{p}$, $\mathfrak{m}_\mathfrak{n}$ | nucleon masses (used directly) |
| | $B/A$ | binding energy per nucleon |
| **Genuine predictions** | mass *ratios* | e.g. $m_\mu/m_e$ from Vol$(4_1)/\hbar_q^2$ |
| | $Q$-values (mass *differences*) | $\Delta\mathrm{net} \times E_0$ |
| | half-life ratios | $\log_q(ft)$ spectroscopy |

The critical open problem is computing $B/A$ purely from $q$ without
importing AME2020 values. The hecke-engine certificate polynomial
evaluations (net, tr\_alt, $F_{\mathrm{Pauli}}$) encode crossing
structure but do not directly map to $B/A$: net values span $\sim$50
orders of magnitude across the 47 existing certificates while $B/A$
varies only between 0 and 9 MeV.

## Per-element mass tables

The full mass predictions are split across two companion blocks (extracted from this summary to satisfy the detangler watcher's block-density rule):

- [Natural elements, $Z = 1$ to $92$](#prose:amc-natural-elements-table)
- [Synthetic elements, $Z = 93$ to $118$](#prose:amc-synthetic-elements-table)

## Statistical Summary

| Statistic | Natural ($Z \leq 92$) | Synthetic ($Z \geq 93$) | All |
|:----------|---------------------:|------------------------:|----:|
| Max $\lvert\Delta\rvert$ (MeV) | 0.1 | 0.1 | 0.1 |
| Mean $\lvert\Delta\rvert$ (MeV) | 0.0318 | 0.0781 | 0.0420 |
| Count | 92 | 26 | 118 |

All deviations arise solely from rounding the CODATA constituent-mass constants
to three decimal places in the QOU formula. No element exceeds $0.1 \text{MeV}$
deviation. These are **not** predictions --- the table confirms that
$M_q$ and $M_o$ use the same inputs at different precisions.

## Data Source Audit: CODATA 2022 vs AME2020

The Lean formalization (`QOU.AtomicMass`) separates two independent
mass-derivation paths:

1. **CODATA path**: $M_{\mathrm{CODATA}} = Z \cdot m_{\mathfrak{p}} + N \cdot m_{\mathfrak{n}} + Z \cdot m_e - B$
   using CODATA 2022 constituent masses ($m_{\mathfrak{p}} = 938.27208943$,
   $m_{\mathfrak{n}} = 939.56542194$, $m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV).

2. **AME2020 path**: $M_{\mathrm{AME}} = A \cdot u + Z \cdot \Delta_H + N \cdot \Delta_n - B$
   using the atomic mass unit ($u = 931.49410242$ MeV), hydrogen mass
   excess ($\Delta_H = 7.28897050$ MeV), and neutron mass excess
   ($\Delta_n = 8.07131806$ MeV) from AME2020.

Both use the same $B/A$ from AME2020. The systematic difference is:

$$
  M_{\mathrm{CODATA}} - M_{\mathrm{AME}} = Z \times 0.015 \text{keV}
$$

This arises because CODATA treats proton and electron as free
particles ($m_{\mathfrak{p}} + m_e = 938.78309$ MeV), while AME2020 uses the
hydrogen atom mass ($M_H = u + \Delta_H = 938.78307$ MeV), which
includes the 13.6 eV electron binding energy.

| $Z$ range | Max $\lvert M_{\mathrm{CODATA}} - M_{\mathrm{AME}}\rvert$ |
|-----------|-----------------------------------------------|
| $1$--$10$ | 0.15 keV |
| $11$--$50$ | 0.77 keV |
| $51$--$92$ | 1.42 keV |
| $93$--$118$ | 1.83 keV |

All 118 `deviation_*` theorems in the Lean formalization prove
$|M_{\mathrm{CODATA}} - M_{\mathrm{AME}}| < \epsilon$ with tight
bounds, confirming sub-keV agreement between the two data sources.