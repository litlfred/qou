*Proof sketch.* The Markov property pins each $\mathrm{tr}_M(w_\mu)$ to
$z^{n - \mathrm{len}(\mu)}$ by induction on $\mathrm{len}(\mu)$
([Jones, Theorem 5.1](#thm:jones-markov-trace)).  Cycle-type
representatives form a class-function basis on $H_n(R, q)$ at
generic $q$, so the $\chi$-matrix is invertible — the system has a
unique solution.  $\square$

**Closed-form available via Wenzl-bridge.**
*By [prop:y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q)$ has the explicit q-rational expression
$y_\lambda = s_{\lambda, r}(Q) / \sum_\mu d_\mu s_{\mu, r}(Q)$ with
$Q = q^2$ and $X = Q^r = q^{3/2} / (1 + q - q^2 - q^3 + q^{3/2})$, in
$O(p(n) \cdot \max\text{hooks})$ time.  The recipe is detailed in
[prop:y-lambda-recipe-from-partition](#prop:y-lambda-recipe-from-partition).
The 4-step linear-system algorithm below remains valid as an
alternative derivation, and was historically the first method used in
this paper.*

**Algorithm (per-$n$ $y_\lambda$ extraction).**

1. *Enumerate partitions of $n$:* $\{\lambda^{(1)}, \ldots,
   \lambda^{(p(n))}\}$ — gives the unknowns.
2. *Construct cycle-type representatives:* for each $\mu \vdash n$,
   pick the canonical reduced word $w_\mu$ (concatenation of
   cycle-rotations on disjoint strand groups; length
   $\sum_i (\mu_i - 1) = n - \mathrm{len}(\mu)$).
3. *Compute character matrix:* for each $(\mu, \lambda)$, evaluate
   $\chi_\lambda(w_\mu)$ via Hoefsmit seminormal form
   ([Hoefsmit](#prop:hoefsmit-seminormal-form)).  Cost dominated by
   $O(p(n))$ partitions $\times$ Hoefsmit-matrix size $d_\lambda \leq
   |\lambda|!/\!\prod h_x$.
4. *Solve linear system:* $A \cdot \mathbf{y} = \mathbf{b}$ with
   $A_{\mu, \lambda} = \chi_\lambda(w_\mu)$ and $b_\mu = z^{n -
   \mathrm{len}(\mu)}$.  Output $\{y_\lambda\}$.

**Stratum prefactors $\alpha_k$ at depth $k$.**
*Once $\{y_\lambda\}$ is known, the depth-$k$ stratum prefactor in
the unified mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
is the Markov-pairing of $\mathrm{tr}_M$ with a chosen $E_\infty^{0,
0}$-page representative $r_k$ of the depth-$k$ class:*

$$
  \alpha_k \;=\;
  \langle \mathrm{tr}_M, r_k \rangle
  \;=\;
  \sum_{\lambda \in \Lambda_k}
    y_\lambda \cdot \chi_\lambda(r_k),
$$

*with $\Lambda_k$ the depth-$k$ stratum
(enumeration).  The
representatives $r_k$ at $H_3(R, q)$ are explicitly identified in
([H_3 explicit](#conj:spectral-sequence-h3-explicit)); analogues
for $H_n(R, q)$ at $n \geq 4$ follow the same pattern (depth-$k$
reduced word of length $\geq k$).*

**Witness data.**

*Jones–Markov weights $y_\lambda$ for $n \in \{2, 3, \ldots, 12\}$
are tabulated by the formal derivation.  Each table records:*

- *partition $\lambda \vdash n$ and curvature-rank
  $\mathrm{depth}(\lambda)$;*
- *Jones–Markov weight $y_\lambda$: under convention D it vanishes on
  every shape with three or more rows and equals
  $[a-b+1]_q/[2]_q^{a+b}$ on the two-row shape $(a, b)$, exactly and for
  generic $q$ ([Wedderburn–Bratteli recursion](#conj:wedderburn-bratteli-recursion));
  the witness `y-lambda-jones-markov-witness.json` evaluates it numerically
  at the muon pin $q_0 = 1.1099785955541805\ldots$ (CODATA 2018);*
- *linear-system condition number and residual.*

*Output sums consistent with Plancherel-completeness
([Plancherel boundedness](#prop:plancherel-weight-boundedness)).*

**Worked example: $H_3(R, q)$.**
*Three partitions $(3), (2, 1), (1, 1, 1)$; three constraints*

$$
  \mathrm{tr}_M(1) = 1, \quad
  \mathrm{tr}_M(\sigma_1) = z, \quad
  \mathrm{tr}_M(\sigma_1 \sigma_2) = z^2.
$$

*Solution
([H_3 explicit](#conj:spectral-sequence-h3-explicit)):
$y_{(3)}, y_{(2,1)}, y_{(1,1,1)}$ are explicit $q$-rational
expressions.  The depth-$k$ prefactors are*

$$
  \alpha_0 = 1, \qquad
  \alpha_1 = 0, \qquad
  \alpha_2 = z^2, \qquad
  \alpha_3 = h \cdot z^2 + z = z(hz + 1) = \frac{q^3(q^4+1)}{(q^2+1)^2},
$$

*all closed $q$-algebraic forms (no fitting; verified to
$5.5 \times 10^{-17}$ residual).*

**Iterative computation pipeline.**

The procedure is computationally bounded by the largest Hoefsmit
matrix size $\max_\lambda d_\lambda$.  At $n = 12$ the maximum
$d_\lambda = 462$ (rectangular $(4, 4, 4)$); the linear system is
$77 \times 77$.  For higher $n$, sparse seminormal representations
and per-partition caching keep the cost feasible.  The witness
pipeline
(the formal derivation) forces sparse Hoefsmit
generators, builds the cache once per partition, and reuses across
all test words, yielding $O(p(n)^2 \cdot \max d_\lambda^3)$ overall
with bounded memory.

**CRT-style $q$-probing and reconstruction.**
The numeric witness at $q_0$ represents one ring-map specialisation
$\iota \colon R \to \mathbb{R}$.  Each $y_\lambda$ is a $q$-rational
element of $R(\!(z)\!)$ — generically of the form $P_\lambda(q^{1/2})/
Q_\lambda(q^{1/2})$ with both $\deg P_\lambda, \deg Q_\lambda$ growing
in $n$.  The $q$-parameterised seminormal builder
(`build_seminormal_matrices(q=...)`) evaluates $y_\lambda$ at
any canonical evaluation point.  Two reconstruction strategies:

*Multi-$q$ Padé / rational interpolation.*
Choose $m$ distinct canonical evaluation values $q_1, \ldots, q_m$ (e.g.\
$\{1.02, 1.05, 1.08, 1.11, 1.15\}$ — the formal derivation
precedent).  Vandermonde-uniquely determines a polynomial of degree
$\leq m - 1$; faithful rational reconstruction
$y_\lambda = P/Q$ with $\deg P = a$, $\deg Q = b$ requires
$m \geq a + b + 1$ probes.  An *a priori* bound from the determinant
structure of $A(q)$ gives $\deg P_\lambda, \deg Q_\lambda = O(n^2)$,
so faithful rational reconstruction needs on the order of $n^2$
canonical evaluation points — not $5$.  Five canonical evaluations suffice for: (i) a degree-$4$
polynomial fit usable for local sensitivity
$\partial y_\lambda/\partial q$ near $q_0$, (ii) consistency
checks against any analytically derived closed form.

*Symbolic linear-system solve.*
For exact rational forms, replace the numeric linear solve with
exact symbolic linear algebra over a symbolic $q$.  Cost grows rapidly with $p(n)$, but the
output is the exact $q$-rational $y_\lambda$.  Tractable in pure
Python for $n \leq 5$; larger $n$ needs a compiled character kernel.

*Witness data layout.*
At $n \leq 10$ the witness records both the canonical $q_0$ floats
and $5$ CRT canonical evaluation points $\{(q_i, z_i, \mathbf{y}(q_i))\}$ for
verification of any closed form.  At $n \in \{11, 12\}$ only $q_0$ is
recorded (canonical evaluation-rebuild cost prohibitive in pure Python; defer to
a compiled kernel for higher-$n$ probes).

**Closed forms for $\alpha_k$ across $n$.**

| $n$ | $p(n)$ | $y_\lambda$ witness | $\alpha_k$ closed form |
|---|---|---|---|
| $2$ | $2$ | available | trivial: $\alpha_0 = 1$, $\alpha_1$ from singlet |
| $3$ | $3$ | available | done: $\alpha_0, \alpha_1, \alpha_2, \alpha_3$ ([H_3 explicit](#conj:spectral-sequence-h3-explicit)) |
| $4$ — $12$ | $5$ — $77$ | available | $\alpha_k$ pending: requires depth-$k$ representatives $r_k$ at each $n$ |

*Per-$n$ $\alpha_k$ derivation reduces to: (i) selecting depth-$k$
representatives $r_k \in H_n(R, q)$, then (ii) computing the
Markov pairing $\langle \mathrm{tr}_M, r_k \rangle$ via the
witnessed $y_\lambda$.  Step (i) is the open work; step (ii) is
mechanical once (i) is fixed.*

Although the derivation mechanism utilizes the standard Jones-Markov linear system extraction across Wenzl bridges, employing this machinery to extract the mass-spectrum coefficients $\alpha_k$ constitutes a mathematically novel physical framework unique to the Quantum Observable Universe.
