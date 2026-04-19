Electrons contribute to the total atomic mass
$\mathcal{M}(Z, N) = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}}
+ Z m_e - B(Z, N)$ ([tower binding energy](#prop:tower-binding-energy))
through the **linear free-electron kinetic term $Z m_e$**, not
through the Hecke-tower binding $B(Z, N)$.  This distinction
resolves an apparent tension between the electron-knot definition
([electron knot](#def:electron-knot)) and the binding formula.

## Statement

**Observation.**
*The binding energy $B(Z, N)$ in
[tower binding energy](#prop:tower-binding-energy) is a sum over
$A - 1$ nucleon-strand generators of the Hecke algebra $H_A(q)$
(protons and neutrons only).  Electrons do **not** appear as
additional strands of $H_A(q)$: the algebra dimension stays
$A = Z + N$, not $A + Z$.  The electron contribution to atomic
mass is the linear term $Z m_e$ in the free-particle baseline
$\mathcal{M}_{\mathrm{free}} = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}}
+ Z m_e$.*

*Computationally: naive extension of $H_A(q)$ to $H_{A+Z}(q)$ by
appending $Z$ electron strands diverges the
$\prod_i \hat{V}_i^{\mathrm{sym}}$ product above the $V = q$
Pochhammer singularity of $\Phi_q$, verified on deuterium and
$^3$He.  Electrons must not be strands of the binding sum.*

## Atomic binding is below the err floor

For neutral atoms, the atomic (electron--nucleus) binding energy
ranges from $13.6$ eV (H) to $\lesssim 27$ keV (all-electron
ionisation, $Z = 20$).  Compared to nuclear binding energies of
$\sim 2$ MeV to $\sim 340$ MeV for the same Z range, atomic
binding is $10^{-5}$ of $B_{\mathrm{nuclear}}$ at worst.

The current prediction-error floor for the H_A 3-channel Wedderburn
formula is $\approx 0.07\%$ of $\mathcal{M}$ (mean across $Z = 1..20$),
which on a $\sim 20$ GeV atomic mass is $\sim 15$ MeV — three orders
of magnitude above atomic-binding scale.  Atomic binding is
therefore absorbed into the rounding of $Z m_e$ in the free-mass
baseline.

For $1$-ppm nuclear-mass predictions ($\sim 1$ keV on $\mathcal{M}$),
atomic binding STARTS to matter for $Z \geq 5$ (B:
$\sim 700$ eV total electron binding).  At that precision a
separate atomic-sector correction $B_{\mathrm{atomic}}(Z)$ is
required; it is NOT inside the nuclear binding formula.

## Electron-knot structural role

The electron's trefoil $T_{2,3}$ cabling
([electron knot](#def:electron-knot)) and shell Hopf-link structure
([electron shells](#rem:electron-shells-hopf)) describe the
**orbital quantum numbers** of the atomic sector.  They carry
information about spin, angular momentum, shell occupancy — but
not mass.  The mass formula's binding $B(Z, N)$ uses only the
nuclear sector (strong + gluon + pe Coulomb inter-nucleon) in
$H_A(q)$.

## Open: categorical atomic sector

A self-consistent $1$-ppm framework will need a separate
categorical treatment of the atomic sector — likely a decoupled
Hecke algebra $H_Z^{\mathrm{EM}}(q)$ or a distinct rigid monoidal
category for the lepton sector — with its own 3-channel tower.
This is future work; current prop:tower-binding-energy is correct
to the stated precision ($0.07\%$).

**Witness**: `full-tower-mass.witness.json` (B without electrons
in formula).
