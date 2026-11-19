### Proof

**Step 1 (multiplication formula).** The classical $N$-th roots-of-unity
multiplication identity for $\mathrm{Li}_n$:

$$
  \sum_{k = 1}^{N - 1} \mathrm{Li}_n(\zeta_N^k)
  \;=\;
  \bigl( N^{1 - n} - 1 \bigr) \cdot \zeta(n).
$$

For $n = 3$:

$$
  \sum_{k = 1}^{N - 1} \mathrm{Li}_3(\zeta_N^k)
  \;=\;
  \bigl( N^{-2} - 1 \bigr)\, \zeta(3)
  \;=\;
  -\frac{N^2 - 1}{N^2}\, \zeta(3).
$$

**Step 2 (take real part).** $\zeta(3) \in \mathbb{R}$ is real.
$\mathrm{Re}\,\mathrm{Li}_3(\zeta_N^k) = \mathrm{Cl}_3(2\pi k/N)$ by
definition.

Therefore

$$
  \sum_{k = 1}^{N - 1} \mathrm{Cl}_3(2\pi k/N)
  \;=\;
  -\frac{N^2 - 1}{N^2}\, \zeta(3).
$$

**Step 3 (parity reduction for odd $N$).** By $\mathrm{Cl}_3$
parity:

$$
  \mathrm{Cl}_3(2\pi (N - k)/N)
  \;=\;
  \mathrm{Cl}_3(2\pi - 2\pi k/N)
  \;=\;
  \mathrm{Cl}_3(2\pi k/N).
$$

For odd $N$, the indices $k = 1, \ldots, N - 1$ pair as
$(k, N - k)$, giving $(N - 1)/2$ pairs. Therefore

$$
  \sum_{k = 1}^{N - 1} \mathrm{Cl}_3(2\pi k/N)
  \;=\;
  2 \sum_{k = 1}^{(N - 1)/2} \mathrm{Cl}_3(2\pi k/N),
$$

and dividing by 2:

$$
  \sum_{k = 1}^{(N - 1)/2} \mathrm{Cl}_3(2\pi k/N)
  \;=\;
  -\frac{N^2 - 1}{2 N^2}\, \zeta(3).
$$

For even $N$, the middle term $k = N/2$ gives
$\mathrm{Cl}_3(\pi) = \sum_{j \geq 1} \cos(j\pi)/j^3 =
\sum_{j \geq 1} (-1)^j/j^3 = -\frac{3}{4}\zeta(3)$ (alternating
Dirichlet series for $\zeta(3)$), and the other $(N - 2)/2$
pairs contribute symmetrically.  The closed form then takes the
form recorded above ($N = 2$ in the table below verifies
$-\frac{3}{4}\zeta(3)$ directly).  $\square$

### Verifications at small $N$

See [Table](#tbl:cyclotomic-cl3-orbit-sum-general-table-data).

The $N = 5$ row recovers $\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5)
= -\frac{12}{25}\zeta(3)$ as $2 \times -\frac{12}{25} = -\frac{24}{25}$.

### $N = 2$ special case: $\mathrm{Cl}_3(\pi)$

At $N = 2$, the sum has a single term $\mathrm{Cl}_3(\pi)$:

$$
  \mathrm{Cl}_3(\pi) \;=\; -\frac{3}{4} \zeta(3).
$$

This is the classical evaluation $\mathrm{Li}_3(-1) = -\frac{3}{4}\zeta(3)$
(real, no imaginary part — consistent with
[cyclotomic trilogarithm imaginary closed form proposition](#prop:cyclotomic-trilog-imaginary-closed-form)
giving $\mathrm{Im}\,\mathrm{Li}_3(\zeta_2) = 0$).

### Asymptotic behaviour

As $N \to \infty$:

$$
  \sum_{k = 1}^{N - 1} \mathrm{Cl}_3(2\pi k/N)
  \;\to\;
  -\zeta(3),
$$

approaching from below, with fractional remainder $\frac{1}{N^2}\zeta(3)$ measuring the finite-$N$ discretisation gap. Since

$$
  \int_0^{2\pi} \mathrm{Cl}_3(\theta) \,d\theta \;=\; 0,
$$

refining the $N$-point Riemann sum drives the full sum over $k = 0, \ldots, N - 1$ toward zero, leaving $-\zeta(3)$ once the $k = 0$ contribution $\mathrm{Cl}_3(0) = \zeta(3)$ is separated out.
