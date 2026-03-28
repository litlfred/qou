Suppose the $q$-logarithmic zeta function
([$q$-logarithmic zeta](#def:q-logarithmic-zeta)) has a non-trivial
zero $\rho = \beta + i\gamma$ with
$\beta \neq \sigma_q = d_H(q)/2$
([$q$-critical line conjecture](#conj:q-critical-line)).  What
breaks?

**1. Orbit-counting anomaly.**
The analogue of the prime-counting function $\pi(x)$ is the
**Reeb orbit-counting function**:

$$
  \Pi_q(N) \;:=\; \#\{\gamma : |\gamma| \leq N\},
$$

counting primitive periodic orbits of $f_q$ up to period $N$.  By a
$q$-analogue of the explicit formula:

$$
  \Pi_q(N)
  \;=\; \operatorname{li}_q(q^N)
  - \sum_\rho \operatorname{li}_q(q^{\rho N})
  + \text{(lower order)},
$$

where $\operatorname{li}_q$ is a $q$-logarithmic integral.  A zero
at $\beta > \sigma_q$ produces an oscillatory term of magnitude
$q^{(\beta - \sigma_q)N}$ — **exponentially growing** fluctuations
in the orbit count.  The Reeb dynamics would have anomalously
clustered periods at some scales and anomalous gaps at others.

**2. Broken unitarity.**
The $q$-functional equation
$\zeta_q(s) = \chi_q(s)\,\zeta_q(d_H - s)$ pairs each zero
$\rho$ with a mirror $d_H - \bar{\rho}$.  If $\beta \neq \sigma_q$,
the zero and its mirror are at different distances from the critical
line.  In the spectral interpretation (Hilbert–Pólya), this means
the underlying operator is **not self-adjoint** on the Julia-set
Hilbert space $L^2(J(f_q), \mu_q)$.

Physically: the $R$-matrix of the braided tensor category would
fail to be unitary.  Braiding two particles and then unbraiding
would not return to the original state — **information would be
lost (or created) in a single braiding operation**.

**3. Entropy bound violation.**
The operational entropy $\eta_q = (2q-1)/q^3$
([operational entropy](#def:operational-entropy)) is derived from
the self-consistency condition $G_{\mathrm{Planck}} = 1$ under the
assumption that the orbit distribution follows the $q$-prime number
theorem (zeros on the $q$-critical line).  An off-critical zero at
$\beta > \sigma_q$ would contribute an excess entropy term:

$$
  \Delta\eta
  \;\sim\; q^{-(\beta - \sigma_q)\,|\gamma|}\,
           \cos(|\gamma|\,\operatorname{Im}(\rho)\,\ln q),
$$

an oscillation modulated by the imaginary part of the zero.  The
gravitational self-consistency
$G_{\mathrm{Planck}} = 1$ would fail at the scale set by
$|\gamma|$ — gravity would **fluctuate** at that scale.

**4. The three regimes.**

| Scenario | $\beta$ vs $\sigma_q$ | Physical consequence |
|----------|----------------------|---------------------|
| $\beta = \sigma_q$ | On critical line | Optimal orbit distribution; unitarity; $G = 1$ exact |
| $\beta > \sigma_q$ | Right of critical | Orbit clustering; entropy excess; gravity too strong at scale $|\gamma|$ |
| $\beta < \sigma_q$ | Left of critical | Orbit gaps; entropy deficit; gravity too weak at scale $|\gamma|$ |

**5. Why classical RH is a special case.**
At $q = 1$: $\sigma_1 = 1/2$, the orbit-counting function
$\Pi_1(N) = \pi(e^N)$ (prime-counting), the Julia set is the unit
circle ($d_H = 1$), and the $R$-matrix is trivially unitary
(braid group collapses to the symmetric group).  The Riemann
Hypothesis is the statement that the **classical limit of the
substrate is unitarity-preserving** — the symmetric group has no
information leakage.

For $q \neq 1$, the question is not whether zeros lie on
$\operatorname{Re}(s) = 1/2$ — they generically do not.  The
question is whether they lie on $\operatorname{Re}(s) = \sigma_q$.
The $q$-RH is a **deformed unitarity condition**: the substrate
parameter shifts the critical line, and the physics is consistent
precisely when zeros track this shift.

**6. Falsifiability.**
The orbit periods $|\gamma|$ are computable for the quadratic
iteration $f_q(z) = z^2 + c(q)$ over $\mathbb{F}_p$ for any prime
$p$ ([discrete Planck step](#rem:discrete-planck-step)).  The
orbit-counting function $\Pi_q(N)$ over $\mathbb{F}_p$ is a finite
sum, and the zeros of the corresponding Weil zeta function are
computable.  For $q$ a prime power, the Weil conjectures (proved
by Deligne) guarantee all zeros are on $\operatorname{Re}(s) = 1/2$
— which equals $\sigma_q$ only when $d_H(q) = 1$.  The tension
between the Weil bound and the $q$-critical line conjecture is
itself a testable prediction: for prime-power $q$ with
$d_H(q) \neq 1$, the dynamical zeta $Z_q$ and the Weil zeta
$Z_{\mathbb{F}_q}$ must **disagree on the location of zeros**.
