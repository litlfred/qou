**Conjecture (Critical exponent).**
The regularity breakdown conjecture predicts that maximum enstrophy diverges as $\Omega_{\max}(q) \sim (q-1)^{-\alpha}$ for some $\alpha > 0$.

Enstrophy evolution satisfies $\frac{d\Omega}{dt} \leq \Lambda_q\Omega$, where $\Lambda_q = \frac{(C_q')^2E_0}{\nu_q} - \nu_q$.

**Computation of $\Lambda_q$ asymptotics.**
Set $\varepsilon = q - 1 \to 0^+$.
- Viscosity: $\nu_q = \varepsilon/(2(1+\varepsilon)) = \varepsilon/2 + O(\varepsilon^2)$.
- Sobolev constant: $C_q'^2 \approx \pi^2/6 + O(\varepsilon^2)$.
- Growth rate: $\Lambda_q \approx \pi^2 E_0/(3\varepsilon) + O(1)$.
So $\Lambda_q \sim (q-1)^{-1}$ as $q \to 1^+$. The Gronwall bound gives exponential growth, which is too crude.

**Refined estimate via cascade depth.**
The $q$-turbulence spectrum gives the cascade depth $N_{\mathrm{eff}} = \lfloor \log_q (\mathrm{Re}_q^{3/4})\rfloor$. At $q = 1 + \varepsilon$:

$$
  \mathrm{Re}_q = \frac{2}{\varepsilon},
  \qquad
  N_{\mathrm{eff}}
  \approx \frac{3}{4}\frac{\ln(2/\varepsilon)}{\varepsilon}.
$$

The maximum enstrophy of the truncated system with $N$ modes is bounded by the Kolmogorov enstrophy sum $\Omega_{\max} \leq \sum_{k=1}^N k^2E(k)$. With $E(k) \sim k^{-5/3}$, the sum is bounded by $N^{4/3}$. Exponential damping ensures higher modes contribute negligibly. The effective enstrophy is dominated by the first $N_{\mathrm{eff}}$ modes:

$$
  \Omega_{\max}(\varepsilon)
  \lesssim
  N_{\mathrm{eff}}^{4/3}
   \sim 
  \left(\frac{\ln(1/\varepsilon)}{\varepsilon}\right)^{4/3}.
$$

**Result (closure-dependent — two heuristic values, neither rigorous).**
The exponent depends on which turbulence closure is imposed on the enstrophy budget:

- **Dissipation closure.** Imposing $\varepsilon = \nu_q\,\Omega$ (mean dissipation $=$ viscosity $\times$ enstrophy) with $\varepsilon$ bounded away from $0$ gives $\Omega_{\max} \sim \varepsilon/\nu_q \sim (q-1)^{-1}$, i.e. $\alpha = 1$. This is the exact algebraic consequence of the closure, and is the same leading order as the crude Gronwall rate $\Lambda_q \sim (q-1)^{-1}$ above.
- **Kolmogorov-cascade closure.** Imposing $E(k) \sim k^{-5/3}$ truncated at $N_{\mathrm{eff}}$ gives $\Omega_{\max} \lesssim N_{\mathrm{eff}}^{4/3} \sim (q-1)^{-4/3}\bigl(\ln(q-1)^{-1}\bigr)^{4/3}$, i.e. $\alpha = 4/3$ with a logarithmic correction.

$$
  \Omega_{\max}(q) \sim (q-1)^{-\alpha},
  \qquad
  \alpha = 1 \ \text{(dissipation closure)}
  \quad\text{vs.}\quad
  \alpha = \tfrac{4}{3} \ \text{(Kolmogorov closure, up to logs)}.
$$

Neither closure is rigorous; the true $\alpha$ is fixed by the actual $q$-Navier--Stokes enstrophy spectrum (the turbulence-closure problem) and is open. The two values bracket it under their respective hypotheses.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
