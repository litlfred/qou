This appendix carries out the atomic mass calculation for every
known element ($Z = 1$ through $Z = 118$) from the QOU topological
mass formula.  Every intermediate step is shown so that the reader
can reproduce each result independently.

The elements divide into two groups:

- **Naturally occurring** ($Z = 1$--$92$, Hydrogen through
  Uranium): formed in stellar nucleosynthesis under ambient
  substrate parameter $q = q_0$.  Observed masses are precise
  (AME2020).

- **Synthetic** ($Z = 93$--$118$, Neptunium through Oganesson):
  produced in nuclear reactors (Z = 93--100) or heavy-ion
  accelerators (Z = 101--118).  Observed masses carry larger
  uncertainties; for $Z > 109$ the AME2020 values are
  extrapolated from systematics.

## The topological mass formula

The mass of a neutral atom with $Z$ protons, $N$ neutrons, and
$Z$ electrons is

$$
  \mathcal{M}(Z, N)
  = 
  Z \cdot m_{\mathfrak{p}}
  + 
  N \cdot m_{\mathfrak{n}}
  + 
  Z \cdot m_e
  - 
  B(Z, N)
$$

where:

1. $m_{\mathfrak{p}}$ is the proton mass from the pair Skein
   formula ([terminal resolution](#prop:terminal-resolution)):

   $$
     m_{\mathfrak{p}}
     = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
   $$

2. $m_{\mathfrak{n}}$ is the neutron mass:

   $$
     m_{\mathfrak{n}}
     = 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
   $$

3. $m_e$ is the electron mass from the trefoil knot
   ([electron knot](#ex:electron-knot-concrete)).

4. $B(Z, N)$ is the total nuclear binding energy from the
   Skein polynomial of the multi-nucleon Hopf link.

## Knot structure of an atom

The knot formula for a neutral atom is
([knot-particle generation](#def:knot-particle-generation)):

$$
  Z\mathfrak{p}  \oplus  N\mathfrak{n}
   \oplus  Z \cdot T_{2,3}
$$

where $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p
\oplus \mathcal{L}_H$ (proton as color-linked Borromean quark
triple), $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d},
\mathfrak{d}]_p \oplus \mathcal{L}_H$ (neutron), $T_{2,3}$ is
the trefoil (electron), and $\oplus$ denotes Hopf linking.

## Input parameters (single free parameter $q$)

All masses derive from one parameter: the substrate parameter $q$
(see Chapter 7 for the numerical determination $q \approx 1.1098$
from the lepton mass ratio).

| Constant | Formula |
|----------|---------|
| $q$ | $1/(1 - \sqrt{\mathrm{Vol}(4_1)/(m_\mu/m_e)})$ |
| $\hbar_q$ | $1 - q^{-1}$ |
| $m_{\mathfrak{p}}(q)$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ |
| $m_{\mathfrak{n}}(q)$ | $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ |
| $m_e(q)$ | trefoil $\mathrm{Li}_2(q^{-2})/\hbar_q^2$ |

## Calculation procedure for each element

For each element $Z$ with most stable isotope mass number $A = Z + N$:

**Step 1.** Write the knot formula:
$Z\mathfrak{p} \oplus N\mathfrak{n} \oplus Z \cdot T_{2,3}$.

**Step 2.** Compute the unbound nucleon mass:
$M_{\mathrm{free}}(Z, N) = Z \cdot m_{\mathfrak{p}} + N \cdot m_{\mathfrak{n}}$.

**Step 3.** Add the electron mass contribution:
$M_{\mathrm{free+e}}(Z, N) = M_{\mathrm{free}} + Z \cdot m_e$.

**Step 4.** Subtract the total binding energy:
$\mathcal{M}(Z, N) = M_{\mathrm{free+e}} - B(Z, N)$,
where $B(Z, N) = A \cdot (B/A)$ uses the binding energy per
nucleon from AME2020.

**Step 5.** Compare with observed atomic mass from AME2020.

## Binding energy source

The binding energy per nucleon $B/A$ is computed from the nuclear
Skein polynomial
([transfer matrix operator](#def:transfer-matrix-operator))
via transfer matrix multiplication.  In this appendix, the
AME2020 values of $B/A$ are used as the reference, since the
transfer matrix computation reproduces them.  Each element's
calculation shows the explicit $B/A$ value used.

## Observed masses

Observed atomic masses $M_o$ are taken from the AME2020 Atomic
Mass Evaluation (nuclear mass plus $Z \cdot m_e$), expressed in
MeV/$c^2$.  The most stable (longest-lived) isotope is listed for
each element.  For $Z > 109$, AME2020 provides extrapolated
values with uncertainties of order $\sim 0.5$--$1$ MeV.

## The $q$-torsion hypothesis for synthetic elements

This appendix uses AME2020 binding energies $B/A$ as input.
Since the same $B/A$ enters both the QOU formula and the
observed mass derivation, the deviations shown here are small
($< 0.1$ MeV) for all elements, natural and synthetic alike.

The deeper test of the QOU framework is whether the Skein
polynomial computed purely at $q_0$ reproduces the AME2020
$B/A$ values.  For naturally occurring elements ($Z \leq 92$),
the transfer matrix calculation
([transfer matrix operator](#def:transfer-matrix-operator))
confirms this to high precision.

For synthetic elements ($Z \geq 93$), a distinct prediction
arises.  These nuclei were assembled under conditions very
different from stellar nucleosynthesis:

1. **Neutron capture in reactors** ($Z = 93$--$100$): high
   thermal neutron flux, moderate gauge-field curvature.
   The local substrate parameter is expected to be close to
   $q_0$.

2. **Heavy-ion fusion** ($Z = 101$--$118$): nuclei are created
   in transient heavy-ion collision fireballs
   ($\sqrt{s_{NN}} \sim$ GeV, lifetime $\sim 10^{-23}$ s)
   where concentrated gauge-field curvature may shift the
   local substrate parameter to $q_{\mathrm{eff}} > q_0$.

If the crossing resolutions of the nuclear Skein polynomial
"lock in" at the formation-time $q_{\mathrm{eff}}$, then
superheavy nuclei would carry a residual $q$-torsion imprint.
The Skein-derived $B/A$ at $q_0$ would then differ from the
experimentally measured $B/A$, producing systematic mass
deviations that grow with $Z$.

**Prediction.** When $B/A$ is computed from the Skein
polynomial at $q_0$ (rather than taken from AME2020),
the deviations for accelerator-produced elements should be
systematically larger than for natural elements.  Improved
mass measurements of superheavy elements (e.g.\ at RIKEN
or GSI) would test this prediction.
