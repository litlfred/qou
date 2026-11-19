The [discrete vortex spectrum](#prop:discrete-vortex-spectrum) identifies the $q$-Laplacian eigenvalues on a vortex filament of length $L$. On the circle they are

$$
  \lambda_k^{(q)} = [k]_q^2 \cdot \frac{\hbar_q}{L_q^2},
  \qquad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}},
$$

the exact eigenvalues $\mu_k^{(q)} = [k]_q^2$ of $\Delta_q$ on $L$-periodic functions, in the variable $z = e^{2\pi i s/L}$; the units enter only through the factor $\hbar_q / L_q^2$. The linearised [q-Navier--Stokes equation](#def:q-navier-stokes) for normal displacements then yields the $q$-deformed Kelvin dispersion and its viscous decay rate,

$$
  \omega_k^{(q)}
  = 
  \frac{\Gamma_q^{1/2}}{2\sqrt{\pi}a_q}
  \frac{[k]_q}{L_q},
  \qquad
  \gamma_k^{(q)}
  = 
  \frac{\nu_q}{2}\frac{[k]_q^2}{L_q^2}
  = 
  \frac{\hbar_q}{4}\frac{[k]_q^2}{L_q^2},
$$

where $\Gamma_q = [j]_q[j+1]_q$ is the quantised circulation at intensity level $j$ and $a_q$ the $q$-deformed core radius. Because $[k]_q \sim q^k$ at large $k$, mode $k$ decays on the timescale $\tau_k = 4L_q^2 / (\hbar_q[k]_q^2)$ — high modes decay **doubly exponentially** in $k$, the rigorous exponential UV cutoff built into the [q-Navier--Stokes definition](#def:q-navier-stokes).
