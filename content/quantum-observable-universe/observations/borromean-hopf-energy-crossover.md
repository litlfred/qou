*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $q > 1$ be the substrate parameter and $\hbar_q = (q-1)/q$.
Consider $6$ quarks (two baryon-number units) with flavor content
$(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})^{\otimes 2}$.  These
$6$ quarks can be assembled in two topologically distinct
configurations:

- **Borromean phase** ($\mathcal{P}_B$): two Borromean baryons
  $\mathcal{B}_3 \cdot \mathcal{B}_3$, each with Borromean
  volume $V_B = 7.32772$ and inter-baryon Hopf binding.

- **Diquark phase** ($\mathcal{P}_D$): three Hopf diquark
  pairs ([Hopf diquark](#def:hopf-diquark))
  $D_{[\mathfrak{u}\mathfrak{d}]} \cdot D_{[\mathfrak{d}\mathfrak{s}]} \cdot D_{[\mathfrak{s}\mathfrak{u}]}$, each bound by $\mathcal{L}_H$.

Then:

1. **Mass comparison.**  The Borromean phase has mass

$$
  M_B
  = 
  2 \cdot \frac{V_B}{\hbar_q^2}
  = 
  \frac{2 \times 7.32772}{((q-1)/q)^2}
  = 
  \frac{14.6554 q^2}{(q-1)^2}.
$$

   The diquark phase has mass from crossing energy only
   (Hopf link volume is zero):

$$
  M_D
  = 
  3 \cdot \tfrac{1}{3}(q + q^{-1})
  = 
  q + q^{-1}
   \approx  2.011  \text{Skein units}.
$$

   Since $\mathrm{Vol}(\mathcal{L}_H) = 0$, the diquark
   mass is **purely from crossing energy**, not from
   hyperbolic volume.  At any $q > 1$: $M_D \ll M_B$.

2. **Binding energy comparison.**  The binding energy
   per baryon number is:

   - Borromean: $\mathfrak{E}_B = -V_B / \hbar_q^2$ (from
     Borromean volume)
   - Diquark: $\mathfrak{E}_D = -\tfrac{3}{2}(q + q^{-1})$
     (from three Hopf links shared between two baryon-number
     units, strong channel only since the CFL condensate is
     color-neutral)

   The crossover occurs when $|\mathfrak{E}_D| > |\mathfrak{E}_B|$,
   i.e., when the Hopf-link binding per baryon number exceeds
   the Borromean binding:

$$
  \frac{3}{2}(q + q^{-1})
   > 
  \frac{V_B}{\hbar_q^2}
  = 
  \frac{7.32772 q^2}{(q-1)^2}.
$$

3. **At $q = q_0$.**

$$
  \frac{3}{2}(q + q^{-1})
  = 
  \frac{3}{2}(q_0 + q_0^{-1})
  = 
  \frac{3}{2} \times 2.0108
  =  3.016.
$$

$$
  \frac{V_B}{\hbar_q^2}
  = 
  \frac{7.32772}{(0.0989)^2}
  = 
  \frac{7.32772}{0.009781}
  =  749.2.
$$

   At $q = q_0$: $3.016 \ll 749.2$.  The Borromean
   binding **vastly exceeds** the Hopf-diquark binding.
   The Borromean phase is energetically dominant by a
   factor of $\sim 250$.

4. **Compression energy.**  At baryon density $\rho$, the
   compression (kinetic + Pauli exclusion) energy per baryon is

$$
  \mathfrak{E}_{\mathrm{comp}}(\rho)
   \sim 
  \frac{\hbar_q^2}{2\mathfrak{m}} \cdot (3\pi^2 \rho)^{2/3},
$$

   which grows as $\rho^{2/3}$.  The compression energy
   destabilizes the Borromean phase (volume-based mass
   grows under compression) while the diquark phase
   (zero-volume, crossing-energy-based) is unaffected.

   The **critical density** $\rho_c$ satisfies

$$
  \mathfrak{E}_{\mathrm{comp}}(\rho_c)
  = 
  \frac{V_B}{\hbar_q^2}
  - 
  \frac{3}{2}(q + q^{-1}),
$$

   i.e., the compression energy closes the gap between
   Borromean and Hopf binding.

*Proof sketch.*
Part (1): the Borromean mass follows from the topological mass
formula $\mathfrak{m} = V/\hbar_q^2$ with $V_B = 7.32772$.  The diquark
mass uses $\mathrm{Vol}(\mathcal{L}_H) = 0$.

Part (2): the binding energies follow from the crossing energy
formula.  In the Borromean phase, the binding is topological
(from the hyperbolic volume of the complement).  In the diquark
phase, the binding is from the $R$-matrix braiding of the Hopf
link ($2$ crossings per diquark pair, $3$ pairs per
$6$-quark unit).

Part (3): direct evaluation at $q = q_0$.

Part (4): the compression energy is the standard Fermi gas
kinetic energy with the $q$-deformed Planck constant
$\hbar_q = (q-1)/q$.  The Borromean volume $V_B$ enters the
mass denominator of the kinetic energy, creating a
volume-dependent feedback.  The diquark phase has zero volume
contribution, so its kinetic energy is independent of $V_B$.
$\square$
