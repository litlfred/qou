### Proof of the sum identity

**Step 1 (multiplication formula).** The classical $N$-th roots-of-unity
multiplication identity for $\mathrm{Li}_n$:

$$
  \sum_{k = 1}^{N - 1} \mathrm{Li}_n(\zeta_N^k)
  \;=\;
  \bigl( N^{1 - n} - 1 \bigr) \cdot \zeta(n).
$$

For $N = 5$, $n = 3$:

$$
  \sum_{k = 1}^{4} \mathrm{Li}_3(\zeta_5^k)
  \;=\;
  -\frac{24}{25} \cdot \zeta(3).
$$

**Step 2 (real part).** Take real parts of both sides.

LHS: $\sum_k \mathrm{Re}\,\mathrm{Li}_3(\zeta_5^k) = \sum_k \mathrm{Cl}_3(2\pi k/5)$.

By the parity $\mathrm{Cl}_3(2\pi - \theta) = \mathrm{Cl}_3(\theta)$ (since
$\cos$ is $2\pi$-periodic and even):

$$
  \mathrm{Cl}_3(8\pi/5) \;=\; \mathrm{Cl}_3(2\pi/5),
  \qquad
  \mathrm{Cl}_3(6\pi/5) \;=\; \mathrm{Cl}_3(4\pi/5).
$$

So LHS $= 2 (\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5))$.

RHS: $\zeta(3) \in \mathbb{R}$, so RHS $= -24\zeta(3)/25$.

**Step 3 (combine).**

$$
  2 (\mathrm{Cl}_3(2\pi/5) + \mathrm{Cl}_3(4\pi/5))
  \;=\;
  -\frac{24}{25} \zeta(3),
$$

giving the boxed sum identity. $\square$

### canonical structural verification at 50 dps

Numerical evaluation at 50 decimal places:

| Quantity | Value (50 dps) |
|---|---|
| $\mathrm{Cl}_3(2\pi/5)$ | $0.18936791501083168387944480476641361363127422974423\ldots$ |
| $\mathrm{Cl}_3(4\pi/5)$ | $-0.76635522852743694087131912229190960919846765006767\ldots$ |
| Sum | $-0.57698731351660525699187431752549599556719342032344\ldots$ |
| $-(12/25)\,\zeta(3)$ | $-0.57698731351660525699187431752549599556719342032344\ldots$ |
| Residual | $1.34 \times 10^{-51}$ |

### The 2-dim Bring trilog regulator image

Combining the reflection-formula reductions with the identity above, the
2-dim Borel-rank space
$K_5^{\mathrm{ind}}(\mathbb{Q}(\zeta_5)) \otimes \mathbb{Q}$ admits the
following decomposition:

| Generator | Closed form / status | Dimension |
|---|---|---|
| **(a)** $\zeta(3)$-line (= sum of real parts $\times$ $-25/12$) | **theorem**: external; classical Apéry constant | 1 |
| **(b)** Antisymmetric: $\mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5)$ | **open**: no closed form modulo $\zeta(3)$ + Tate | 1 |
| **Total** | | **2** (matches Borel rank) |

The genuinely-new content of the depth correspondence at depth 3 over $\mathbb{Q}(\zeta_5)$
is therefore **one specific real number**:

$$
  \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right)
  \;=\; 0.95572314353826862475076392705832322282974187981191\ldots
$$

Whether this admits a closed form modulo $\zeta(3)$ + Tate is **open**.
Reflection-formula reductions and multiplication-formula
reductions (the present proposition) have been exhausted at depth 3 over $\mathbb{Q}(\zeta_5)$;
further reductions would require Goncharov's 22-term relation or
similar weight-3 functional equations.

### Reduction of the depth-3 surface

| Item | Status before this proposition | Status after |
|---|---|---|
| Im Li_3(ζ_5) | Tate-rational (reflection formula) | Tate-rational (no change) |
| Im Li_3($\zeta_5^2$) | candidate | **Tate-rational**: $2\pi^3/125$ |
| Cl_3(2π/5) + Cl_3(4π/5) | candidate (open) | **theorem**: $-12\zeta(3)/25$ |
| Cl_3(2π/5) - Cl_3(4π/5) | candidate (open) | **still open** — only remaining genuinely-new content |

**The depth-3 unproved surface for the depth correspondence over $\mathbb{Q}(\zeta_5)$
shrinks from "2 candidate generators, 4 unknowns" to "1 specific
real number" ($\approx$ 0.955).**
