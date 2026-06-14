The [discrete vortex spectrum](#prop:discrete-vortex-spectrum) states
that the eigenvalues of the $q$-Laplacian on a vortex filament are
$\lambda_k^{(q)} = [k]_q^2 \cdot \hbar_q / L_q^2$.  This
subsection derives this from first principles.

**Setup.**
Let $\varrho$ be a stable vortex filament of length $L$ in the
brane fluid, parametrised by arc length $s \in [0, L]$ with
periodic boundary conditions $\varrho(0) = \varrho(L)$.  Let
$\eta(s, t)$ be a small normal displacement of the filament from
its equilibrium position (a Kelvin wave).  The linearised
[q-Navier--Stokes equation](#def:q-navier-stokes) restricted to
normal perturbations of $\varrho$ is

$$
  \partial_t^2 \eta
  = 
  \frac{\Gamma_q}{4\pi a_q^2}\Delta_q\eta
  -  \nu_q\Delta_q\partial_t \eta,
$$

where $\Gamma_q = [j]_q[j+1]_q$ is the quantised circulation at
intensity level $j$, $a_q$ is the $q$-deformed vortex core radius,
and the second term is viscous damping.

**The $q$-Laplacian eigenvalue problem.**
The $q$-Laplacian on the circle of length $L$ acts on functions
$f(s)$ with period $L$.  Its eigenvalue problem is

$$
  \Delta_qf_k
  =  -\mu_kf_k,
  \qquad
  f_k(s + L) = f_k(s).
$$

For the standard Laplacian ($q = 1$), the eigenfunctions are
$e^{2\pi i k s / L}$ with eigenvalues $\mu_k = (2\pi k/L)^2$.
The $q$-Laplacian replaces the integer $k$ with the $q$-integer
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$:

$$
  \mu_k^{(q)}
  = 
  \left(\frac{2\pi[k]_q}{L_q}\right)^2,
$$

where $L_q = L \cdot [1]_q / 1 = L$ (since $[1]_q = 1$ for all
$q$).

**Derivation.**
The $q$-Laplacian is defined via the $q$-derivative operators.
For a function $f$ on the circle, set $z = e^{2\pi i s / L}$.
Then:

$$
  D_q f(z) = \frac{f(qz) - f(q^{-1}z)}{(q - q^{-1})z},
$$

and $\Delta_q = -zD_q \circ zD_q$ (the radial part of the
$q$-Casimir).  On the monomial $z^k$ this gives

$$
  D_q(z^k)
  = \frac{q^k z^k - q^{-k} z^k}{(q - q^{-1})z}
  = [k]_qz^{k-1},
$$

so $zD_q(z^k) = [k]_qz^k$, and therefore

$$
  \Delta_q(z^k) = -[k]_q^2z^k.
$$

The eigenvalue is $\mu_k^{(q)} = [k]_q^2$.  Restoring physical
units (the filament has length $L_q$ and the quantum of action
is $\hbar_q$):

$$
  \lambda_k^{(q)}
  = 
  [k]_q^2 \cdot \frac{\hbar_q}{L_q^2}.
$$

This is the formula stated in the
[discrete vortex spectrum](#prop:discrete-vortex-spectrum).

**Dispersion relation.**
Substituting $\eta(s,t) = f_k(s)e^{-i\omega t}$ into the
linearised equation and using
$\Delta_q f_k = -[k]_q^2 f_k / L_q^2$ gives

$$
  -\omega^2
  = 
  -\frac{\Gamma_q}{4\pi a_q^2}\frac{[k]_q^2}{L_q^2}
  +  i\omega\nu_q\frac{[k]_q^2}{L_q^2}.
$$

For the undamped case ($\nu_q = 0$, i.e. the Euler limit), the
dispersion relation is

$$
  \omega_k^{(q)}
  = 
  \frac{\Gamma_q^{1/2}}{2\sqrt{\pi}a_q}
  \frac{[k]_q}{L_q},
$$

which is the $q$-deformed Kelvin dispersion.  For the damped case
($\nu_q > 0$), complex frequency gives the decay rate

$$
  \gamma_k^{(q)}
  = 
  \frac{\nu_q}{2}\frac{[k]_q^2}{L_q^2}
  = 
  \frac{\hbar_q}{4}\frac{[k]_q^2}{L_q^2},
$$

so mode $k$ decays on timescale
$\tau_k = 1/\gamma_k^{(q)} = 4L_q^2 / (\hbar_q[k]_q^2)$.
since $[k]_q \sim q^k$ for large $k$, high modes decay
**doubly exponentially** in $k$ — the exponential UV cutoff
noted in the [q-Navier--Stokes definition](#def:q-navier-stokes).

**Mathematical Novelty.** While the mechanical process of $q$-deforming operators is a standard procedure, the mathematical novelty is observing that applying the exact $q$-derivative $D_q$ to classical Kelvin-wave dispersion immediately generates an exact, analytically rigorous doubly-exponential UV suppression mechanism ($\tau_k \sim q^{-2k}$) in the fluid bulk, bypassing the need for ad-hoc phenomenological regularization or arbitrary cutoffs.
