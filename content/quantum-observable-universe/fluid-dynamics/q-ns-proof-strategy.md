We build the proof of [global regularity](#thm:q-ns-wellposedness) on
three mechanisms, each exploiting $q > 1$.

**Step 1: Exponential UV damping.**
The $q$-Laplacian eigenvalues $[k]_q^2$ grow as
$q^{2k}/(q-q^{-1})^2$ for large $k$
([Kelvin dispersion](#prop:kelvin-dispersion-derivation)).
We find that mode $k$ dissipates at rate
$\gamma_k = \nu_q [k]_q^2 / L_q^2$, which grows exponentially in
$k$.  The enstrophy $\Omega(t) = \sum_k [k]_q^2 |\hat{v}_k|^2$
satisfies $d\Omega/dt \leq -\nu_q [1]_q^2\Omega + C\Omega^{3/2}$.
At $q = 1$ the damping coefficient vanishes; at $q > 1$ it
provides a linear restoring term.

**Step 2: Finite cascade depth.**
The [Planck--Reynolds number](#rem:planck-reynolds)
$\mathrm{Re}_q = 2/(q-1)$ bounds the number of active modes:
$N_{\mathrm{eff}} \leq \lfloor \log_q(\mathrm{Re}_q^{3/4})
\rfloor < \infty$.  We therefore reduce the q-NS equation to a
finite-dimensional ODE, which we recognize as globally well-posed
by Picard--Lindelof.

**Step 3: Bootstrap to smoothness.**
We observe that higher modes decay to zero in finite time.  Applying
parabolic regularity to the truncated system, we obtain $v \in C^\infty$
for $t > 0$.  Uniqueness then extends the initial regularity.

| Mechanism | Role | Failure at $q = 1$ |
|---|---|---|
| Exponential eigenvalue growth | UV regularisation | $[k]_1 = k$ (polynomial) |
| Positive viscosity $\nu_q > 0$ | Enstrophy damping | $\nu_1 = 0$ |
| Finite cascade depth | Dimensional reduction | $N_{\mathrm{eff}} \to \infty$ |

The dissipation term $2\nu_q\sum_k [k]_q^2 |\hat{v}_k|^2$ in
the energy inequality converges absolutely for $q > 1$ because
$[k]_q^2 |\hat{v}_k|^2$ decays faster than any geometric
series.  This absolute convergence — absent at $q = 1$ — is
the analytic content of the exponential UV cutoff.
