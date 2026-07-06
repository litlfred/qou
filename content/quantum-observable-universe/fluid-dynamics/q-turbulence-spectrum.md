In the brane fluid with [substrate parameter](#def:substrate-parameter) $q > 1$ and [Planck--Reynolds number](#rem:planck-reynolds) $\mathrm{Re}_q = 2/(q-1)$, the energy spectrum of a turbulent vortex tangle satisfies a $q$-deformed Kolmogorov law.

1. **$q$-deformed energy spectrum.** Let $E(k)$ denote the energy per unit wavenumber in the brane fluid. In the inertial range $1 \ll k \ll k_{\max}$, where $k_{\max}$ is the viscous cutoff set by $\mathrm{Re}_q$, the spectrum is

   $$
     E_q(k)
     = 
     C_q\varepsilon^{2/3}
     \frac{[k]_q^{-5/3}}{[k]_q / k},
   $$

   where $\varepsilon$ is the energy dissipation rate, $C_q$ is a $q$-dependent Kolmogorov constant, and the ratio $[k]_q / k$ accounts for the non-uniform spacing of $q$-integers. As $q \to 1$, $[k]_q \to k$ and the classical Kolmogorov spectrum $E(k) = C_K\varepsilon^{2/3}k^{-5/3}$ is recovered.

2. **Discrete cascade.** Unlike classical turbulence, where energy cascades continuously from large to small scales, the $q$-deformed cascade is discrete. Energy transfers occur between modes labelled by $q$-integers $[k]_q$, with transfer rate

   $$
     T_{k \to k+1}
     = 
     \varepsilon
     \frac{[k+1]_q^{2/3} - [k]_q^{2/3}}
          {[k+1]_q - [k]_q}.
   $$

   For the symmetric $q$-integer, the denominator satisfies $[k+1]_q - [k]_q \sim q^k \cdot q/(q+1)$ for large $k$. The transfer rate decreases exponentially at high wavenumbers. This provides a natural UV cutoff.

3. **Finite cascade depth.** The number of active modes in the cascade is bounded by

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

   At $q \approx 1.110$, $N_{\mathrm{modes}} \approx 21$. This counts all modes participating in the cascade. The [Planck--Reynolds](#rem:planck-reynolds) bound $k_{\max} \approx 4$ is the stricter count of modes with significant amplitude.

4. **Spectral gap.** Below the fundamental mode $k = 1$, there is a spectral gap

   $$
     \Delta E_{\mathrm{gap}}
     = 
     C_q\varepsilon^{2/3}
     \bigl([1]_q^{-5/3} - [2]_q^{-5/3}\bigr)
      >  0.
   $$

   This gap separates the ground state (laminar flow) from the first excited mode. It prevents spontaneous onset of turbulence below a threshold energy injection rate. The brane fluid is stable against infinitesimal perturbations, unlike classical Navier--Stokes where $\mathrm{Re} \to \infty$ always produces instability.

