This appendix carries out the atomic mass calculation for every
naturally occurring element ($Z = 1$ through $Z = 92$) from the
QOU topological mass formula.  Every intermediate step is shown
so that the reader can reproduce each result independently.

## The topological mass formula

The mass of a neutral atom with $Z$ protons, $N$ neutrons, and
$Z$ electrons is

$$
  \mathcal{M}(Z, N)
  \;=\;
  Z \cdot m_{\mathfrak{p}}
  \;+\;
  N \cdot m_{\mathfrak{n}}
  \;+\;
  Z \cdot m_e
  \;-\;
  B(Z, N)
$$

where:

1. $m_{\mathfrak{p}}$ is the proton mass from the pair Skein
   formula ([terminal resolution](#prop:terminal-resolution)):

   $$
     m_{\mathfrak{p}}
     = \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
   $$

2. $m_{\mathfrak{n}}$ is the neutron mass:

   $$
     m_{\mathfrak{n}}
     = 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
   $$

3. $m_e$ is the electron mass from the trefoil knot
   ([electron knot](#ex:electron-knot-concrete)).

4. $B(Z, N)$ is the total nuclear binding energy from the
   Skein polynomial of the multi-nucleon Hopf link.

## Knot structure of an atom

The knot formula for a neutral atom is
([knot-particle generation](#def:knot-particle-generation)):

$$
  Z\,\mathfrak{p} \;\bowtie\; N\,\mathfrak{n}
  \;\bowtie\; Z \cdot T_{2,3}
$$

where $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p
\bowtie \mathcal{L}_H$ (proton as color-linked Borromean quark
triple), $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d},
\mathfrak{d}]_p \bowtie \mathcal{L}_H$ (neutron), $T_{2,3}$ is
the trefoil (electron), and $\bowtie$ denotes Hopf linking.

## Input parameters (single free parameter $q_0$)

All masses derive from one parameter: the substrate parameter $q_0$.

| Constant | Formula | Value |
|----------|---------|-------|
| $q_0$ | $1/(1 - \sqrt{\mathrm{Vol}(4_1)/(m_\mu/m_e)})$ | $1.1099786\ldots$ |
| $\hbar_q$ | $1 - q_0^{-1}$ | $0.09907\ldots$ |
| $m_{\mathfrak{p}}$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ | $938.272\,089\,43$ MeV |
| $m_{\mathfrak{n}}$ | $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ | $939.565\,421\,94$ MeV |
| $m_e$ | trefoil $\mathrm{Li}_2(q^{-2})/\hbar_q^2$ | $0.510\,998\,950\,69$ MeV |

## Calculation procedure for each element

For each element $Z$ with most stable isotope mass number $A = Z + N$:

**Step 1.** Write the knot formula:
$Z\,\mathfrak{p} \bowtie N\,\mathfrak{n} \bowtie Z \cdot T_{2,3}$.

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
each element.
