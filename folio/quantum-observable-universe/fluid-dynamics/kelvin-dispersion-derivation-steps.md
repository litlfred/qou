**Setup.**
Let $\varrho$ describe a stable vortex filament of length $L$ in the brane fluid, parametrised by arc length $s \in [0, L]$ under periodic boundary conditions $\varrho(0) = \varrho(L)$. Let $\eta(s, t)$ denote a small normal displacement of the filament from equilibrium (a Kelvin wave). The linearised [q-Navier--Stokes equation](#def:q-navier-stokes) governing normal perturbations of $\varrho$ reads

$$
  \partial_t^2 \eta
  = 
  \frac{\Gamma_q}{4\pi a_q^2}\Delta_q\eta
  -  \nu_q\Delta_q\partial_t \eta,
$$

where $\Gamma_q = [j]_q[j+1]_q$ fixes the quantised circulation at intensity level $j$, $a_q$ specifies the $q$-deformed vortex core radius, and the trailing term applies viscous damping.

**The $q$-Laplacian eigenvalue problem.**
The $q$-Laplacian evaluated on a circle of length $L$ acts exclusively on $L$-periodic functions $f(s)$. Its eigenvalue problem reads

$$
  \Delta_qf_k
  =  -\mu_kf_k,
  \qquad
  f_k(s + L) = f_k(s).
$$

For the classical Laplacian ($q = 1$) in arc length $s$, the eigenfunctions are $e^{2\pi i k s / L}$ with eigenvalues $\mu_k = (2\pi k/L)^2$. The $q$-Laplacian replaces the integer $k$ with the $q$-integer $[k]_q = (q^k - q^{-k})/(q - q^{-1})$. The derivation below works in the variable $z = e^{2\pi i s / L}$, where the eigenvalue is the dimensionless
$$
  \mu_k^{(q)}
  = 
  [k]_q^2 .
$$
The arc-length factor $(2\pi/L)^2$ is a change of unit, not part of the algebraic operator. All units are restored at once by the single factor $\hbar_q / L_q^2$ below. So $L_q$ is the length in that normalisation: matching $\hbar_q$ times the arc-length eigenvalue $(2\pi[k]_q/L)^2$ sets $L_q = L/(2\pi)$.

**Derivation.**
The $q$-derivative operators define the $q$-Laplacian. Assign $z = e^{2\pi i s / L}$ for a function $f$ on the circle. Then:

$$
  D_q f(z) = \frac{f(qz) - f(q^{-1}z)}{(q - q^{-1})z},
$$

and $\Delta_q = -zD_q \circ zD_q$ (composing the radial part of the $q$-Casimir). Operating on the monomial $z^k$ yields

$$
  D_q(z^k)
  = \frac{q^k z^k - q^{-k} z^k}{(q - q^{-1})z}
  = [k]_qz^{k-1}.
$$

Consequently $zD_q(z^k) = [k]_qz^k$, proving

$$
  \Delta_q(z^k) = -[k]_q^2z^k.
$$

The exact eigenvalue reads $\mu_k^{(q)} = [k]_q^2$. Restoring physical units (filament length $L_q$ and quantum of action $\hbar_q$) produces:

$$
  \lambda_k^{(q)}
  = 
  [k]_q^2 \cdot \frac{\hbar_q}{L_q^2}.
$$

This precisely matches the formula declared in the [discrete vortex spectrum](#prop:discrete-vortex-spectrum).

**Dispersion relation.**
Inserting $\eta(s,t) = f_k(s)e^{-i\omega t}$ into the linearised equation and applying $\Delta_q f_k = -[k]_q^2 f_k / L_q^2$ yields

$$
  -\omega^2
  = 
  -\frac{\Gamma_q}{4\pi a_q^2}\frac{[k]_q^2}{L_q^2}
  +  i\omega\nu_q\frac{[k]_q^2}{L_q^2}.
$$

In the undamped limit ($\nu_q = 0$, tracing the Euler limit), the dispersion relation simplifies to

$$
  \omega_k^{(q)}
  = 
  \frac{\Gamma_q^{1/2}}{2\sqrt{\pi}a_q}
  \frac{[k]_q}{L_q},
$$

producing the $q$-deformed Kelvin dispersion. In the damped regime ($\nu_q > 0$), the complex frequency isolates the decay rate

$$
  \gamma_k^{(q)}
  = 
  \frac{\nu_q}{2}\frac{[k]_q^2}{L_q^2}
  = 
  \frac{\hbar_q}{4}\frac{[k]_q^2}{L_q^2}.
$$

Mode $k$ decays on the timescale $\tau_k = 1/\gamma_k^{(q)} = 4L_q^2 / (\hbar_q[k]_q^2)$. Because $[k]_q \sim q^k$ at large $k$, high modes decay **doubly exponentially** in $k$. This generates the rigorous exponential UV cutoff built into the [q-Navier--Stokes definition](#def:q-navier-stokes).
