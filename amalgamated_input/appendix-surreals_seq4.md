<!-- FILE_START: b1-current-status.md -->
**Remark (canonical B1 current-status synthesis — what is theorem, what is open, after eleven rounds of sharpening).**

The keystone B1 ([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)) has been progressively sharpened across eleven rounds. We collect the current status in one canonical place.

**Summary:** B1 is theorem-level at depths 1, 2 over every Bring-natural number field and at the figure-8 / 7 torus-knot / Borromean / Whitehead rows; conditionally theorem-level at depth 3 over $\mathbb{Q}(\zeta_5)$ modulo a single specific real number; conjectural at depth $\ge$ 3 over arbitrary $F$ via Beilinson/Goncharov.

After eleven rounds, B1's open content reduces to:

1. **Per-knot VC discharges** for chiral hyperbolic Bring-embeddable knots ($5_2$, $6_*$, $7_*$, $8_*$). This is active classical knot-theory research, not paper-internal.
2. **One specific real number** at depth 3 over $\mathbb{Q}(\zeta_5)$:
   $$
     \mathrm{Cl}_3\!\left(\tfrac{2\pi}{5}\right) - \mathrm{Cl}_3\!\left(\tfrac{4\pi}{5}\right) \approx 0.95572314353826862\ldots
   $$
   This has no known closed form modulo $\zeta(3) + (2\pi i)^3 \mathbb{Q}$. It generates the antisymmetric component of the 2-dim regulator image.
3. **Goncharov motivic conjecture at $\mathbb{Q}(\zeta_5)$**. The discharge plan resides in [`conj:qou-infra-discharges-goncharov-zeta5`](#conj:qou-infra-discharges-goncharov-zeta5).
4. **Beilinson's conjecture at depth $\ge$ 4** (external).
5. **Geometric realisation of $\mathrm{Cl}_3(2\pi/5)$**. Three candidates are listed; SnapPy CS computation on Bring torus knots is the smallest concrete test.

See [Table 2](#tbl:b1-current-status-table2-data) for numerical witnesses (50-dps verified).
See [Table 3](#tbl:b1-current-status-table3-data) for contributions of rounds 1–11.

The graded-Mikusiński / Goncharov-period-correspondence framework is substantially established:
- **Structural conjectures** (joint action, bridge map at small $n$, bi-filtration well-definedness, Hecke-Baer-* at generic $q$) are all theorem-level.
- **Numerical witnesses** at depths 2 and 3 are verified to 50 dps.
- **B1 keystone** is theorem-level on its principal rows (figure-8, torus knots, Borromean, Whitehead) and conditionally theorem-level on others modulo VC discharges.
- **The depth-3 unproved surface** has shrunk to a single specific real number plus standard external conjectures.

The remaining work is outsourced to established research areas (Volume Conjecture, Beilinson, motivic cohomology) rather than residing as paper-internal conjectural content.
<!-- FILE_END: b1-current-status.md -->

<!-- FILE_START: calculus-up-to-epsilon.md -->
While surreal numbers lack a Hilbert-space completion and canonical Lebesgue measure, a substantial fragment of differential and formal integral calculus lifts to $\mathbf{No}$ up to an infinitesimal correction. We record what works and how classical analysis is recovered via the standard-part map.

**1. Differential calculus: Jackson derivative as the native $d/dx$**
Fix an infinitesimal $\varepsilon \in \mathbf{No}$ with $\varepsilon > 0$ and set $q = 1 + \varepsilon$. The Jackson $q$-derivative

$$
  d_q f(x) = \frac{f(q x) - f(x)}{(q - 1)\, x} = \frac{f((1+\varepsilon) x) - f(x)}{\varepsilon\, x}
$$

is a native difference quotient on $\mathbf{No}$. Both numerator and denominator are surreals, and their ratio is well-defined wherever $\varepsilon \, x \neq 0$. For a standard function $f : \mathbb{R} \to \mathbb{R}$ lifted polynomially to $\mathbf{No}$, the classical derivative is recovered as

$$
  \frac{df}{dx}(x_0) = \mathrm{st}\!\left(d_q f(x_0)\right) \qquad (x_0 \in \mathbb{R},\; q = 1 + \varepsilon).
$$

The classical-limit functor, which breaks as an honest limit under surreal replacement, is replaced by the standard-part map composed with evaluation at a specific surreal $q$. More generally, Berarducci--Mantova (2018) construct a genuine derivation $D : \mathbf{No} \to \mathbf{No}$ extending $d/dx$ on $\mathbb{R}$, making $\mathbf{No}$ a differential field. Many transcendental identities extend accordingly.

**2. Formal integration: antiderivative exists, measure does not**
Berarducci--Mantova show that $\mathbf{No}$ admits a right inverse to $D$. For every $f \in \mathbf{No}$ there exists an antiderivative $F$ with $D(F) = f$. This gives an honest indefinite integral $\int f \, dx \in \mathbf{No}$ for every surreal function, up to a constant of integration.

A definite integral $\int_a^b f \, dx$ agreeing with Lebesgue on $\mathbb{R}$-valued inputs does not exist. We use $d_q$ as the native derivative and reserve $\int$ for either the categorical Frobenius integral or the standard-part of Riemann sums computed on $\mathbf{No}$-valued partitions.

**3. Limits become evaluations**
Every classical sequential limit $L = \lim_{n \to \infty} a_n$ translates to $L = \mathrm{st}(a_\omega)$, where $\omega \in \mathbf{No}$ is the first infinite ordinal and $a_\omega$ is the surreal obtained by transfer of the formula defining $a_n$. Limits become named values rather than formal processes. $\lim_{q \to 1}$ becomes evaluation at $q = 1 + \varepsilon$, and the classical result is the standard-part. Double limits and iterated sup/inf over uncountable index sets require care.

**4. Formal power series: the safe regime**
All formal-power-series identities used in the main paper ($\exp_q, \log_q, \mathrm{Li}_2^q$, quantum dilogarithm, character generating functions) lift directly because they are manipulations in $K[[x]]$ for $K = \mathbf{No}$. Convergence is replaced by formal convergence. The information-theory chapter computations survive: entropies, Lyapunov exponents, and bandwidth formulas are rational or formal-power-series expressions in $q$.

**5. Measure up to $\varepsilon$: Loeb construction**
Given a hyperfinite partition of $[0, 1] \subset \mathbf{No}$ into $N = \omega$ equal subintervals, the counting measure divided by $N$ gives a hyperfinite measure on $[0,1]_{\mathbf{No}}$. Its standard-part is Lebesgue measure on $[0, 1] \subset \mathbb{R}$. This Loeb measure is not canonical but behaves well for standard integrands. For the Möbius energy integral, one can define a Loeb measure on $S^1 \times S^1 \subset \mathbf{No}^2$, evaluate the integrand $1/|x - y|^2$ against it, and take the standard-part after subtracting the regulariser. To infinitesimal precision, this yields the classical Möbius energy.

See [Table](#tbl:calculus-up-to-epsilon-table-data).

For the substrate-parameter $q \to 1$ limit, the surreal framework sharpens the theory by naming the infinitesimal regime explicitly. The absence of a canonical Lebesgue measure and a Hilbert completion is manageable because QOU uses neither in a load-bearing way: integration is categorical (Frobenius counit), decomposition is algebraic (Hoefsmit), and analytic-looking quantities ($d_H(q)$, $c_q$, $\hbar_q$) are rational in $q$.
<!-- FILE_END: calculus-up-to-epsilon.md -->

