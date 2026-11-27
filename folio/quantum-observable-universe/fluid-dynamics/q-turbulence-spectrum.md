In the brane fluid defined by [aether parameter](#def:substrate-parameter) $q > 1$ and [Planck--Reynolds number](#rem:planck-reynolds) $\mathrm{Re}_q = 2/(q-1)$, the energy spectrum of a turbulent vortex tangle obeys a $q$-deformed Kolmogorov law.

1. **$q$-deformed energy spectrum.** Let $E(k)$ denote the energy per unit wavenumber. In the inertial range $1 \ll k \ll k_{\max}$, where $k_{\max}$ denotes the viscous cutoff imposed by $\mathrm{Re}_q$, the spectrum evaluates to

   $$
     E_q(k)
     = 
     C_q\varepsilon^{2/3}
     \frac{[k]_q^{-5/3}}{[k]_q / k},
   $$

   where $\varepsilon$ represents the energy dissipation rate, $C_q$ acts as a $q$-dependent Kolmogorov constant, and the ratio $[k]_q / k$ corrects for the non-uniform spacing of $q$-integers. As $q \to 1$, $[k]_q \to k$ and the spectrum converges to the classical Kolmogorov law $E(k) = C_K\varepsilon^{2/3}k^{-5/3}$.

2. **Discrete cascade.** Classical turbulence cascades energy continuously from large to small scales. The $q$-deformed cascade operates **discretely**: energy transfers sequentially between modes indexed by $q$-integers $[k]_q$, executing at the transfer rate

   $$
     T_{k \to k+1}
     = 
     \varepsilon
     \frac{[k+1]_q^{2/3} - [k]_q^{2/3}}
          {[k+1]_q - [k]_q}.
   $$

   For large $k$, the denominator scales as $[k+1]_q - [k]_q \sim q^k \cdot q/(q+1)$. The transfer rate thus drops exponentially at high wavenumbers, enforcing a strict structural UV cutoff.

3. **Finite cascade depth.** The number of active modes participating in the cascade is bounded by

   $$
     N_{\mathrm{modes}}
      \leq 
     \bigl\lfloor \log_q(\mathrm{Re}_q^{3/4}) \bigr\rfloor
     = 
     \biggl\lfloor
       \frac{3}{4}
       \frac{\ln(2/(q-1))}{\ln q}
     \biggr\rfloor.
   $$

   The bound is the logarithmic form of the dissipation-scale cutoff $q^{N_{\mathrm{modes}}} \leq \mathrm{Re}_q^{3/4}$ (every active mode lies below the Kolmogorov scale), which is the modeling hypothesis of the derivation; the passage from the cutoff to the stated bound is elementary. At the physical anchor $q \approx 1.110$, $N_{\mathrm{modes}} \approx 21$. (This accounts for all modes spanning the cascade; the [Planck--Reynolds](#rem:planck-reynolds) bound $k_{\max} \approx 4$ measures only those modes carrying significant amplitude.)

4. **Spectral gap.** Below the fundamental mode $k = 1$, a **spectral gap** isolates the ground state (laminar flow) from the first excited mode:

   $$
     \Delta E_{\mathrm{gap}}
     = 
     C_q\varepsilon^{2/3}
     \bigl([1]_q^{-5/3} - [2]_q^{-5/3}\bigr)
      >  0.
   $$

   This gap halts the spontaneous onset of turbulence below a rigid threshold energy injection rate. The brane fluid remains structurally stable against infinitesimal perturbations, unlike classical Navier--Stokes where $\mathrm{Re} \to \infty$ guarantees instability.
