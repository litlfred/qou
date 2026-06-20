*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $q > 1$ be the substrate parameter, $\hbar_q = (q-1)/q$,
and $V_B = 7.32772$ the Borromean volume.  The two topological
phases of dense quark matter have distinct equations of state:

**1. Borromean phase** (confined hadronic matter, $\rho < \rho_c$).

The baryon mass is $M_B = V_B / \hbar_q^2$.  For a cold,
degenerate Fermi gas of baryons at number density $n_B$, the
energy density and pressure are

$$
  \varepsilon_B(n_B)
  = 
  M_B  n_B
  + 
  \frac{3}{5}
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{2M_B}
   n_B^{5/3},
$$

$$
  P_B(n_B)
  = 
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{5M_B}
   n_B^{5/3}.
$$

The speed of sound in the Borromean phase is

$$
  c_{s,B}^2
  = 
  \frac{dP_B}{d\varepsilon_B}
  = 
  \frac{2}{3}
  \frac{E_F}{M_B + E_F}
$$

where $E_F = \hbar_q^2(3\pi^2 n_B)^{2/3} / (2M_B)$ is the
Fermi energy.  Since $M_B \gg E_F$ at nuclear densities:
$c_{s,B}^2 \ll 1$ (non-relativistic regime).

**2. CFL phase** (color superconducting, $\rho > \rho_c$).

The effective quark mass is $M_D = \frac{1}{3}(q + q^{-1})$
(crossing energy per quark, no volume contribution since
$\mathrm{Vol}(\mathcal{L}_H) = 0$).  For a degenerate quark
Fermi gas at quark number density $n_q = 3 n_B$, the energy
density includes the CFL gap contribution:

$$
  \varepsilon_D(n_B)
  = 
  3M_D n_B
  + 
  \frac{3}{5}
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{2M_D}
   (3 n_B)^{5/3}
  - 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2},
$$

$$
  P_D(n_B)
  = 
  \frac{\hbar_q^2(3\pi^2)^{2/3}}{5M_D}
   (3 n_B)^{5/3}
  + 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2},
$$

where $\mu_q = \hbar_q(3\pi^2 n_q)^{1/3}/(2M_D)^{1/2}$ is
the quark chemical potential and
$\Delta_{\mathrm{CFL}} = q + q^{-1}$ is the gap
([Hopf diquark](#def:hopf-diquark)).

**3. Stiffness ratio.**  The ratio of pressures at equal baryon
density is

$$
  \frac{P_D}{P_B}
  = 
  \frac{M_B}{M_D} \cdot 3^{5/3}
  + 
  \frac{3\Delta_{\mathrm{CFL}}^2 \mu_q^2}{\pi^2 P_B}.
$$

The first term gives the dominant contribution.  At
$q = q_0$:

$$
  \frac{M_B}{M_D}
  = 
  \frac{V_B / \hbar_q^2}{\frac{1}{3}(q + q^{-1})}
  = 
  \frac{749.2}{0.670}
   \approx  1118.
$$

Including the $3^{5/3} \approx 6.24$ factor:

$$
  \frac{P_D}{P_B}
   \approx 
  1118 \times 6.24
   \approx  6977.
$$

The CFL equation of state is **nearly $7000\times$ stiffer** than
the Borromean EOS at equal baryon density.

**4. Speed of sound and the conformal limit.**

In the CFL phase at high density, $E_F \gg M_D$ and

$$
  c_{s,D}^2
   \to 
  \frac{1}{3}
  \qquad (\text{as } n_B \to \infty).
$$

This is the **conformal limit** $c_s^2 = 1/3$ — the maximum
speed of sound for a conformally symmetric fluid.  The CFL phase
approaches this limit because its mass contribution is a
constant ($M_D = (q + q^{-1})/3$, independent of density), so
at high density the kinetic term dominates and the fluid becomes
approximately conformal.

In contrast, the Borromean phase has $c_{s,B}^2 \to 1/3$ only
at densities so extreme that $E_F \sim M_B = 749$ Skein units —
far beyond any physical baryon density.  At nuclear saturation
density $\rho_0$: $c_{s,B}^2 \sim 0.01$, deeply non-relativistic.

**Summary.**

See [Table](#tbl:eos-borromean-cfl-table-data).

*Proof.*
The energy density and pressure follow from the standard
non-relativistic Fermi gas formulas with the mass parameter set
by the [algebraic-quantum-volume](#def:algebraic-quantum-volume)
form of the topological mass formula. In the Borromean phase,
$M_B = \mathrm{Vol}_q(\beta_B) / \hbar_q^2$ is the algebraic
quantum-volume contribution (an element of $\mathbb{Z}[q^{\pm 1/2}]$);
its τ-image is the hyperbolic volume of the Borromean rings
complement. In the CFL phase, $M_D = (q + q^{-1})/3$ is the
crossing-energy contribution per quark (three quarks per baryon),
with $\mathrm{Vol}_q(\beta_{\mathcal{L}_H}) = 0$ in
$\mathbb{Z}[q^{\pm 1/2}]$ — the algebraic quantum volume vanishes
identically for the CFL Hopf-link braid — eliminating the volume
term without invoking the geometric (3-manifold) interpretation.

The stiffness ratio is immediate from $P \propto n^{5/3}/M$:
at equal density, $P_D / P_B = (M_B / M_D) \cdot 3^{5/3}$
(the $3^{5/3}$ from $n_q = 3 n_B$ in the CFL quark gas).

The conformal limit $c_s^2 \to 1/3$ follows from the
ultra-relativistic limit of the Fermi gas: when $E_F \gg M$,
$\varepsilon \approx 3P$ and $c_s^2 = dP/d\varepsilon = 1/3$.
The CFL phase reaches this at moderate density because $M_D$ is
small; the Borromean phase requires $E_F \sim 749$ Skein units,
corresponding to unphysical compression. $\square$
