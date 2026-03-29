The six embeddable torus knots on the Bring surface determine
the **shell binding hierarchy** of the nuclear Skein polynomial.
The four knots $T_{2,n}$ with $n = 3, 5, 7, 9$ on two strands
provide crossing coefficients for the transfer matrix.  The two
knots $T_{3,4}$ and $T_{3,5}$ on three strands mediate shell
reorganisation and weak transitions respectively.

## The six torus knots

The four $T_{2,n} = \sigma^n$ in $H_2(q)$ reduce via the Hecke
recurrence $\sigma^{k+1} = (q - q^{-1})\sigma^k + \sigma^{k-1}$
to a linear element $c_n \sigma + d_n$.  The two $T_{3,m} =
(\sigma_1\sigma_2)^m$ in $H_3(q)$ reduce to 6-term elements.

| Knot | Strands | Crossings | $r \times s$ | Trace | $\log_q$ | Fiber |
|:----:|:-------:|:---------:|:---:|:---:|:---:|:---:|
| $T_{2,3}$ | $2$ | $3$ | $6$ | $0.730$ | $-3.01$ | deg $1$ |
| $T_{2,5}$ | $2$ | $5$ | $10$ | $0.993$ | $-0.07$ | deg $1$ |
| $T_{2,7}$ | $2$ | $7$ | $14$ | $1.299$ | $+2.51$ | deg $1$ |
| $T_{2,9} = T_{2,3^2}$ | $2$ | $9$ | $18$ | $1.662$ | $+4.87$ | deg $2$ |
| $T_{3,4} = T_{3,2^2}$ | $3$ | $8$ | $12$ | $0.585$ | $-5.14$ | deg $2$ |
| $T_{3,5}$ | $3$ | $10$ | $15$ | $0.704$ | $-3.37$ | deg $1$ |

The degree-$2$ knots are **fiber ascents**: $T_{2,9} = (T_{2,3})^3$
squares the trefoil along the color fiber ($3 \to 3^2 = 9$),
and $T_{3,4} = T_{3,2^2}$ squares the Hopf structure along the
degree-$2$ fiber on $3$ strands ($2 \to 2^2 = 4$).

Both degree-$2$ knots have **unit-modulus eigenvalues** in the
standard representation ($|\mu| = 1$, $\det = 1$), acting as
pure rotations:
- $T_{3,4}$: phase $105.7°$ per period, period $3.4$ channels
- $T_{3,5}$: phase $153.6°$ per period, period $2.3$ channels

## Shell-size assignment

Each torus knot contributes **two invariants**: its product
$r \times s$ and its crossing number $\min(r(s\!-\!1),\,
s(r\!-\!1))$.  The shell sizes of the nuclear chart are
determined by these invariants.

| Shell | Size | Knot match | Invariant |
|:-----:|:----:|:----------:|:---------:|
| $1$ | $2$ | bare | Below knot threshold |
| $2$ | $6$ | $T_{2,3}$ | $r \times s = 2 \times 3 = 6$ |
| $3$ | $12$ | $T_{3,4}$ | $r \times s = 3 \times 4 = 12$ |
| $4$ | $8$ | $T_{3,4}$ | crossings $= 8$ |
| $5$–$7$ | $22, 32, 44$ | combinations | Open (sums of products) |

The first four shells match exactly to the knot invariants.
Shells $5$–$7$ require **combinations** of knot products and
are the subject of ongoing computation.

The degree-$2$ knot $T_{3,4} = T_{3,2^2}$ appears **twice**:
its product ($12$) determines shell $3$, and its crossing
number ($8$) determines shell $4$.  This dual role reflects
the degree-$2$ fiber structure — $T_{3,4}$ has two independent
invariants because it ascends one level in the fiber.

## The $\mathcal{Q}_q$-value as a knot operator product

**Proposition.**
*The $\mathcal{Q}_q$-value for $\beta^-$ decay
$\mathcal{N}(Z, N) \to \mathcal{N}(Z\!+\!1, N\!-\!1)$ is:*

$$
  \mathcal{Q}_q
  \;=\;
  \mathcal{Q}_{\mathrm{bare}}
  \;\times\;
  \prod_{T_{r,s}}
  F(T_{r,s},\, N)
