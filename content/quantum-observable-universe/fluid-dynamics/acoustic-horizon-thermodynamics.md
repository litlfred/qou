**Surface gravity and Hawking temperature.**
Evaluating the surface gravity at an acoustic horizon gives

$$
  \kappa_H
  = 
  \frac{1}{2}\frac{\partial(c_s^2 - |v|^2)}{\partial n}
  \bigg|_\Sigma,
$$

where $n$ points strictly outward from $\Sigma$. Tracking Unruh's acoustic black hole mapping, the horizon radiates at the Hawking temperature

$$
  T_H
  = 
  \frac{\hbar_q\kappa_H}{2\pi c_s}.
$$

Applying the brane fluid identity $\hbar_q = (q-1)/q$ produces:

$$
  T_H
  = 
  \frac{(q-1)}{2\pi q}
  \frac{\kappa_H}{c_s}.
$$

As $q \to 1$, $T_H \to 0$: the classical limit eliminates Hawking radiation entirely, matching the collapse of $\hbar_q$. At the physical value $q \approx 1.110$, the geometric factor $(q-1)/q \approx 0.099$ heavily suppresses $T_H$ compared to the generic estimate $\kappa_H / (2\pi c_s)$.

**Types of acoustic horizon in the brane fluid.**

| Configuration | Flow structure | Physical analogue |
|---|---|---|
| **Spherical inflow** | Radial $v = -v_r(r)\hat{r}$ where $v_r(r_H) = c_s$ | Schwarzschild black hole |
| **Vortex drain** | Circular $v = v_\varTheta(r)\hat\varTheta + v_r(r)\hat{r}$ | Kerr (rotating) black hole |
| **Expanding shell** | Outward $v = v_r(r)\hat{r}$ where $v_r(r_C) = c_s$ | Cosmological horizon (de Sitter) |
| **Vortex core** | Concentrated circulation $\lvert v\rvert \to \infty$ as $r \to 0$ | Naked singularity (requires $\lvert v\rvert > c_s$ exclusively for $r < r_0$) |

**$q$-dependent horizon radius.**
Evaluated for spherically symmetric inflow operating at velocity $v_r = -\Gamma_q / (4\pi r^2)$, the horizon nucleates at

$$
  r_H
  = 
  \left(\frac{\Gamma_q}{4\pi c_s}\right)^{1/2}
  = 
  \left(\frac{[j]_q[j+1]_q}{4\pi c_q}\right)^{1/2}
  \cdot (1 + O(\hbar_q)).
$$

At the fundamental level $j = 1/2$, the circulation evaluates to $[1/2]_q[3/2]_q = (q^2 + q^{-2} - q - q^{-1})/(q - q^{-1})^2 \approx 0.75$ using the physical anchor $q \approx 1.110$. The resulting horizon radius $r_H$ matches the scale of $\ell_q = (q-1)/q$.
