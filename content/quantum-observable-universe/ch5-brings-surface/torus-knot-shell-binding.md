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

## The $\mathcal{Q}_q$-value with representation-theoretic correction

**Proposition.**
*The $\mathcal{Q}_q$-value for $\beta^-$ decay
$\mathcal{N}(Z, N) \to \mathcal{N}(Z\!+\!1, N\!-\!1)$ is:*

$$
  \mathcal{Q}_q
  \;=\;
  \mathcal{Q}_{\mathrm{bare}}
  \;\times\;
  F_{\mathrm{deg}}
  \;\times\;
  F_{\mathrm{Pauli}}
$$

*where:*

*1. $\mathcal{Q}_{\mathrm{bare}} = |\ln(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times
   \mathfrak{E}_{\times} \times \mu_0$ is the Level 0 transfer matrix
   ratio, with $P(q) = \prod_i \hat{V}_i(q)$ the Skein polynomial.*

*2. The **degree-$2$ operator average**:*

$$
  F_{\mathrm{deg}}
  \;=\;
  \begin{cases}
    1 & \text{if converting neutron in degree-$1$ shell (}N \leq 28\text{)} \\[4pt]
    \tfrac{1}{2}\bigl(
      \mathrm{tr}_M(T_{2,9} \cdot \Delta_{\mathrm{mix}})
      + \mathrm{tr}_M(T_{3,4} \cdot \Delta_{\mathrm{mix}})
    \bigr)
    & \text{if converting neutron in degree-$2$ shell (}N > 28\text{)}
  \end{cases}
$$

*where $\Delta_{\mathrm{mix}} = \sigma_0 \sigma_1^{-1}$ is the
universal $\pm 1$ transition operator and $\mathrm{tr}_M$ is the
Markov trace on $H_3(q)$.  Numerically $F_{\mathrm{deg}} = 0.5949$
at the substrate $q$.*

*3. The **Pauli projection** (Schur–Weyl factor):*

$$
  F_{\mathrm{Pauli}}
  \;=\;
  \begin{cases}
    1 & \text{if converting neutron's shell is not full} \\[4pt]
    \dfrac{|\mathrm{tr}_M(e_{(1^3)} \cdot \Delta_{\mathrm{mix}} \cdot e_{(1^3)})|}{|\mathrm{tr}_M(\Delta_{\mathrm{mix}})|}
    & \text{if converting neutron's shell is full (magic $N$, deg $\geq 2$)}
  \end{cases}
$$

*where $e_{(1^3)}$ is the alternating Young symmetrizer idempotent
of $H_3(q)$.  A completely filled shell is fully antisymmetric
by the Pauli principle; under the Schur–Weyl decomposition,
$\Delta_{\mathrm{mix}}$ is projected onto the alternating irrep
$(1,1,1)$.  Numerically $F_{\mathrm{Pauli}} = 0.6382$.  At degree $1$,
Pauli exclusion is already encoded in the crossing coefficients
($\mathfrak{p}\mathfrak{p}$, $\mathfrak{n}\mathfrak{n}$,
$\mathfrak{p}\mathfrak{n}$ have distinct transfer matrices), so
$F_{\mathrm{Pauli}} = 1$ regardless of shell filling.*

**Remark (error structure).**
Let $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$
(CODATA).  All three factors are smooth functions of $q$, so
$\delta \mathcal{Q}_q / \mathcal{Q}_q = O(\varepsilon)$.
The dominant sensitivity is
$\partial \ln \mathcal{Q}_{\mathrm{bare}} / \partial \ln q
\approx 10$, giving $\delta \mathcal{Q}_q \approx 10\varepsilon
\approx 10^{-7}$ — negligible.  The observed $5$–$9\%$ deviations
from experiment are structural: nucleon ordering, degree-$2$
averaging, and truncation of the degree tower.  These are $O(1)$
relative to $\varepsilon$.

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