$$

*where the product runs over **all** torus knots $T_{r,s}$, and
each knot contributes the operator:*

$$
  F(T_{r,s},\, N)
  \;=\;
  \begin{cases}
    1
    & \text{if } \tfrac{(r-1)(s-1)}{2} > g
    \quad\text{(not embeddable on $\Sigma_g$: null operator)} \\[6pt]
    1
    & \text{if shell}(T_{r,s}) \text{ is identical in parent and daughter}
    \quad\text{(cancels in $\mathcal{Q}$ ratio)} \\[6pt]
    \mathrm{tr}_M\!\bigl(T_{r,s} \cdot \Delta_{\mathrm{mix}}\bigr)
    & \text{if shell}(T_{r,s}) \text{ contains the converting neutron, partially filled} \\[6pt]
    \dfrac{\bigl|\mathrm{tr}_M\!\bigl(
      e_{(1^3)} \cdot T_{r,s} \cdot \Delta_{\mathrm{mix}} \cdot e_{(1^3)}
    \bigr)\bigr|}{\bigl|\mathrm{tr}_M(\Delta_{\mathrm{mix}})\bigr|}
    & \text{if shell}(T_{r,s}) \text{ contains the converting neutron, fully filled}
  \end{cases}
$$

*Here:*

*1. $\mathcal{Q}_{\mathrm{bare}} = |\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times
   \hbar_q \cdot \mathfrak{E}_{\times} \cdot \mu_0$ is the Level 0
   transfer matrix ratio, with $P(q) = \prod_i \hat{V}_i(q)$ the
   Skein polynomial.  Here $\log_q(x) = \ln x / \ln q$ is the
   $q$-natural logarithm and $\hbar_q = 1 - q^{-1}$ is the quantum
   Planck constant.  The product $\hbar_q / \ln q$ is the
   **$q$-anomaly factor**: it equals $1$ at $q = 1$ and $0.9496$
   at the substrate $q$, encoding the $5\%$ deviation of the
   quantum Planck constant from its classical limit.*

*2. $\Delta_{\mathrm{mix}} = \sigma_0 \sigma_1^{-1}$ is the
   universal $\pm 1$ transition operator.*

*3. $e_{(1^3)} = \sum_{w \in S_3} (-q^{-1})^{\ell(w)} T_w \,/\,
   P_3(q^{-2})$ is the alternating Young symmetrizer idempotent
   of $H_3(q)$.*

*4. $g = 4$ is the genus of the Bring surface $\Sigma_4$.*

### Why the product collapses to one term

The $\mathcal{Q}_q$-value is a **difference** $S_q(\mathrm{par})
- S_q(\mathrm{dau})$.  The parent and daughter share all shells
except the one containing the converting neutron: inner shells
cancel in the ratio $P_{\mathrm{dau}}/P_{\mathrm{par}}$.  Hence
$F(T_{r,s}, N) = 1$ for every knot whose shell is unchanged by
the decay.  The product reduces to a **single active term** —
the knot $T_{k^*}$ of the converting neutron's shell:

$$
  \prod_{T_{r,s}} F(T_{r,s}, N)
  \;=\;
  F(T_{k^*}, N)
$$

Non-embeddable knots ($\tfrac{(r-1)(s-1)}{2} > 4$) contribute
the identity automatically — they have zero topological action
on $\Sigma_4$, analogous to a zero-volume knot in the hyperbolic
picture.

### Numerical values

The six embeddable torus knots give the following operator
averages with $\Delta_{\mathrm{mix}}$:

| Knot | $\mathrm{tr}_M(T \cdot \Delta)$ | $|\mathrm{tr}_M(e_{\mathrm{alt}} \cdot T \cdot \Delta \cdot e_{\mathrm{alt}})| / |\mathrm{tr}_M(\Delta)|$ | Shell | Active when |
|:----:|:---:|:---:|:---:|:---:|
| $T_{2,3}$ | $0.3649$ | $0.4667$ | $1$ | $N \leq 2$ |
| $T_{2,5}$ | $0.4251$ | $0.3788$ | $2$ | $2 < N \leq 8$ |
| $T_{2,7}$ | $0.5040$ | $0.3075$ | $3$ | $8 < N \leq 20$ |
| $T_{3,5}$ | $1.5586$ | $0.2248$ | $4$ | $20 < N \leq 28$ |
| $T_{2,9}$ | $0.6048$ | $0.2495$ | $5$ | $28 < N \leq 50$ |
| $T_{3,4}$ | $0.5850$ | $0.2770$ | $6$ | $50 < N \leq 82$ |

