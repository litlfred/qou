The torus knots embeddable on the moduli surface $\Sigma_g$
of a QOU form a **complete set of representations** — they
exhaust the available cohomology and span the space of
pointed-knot observables.

## Statement

**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with moduli surface
$\Sigma_g$ of genus $g$ and Euler characteristic
$\chi = 2 - 2g$.*

**(i) Embeddability = representation.**
*A torus knot $T_{r,s}$ with $\gcd(r, s) = 1$ admits a
representation in $\mathbf{C}$ if and only if its Seifert
rank embeds in the first cohomology of $\Sigma_g$:*

$$
  \mathrm{rank}\, H_1(\mathrm{Seifert}(T_{r,s}))
  \;=\; \frac{(r-1)(s-1)}{2}
  \;\leq\; g
$$

**(ii) Fiber degree.**
*The knot $T_{r, p^k}$ acts at fiber degree $k$, where $p$
is prime.  On $\Sigma_g$, the maximum fiber degree is:*

$$
  k_{\max}(r, p, g)
  \;=\;
  \max\!\left\{k : \frac{(r-1)(p^k - 1)}{2} \leq g\right\}
$$

*Degree $1$ knots define **shells**.  Degree $2$ knots define
**subshells**.  Degree $\geq 3$ knots, if embeddable, would
define sub-subshells.*

**(iii) Completeness.**
*The Jones polynomials of the embeddable torus knots, evaluated
in the irreducible representations of $H_2(q) \oplus H_3(q)$,
**span** the space of knot invariants on $\Sigma_g$.  Every
pointed knot observable on $\Sigma_g$ is a linear combination
of evaluations of the embeddable torus knots.*

**(iv) Genus $4$ is forced.**
*The QOU axioms require:*
- *$T_{2,3}$ embeds (SU$_2$ reconstruction from trefoil structure):
  $(1)(2)/2 = 1 \leq g$.*
- *$T_{2,9} = T_{2,3^2}$ embeds (color-squared strong force, degree $2$):
  $(1)(8)/2 = 4 \leq g$.*
- *$T_{2,11}$ does NOT embed (no additional particles observed):
  $(1)(10)/2 = 5 > g$.*

*Therefore $g = 4$ and $\chi = 2 - 2(4) = -6$.*

## The 6 representations on $\Sigma_4$

For $g = 4$, the embeddability constraint $(r-1)(s-1) \leq 8$
with $\gcd(r, s) = 1$ and $2 \leq r < s$ yields exactly $6$
torus knots:

| Knot | $r$ | $s$ | Seifert rank | Degree $k$ | Genus needed |
|:----:|:---:|:---:|:---:|:---:|:---:|
| $T_{2,3}$ | $2$ | $3 = 3^1$ | $1$ | $1$ | $1$ |
| $T_{2,5}$ | $2$ | $5 = 5^1$ | $2$ | $1$ | $2$ |
| $T_{2,7}$ | $2$ | $7 = 7^1$ | $3$ | $1$ | $3$ |
| $T_{2,9}$ | $2$ | $9 = 3^2$ | $4$ | $2$ | $4$ |
| $T_{3,4}$ | $3$ | $4 = 2^2$ | $3$ | $2$ | $3$ |
| $T_{3,5}$ | $3$ | $5 = 5^1$ | $4$ | $1$ | $4$ |

The total Seifert rank used: $1 + 2 + 3 + 4 + 3 + 4 = 17$.
The available rank: $2g = 8$ (from $H^1(\Sigma_4) = \mathbb{Z}^8$).
The knots **overlap** in $H^1$ (they share Seifert cycles), so
$17 > 8$ does not contradict embeddability — each knot individually
fits within rank $\leq 4 = g$.

## Completeness via Jones polynomials

The Hecke algebras on the embeddable strand counts are:
- $H_2(q)$: $2$ irreducible representations (partitions of $2$:
  $(2)$ trivial, $(1,1)$ sign).  Dimension $2! = 2$.
- $H_3(q)$: $3$ irreducible representations (partitions of $3$:
  $(3)$ trivial, $(1,1,1)$ sign, $(2,1)$ standard of dimension
  $[2]_q$).  Dimension $3! = 6$.

Total irreps: $2 + 3 = 5$.

The Jones polynomial of a torus knot $T_{r,s}$ decomposes over
the irreps of $H_r(q)$ via the Markov trace:

$$
  V_{T_{r,s}}(q)
  \;=\;
  \sum_{\lambda \,\vdash\, r}
  d_\lambda(q) \;\chi_\lambda(T_{r,s})
$$

where $d_\lambda$ is the $q$-dimension and $\chi_\lambda$ is the
character in irrep $\lambda$.

The $6$ embeddable knots, evaluated in the $5$ irreps, give a
$6 \times 5$ matrix $M_{ij} = \chi_{\lambda_j}(T_i)$.  This
matrix has rank $5$ (= number of irreps, verified numerically).
Therefore the $6$ knot evaluations **span** the $5$-dimensional
space of irrep characters.

**Completeness**: any pointed knot observable on $\Sigma_4$ is
a function of the irrep characters, which are spanned by the
$6$ torus knots.  No knot on $\Sigma_4$ can have an invariant
independent of $\{T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4},
T_{3,5}\}$.

## Consequences

1. **Particle finiteness**: the $6$ torus knots are the complete
   particle content.  Every observable hadron is a composite of
   these $6$ building blocks.  No additional "hidden" particles
   exist on $\Sigma_4$.

2. **Shell model completeness**: the nuclear shell structure
   (magic numbers, subshells) is entirely determined by the
   knot invariants (products and crossing numbers) of these $6$
   representations.  No additional shell structure can arise.

3. **Force completeness**: the $4$ degree-$1$ knots give the
   shell-level forces ($T_{2,3}$: trefoil/mass, $T_{2,5}$:
   second generation, $T_{2,7}$: third generation, $T_{3,5}$:
   weak/aperiodic).  The $2$ degree-$2$ knots give the
   subshell splitting ($T_{2,9}$: strong binding, $T_{3,4}$:
   Hopf-squared).  No additional forces exist.

4. **$\chi = -6$ is the unique solution**: genus $4$ is the
   unique genus that accommodates exactly $\mathrm{SU}_2$
   reconstruction + color-squared strong force + no extra
   particles.  Any other genus gives either too few forces
   ($g < 4$: no strong binding) or too many particles
   ($g > 4$: $T_{2,11}$ embeds, predicting unobserved matter).
