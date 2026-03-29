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

## The $\mathcal{Q}_q$-value with torus-knot correction

**Proposition.**
*The $\mathcal{Q}_q$-value for $\beta^-$ decay
$\mathcal{N}(p, n) \to \mathcal{N}(p\!+\!1, n\!-\!1)$ is:*

$$
  \mathcal{Q}_q
  \;=\;
  \Bigl|
    \log_q\!\frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}
    \;-\;
    n_B \cdot \Delta_{\mathrm{shell}}
  \Bigr|
  \;\times\;
  \hbar_q \cdot E_{\times} \cdot \mu_0
$$

*where:*

*1. $P_{\mathrm{par}}(q)$ and $P_{\mathrm{dau}}(q)$ are the
   Level 0 Skein polynomials from the transfer matrix chain.*

*2. $n_B = 2$ is the number of **Borromean partners** of the
   converting nucleon within its shell — the two other nucleons
   in the converting nucleon's Borromean triple $\mathcal{B}_3$.*

*3. $\Delta_{\mathrm{shell}} = \log_q(\hat{V}_{T_{2,n}} /
   \hat{V}_{\mathrm{bare}})$ is the per-crossing correction
   from the dominant torus knot $T_{2,n}$ of the converting
   shell, where $\hat{V}_{\mathrm{bare}}$ is the average of
   $\hat{V}_{nn}$ and $\hat{V}_{\mathrm{mix}}$ (the bare
   crossing types at the converting generator).*

*4. $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant,
   NOT $\ln q$ (which is the classical limit $q \to 1$).*

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

1. **No $T_i^2$**: the Hecke recurrence eliminates all
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