For degree-$1$ shells (shells $1$–$4$), the knot operator
averages are already encoded in $\mathcal{Q}_{\mathrm{bare}}$
through the crossing coefficients ($\mathfrak{p}\mathfrak{p}$,
$\mathfrak{n}\mathfrak{n}$, $\mathfrak{p}\mathfrak{n}$ have
distinct transfer matrices).  The operator $F$ therefore
contributes $1$ for degree-$1$ shells, and the table reduces to:

$$
  F(T_{k^*}, N)
  \;=\;
  \begin{cases}
    1 & N \leq 28 \;\text{(degree-$1$ shell: already in $\mathcal{Q}_{\mathrm{bare}}$)} \\[4pt]
    0.5949 & N > 28,\; N \notin \{50, 82, 126\}
    \;\text{(degree-$2$ shell, partial)} \\[4pt]
    0.5949 \times 0.6382 = 0.3797
    & N \in \{50, 82, 126\} \;\text{(degree-$2$ shell, full / Pauli)}
  \end{cases}
$$

where $0.5949 = \tfrac{1}{2}(\mathrm{tr}_M(T_{2,9} \cdot \Delta)
+ \mathrm{tr}_M(T_{3,4} \cdot \Delta))$ and $0.6382 =
|\mathrm{tr}_M(e_{(1^3)} \cdot \Delta \cdot e_{(1^3)})| /
|\mathrm{tr}_M(\Delta)|$.

**Remark (error structure).**
Let $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$
(CODATA).  All factors are smooth functions of $q$, so
$\delta \mathcal{Q}_q / \mathcal{Q}_q = O(\varepsilon)$.
The dominant sensitivity is
$\partial \ln \mathcal{Q}_{\mathrm{bare}} / \partial \ln q
\approx 10$, giving $\delta \mathcal{Q}_q \approx 10\varepsilon
\approx 10^{-7}$ — negligible.  The observed $5$–$9\%$ deviations
from experiment are structural: nucleon ordering, degree-$2$
averaging, and truncation of the degree tower.  These are $O(1)$
relative to $\varepsilon$.

### Geometric interpretation: exceptional divisors and the jet bundle

The $\log_q$ in $\mathcal{Q}_{\mathrm{bare}}$ counts **steps along
the exceptional divisor chain** of $\Sigma_4$.  Each blow-up of the
Bring surface produces an exceptional divisor $E_k$; the color tube
coordinate along the fiber ascends by one $q$-power per divisor.
The quantity $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})$ measures
how many divisor levels the decay traverses.

The four factors in $\mathcal{Q}_q$ each have a geometric reading:

| Factor | Geometry |
|--------|----------|
| $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})$ | Divisor levels traversed (color tube degrees) |
| $\hbar_q = 1 - q^{-1}$ | Action quantum per divisor step (discrete fiber spacing) |
| $\mathfrak{E}_{\times}$ | Crossing energy from the Hecke relation |
| $\mu_0$ | Dimensional anchor ($T_{2,3}$ trefoil $=$ electron) |

The degree tower maps to the divisor hierarchy:

- **Degree $0$**: base level — bare crossings in the transfer matrix.
  At $q = 1$ all crossing types coincide; $\mathcal{Q}_q = 0$.
- **Degree $1$**: first exceptional divisor — knots
  $T_{2,3}, T_{2,5}, T_{2,7}, T_{3,5}$ (shells $1$–$4$).
  Already captured by $\mathcal{Q}_{\mathrm{bare}}$ through the
  crossing coefficients.
- **Degree $2$**: second exceptional divisor — tower knots
  $T_{2,9} = T_{2,3^2}, T_{3,4} = T_{3,2^2}$ (shells $5$–$6$).
  The knot operator $F(T_{k^*}, N)$.
