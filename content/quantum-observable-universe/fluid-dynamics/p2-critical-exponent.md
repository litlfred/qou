**Conjecture (assuming [`conj:regularity-breakdown`](#conj:regularity-breakdown)).**

The [regularity breakdown conjecture](#conj:regularity-breakdown)
predicts that the maximum enstrophy diverges as
$\Omega_{\max}(q) \sim (q-1)^{-\alpha}$ for some $\alpha > 0$.

From the [enstrophy evolution](#prop:q-ns-nonlinear-uniqueness),
the enstrophy satisfies

$$
  \frac{d\Omega}{dt}
   \leq 
  \Lambda_q\Omega,
  \qquad
  \Lambda_q = \frac{(C_q')^2E_0}{\nu_q} - \nu_q.
$$

The maximum enstrophy over all time is bounded by
$\Omega_{\max}(q) \leq \Omega(0)e^{\Lambda_qT}$ for any
time horizon $T$.  But the **tightest** bound comes from
balancing dissipation against stretching at the critical mode.

**Computation of $\Lambda_q$ asymptotics.**

Set $\varepsilon = q - 1 \to 0^+$.  Then:

- Viscosity: $\nu_q = \varepsilon/(2(1+\varepsilon))
  = \varepsilon/2 + O(\varepsilon^2)$.

- Sobolev constant:
  $C_q' = \bigl(\sum_k [k]_q^{-2}\bigr)^{1/2}$.
  For small $\varepsilon$, $[k]_q \approx k + k(k^2-1)\varepsilon^2/6
  + O(\varepsilon^4)$, so $[k]_q^{-2} \approx k^{-2}(1 - (k^2-1)
  \varepsilon^2/3)$.  The sum converges:
  $C_q'^2 \approx \pi^2/6 + O(\varepsilon^2)$.

- Growth rate: $\Lambda_q \approx
  (\pi^2/6)E_0 \cdot 2/\varepsilon - \varepsilon/2
  = \pi^2 E_0/(3\varepsilon) + O(1)$.

So $\Lambda_q \sim (q-1)^{-1}$ as $q \to 1^+$.

**The Gronwall bound gives $\alpha = 1$.**
From $\Omega_{\max} \leq \Omega(0)e^{\Lambda_q T}$ with
$\Lambda_q \sim (q-1)^{-1}$, this gives exponential growth in
$(q-1)^{-1}$, not power-law.  This bound is too crude.

**Refined estimate via cascade depth.**
The [q-turbulence spectrum](#prop:q-turbulence-spectrum) gives the
cascade depth $N_{\mathrm{eff}} = \lfloor \log_q
(\mathrm{Re}_q^{3/4})\rfloor$.  At $q = 1 + \varepsilon$:

$$
  \mathrm{Re}_q = \frac{2}{\varepsilon},
  \qquad
  N_{\mathrm{eff}}
  \approx \frac{3}{4}\frac{\ln(2/\varepsilon)}{\ln(1+\varepsilon)}
  \approx \frac{3}{4}\frac{\ln(2/\varepsilon)}{\varepsilon}.
$$

The maximum enstrophy of the truncated system with $N$ modes
is bounded by the Kolmogorov enstrophy sum
$\Omega_{\max} \leq \sum_{k=1}^N k^2E(k)$.  With
$E(k) \sim k^{-5/3}$: $\sum_{k=1}^N k^{1/3} \sim N^{4/3}$.

For the $q$-deformed system, the exponential damping
$e^{-\nu_q [k]_q^2 t}$ ensures higher modes contribute
negligibly.  The effective enstrophy is dominated by the
first $N_{\mathrm{eff}}$ modes, giving

$$
  \Omega_{\max}(\varepsilon)
  \lesssim
  N_{\mathrm{eff}}^{4/3}
   \sim 
  \left(\frac{\ln(1/\varepsilon)}{\varepsilon}\right)^{4/3}.
$$

**Result.**
The critical exponent is $\alpha = 4/3$ with a logarithmic
correction:

$$
  \boxed{
    \Omega_{\max}(q)
    \lesssim
    (q-1)^{-4/3}\bigl(\ln(q-1)^{-1}\bigr)^{4/3}
    \quad\text{as } q \to 1^+.
  }
$$

