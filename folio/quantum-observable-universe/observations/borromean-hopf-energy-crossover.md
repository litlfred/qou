*Let $q > 1$ be the aether parameter and $\hbar_q = (q-1)/q$. Consider six quarks (two baryon-number units) with flavor content $(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})^{\otimes 2}$. These six quarks can assemble in two topologically distinct configurations:*

*1. Borromean phase ($\mathcal{P}_B$): Two Borromean baryons $\mathcal{B}_3 \cdot \mathcal{B}_3$. Each baryon possesses Borromean volume $V_B = 7.32772$ and features inter-baryon Hopf binding.*
*2. Diquark phase ($\mathcal{P}_D$): Three Hopf diquark pairs ([Hopf diquark](#def:hopf-diquark)) $D_{[\mathfrak{u}\mathfrak{d}]} \cdot D_{[\mathfrak{d}\mathfrak{s}]} \cdot D_{[\mathfrak{s}\mathfrak{u}]}$. Each pair is bound by $\mathcal{L}_H$.*

*Then the following properties hold:*

*1. Mass comparison.*
*The Borromean phase yields mass*
$$
  M_B
  = 
  2 \cdot \frac{V_B}{\hbar_q^2}
  = 
  \frac{2 \times 7.32772}{((q-1)/q)^2}
  = 
  \frac{14.6554 q^2}{(q-1)^2}.
$$
*The diquark phase acquires mass from crossing energy alone, because the Hopf link volume is zero:*
$$
  M_D
  = 
  3 \cdot \tfrac{1}{3}(q + q^{-1})
  = 
  q + q^{-1}
   \approx  2.011  \text{Skein units}.
$$
*Since $\mathrm{Vol}(\mathcal{L}_H) = 0$, the diquark mass derives purely from crossing energy rather than hyperbolic volume. For any $q > 1$, $M_D \ll M_B$.*

*2. Binding energy comparison.*
*The binding energy per baryon number is:*
- *Borromean: $\mathfrak{E}_B = -V_B / \hbar_q^2$ (from Borromean volume).*
- *Diquark: $\mathfrak{E}_D = -\tfrac{3}{2}(q + q^{-1})$ (from three Hopf links shared between two baryon-number units; this uses the strong channel only, as the CFL condensate remains color-neutral).*

*The crossover occurs when $|\mathfrak{E}_D| > |\mathfrak{E}_B|$. At this point, the Hopf-link binding per baryon number exceeds the Borromean binding:*
$$
  \frac{3}{2}(q + q^{-1})
   > 
  \frac{V_B}{\hbar_q^2}
  = 
  \frac{7.32772 q^2}{(q-1)^2}.
$$

*3. Evaluation at $q = q_0$.*
*Evaluating the respective bindings at the aether parameter gives:*
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
  \frac{7.32772}{(0.09908)^2}
  = 
  \frac{7.32772}{0.0098172}
  =  746.4.
$$
*At $q = q_0$, the inequality $3.016 \ll 746.4$ demonstrates that the Borromean binding vastly exceeds the Hopf-diquark binding. The Borromean phase dominates energetically by a factor of roughly $250$.*

*4. Compression energy.*
*At baryon density $\rho$, the compression energy (kinetic plus Pauli exclusion) per baryon scales as*
$$
  \mathfrak{E}_{\mathrm{comp}}(\rho)
   \sim 
  \frac{\hbar_q^2}{2\mathfrak{m}} \cdot (3\pi^2 \rho)^{2/3}.
$$
*This energy grows as $\rho^{2/3}$. The compression energy destabilizes the Borromean phase, as the volume-based mass rises under compression. The zero-volume, crossing-energy-based diquark phase remains unaffected.*

*The critical density $\rho_c$ satisfies*
$$
  \mathfrak{E}_{\mathrm{comp}}(\rho_c)
  = 
  \frac{V_B}{\hbar_q^2}
  - 
  \frac{3}{2}(q + q^{-1}).
$$
*At this density, the compression energy exactly closes the gap between the Borromean and Hopf binding energies.*