- **Degree $\geq 3$**: the tower terminates
  ($T_{2,27}$ needs genus $13 > 4$), so higher divisors are
  absent on $\Sigma_4$.  The knot operator is $F = 1$ (null).

The knot operators are naturally organised as **jets on the
exceptional divisor bundle**, indexed by the Gröbner class
of the torus knot.  The jet at degree $k$ records the
$k$-th order correction to the Skein polynomial along the
fiber.  Composed operators collapse (contribute $F = 1$)
precisely when their jet index exceeds the embedding genus:
a non-embeddable knot has zero action on $\Sigma_4$, hence
its jet vanishes — analogous to a zero-volume knot in the
hyperbolic picture.

The ratio $\hbar_q / \ln q = 0.9496$ is the **discretisation
correction**: the exceptional divisors are spaced by $q$
(discrete), not by $e$ (continuous).  The $5\%$ deviation
encodes the finiteness of the fiber lattice.  In the $q \to 1$
limit, $\hbar_q / \ln q \to 1$ and the divisor spacing becomes
continuous.

## Gröbner normal form of the corrected element

The torus-knot correction modifies the **crossing coefficients**
at the converting generator, replacing bare $(c, d)$ with
renormalized $(c_n, d_n)$ from $T_{2,n}$.  The resulting
transfer matrix $T(c_n, d_n)$ is a **polynomial in $q$**
(since $c_n$ and $d_n$ are polynomials in $q$ from the Hecke
recurrence).

The Skein polynomial $P(q) = \prod_i \hat{V}_i(q)$ with
renormalized coefficients is therefore still a **polynomial
in $q^{1/2}$**, and the Hecke element corresponding to
the renormalized transfer matrix chain is in **Gröbner normal
form** — it satisfies all three conditions:

1. **No $\sigma_i^2$**: the Hecke recurrence eliminates all
   squares (the renormalized coefficients are the OUTPUT of
   the recurrence, not the input).

2. **Yang–Baxter reduced**: the torus knot $T_{2,n} = \sigma^n$
   lives on a single generator (only $\sigma_0$ for $T_{2,n}$
   in $B_2$), so no Yang–Baxter relations apply.

3. **Far-commutativity sorted**: single-generator elements
   have no far-commutativity issues.

By the inductive normal form theorem
([shell closure normal form](#prop:shell-closure-normal-form)),
the sequential construction with renormalized coefficients
produces a Gröbner normal form at every step.

## The hierarchy as degree-2 fiber ascent

The torus knots $T_{2,n}$ for $n = 3, 5, 7, 9$ form a chain
along the degree-2 fiber of the Bring surface:

$$
  T_{2,3} \;\subset\; T_{2,5} \;\subset\; T_{2,7} \;\subset\; T_{2,9}
$$

The transfer matrix coefficients satisfy the **Chebyshev
recurrence** (since $\sigma^n$ in $H_2(q)$ generates Chebyshev
polynomials of the second kind):

$$
  c_{n+2} = (q - q^{-1}) \cdot c_{n+1} + c_n
  \qquad
  d_{n+2} = (q - q^{-1}) \cdot d_{n+1} + d_n
$$

with $c_1 = 1, d_1 = 0$ (single crossing = $T_{2,1}$).
The strong force $T_{2,9} = (T_{2,3})^3$ ascends the color
fiber: each level multiplies the crossing structure by the
$3$-fold Borromean symmetry, giving $3 \to 9 = 3^2$ crossings.

## Connection to $T_{3,5}$

The weak vertex $T_{3,5}$ mediates **transitions between shells**
(aperiodic, $5$-fold, [five-fold symmetry](#rem:fivefold-symmetry)).
The strong binding $T_{2,9}$ creates **stability within shells**
(periodic, $3$-fold color).

Beta decay is the process of **breaking a $T_{2,n}$ strong bond**
via the **$T_{3,5}$ weak vertex**: one Borromean partner in the
converting triple is converted $\mathfrak{n} \to \mathfrak{p}$,
disrupting $n_B = 2$ strong-bound crossings.  The
$\mathcal{Q}_q$-value is the energy cost of this disruption.
