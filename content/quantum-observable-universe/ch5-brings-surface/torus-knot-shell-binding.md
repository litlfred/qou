The five embeddable torus knots on the Bring surface
([five-fold symmetry](#rem:fivefold-symmetry)) determine the
**shell binding hierarchy** of the nuclear Skein polynomial.
Each torus knot $T_{2,n}$ with $n = 3, 5, 7, 9$ provides a
crossing coefficient $(c_n, d_n)$ for the transfer matrix at
shell boundaries, and $T_{3,5}$ mediates transitions between
shells.

## The five transfer matrix coefficients

Each $T_{2,n} = \sigma^n$ in $H_2(q)$ reduces via the Hecke
recurrence $\sigma^{k+1} = (q - q^{-1})\sigma^k + \sigma^{k-1}$
to a linear element $c_n \sigma + d_n$.  The traced volume
$\hat{V}_n = z \cdot (c_n \cdot (q - q^{-1}) + d_n) + c_n$
gives the per-crossing contribution to the Skein polynomial.

| Knot | $n$ | $c_n$ | $d_n$ | $\hat{V}_n$ | $\log_q \hat{V}_n$ |
|:----:|:---:|:---:|:---:|:---:|:---:|
| $T_{2,3}$ | $3$ | $1.044$ | $0.209$ | $1.257$ | $+2.19$ |
| $T_{2,5}$ | $5$ | $1.133$ | $0.427$ | $1.465$ | $+3.66$ |
| $T_{2,7}$ | $7$ | $1.272$ | $0.664$ | $1.736$ | $+5.29$ |
| $T_{2,9}$ | $9$ | $1.466$ | $0.930$ | $2.084$ | $+7.04$ |

The weak vertex $T_{3,5} = (\sigma_1\sigma_2)^5$ in $H_3(q)$
gives $\hat{V}_{3,5} = 0.704$ with $\log_q = -3.37$ (negative:
transitions cost action, unlike binding which gains action).

## Shell-size assignment

The dominant binding knot for a shell of size $n_s$ is the
**largest** $T_{2,n}$ whose crossing number $n$ fits within
the shell ($n \leq n_s$):

| Shell size $n_s$ | Dominant $T_{2,n}$ | Physical role |
|:---:|:---:|:---:|
| $\leq 2$ | bare (no torus knot) | Too few nucleons for binding |
| $3$–$4$ | $T_{2,3}$ ($n = 3$) | Trefoil binding (mass scale) |
| $5$–$6$ | $T_{2,5}$ ($n = 5$) | Second-generation threshold |
| $7$–$8$ | $T_{2,7}$ ($n = 7$) | Third-generation channel |
| $\geq 9$ | $T_{2,9}$ ($n = 9$) | Full strong binding ($3^2$ color) |

This assignment uses **only** the shell size (determined by the
palindromic normal form at each closure,
[shell closure](#prop:shell-closure-normal-form)) and the
embeddability constraint $(m-1)(n-1) \leq 8$
([finiteness bound](#prop:skein-finiteness-bound)).  No external
nuclear physics model is imported.

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
